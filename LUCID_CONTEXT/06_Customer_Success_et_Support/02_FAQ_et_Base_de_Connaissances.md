# ❓ FAQ et Base de Connaissances — LUCID

---

## 1. Questions Générales

### Q: C'est quoi LUCID ?
**R:** LUCID est une application mobile gratuite qui se connecte à ton compte Pronote et transforme ton expérience scolaire. Tu retrouves tes notes, ton emploi du temps et tes devoirs dans une interface moderne et stylée, avec en plus une IA qui t'aide à réviser (quiz, flashcards, fiches) et un système de gamification (XP, niveaux, badges, classement).

### Q: C'est gratuit ?
**R:** Oui ! LUCID est 100% gratuit actuellement. À terme, une version Pro sera disponible à 4.99€/mois avec des fonctionnalités IA illimitées, mais le cœur de l'app (notes, EDT, gamification) restera toujours gratuit.

### Q: Qui a créé LUCID ?
**R:** LUCID a été créé par 2 lycéens passionnés du Lycée Henri Matisse (Vence) : Lucas Gerhardt (CTO) et Clément Bellet-Odent (CEO). Le projet a remporté le prix Science Factor (Prix Lycée + Prix Orange Numérique) et a été couvert par France 3.

### Q: Sur quels appareils ça fonctionne ?
**R:** LUCID est disponible sur iPhone (iOS 16+) via l'App Store. La version Android est en cours de développement.

### Q: LUCID remplace Pronote ?
**R:** Non ! LUCID ne remplace pas Pronote, il l'enrichit. Tu continues d'avoir ton compte Pronote normalement, mais LUCID te propose une interface bien plus moderne, l'IA pour réviser, et la gamification pour te motiver.

---

## 2. Connexion et Compte

### Q: Comment me connecter ?
**R:** 
1. Ouvre LUCID
2. Clique "Se connecter avec Pronote"
3. Entre l'URL de ton Pronote (ou sélectionne ton établissement)
4. Entre tes identifiants Pronote (login et mot de passe)
5. C'est fait ! Tes données apparaissent automatiquement.

### Q: Mon établissement utilise un ENT (Atrium, etc.), comment faire ?
**R:** Si ton établissement utilise un ENT, LUCID te proposera une connexion via WebView. Tu te connecteras à ton ENT normalement et LUCID récupérera tes données.

### Q: Mes identifiants sont-ils stockés ?
**R:** Tes identifiants Pronote sont stockés de manière chiffrée uniquement sur TON appareil (via Expo SecureStore). Ils ne sont jamais stockés en clair sur nos serveurs. Le transit est chiffré en HTTPS/TLS.

### Q: J'ai oublié mes identifiants Pronote
**R:** LUCID ne gère pas les identifiants Pronote. Contacte le secrétariat de ton établissement ou le service informatique pour récupérer tes identifiants.

### Q: Mes notes n'apparaissent pas
**R:**
1. Vérifie ta connexion Internet
2. Relance l'application
3. Si le problème persiste, déconnecte-toi et reconnecte-toi à Pronote
4. Certaines données peuvent mettre quelques secondes à charger

---

## 3. IA et Fonctionnalités

### Q: Comment l'IA génère les quiz ?
**R:** LUCID embarque des modèles d'IA fine-tunés (Gemma E2B/E4B) directement sur ton téléphone. L'IA analyse le contenu de tes cours dans Pronote grâce à un système de RAG (Retrieval-Augmented Generation) et génère des questions QCM adaptées. Les quiz sont basés sur TES vrais cours, pas sur du contenu générique. En phase beta, l'API Gemini est utilisée temporairement en complément pour garantir la fluidité.

### Q: L'IA fait mes devoirs à ma place ?
**R:** Non ! L'IA de LUCID est conçue pour t'aider à COMPRENDRE, pas pour te donner les réponses. Le tuteur socratique te guide par des questions, l'aide aux devoirs te donne des stratégies et des exemples sans résoudre le devoir.

### Q: Quels sont les différents modes de quiz ?
**R:**
- **Recall** : Quiz multi-matières basé sur les cours du lendemain
- **Single Subject** : Quiz sur une seule matière
- **All Subjects** : Quiz qui mélange toutes les matières

### Q: Combien de quiz puis-je faire par jour ?
**R:** Actuellement, illimité (version gratuite complète). À terme, la version gratuite sera limitée à 3 quiz/jour, la version Pro sera illimitée.

### Q: L'IA se trompe parfois, que faire ?
**R:** Comme toute IA, LUCID peut occasionnellement commettre des erreurs. Si tu repères une erreur, signale-la. Nos prompts sont conçus pour garantir la rigueur pédagogique, et nous travaillons constamment à améliorer la qualité.

---

## 4. Gamification

### Q: Comment gagner de l'XP ?
**R:** Tu gagnes de l'XP en :
- Ayant de bonnes notes
- Rendant tes devoirs
- Complétant des quiz IA
- Te connectant quotidiennement

### Q: Qu'est-ce que le leaderboard ?
**R:** Le leaderboard est un classement de tous les élèves de ton lycée par XP. Les 3 premiers sont mis en avant. C'est une compétition amicale pour te motiver !

### Q: Mon XP n'est pas synchronisé entre mes appareils
**R:** LUCID utilise une stratégie "Max XP Wins" : la valeur la plus haute entre ton appareil et le serveur est conservée. Si tu vois une incohérence, relance l'app pour forcer la synchronisation.

### Q: Comment débloquer des badges ?
**R:** Les badges se débloquent automatiquement en atteignant certains objectifs (un certain niveau, un nombre de quiz complétés, etc.). Consulte la page Rewards pour voir les badges disponibles.

---

## 5. Sécurité et Confidentialité

### Q: Mes données sont-elles en sécurité ?
**R:** Oui. Voici nos mesures de sécurité :
- Chiffrement HTTPS/TLS pour toutes les communications
- **IA embarquée on-device** : tes données scolaires ne quittent jamais ton téléphone
- Identifiants stockés chiffrés localement (jamais sur nos serveurs)
- Données scolaires stockées uniquement en local sur ton appareil
- Proxy Pronote open-source (code vérifiable sur GitHub)
- Conformité RGPD complète

### Q: Est-ce que vous vendez mes données ?
**R:** **Non, jamais.** C'est écrit noir sur blanc dans notre politique de confidentialité. Nous ne vendons aucune donnée personnelle à des tiers.

### Q: Comment supprimer mon compte ?
**R:** Va dans Paramètres → "Supprimer mon compte". Toutes tes données seront effacées de nos serveurs sous 30 jours, conformément au RGPD.

### Q: Qui est le responsable de traitement ?
**R:** Pierre Aboussouan, Lycée Henri Matisse, Vence. Contact : pierre.aboussouan@ac-nice.fr

---

## 6. Support

### Q: J'ai un problème, comment contacter le support ?
**R:** 
- **Instagram DM :** @_lucid_app_ (réponse <24h)
- **Email :** Via la page Contact sur le site officiel
- **In-app :** Paramètres → Contact/Support

### Q: L'app crash / bug
**R:**
1. Ferme et relance l'app
2. Vérifie que tu as la dernière version (App Store → Mises à jour)
3. Redémarre ton iPhone
4. Si le problème persiste, contacte-nous via Instagram avec une capture d'écran
