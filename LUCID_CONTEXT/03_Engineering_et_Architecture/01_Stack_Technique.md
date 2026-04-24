# ⚙️ Stack Technique — LUCID

---

## 1. Architecture des Repositories

Le projet LUCID est organisé en **deux repositories séparés** :

### Repository 1 — Application Mobile (privé)
```
lucid_app/                   # Application mobile React Native / Expo
├── app/                     # Expo Router (file-based routing)
├── components/              # Composants UI React Native
├── stores/                  # Zustand stores (profil, gamification)
├── lib/                     # Utilitaires, clients Supabase
└── assets/                  # Images, fonts
```

### Repository 2 — Sites Satellites (npm workspaces)
```
LUCID_WORKSPACE/
├── sites/
│   ├── lucid_official_website/   # Site vitrine (Vite + React)
│   ├── lucid_labs/               # R&D + Dataset Factory (Next.js)
│   ├── lucid_dashboard/          # Admin panel (Next.js)
│   ├── lucid_prof/               # Plateforme professeurs (Next.js)
│   ├── lucid_finance/            # Dashboard financier (Next.js)
│   ├── lucid_hub/                # Hub de redirection (Vite + React)
│   ├── lucid_roadmap/            # Roadmap publique (Vite + React)
│   ├── lucid_media_tracker/      # Press room (Vite + React)
│   └── lucid_redirect/           # Redirection store (HTML statique)
└── package.json              # Workspaces root config (sites only)
```

### Repository 3 — Proxy Pronote (open-source)
```
pronotebackend/              # github.com/NovaVibeCoding/pronotebackend
```

> ⚠️ **L'application mobile est dans un repository séparé** des sites satellites. Ce n'est PAS un monorepo unique.



---

## 2. Application Mobile — `lucid_app`

| Couche | Technologie | Version |
|---|---|---|
| **Framework** | React Native | ^0.76+ |
| **Build System** | Expo (Managed Workflow) | SDK ~52 |
| **Router** | Expo Router (file-based routing) | v4 |
| **Langage** | TypeScript | ^5 |
| **State Management** | Zustand | ~5 |
| **Storage Local** | AsyncStorage | via @react-native-async-storage |
| **Secure Storage** | Expo SecureStore | Identifiants Pronote |
| **Connexion Pronote** | Pawnote (fork/wrapper) | Custom |
| **Backend** | Supabase | ^2.x |
| **Auth** | Supabase Auth (ID déterministe) | Via `deterministicUUID.ts` |
| **IA** | Google Gemini API | Via Supabase Edge Functions ou API directe |
| **Calendrier** | Expo Calendar | `WRITE_CALENDAR` |
| **Notifications** | Expo Notifications + Expo Push | Push tokens |
| **UI** | Custom components + Expo Vector Icons | — |
| **Animations** | React Native Reanimated / Animated API | — |

### Stores Zustand Principaux
- `userProfile.store.ts` — Profil Supabase, syncProfile, fetchProfile
- `gamificationStore.ts` — XP, niveaux, badges (local AsyncStorage + sync Supabase)

---

## 3. Sites Web — Stack par Projet

### 3.1. Sites Vite + React (SPA)

| Projet | Framework | Libs Principales |
|---|---|---|
| `lucid_official_website` | Vite 7 + React 19 | Framer Motion, Lucide React, TailwindCSS 3, React Router DOM 7, Supabase JS, React Simple Maps, D3-Geo |
| `lucid_hub` | Vite 7 + React 19 | Lucide React |
| `lucid_roadmap` | Vite 7 + React 19 | TailwindCSS 4, Firebase, Lucide React |
| `lucid_media_tracker` | Vite 8 + React 19 | Lucide React, React Icons |

### 3.2. Sites Next.js (SSR / Server Actions)

| Projet | Framework | Libs Principales |
|---|---|---|
| `lucid_labs` | Next.js 16 + React 19 | @google/generative-ai, Supabase JS, Zod, Recharts, TailwindCSS 4, Framer Motion |
| `lucid_dashboard` | Next.js 16 + React 19 | Radix UI, Recharts, Supabase JS, Resend, TanStack Table, Framer Motion, html2canvas, jspdf, D3-Scale, React Force Graph 2D, React Simple Maps, TailwindCSS 4 |
| `lucid_prof` | Next.js 16 + React 19 | @google/generative-ai, Supabase JS, Recharts, TailwindCSS 4, Framer Motion |
| `lucid_finance` | Next.js 16 + React 19 | Supabase JS + SSR, Yahoo Finance 2, PapaParse, XLSX, Radix UI, Recharts, Shadcn, TailwindCSS 4 |

### 3.3. Site Statique

| Projet | Stack |
|---|---|
| `lucid_redirect` | HTML pur (39KB) — Détection User-Agent + redirection App Store/Play Store |

---

## 4. Backend & Services

| Service | Technologie | Usage |
|---|---|---|
| **Base de données** | Supabase (PostgreSQL) | Profils utilisateurs, gamification, exemples IA, pipeline datasets |
| **Auth** | Supabase Auth | Authentification (IDs déterministes côté client) |
| **Edge Functions** | Supabase Edge Functions (Deno) | Proxy Gemini, RPCs atomiques |
| **Proxy Pronote** | Node.js sur VPS (Scaleway/OVH) | Relay sécurisé pour la connexion Pronote |
| **IA / LLM** | Google Gemini API (Flash + Pro) | Génération de contenu, juge, tuteur |
| **Email** | Resend | Envoi de rapports automatisés (Dashboard) |
| **File Storage** | Supabase Storage | Assets, avatars |
| **Hosting Web** | Vercel | Tous les sites (prod + preview) |

---

## 5. IA & Machine Learning

### 5.1. Architecture IA Edge-First (Cœur du Projet)

| Composant | Technologie | Usage |
|---|---|---|
| **Modèle Edge (Production)** | **Google Gemma E2B / E4B (fine-tuné)** | Inférence locale on-device pour les 5 assistants pédagogiques |
| **RAG** | Retrieval-Augmented Generation (custom) | Injection du contexte scolaire réel (cours Pronote) dans les prompts |
| **Dataset d'entraînement** | 10 000+ exemples Gold Data (JSONL / ChatML) | Données validées par LLM-as-a-Judge (seuil 9/10) |
| **Format Dataset** | ChatML (JSONL) | `<\|im_start\|>system\n...<\|im_end\|>` |

### 5.2. Backend IA Transitoire (Phase Beta)

> 💡 Pendant la phase de beta, l'API Gemini est utilisée temporairement pour garantir la fluidité de l'expérience.

| Composant | Technologie | Usage |
|---|---|---|
| **LLM Transitoire** | Google Gemini Flash (gemini-flash-latest) | Génération Quiz, Flashcards, Fiches, Aide, Contextes (en attendant le modèle edge) |
| **LLM Expert** | Google Gemini 2.5 Pro | Tâches complexes, vérification |
| **LLM Judge** | Google Gemini Flash (temp=0.3) | Validation des exemples pour le dataset |
| **Key Rotation** | Custom (supabase.ts) | Rotation automatique des clés Gemini API |
| **Validation** | Zod | Schémas de validation JSON strict |

---

## 6. Outils & DevTooling

| Outil | Usage |
|---|---|
| **Git** | Versioning (GitHub) |
| **npm Workspaces** | Sites satellites management (pas de monorepo global) |
| **ESLint** | Linting (tous les projets) |
| **TypeScript** | Type-checking (tous les projets sauf static) |
| **PostCSS** | Processing CSS (TailwindCSS) |
| **Vercel CLI** | Deployment |
| **Expo CLI** | Mobile builds + OTA updates |
| **Supabase CLI** | DB migrations, type generation |
| **tsx** | TypeScript execution (scripts mining) |

---

## 7. Résumé des Versions Clés

| Package | Version |
|---|---|
| React | 19.2.x |
| React Native | ~0.76 |
| Expo SDK | ~52 |
| Next.js | 16.1.x |
| Vite | 7.x / 8.x |
| TypeScript | ^5 |
| TailwindCSS | 3.4 (website) / 4.x (Next.js) |
| Supabase JS | ^2.87 - ^2.95 |
| Framer Motion | ^12.x |
| Lucide React | ^0.554 - ^0.577 |
| Recharts | ^2.15 / ^3.7 |
