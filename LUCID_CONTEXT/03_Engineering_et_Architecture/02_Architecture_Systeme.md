# 🏗️ Architecture Système — LUCID

---

## 1. Vue d'Ensemble

LUCID suit une architecture **client-serveur hybride évoluant vers le edge** :
- Une application mobile (client principal) — **repository séparé**
- Plusieurs applications web satellites — **repository commun (npm workspaces)**
- Supabase comme Backend-as-a-Service central
- Un proxy VPS pour la connexion Pronote
- **Modèles IA edge (Gemma E2B/E4B fine-tunés)** embarqués sur l'appareil (objectif production)
- Google Gemini comme backend IA transitoire (phase beta)
- **RAG** pour l'injection de contexte scolaire

---

## 2. Schéma d'Architecture

```
                        ┌─────────────────────────────┐
                        │      UTILISATEURS            │
                        │  (Élèves, Profs, Admins)     │
                        └────────────┬────────────────┘
                                     │
                    ┌────────────────┼────────────────┐
                    │                │                │
              ┌─────▼─────┐   ┌─────▼─────┐   ┌─────▼─────┐
              │  📱 App   │   │  🌐 Sites │   │  🌐 Sites │
              │  Mobile   │   │  Next.js   │   │  Vite SPA │
              │(Expo/RN)  │   │  (SSR)     │   │ (Static)  │
              └─────┬─────┘   └─────┬─────┘   └─────┬─────┘
                    │               │                │
                    │         Server Actions    Client-side
                    │          (Node.js)         fetch
                    │               │                │
         ┌──────────┴───────┐      │                │
         │                  │      │                │
    ┌────▼────┐       ┌────▼───────▼────────────────▼───┐
    │  Proxy  │       │          SUPABASE                │
    │ Pronote │       │  ┌──────────────────────────┐   │
    │  (VPS)  │       │  │    PostgreSQL Database    │   │
    │         │       │  │  • profiles              │   │
    │  Node.js│       │  │  • gamification          │   │
    │  Pawnote│       │  │  • examples              │   │
    │ library │       │  │  • contexts              │   │
    └─────────┘       │  │  • judgments             │   │
                      │  │  • pipeline_runs         │   │
                      │  │  • combos                │   │
                      │  │  • lucid_labs_entries     │   │
                      │  └──────────────────────────┘   │
                      │                                  │
                      │  ┌──────────────────────────┐   │
                      │  │    Edge Functions (Deno)  │   │
                      │  │  • gemini-proxy          │   │
                      │  │  • RPCs atomiques        │   │
                      │  └──────────────────────────┘   │
                      │                                  │
                      │  ┌──────────────────────────┐   │
                      │  │    Auth                   │   │
                      │  │  • ID déterministe       │   │
                      │  │  • Session management    │   │
                      │  └──────────────────────────┘   │
                      │                                  │
                      │  ┌──────────────────────────┐   │
                      │  │    Storage               │   │
                      │  │  • Avatars, assets       │   │
                      │  └──────────────────────────┘   │
                      └─────────────┬───────────────────┘
                                    │
                          ┌───────────────────────────┐
                          │  🧠 IA EDGE ON-DEVICE  │
                          │  Gemma E2B/E4B       │
                          │  fine-tuné + RAG      │
                          │  (inférence locale)   │
                          └───────────────────────────┘
                                    │
                          ┌────────────────────┘
                          │ (fallback transitoire)
                          │
                          ┌─────────▼──────────┐
                          │   Google Gemini API │
                          │  • Flash (génération)│
                          │  • Pro (expert)     │
                          │  • Key Rotation     │
                          └────────────────────┘
```

---

## 3. Flux de Données

### 3.1. Flux Pronote (Données Scolaires)

```
Élève → App Mobile  → [Identifiants Pronote]
                     → Proxy VPS (Node.js + Pawnote)
                     → [HTTPS/TLS] → Serveur Pronote Établissement
                     ← [Notes, EDT, Devoirs, Absences]
                     ← App Mobile (stocké en cache AsyncStorage)
```

**Points clés :**
- Les identifiants Pronote ne sont **pas** conservés en clair sur le serveur proxy
- Le transit est **chiffré** (HTTPS/TLS)
- Les données scolaires sont **stockées localement** (pas sur Supabase)
- Le code du proxy est **open-source** : `github.com/NovaVibeCoding/pronotebackend`

### 3.2. Flux IA (Génération de Contenu)

**Architecture cible (Production) — Edge AI :**
```
App Mobile → [Contexte Pronote local]
           → RAG Pipeline (embedding + retrieval local)
           → Modèle Gemma E2B/E4B (inférence on-device)
           ← [JSON structuré (Quiz/Flashcards/Fiche/...)]
           ← App Mobile (affichage)
```

**Architecture transitoire (Beta) — API Cloud :**
```
App Mobile → [Contexte Pronote + Commande]
           → Supabase Edge Function (gemini-proxy)
           → Google Gemini API
           ← [JSON structuré]
           ← App Mobile (affichage)
```

### 3.3. Flux Gamification

```
App Mobile → [Action: bonne note, quiz complété, etc.]
           → gamificationStore (local AsyncStorage)
           → userProfileStore.syncFromSupabase()
           → Supabase (table profiles) [bidirectionnel, "Max XP Wins"]
```

### 3.4. Flux Dataset Factory (Lucid Labs)

```
Pipeline Autopilot (frontend) → Server Actions (Next.js)
  ├── Phase 1: Contexte  → Gemini Flash → Supabase (contexts)
  ├── Phase 2: Generate  → Gemini Flash → Supabase (examples)
  │   ├── Quiz, Flashcards, Revision, Homework (JSON)
  │   └── Tutor (Multi-turn, 4 appels séquentiels)
  └── Phase 3: Judge     → Gemini Flash (temp=0.3) → Supabase (judgments)
      └── Score ≥ 9/10 → Gold Data ✅
      └── Score < 9/10 → Rejected ❌
```

---

## 4. Type d'Architecture

### Monolithique Modulaire avec Edge AI (pas Microservices)

L'architecture actuelle est un **monolithe modulaire évoluant vers le edge** :
- L'app mobile et les sites web sont dans des **repositories séparés**
- L'app mobile intègre les modèles IA directement (inférence locale Gemma)
- Les sites satellites partagent la même base Supabase via npm workspaces
- Il n'y a pas de communication inter-services (pas de message broker)
- Les "Server Actions" de Next.js servent de pseudo-API pour les apps full-stack

**Justification :** Pour une équipe de 2 personnes, la simplicité l'emporte. L'IA edge réduit la dépendance au cloud et améliore la confidentialité des données.

---

## 5. Hébergement & Infrastructure

| Composant | Hébergeur | Type |
|---|---|---|
| Application Mobile | App Store (iOS), Play Store (Android) | Distribué |
| Tous les sites web | **Vercel** | Serverless + Edge |
| Base de données | **Supabase** (AWS sous le capot) | Managed PostgreSQL |
| Edge Functions | **Supabase** (Deno Deploy) | Serverless |
| Proxy Pronote API | **Scaleway/OVH** (VPS) | Serveur dédié |
| DNS | Vercel (auto) + domaine custom | — |
| Stockage fichiers | Supabase Storage | S3-compatible |

### Configuration Vercel

Chaque site a un `vercel.json` :
```json
{
  "buildCommand": "cd ../.. && npm install && npm run build --workspace=sites/lucid_official_website",
  "installCommand": "echo skip"
}
```

---

## 6. Sécurité

| Mesure | Implémentation |
|---|---|
| **Chiffrement transit** | HTTPS/TLS partout (Vercel, Supabase, Proxy) |
| **Stockage sécurisé** | Expo SecureStore pour les identifiants sensibles |
| **Row Level Security** | RLS activée sur toutes les tables Supabase |
| **Service Role Key** | Séparée de l'anon key, utilisée uniquement côté serveur (Server Actions) |
| **Env Variables** | `.env.local` non versionné, clés jamais en dur dans le code |
| **Proxy Open Source** | Transparence totale sur le transit des données Pronote |
| **RGPD** | Politique de confidentialité détaillée, droit de suppression |

---

## 7. Scaling (Futur)

| Seuil | Action |
|---|---|
| 1K users | Architecture actuelle suffit |
| 10K users | Upgrade Supabase Plan (Pro), monitoring |
| 100K users | CDN pour assets, read replicas Supabase, cache Redis |
| 500K+ users | Évaluer migration vers microservices + API Gateway |
