# 🎯 Fonctionnalités Core — MVP LUCID

---

## 1. Périmètre du MVP (Minimum Viable Product)

Le MVP de LUCID comprend les fonctionnalités suivantes, toutes opérationnelles et publiées sur l'App Store iOS.

---

## 2. Module 1 — Hub Scolaire (Connexion Pronote)

### 2.1. Authentification Pronote
- Connexion aux comptes élèves via identifiants Pronote (login/mot de passe)
- Transit sécurisé via un proxy API Node.js open-source (`pronotebackend`)
- Support des ENT (Atrium pour l'académie de Nice)
- Stockage sécurisé des tokens de session via `Expo SecureStore`
- Détection automatique de l'établissement via URL Pronote

### 2.2. Consultation des Notes
- Affichage des notes par matière avec graphiques de progression
- Calcul de moyennes par matière et moyenne générale
- Visualisation des tendances (hausse/baisse)
- Cache offline via AsyncStorage

### 2.3. Emploi du Temps
- Vue dynamique de l'emploi du temps quotidien et hebdomadaire
- Export vers le calendrier iOS natif (`WRITE_CALENDAR`)
- Détection des cours annulés / remplacés

### 2.4. Devoirs
- Liste des devoirs avec filtrage par matière et date
- Marquage "fait" / "non fait"
- Passerelle vers l'aide IA

### 2.5. Absences & Retards
- Consultation du registre d'absences et retards
- Notification visuelle

---

## 3. Module 2 — IA Pédagogique (5 Assistants)

### 3.1. Quiz QCM (📝)
- **Input :** Cours Pronote de l'élève (cahier de texte)
- **Output :** 10 questions QCM structurées en JSON
- **3 modes :**
  - `recall` — Quiz multi-matières basé sur les cours du lendemain
  - `single_subject` — Quiz mono-matière
  - `all_subjects` — Quiz toutes matières combinées
- **Règles pédagogiques :**
  - 4 propositions plausibles par question
  - Répartition équilibrée des bonnes réponses (A/B/C/D)
  - Explications détaillées pour chaque réponse
  - Tags par notion testée
- **Modèle :** Gemma E2B/E4B fine-tuné (inférence locale on-device). Gemini Flash utilisé temporairement en phase beta.

### 3.2. Flashcards (🃏)
- **Input :** Contenu de cours + niveau scolaire
- **Output :** 12 cartes recto/verso structurées en JSON
- **3 modes :**
  - `standard` — Questions/réponses classiques
  - `word_for_word` — Définitions mot-à-mot à apprendre par cœur
  - `long_definition` — Explications étendues et détaillées
- **Chaque carte contient :**
  - `front` (question/terme)
  - `back` (réponse auto-suffisante)
  - `retentionScore` (pour la répétition espacée future)

### 3.3. Fiches de Révision (📋)
- **Input :** Contenu de cours + niveau scolaire
- **Output :** Fiche structurée en JSON avec sections prédéfinies
- **3 longueurs :** `short`, `regular`, `long`
- **Sections obligatoires :**
  1. Objectifs et enjeux
  2. L'essentiel (avec mise en gras)
  3. Pièges et erreurs fréquentes
  4. Méthode et astuces
  5. Exemple concret
- **Format Markdown** dans le contenu des sections

### 3.4. Aide aux Devoirs (📚)
- **Input :** Devoir spécifique Pronote + niveau scolaire
- **Output :** Aide méthodologique en JSON (jamais la solution !)
- **Contenu de l'aide :**
  - Reformulation claire de la consigne
  - Plan d'action étape par étape
  - Checklist de vérification
  - Erreurs fréquentes à éviter
  - Astuces et conseils pratiques
  - Exemples d'amorçage (génériques, pas la solution)
- **Méthode selon le type :**
  - Exercice → Identifie données, résultats attendus, propose une stratégie
  - Leçon → Protocole de mémorisation active (auto-interrogation)

### 3.5. Tuteur Socratique (🎓)
- **Type :** Conversation libre multi-tour (chat)
- **Principe :** L'IA pose des questions au lieu de donner des réponses
- **Règles de comportement :**
  - 1 question à la fois
  - Part de ce que l'élève sait, construit dessus
  - Ne corrige jamais brutalement (reformule, donne des indices)
  - Tutoie l'élève, reste concis (2-3 phrases)
  - Ne donne JAMAIS la réponse directement

---

## 4. Module 3 — Gamification

### 4.1. Système XP
- Attribution d'XP pour : bonnes notes, devoirs rendus, quiz complétés, connexions quotidiennes
- Total XP = indicateur de progression global
- Synchronisation bidirectionnelle locale ↔ Supabase (stratégie "Max XP Wins")

### 4.2. Niveaux & Titres
- Système de niveaux progressifs (1 → ∞)
- Titres débloquables à chaque palier
- Barre de progression visuelle vers le niveau suivant

### 4.3. Badges / Succès
- Récompenses thématiques débloquables (ex: "Maître des Maths", "Polyglotte")
- Badges rares et badges communs
- Affichage sur le profil

### 4.4. Leaderboard (Classement)
- Classement entre élèves d'un même établissement
- Données en temps réel via Supabase
- Top 3 mis en avant visuellement
- Accessible sur le site officiel (page Concours)

### 4.5. Système d'Amis
- Ajout d'amis par recherche
- Notifications de demandes d'amitié (bell icon + red dot badge)
- Comparaison de progression entre amis

---

## 5. Module 4 — Personnalisation

### 5.1. Profil Utilisateur
- Avatar personnalisable
- Nom d'affichage
- Titre sélectionnable (débloqué via les niveaux)
- Statistiques de progression

### 5.2. Préférences
- Choix du thème (dark mode par défaut)
- Paramètres de notification
- Gestion de la connexion Pronote

---

## 6. Fonctionnalités Exclues du MVP

| Fonctionnalité | Raison de l'exclusion | Phase prévue |
|---|---|---|
| Carte Mentale IA | Complexité de rendu visuel en mobile | Phase 2 |
| Mode multi-joueur (défis) | Nécessite infrastructure temps réel | Phase 2 |
| Support École Directe | Priorité à Pronote (>80% marché) | Phase 2 |
| Tableau de bord parental | Cible secondaire | Phase 2 |
| Import notes manuscrites (OCR) | R&D nécessaire | Phase 3 |
| Mode hors-ligne IA (inférence locale) | Déjà intégré (Gemma edge) — optimisation continue | Phase 1 |
| Android | Développement en cours | Phase 1 |
