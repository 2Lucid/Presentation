# 🎉 Onboarding Client — LUCID

---

## 1. Flux d'Onboarding (App Mobile)

### 1.1. Pré-requis
- iPhone avec iOS 16+
- Compte Pronote actif (identifiants élève)
- Connexion Internet

### 1.2. Étapes Détaillées

```
ÉTAPE 1 — TÉLÉCHARGEMENT
├── Scan QR code (lucid_redirect) OU recherche "Lucid" sur l'App Store
├── lucid_redirect détecte iOS → redirige vers App Store
├── Téléchargement (~50MB)
└── Installation automatique

ÉTAPE 2 — LANCEMENT
├── Écran de bienvenue avec branding LUCID (dark mode)
├── Animations d'accueil premium (Framer Motion style)
└── Bouton "Commencer" / "Se connecter avec Pronote"

ÉTAPE 3 — CONNEXION PRONOTE
├── Sélection de la méthode :
│   ├── Connexion directe Pronote (login + mot de passe)
│   └── Connexion via ENT (ex: Atrium pour l'académie de Nice → WebView SSO)
├── Saisie de l'URL Pronote (auto-détectée ou manuelle)
├── Saisie des identifiants
├── Transit sécurisé via le proxy API (HTTPS/TLS)
└── Vérification de session réussie ✅

ÉTAPE 4 — CRÉATION DE PROFIL
├── Extraction automatique du nom depuis Pronote
│   └── Utilisation de GetIdentityFromPronoteUsername (regex)
│   └── Gestion des noms composés (ex: BELLET-ODENT)
├── Génération d'un auth_id déterministe
│   └── deterministicUUID.ts (basé sur nom + classe + école)
├── syncProfile() → Supabase
│   ├── Si profil existant avec cet ID → adoption ("bienvenue à nouveau !")
│   └── Si pas de profil → création (XP=0, Level=1, Badges=[])
├── gamificationStore.syncFromSupabase() ← CRITIQUE
└── Cache local initialisé (AsyncStorage)

ÉTAPE 5 — PREMIER ÉCRAN (HOME)
├── Affichage des notes récentes
├── Emploi du temps du jour
├── Widget XP (0 XP, Niveau 1)
├── CTA : "Fais ton premier quiz ! 🧠"
└── Notification de bienvenue : "Bienvenue sur LUCID ! +10 XP 🎉"
```

---

## 2. Activation (Premier "Aha Moment")

### 2.1. Objectif
L'élève doit vivre son **premier moment "wow"** en moins de 5 minutes après l'installation.

### 2.2. Parcours d'Activation Idéal

| Minute | Action | Émotion |
|---|---|---|
| 0 | Installation + lancement | Curiosité |
| 1 | Connexion Pronote | Attente |
| 2 | Voir ses notes dans LUCID | **WOW** — "C'est trop beau" |
| 3 | Lancer un quiz IA | Excitation |
| 4 | Répondre aux questions | Engagement |
| 5 | Score + premiers XP gagnés | **Satisfaction** + Envie de continuer |

### 2.3. Métriques d'Activation

| KPI | Seuil de Succès |
|---|---|
| % de complétion de l'onboarding | >70% |
| % qui lancent un quiz dans la première session | >30% |
| % qui ouvrent l'app le lendemain (D1 Retention) | >50% |
| Time to first value | <5 min |

---

## 3. Checklist de Premier Usage

- [x] Télécharger l'app
- [x] Se connecter à Pronote
- [x] Voir ses notes
- [ ] Faire un quiz IA
- [ ] Consulter le leaderboard
- [ ] Ajouter un ami
- [ ] Personnaliser son profil

---

## 4. Erreurs Courantes à l'Onboarding

| Erreur | Cause | Solution |
|---|---|---|
| "Connexion Pronote échouée" | Mauvais identifiants ou URL Pronote incorrecte | Guide interactif avec les URLs fréquentes + lien de support |
| "Session expirée" | Token Pronote expiré | Reconnexion automatique en arrière-plan |
| XP affiché à 0 mais profil ancien | `syncProfile()` ne call pas `syncFromSupabase()` | Bug identifié et documenté (Knowledge Item) |
| Nom composé mal parsé | Split naïf au lieu de regex | Utiliser `GetIdentityFromPronoteUsername` (regex-based) |

---

## 5. Onboarding Professeur (Lucid Prof)

### 5.1. Pré-requis
- Navigateur web moderne
- Compte email

### 5.2. Étapes

1. **Accès :** `lucid-prof.vercel.app`
2. **Inscription :** Email + mot de passe (Supabase Auth)
3. **Premier cours :** Créer ou importer un contenu de cours
4. **Génération IA :** L'IA génère des exercices à partir du contenu
5. **Validation :** Le prof revoit et publie
6. **Distribution :** Les exercices sont disponibles pour les élèves dans l'app

> **Statut :** Le onboarding prof est en beta, pas encore ouvert au public.
