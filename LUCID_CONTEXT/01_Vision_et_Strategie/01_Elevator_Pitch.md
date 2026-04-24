# 🚀 Elevator Pitch — LUCID

---

## 🎯 En 1 Phrase

**LUCID est l'application mobile IA qui transforme le parcours scolaire des lycéens et collégiens français en une expérience gamifiée, motivante et intelligente, directement depuis leur poche.**

---

## 📝 En 1 Paragraphe

LUCID est une application mobile éducative créée **par des élèves, pour des élèves**, née au sein du Lycée Henri Matisse à Vence (06). Elle se connecte directement à Pronote (et bientôt École Directe) pour récupérer les notes, l'emploi du temps et les devoirs de l'élève, puis les transforme en une expérience moderne et engageante. Sa force : une **IA embarquée on-device** (modèles Gemma E2B/E4B fine-tunés + RAG) qui fonctionne sans connexion, un système de **gamification** (XP, niveaux, badges, classements), et **5 assistants pédagogiques IA** (quiz adaptatifs, flashcards, fiches de révision, tuteur socratique, aide aux devoirs). LUCID réinvente l'interface entre l'élève et sa scolarité, avec une IA qui tourne directement dans la poche de l'élève. L'application est disponible sur l'App Store (iOS) et bientôt sur Google Play.

---

## 📄 En 1 Page

### Le Constat

Les interfaces scolaires actuelles (Pronote, ENT) sont **datées, froides et démotivantes**. Les élèves les subissent au lieu de les utiliser activement. L'engagement scolaire chute, et les outils existants ne parlent pas le langage de la génération actuelle — celle des apps, du gaming et de l'instantanéité.

### La Solution : LUCID

LUCID est une **application mobile iOS** (React Native / Expo) qui agit comme un compagnon intelligent et motivant pour l'élève. Elle se décompose en trois piliers fondamentaux :

**1. Hub Scolaire Unifié 📱**
L'application se connecte aux systèmes scolaires existants (Pronote via un proxy API open-source) et présente les données académiques — notes, emploi du temps, devoirs, absences — dans une interface ultra-moderne, fluide et intuitive. Fini les interfaces Web des années 2000.

**2. IA Pédagogique Edge-First 🧠**
LUCID embarque des **modèles d'IA fine-tunés** (Gemma E2B / E4B) directement sur l'appareil de l'élève, couplés à un système de **RAG (Retrieval-Augmented Generation)** qui injecte le contexte scolaire réel. Cette architecture "edge AI" permet une IA instantanée, privée (les données restent sur l'appareil) et disponible même hors-ligne. Les 5 assistants pédagogiques :
- **Quiz QCM** adaptatifs générés à partir des cours réels de l'élève
- **Flashcards** pour la mémorisation active (3 modes)
- **Fiches de Révision** structurées (courtes, régulières, longues)
- **Aide aux Devoirs** méthodologique (sans donner les réponses)
- **Tuteur Socratique** conversationnel qui guide par le questionnement

Toutes ces fonctionnalités utilisent le **vrai contexte scolaire** de l'élève (ses cours Pronote) via le RAG, rendant l'apprentissage hyper-personnalisé. En phase de beta, l'API Gemini est utilisée temporairement pour garantir la fluidité de l'expérience pendant la finalisation du modèle edge.

**3. Gamification & Communauté 🏆**
Un système complet de points d'expérience (XP), de niveaux, de badges et de classements (leaderboard) transforme chaque interaction scolaire en récompense. Les élèves sont motivés par la progression, la compétition amicale et les succès débloquables.

### L'Équipe

LUCID est fondée par **2 étudiants** passionnés : **Lucas Gerhardt** (CTO — architecture technique, IA, développement full-stack) et **Clément Bellet-Odent** (CEO — vision stratégique, partenariats, communication). Le projet est né d'une frustration partagée et d'une ambition commune : prouver que l'école peut être aussi captivante que nos apps préférées.

### Traction & Reconnaissance

- 🏆 **Lauréat Science Factor** — Prix Lycée + Prix Orange Numérique
- 📺 **Passage sur France 3** (reportage télévisé)
- 🍎 **Publiée sur l'App Store** (iOS) — ID : `id6757653389`
- 📋 **Dépôt de brevet** en partenariat avec **AXEPI** (cabinet de propriété intellectuelle)
- 🎯 **Concours Beta Test** au Lycée Henri Matisse avec prizes réelles (50€, 25€, 10€)
- 🔬 **Lucid Labs** — Plateforme R&D générant 10 000+ exemples de données pour le fine-tuning d'un modèle IA propriétaire

### La Vision

> *"Nous ne construisons pas seulement une application, nous construisons le futur de l'engagement étudiant."*

L'objectif est de positionner LUCID comme la **technologie de référence** pour l'expérience scolaire numérique en France, avec un modèle IA propriétaire edge-first entraîné sur des données pédagogiques françaises Gold Data. La stratégie de sortie privilégiée est une **acquisition par un acteur majeur de l'éducation** (ex: Index Éducation / Pronote) qui bénéficierait de la technologie IA et du brevet de gamification, tout en permettant aux fondateurs de conserver une participation.
