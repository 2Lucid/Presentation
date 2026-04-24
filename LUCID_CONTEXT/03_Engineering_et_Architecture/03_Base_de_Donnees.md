# 🗄️ Base de Données — LUCID

---

## 1. Système de Gestion

- **SGBD :** PostgreSQL (via Supabase)
- **Hébergement :** Supabase (AWS sous le capot)
- **ORM / Client :** `@supabase/supabase-js` v2.x (pas d'ORM, requêtes directes)
- **Migrations :** SQL brut dans `supabase/migrations/`

---

## 2. Projets Supabase

L'écosystème utilise **deux projets Supabase distincts** :

| Projet | Usage | Tables Principales |
|---|---|---|
| **Supabase Principal** | App mobile + Dashboard + Site officiel | profiles, gamification, leaderboard |
| **Supabase Labs** | Lucid Labs (Dataset Factory) | contexts, examples, judgments, combos, pipeline_runs |

---

## 3. Schéma — Supabase Principal (App Mobile)

### 3.1. Table `profiles`

| Colonne | Type | Description |
|---|---|---|
| `id` | UUID (PK) | ID déterministe généré côté client (`deterministicUUID.ts`) |
| `auth_id` | TEXT | Identifiant d'authentification stable |
| `display_name` | TEXT | Nom affiché (extrait de Pronote) |
| `avatar_url` | TEXT | URL de l'avatar |
| `xp` | INTEGER | Points d'expérience totaux |
| `level` | INTEGER | Niveau actuel |
| `title` | TEXT | Titre sélectionné |
| `badges` | JSONB | Liste des badges débloqués |
| `preferences` | JSONB | Préférences utilisateur |
| `friends` | JSONB | Liste d'amis |
| `friend_requests` | JSONB | Demandes d'amitié en attente |
| `last_login` | TIMESTAMPTZ | Dernière connexion |
| `created_at` | TIMESTAMPTZ | Date de création |
| `updated_at` | TIMESTAMPTZ | Dernière mise à jour |

**Règles :**
- L'ID est **déterministe** : même élève (nom + classe + école) = même ID
- Stratégie de sync **"Max XP Wins"** : lors du merge local/remote, la valeur XP la plus haute est conservée
- RLS activée

### 3.2. Table `app_banners` (Dashboard)

| Colonne | Type | Description |
|---|---|---|
| `id` | UUID (PK) | ID auto-généré |
| `title` | TEXT | Titre de la bannière |
| `message` | TEXT | Message affiché dans l'app |
| `type` | TEXT | Type (info, warning, success) |
| `is_active` | BOOLEAN | Active ou non |
| `created_at` | TIMESTAMPTZ | — |

### 3.3. Table `scheduled_analyst_reports` (Dashboard)

| Colonne | Type | Description |
|---|---|---|
| `id` | UUID (PK) | — |
| `email` | TEXT | Email de destination |
| `scheduled_date` | DATE | Date d'envoi |
| `scheduled_time` | TIME | Heure d'envoi |
| `frequency` | TEXT | once / daily / weekly / monthly |
| `api_key` | TEXT | Clé Gemini pour le rapport IA |
| `is_active` | BOOLEAN | — |
| `last_sent_at` | TIMESTAMPTZ | Dernière exécution |
| `created_at` | TIMESTAMPTZ | — |

---

## 4. Schéma — Supabase Labs (Dataset Factory)

### 4.1. Table `contexts`

| Colonne | Type | Description |
|---|---|---|
| `id` | UUID (PK) | — |
| `subject` | TEXT | Matière (ex: "Mathématiques") |
| `level` | TEXT | Niveau (ex: "Terminale") |
| `style` | TEXT | telegraphic / structured |
| `content` | JSONB | Contenu du cahier de texte simulé |
| `is_used` | BOOLEAN | Deprecated (remplacé par colonnes spécifiques) |
| `used_quiz` | BOOLEAN | Ce contexte a été utilisé pour un quiz |
| `used_homework` | BOOLEAN | — |
| `used_flashcards` | BOOLEAN | — |
| `used_revision` | BOOLEAN | — |
| `used_tutor` | BOOLEAN | — |
| `pipeline_run_id` | UUID (FK) | Lien vers le run de pipeline |
| `metadata` | JSONB | Tokens, modèle utilisé |
| `created_at` | TIMESTAMPTZ | — |

**Règles :**
- Un contexte peut être utilisé par **chaque type de tâche indépendamment** (5 colonnes `used_*`)
- L'attribution atomique est gérée par la RPC `claim_unused_context` (PostgreSQL function)

### 4.2. Table `examples`

| Colonne | Type | Description |
|---|---|---|
| `id` | UUID (PK) | — |
| `task_type` | TEXT | quiz / homework / flashcards / revision / tutor |
| `subject` | TEXT | Matière |
| `level` | TEXT | Niveau scolaire |
| `mode` | TEXT | Mode spécifique (recall, single_subject, short, standard...) |
| `topic` | TEXT | Sujet du contexte |
| `context_id` | UUID (FK) | Référence vers la table contexts |
| `content` | JSONB | Contenu généré par l'IA (le "gold data") |
| `system_prompt` | TEXT | System prompt utilisé |
| `user_prompt` | TEXT | User prompt utilisé |
| `tokens_used` | INTEGER | Tokens consommés |
| `model_used` | TEXT | Modèle Gemini utilisé |
| `is_judged` | BOOLEAN | A été jugé (ou en cours de jugement) |
| `judge_score` | INTEGER | Score du juge (0-10, -1 = en cours) |
| `is_gold` | BOOLEAN | Score ≥ 9/10 = Gold Data |
| `pipeline_run_id` | UUID (FK) | — |
| `created_at` | TIMESTAMPTZ | — |

**Règles :**
- Le champ `is_judged=true, judge_score=-1` sert de **verrou pessimiste** pour empêcher le jugement concurrent
- Seuls les exemples `is_gold=true` seront exportés dans le dataset JSONL final

### 4.3. Table `judgments`

| Colonne | Type | Description |
|---|---|---|
| `id` | UUID (PK) | — |
| `example_id` | UUID (FK) | Lien vers examples |
| `score` | INTEGER | Note /10 |
| `is_gold` | BOOLEAN | Score ≥ 9 |
| `reason` | TEXT | Explication du juge si < 10 |
| `criteria` | JSONB | Détails du verdict complet |
| `tokens_used` | INTEGER | — |
| `created_at` | TIMESTAMPTZ | — |

### 4.4. Table `combos` (Déduplication)

| Colonne | Type | Description |
|---|---|---|
| `id` | UUID (PK) | — |
| `task_type` | TEXT | — |
| `subject` | TEXT | — |
| `level` | TEXT | — |
| `mode` | TEXT | — |
| `topic` | TEXT | — |
| `example_id` | UUID (FK) | — |
| `created_at` | TIMESTAMPTZ | — |

**Contrainte UNIQUE :** `(task_type, subject, level, mode, topic)` — empêche les doublons de combinaison

### 4.5. Table `pipeline_runs`

| Colonne | Type | Description |
|---|---|---|
| `id` | UUID (PK) | — |
| `config` | JSONB | Configuration du run (concurrency, targets...) |
| `status` | TEXT | running / completed / failed |
| `phase` | TEXT | context / generate / judge |
| `created_at` | TIMESTAMPTZ | — |

### 4.6. Table `lucid_labs_entries` (Legacy)

| Colonne | Type | Description |
|---|---|---|
| `id` | UUID (PK) | — |
| `type` | TEXT | quiz / flashcard / tutor_chat |
| `subject` | TEXT | — |
| `content` | JSONB | Contenu généré |
| `is_validated` | BOOLEAN | — |
| `metadata` | JSONB | — |
| `created_at` | TIMESTAMPTZ | — |

---

## 5. Fonctions RPC PostgreSQL

### 5.1. `claim_unused_context`
- **But :** Attribution atomique d'un contexte pour éviter les race conditions entre workers parallèles
- **Paramètres :** `p_task_type`, `p_subject`, `p_level`
- **Logique :** `UPDATE ... SET used_{task_type} = true WHERE used_{task_type} = false ... LIMIT 1 RETURNING *`

### 5.2. `try_register_combo`
- **But :** Enregistrement atomique d'une combinaison (INSERT OR DO NOTHING)
- **Paramètres :** `p_task_type`, `p_subject`, `p_level`, `p_mode`, `p_topic`, `p_example_id`
- **Retourne :** `true` si nouveau (inséré), `false` si déjà existant

### 5.3. `get_dashboard_stats_rpc`
- **But :** Statistiques agrégées pour le dashboard Labs
- **Retourne :** Totaux par tâche (total, gold, judged), unjudged count

---

## 6. Sécurité des Données

| Mesure | Détail |
|---|---|
| **Row Level Security (RLS)** | Activée sur toutes les tables |
| **Service Role Key** | Utilisée uniquement côté serveur (Server Actions Next.js) |
| **Anon Key** | Utilisée côté client (accès limité) |
| **Pas de données scolaires en BDD** | Notes, EDT, devoirs stockés uniquement en local (AsyncStorage) |
| **Identifiants Pronote** | Stockés chiffrés localement (Expo SecureStore), jamais en BDD |
