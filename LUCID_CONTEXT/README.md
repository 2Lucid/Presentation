# 📁 LUCID — Dossier Contexte Complet

> **Version :** V1 — Avril 2026  
> **Objectif :** Fournir un contexte exhaustif et structuré de l'ensemble du projet LUCID pour l'IA, l'audit, le développement et la planification stratégique.

---

## 🏗️ Architecture du Dossier

```
LUCID_CONTEXT/
│
├── 📁 01_Vision_et_Strategie/
│   ├── 📄 01_Elevator_Pitch.md            → Résumé en 1 phrase, 1 paragraphe, 1 page
│   ├── 📄 02_Probleme_et_Solution.md      → Pain point marché + 3 couches de solution
│   ├── 📄 03_Cibles_et_Personas.md        → 6 personas détaillés + matrice TAM/SAM/SOM
│   ├── 📄 04_Analyse_Concurrentielle.md   → Mapping concurrents + Unfair Advantage
│   └── 📄 05_Roadmap_Globale.md           → 3 mois, 6 mois, 1 an, 5 ans
│
├── 📁 02_Produit_et_Design/
│   ├── 📄 01_Fonctionnalites_Core.md      → 4 modules MVP détaillés
│   ├── 📄 02_User_Journeys.md             → 7 parcours utilisateur complets
│   ├── 📄 03_Design_System.md             → Couleurs, typo, composants, animations
│   └── 📄 04_Backlog_et_Features_Futures.md → 35+ features priorisées
│
├── 📁 03_Engineering_et_Architecture/
│   ├── 📄 01_Stack_Technique.md           → Tech stack complet (every package)
│   ├── 📄 02_Architecture_Systeme.md      → Schémas d'architecture + flux de données
│   ├── 📄 03_Base_de_Donnees.md           → Schéma complet PostgreSQL + RPCs
│   ├── 📄 04_API_et_Integrations.md       → Gemini, Pronote, Supabase, Resend…
│   └── 📄 05_DevOps_et_CI_CD.md           → Déploiement, tests, monitoring, coûts
│
├── 📁 04_Marketing_et_Acquisition/
│   ├── 📄 01_Brand_Voice.md               → Ton, vocabulaire, slogans, emojis
│   ├── 📄 02_Strategie_Go_To_Market.md    → GTM en 3 phases avec funnel complet
│   ├── 📄 03_SEO_et_Content.md            → Mots-clés, piliers de contenu, ASO
│   └── 📄 04_Canaux_Acquisition.md        → 13 canaux détaillés par phase
│
├── 📁 05_Sales_et_Business_Model/
│   ├── 📄 01_Pricing_et_Tiers.md          → Free / Pro / Enterprise + projections
│   ├── 📄 02_Sales_Playbook.md            → Arguments B2C/B2B, scripts, objections
│   └── 📄 03_KPIs_et_Metriques.md         → 50+ KPIs par catégorie
│
├── 📁 06_Customer_Success_et_Support/
│   ├── 📄 01_Onboarding_Client.md         → Flow d'onboarding + métriques activation
│   └── 📄 02_FAQ_et_Base_de_Connaissances.md → 30+ Q&A structurées
│
├── 📁 07_Operations_et_Equipe/
│   ├── 📄 01_Equipe_et_Roles.md           → 2 fondateurs, exit strategy, branding TODO
│   └── 📄 02_Juridique_et_RGPD.md         → Brevet, RGPD, CGU, données mineur
│
├── 📄 08_Glossaire.md                     → 60+ termes définis
│
└── 📄 README.md                           → CE FICHIER (index)
```

---

## 📊 Chiffres Clés

| Métrique | Valeur |
|---|---|
| 🏗️ Projets dans l'écosystème | 10 (1 app mobile + 8 sites + 1 proxy) |
| 📁 Repositories | 3 (app mobile / sites satellites / proxy Pronote) |
| 🧠 Architecture IA | **Edge-First** (Gemma E2B/E4B fine-tuné + RAG on-device) |
| 🧠 Tâches IA | 5 (quiz, flashcards, revision, homework, tutor) |
| 📊 Dataset cible | 10 000 exemples Gold Data |
| 🏆 Distinctions | Science Factor (Prix Lycée + Prix Orange) |
| 📺 Médias | France 3 |
| 🍎 App Store | Publié (iOS) — id6757653389 |
| 💰 Pricing prévu | Free / Pro 4.99€/mois / Enterprise sur devis |
| 👥 Équipe | **2 co-fondateurs** (Lucas Gerhardt, Clément Bellet-Odent) |
| 🔐 Brevet | Dépôt en cours (AXEPI) |
| 🎯 Exit Strategy | Acquisition (Index Éducation / Pronote) ou levée de fonds |

---

## 🎯 Comment Utiliser ce Dossier

### Pour le Développement (IA Assistant)
```
Contexte minimal : 01_Elevator_Pitch.md + 03_Design_System.md + 01_Stack_Technique.md
Contexte complet : Tout le dossier 01/ + 02/ + 03/
```

### Pour le Marketing
```
Contexte : 01_Elevator_Pitch.md + 01_Brand_Voice.md + 02_Strategie_GTM.md
```

### Pour les Investisseurs
```
Contexte : 01/ complet + 05/ complet + 04_Analyse_Concurrentielle.md
```

### Pour la Conformité / Juridique
```
Contexte : 02_Juridique_et_RGPD.md + 02_FAQ.md
```

---

## ⚠️ Notes

- Ce dossier est une **V1**. Certaines sections (notamment les métriques exactes d'utilisateurs et les projections financières) nécessitent une mise à jour régulière.
- Les informations techniques (stack, schéma BDD) sont **synchronisées avec le code source** au moment de la rédaction.
- Pour les détails techniques précis, toujours se référer au code source dans `apps/` et `sites/`.
