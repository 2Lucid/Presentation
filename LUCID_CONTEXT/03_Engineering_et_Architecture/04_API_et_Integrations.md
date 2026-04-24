# 🔌 API et Intégrations — LUCID

---

## 1. Services Tiers Intégrés

| Service | Usage | Environnement |
|---|---|---|
| **Supabase** | BDD, Auth, Storage, Edge Functions, Realtime | Tous les projets |
| **Google Gemini API** | LLM (Flash + Pro) pour l'IA pédagogique | App, Labs, Dashboard, Prof |
| **Pronote** (via Proxy) | Données scolaires (notes, EDT, devoirs) | App Mobile |
| **Vercel** | Hosting, CI/CD, Preview Deployments | Tous les sites web |
| **Apple App Store** | Distribution iOS | App Mobile |
| **Expo** | Build, OTA Updates, Push Notifications | App Mobile |
| **Resend** | Envoi d'emails transactionnels | Dashboard (rapports IA) |
| **Firebase** | Backend pour la Roadmap (Firestore) | lucid_roadmap |
| **Yahoo Finance** | Données boursières | lucid_finance |
| **AXEPI** | Partenaire brevet (non technique) | — |

---

## 2. API Interne — Supabase (Tables + RPCs)

### 2.1. Client Supabase

Deux clients sont configurés dans chaque projet :

```typescript
// Client public (côté client)
export const supabase = createClient(supabaseUrl, supabaseAnonKey);

// Client admin (côté serveur — Server Actions)
export const supabaseAdmin = createClient(
    supabaseUrl,
    supabaseServiceKey || supabaseAnonKey,
    { auth: { persistSession: false } }
);
```

### 2.2. Variables d'Environnement (Structure)

```bash
# ⚠️ AUCUN SECRET RÉEL ICI — Structure uniquement

# Supabase
NEXT_PUBLIC_SUPABASE_URL=https://xxxxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIs...
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIs...  # ⚠️ SERVER ONLY

# Gemini API (support multi-clés avec rotation)
GEMINI_API_KEYS=key1,key2,key3,...
GEMINI_API_KEY=single_key_fallback
GOOGLE_GENERATIVE_AI_API_KEY=alternative_key

# Resend (Dashboard uniquement)
RESEND_API_KEY=re_xxxxx

# Firebase (Roadmap uniquement)
# Configuré via firebase.js
```

### 2.3. Endpoints API (Server Actions Next.js)

Les projets Next.js (Labs, Dashboard, Prof) utilisent des **Server Actions** (`"use server"`) au lieu d'API Routes classiques. Ce sont des fonctions TypeScript appelées directement depuis le client.

#### Lucid Labs — Server Actions (`app/actions.ts`)

| Action | Signature | Description |
|---|---|---|
| `createPipelineRun` | `(config) → PipelineRun` | Crée un run de pipeline |
| `updatePipelineRun` | `(id, updates) → void` | Met à jour le statut d'un run |
| `getPipelineRuns` | `() → PipelineRun[]` | Liste les 20 derniers runs |
| `generateContexts` | `({subject, level, count, style}) → {contexts, tokens}` | Phase 1 : Génère des contextes Pronote simulés |
| `generateQuizExample` | `({subject?, level?, mode}) → {example, tokens}` | Phase 2 : Génère un quiz |
| `generateHomeworkExample` | `({subject?, level?}) → {example, tokens}` | Phase 2 : Génère une aide aux devoirs |
| `generateFlashcardExample` | `({subject?, level?, mode}) → {example, tokens}` | Phase 2 : Génère des flashcards |
| `generateRevisionExample` | `({subject?, level?, length}) → {example, tokens}` | Phase 2 : Génère une fiche de révision |
| `generateTutorExample` | `({subject?, level?}) → {example, tokens}` | Phase 2 : Génère une conversation tutorat |
| `judgeExample` | `(exampleId) → {score, isGold, reason}` | Phase 3 : Juge un exemple |
| `judgeUnjudgedBatch` | `(limit) → {judged, gold, rejected}` | Phase 3 : Juge un batch |
| `overrideJudgeScore` | `(judgmentId, exampleId, newScore) → void` | Override manuel |
| `getRecentJudgments` | `(limit) → Judgment[]` | Liste des jugements récents |
| `runAutopilotCycle` | `(concurrency, ignoreTargets, allowedTasks) → AutopilotResult` | Cycle automatique complet |

---

## 3. API Gemini (Transitoire — Phase Beta)

> ⚠️ **L'API Gemini est utilisée temporairement** pendant la phase de beta pour garantir la fluidité de l'expérience. L'architecture cible est l'**IA edge embarquée** (Gemma E2B/E4B fine-tuné + RAG on-device).

### 3.1. Smart Caller avec Key Rotation

Le fichier `lib/supabase.ts` implémente un système sophistiqué :

```
callGemini(params)
  ├── Si clés locales disponibles → callGeminiDirect()
  │   ├── Rotation automatique des clés API
  │   ├── Retry avec backoff exponentiel (429 Rate Limit)
  │   ├── Fallback sur clé suivante si quota daily exhausted
  │   └── Fallback sur modèle alternatif si erreur
  └── Sinon → callGeminiViaEdge()
      └── Supabase Edge Function "gemini-proxy"
```

### 3.2. Endpoint Gemini

```
POST https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}
```

### 3.3. Modèles Utilisés

| Modèle | Usage | Température |
|---|---|---|
| `gemini-flash-latest` | Contextes, Quiz, Flashcards, Revision, Homework, Tutor, Judge | 0.3 - 0.9 |
| `gemini-2.5-pro` | Tâches expertes (fallback/vérification) | 0.7 |

### 3.4. Paramètres d'Appel

```json
{
  "generationConfig": {
    "temperature": 0.7,
    "maxOutputTokens": 8192,
    "responseMimeType": "application/json"  // si jsonMode=true
  },
  "system_instruction": {
    "parts": [{"text": "System prompt..."}]
  },
  "contents": [
    {"role": "user", "parts": [{"text": "User prompt..."}]}
  ]
}
```

## 4. IA Edge Embarquée (Architecture Cible)

### 4.1. Modèles
| Composant | Technologie | Rôle |
|---|---|---|
| **Gemma E2B** | Google Gemma 2B fine-tuné | Modèle compact pour tâches rapides (quiz, flashcards) |
| **Gemma E4B** | Google Gemma 4B fine-tuné | Modèle plus puissant pour tâches complexes (tuteur, aide devoirs) |
| **RAG** | Custom (embeddings + retrieval local) | Injection du contexte scolaire Pronote |

### 4.2. Avantages Edge vs Cloud
| Critère | Cloud (Gemini API) | Edge (Gemma on-device) |
|---|---|---|
| **Latence** | 1-3s | <500ms |
| **Connectivité** | Nécessaire | Pas nécessaire (hors-ligne) |
| **Vie privée** | Transit de données | Zéro transit, tout local |
| **Coût** | API payante (quotas) | Gratuit (modèle embarqué) |
| **Contrôle** | Dépendance Google | Total |

---

## 5. API Pronote (via Proxy)

### 4.1. Architecture du Proxy

```
App Mobile → HTTPS → Proxy VPS (Scaleway/OVH) → Pronote Server
                     └── Node.js + Pawnote library
```

### 4.2. Repository
- **URL :** `https://github.com/NovaVibeCoding/pronotebackend`
- **Stack :** Node.js
- **Bibliothèque :** Pawnote (wrapper Pronote protocol)
- **Open Source :** Oui (transparence RGPD)

### 4.3. Données Récupérées

| Endpoint (conceptuel) | Données |
|---|---|
| Timetable | Emploi du temps (par semaine) |
| Grades | Notes et moyennes (par période) |
| Homework | Devoirs à faire (par date) |
| Absences | Absences et retards |
| Content (Cahier de Texte) | Contenus de cours (utilisés par l'IA) |

---

## 5. Webhooks et Événements Temps Réel

### 5.1. Supabase Realtime (Futur)
- **Usage potentiel :** Leaderboard live, notifications de dépassement au classement
- **Statut :** Non implémenté (polling actuellement)

### 5.2. Expo Push Notifications
- **Service :** Expo Push Service
- **Token :** Généré par `Expo Notifications`
- **Usage :** Rappels de devoirs, alertes XP, demandes d'amitié

---

## 6. Intégrations Futures

| Service | Usage Planifié | Phase |
|---|---|---|
| **Stripe** | Paiements abonnement Pro | Phase 2 |
| **Apple In-App Purchase** | Paiements in-app iOS | Phase 2 |
| **PostHog / Mixpanel** | Analytics d'usage | Phase 2 |
| **Sentry** | Error tracking (crash reporting) | Phase 2 |
| **École Directe API** | 2ème ENT français | Phase 2 |
| **Google Classroom** | 3ème source de données scolaires | Phase 3 |
| **Notion / Jira** | Connexion Roadmap ↔ Issues | Phase 2 |

---

## 7. Rate Limits et Quotas

| Service | Limite Gratuite | Action LUCID |
|---|---|---|
| Gemini Flash (free tier) | ~1500 req/day/key | Key rotation (multi-clés séparées par virgule) |
| Supabase Free | 500MB DB, 50K MAU | Upgrade vers Pro si nécessaire |
| Vercel Hobby | 100 deploys/day | Suffisant actuellement |
| Expo Push | 600 notif/sec | Largement suffisant |
