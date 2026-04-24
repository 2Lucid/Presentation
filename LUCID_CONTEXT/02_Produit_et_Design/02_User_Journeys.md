# 🚶 User Journeys — LUCID

---

## Journey 1 — Premier Lancement (Onboarding Élève)

### Contexte
Un élève du Lycée Henri Matisse découvre LUCID via un QR code dans le couloir ou un ami.

### Étapes

```
1. 📱 SCAN/DOWNLOAD
   └─ L'élève scanne le QR code
   └─ Lucid Redirect détecte iOS → redirige vers App Store
   └─ Téléchargement + installation
   
2. 🚀 PREMIER LANCEMENT
   └─ Écran d'accueil avec branding LUCID (dark mode, gradients)
   └─ Bouton "Se connecter avec Pronote"
   
3. 🔑 AUTHENTIFICATION PRONOTE
   └─ Sélection de l'établissement (URL Pronote auto-détectée ou manuelle)
   └─ Saisie identifiants Pronote (login + mot de passe)
   └─ Transit sécurisé via proxy API (HTTPS/TLS)
   └─ Si ENT (Atrium) → WebView pour SSO
   └─ Pawnote library crée la session
   
4. 👤 CRÉATION DE PROFIL
   └─ Extraction automatique du nom depuis Pronote (GetIdentityFromPronoteUsername)
   └─ Génération d'un auth_id déterministe (deterministicUUID.ts)
   └─ syncProfile() → Supabase : création ou adoption du profil
   └─ Initialisation du gamificationStore local (AsyncStorage)
   └─ Premier sync : XP = 0, Niveau = 1, Badges = []
   
5. 🏠 HOME SCREEN
   └─ Affichage des notes récentes (cache offline créé)
   └─ Emploi du temps du jour
   └─ Devoirs à venir
   └─ Widget XP + Niveau
   └─ CTA "Commencer un quiz" / "Explorer l'IA"
```

### Points critiques
- ⚠️ Le parsing des noms composés (ex: "BELLET-ODENT Clément") nécessite le regex de `GetIdentityFromPronoteUsername` — un split naïf casse les noms à tiret
- ⚠️ `syncProfile()` doit appeler `gamificationStore.syncFromSupabase()` pour éviter la désynchronisation XP

---

## Journey 2 — Utilisation Quotidienne (Consultation + XP)

### Contexte
L'élève ouvre LUCID le matin avant les cours.

```
1. 📱 OUVERTURE APP
   └─ Chargement depuis cache (AsyncStorage) → affichage instantané
   └─ En arrière-plan : fetchProfile() → sync Supabase → sync gamificationStore
   
2. 📊 CONSULTATION NOTES
   └─ Nouvelles notes détectées (badge de notification)
   └─ Affichage détaillé par matière
   └─ XP automatiquement calculé si bonne note
   └─ Animation d'XP gagné (micro-animation)
   
3. 📅 EMPLOI DU TEMPS
   └─ Vue du jour avec cours à venir
   └─ Option "Ajouter au calendrier iOS"
   
4. 📝 DEVOIRS
   └─ Liste des devoirs par deadline
   └─ Bouton "IA Aide aux Devoirs" sur chaque devoir
   
5. 🏆 REWARDS (Tab Rewards)
   └─ Affichage de la progression XP et niveau
   └─ Badges débloqués et verrouillés
   └─ Source : gamificationStore (local)
```

---

## Journey 3 — Révision avec l'IA (Quiz avant un contrôle)

### Contexte
L'élève a un contrôle de SVT demain. Il utilise LUCID pour réviser.

```
1. 🧠 ACCÈS IA
   └─ Tab "IA" ou bouton contextuel depuis les devoirs
   └─ Sélection du type : "Quiz QCM"
   
2. ⚙️ CONFIGURATION
   └─ Mode : "single_subject" (SVT uniquement)
   └─ Les cours SVT récents sont automatiquement extraits de Pronote
   └─ Optionnel : précision de l'élève ("je veux réviser la photosynthèse")
   
3. ⏳ GÉNÉRATION
   └─ Appel à Gemini API (system prompt + user prompt + contexte cours)
   └─ Parsing JSON de la réponse
   └─ Validation : 10 questions exactement ?
   
4. 📝 QUIZ
   └─ Affichage question par question (UI interactive)
   └─ Selection de la réponse (A/B/C/D)
   └─ Feedback immédiat : bonne/mauvaise réponse + explication
   └─ Barre de progression (1/10 → 10/10)
   
5. 📊 RÉSULTAT
   └─ Score final (ex: 8/10)
   └─ XP gagné pour la tentative
   └─ Bouton "Refaire" / "Autre quiz"
   └─ Animation celebrate si score > 7/10
```

---

## Journey 4 — Tuteur Socratique (Comprendre un concept)

### Contexte
L'élève ne comprend pas les dérivées en Maths.

```
1. 🎓 ACCÈS TUTEUR
   └─ Tab "IA" → "Tuteur"
   └─ Matière auto-détectée ou sélection manuelle
   
2. 💬 CONVERSATION
   └─ L'élève pose sa question : "c'est quoi la dérivée de x² ?"
   └─ Le tuteur NE répond PAS directement
   └─ Le tuteur pose une question : "Tu te souviens de la formule (x^n)' = n×x^(n-1) ?"
   └─ L'élève hésite : "ah oui je crois... donc c'est 2x ?"
   └─ Le tuteur confirme et consolide : "Exactement ! Et pour x³, ça donnerait ?"
   
3. 🔄 BOUCLE SOCRATIQUE
   └─ L'IA continue de guider sans jamais donner les réponses
   └─ Elle reformule si l'élève se trompe
   └─ Elle donne des indices progressifs
   
4. ✅ FIN DE SESSION
   └─ L'élève quitte quand il a compris
   └─ XP gagné pour la session de tutorat
```

---

## Journey 5 — Social / Compétition (Leaderboard)

```
1. 🏆 CLASSEMENT
   └─ Tab "Classement" ou "Rewards"
   └─ Vue du leaderboard de l'établissement
   └─ Position de l'élève mise en évidence
   └─ Top 3 avec animation spéciale

2. 👥 AMIS
   └─ Ajout d'amis par recherche de nom
   └─ Notification de demande reçue (bell icon + red dot)
   └─ Modal de gestion des demandes (accepter/refuser)
   └─ Vue comparée de la progression

3. 🔔 NOTIFICATIONS
   └─ Push notification quand un ami dépasse l'élève au classement
   └─ Rappel de devoirs non faits
   └─ Nouveau badge débloqué
```

---

## Journey 6 — Lucid Prof (Professeur)

### Contexte
Un professeur de Maths veut créer un quiz pour sa classe de 3ème.

```
1. 🔑 CONNEXION
   └─ lucid-prof.vercel.app
   └─ Authentification via Supabase (email/password)
   
2. 📝 CRÉATION DE CONTENU
   └─ Option A (Manuel) : Le prof tape son contenu directement
   └─ Option B (IA) : Le prof fournit des instructions + plan de cours
   └─ L'IA (@google/generative-ai) génère les exercices
   
3. ✅ VALIDATION
   └─ Le prof revoit, modifie si nécessaire
   └─ Publication dans la base Supabase
   
4. 📲 DISTRIBUTION
   └─ Les exercices sont automatiquement disponibles pour les élèves
   └─ dans l'application LUCID mobile
```

---

## Journey 7 — Conversion Freemium → Pro (Futur)

```
1. 🔒 FRICTION FREEMIUM
   └─ L'élève atteint la limite de quiz gratuits (ex: 3/jour)
   └─ Popup : "Débloquer les quiz illimités avec LUCID Pro"
   
2. 💳 UPGRADE
   └─ Présentation de l'offre Pro (4.99€/mois)
   └─ Features Pro : Quiz illimités, Tuteur prioritaire, Badges exclusifs
   └─ Paiement via Apple In-App Purchase
   
3. ✅ ACTIVATION
   └─ Déblocage immédiat
   └─ Badge "Pro" affiché sur le profil
```
