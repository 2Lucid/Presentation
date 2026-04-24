# 🎤 LUCID — Script Oral V4

*Durée visée : 10 minutes / 4 Présentateurs*
*Concours : C'Génial 2026 / Faites de la Science*

---

## 🎭 1. Rôles et Placement

**A (Coordinateur)** : Ouvre et ferme la présentation. Porte la problématique, les transitions et la conclusion. Distribue les rapports scientifiques (PISA).
**B (Architecte technique)** : Explique les choix techniques et l'architecture locale. Distribue les fiches plastifiées de l'architecture et guide le jury dessus.
**C (Responsable Recherche & Évaluation)** : Présente les fondements scientifiques, le protocole d'évaluation et la discussion critique. Distribue l'étude du MIT.
**D (Démonstrateur)** : Gère les démonstrations live sur les téléphones. Apporte les preuves expérimentales en temps réel.

> **Note :** Si seulement 2 présentateurs, A absorbe C et B absorbe D.

---

## 🎬 2. Le Script

---

### ⏱️ 0:00 → 1:45 — PROBLÉMATIQUE & ACCROCHE (A + D)

**[A s'approche du jury. D est en retrait, téléphone en main, prêt.]**

**A** *(naturel, regarde le jury dans les yeux)* :
> *"On a tous vu la même scène dans nos classes. L'élève sort son téléphone sous la table, prend en photo l'exercice, le colle dans ChatGPT, et recopie la réponse. C'est rapide, c'est efficace, et c'est un désastre éducatif. Le rapport PISA 2022 de l'OCDE confirme ce qu'on voit tous les jours : 60% des élèves français ne savent pas organiser leurs révisions. Avec ChatGPT, ils ne révisent plus du tout — ils recopient."*

*[Pause. A change de ton.]*

**A** :
> *"Alors on s'est posé une question simple. Et si l'intelligence artificielle, au lieu de faire le travail à la place de l'élève, le forçait à réfléchir par lui-même ? Et si on construisait une IA qui refuse obstinément de donner la réponse ?"*

> *"Pour comprendre ce que ça change, regardez."*

*[D sort deux téléphones et les tient côte à côte, bien visibles du jury. Sur le second, il active le Mode Avion ostensiblement.]*

**A** :
> *"À gauche, ChatGPT. À droite, notre solution, LUCID — en mode avion, aucune connexion. Même question sur les deux : « Résous 2x + 5 = 13 »."*

*[D tape la question simultanément sur les deux écrans. Silence. Les deux IA répondent.]*

**A** *(pointe l'écran de gauche)* :
> *"ChatGPT : réponse complète en 3 secondes. « x = 4 ». L'élève recopie, il a sa note, il n'a rien compris."*

*(pointe l'écran de droite)* :
> *"LUCID : « Que se passe-t-il si tu isoles le terme avec x d'un côté ? » Pas de réponse. Un guidage."*

*[A laisse 3 secondes au jury pour observer le contraste.]*

**A** :
> *"À gauche, une IA qui travaille à la place de l'élève. À droite, sans aucune connexion, une IA qui force l'élève à travailler. Ce contraste résume huit mois de recherche. Nous sommes quatre lycéens du Lycée Henri Matisse à Vence, et nous nous sommes attaqués à une problématique précise :"*

**A** *(articule lentement)* :
> ***"Comment concevoir un assistant scolaire basé sur l'intelligence artificielle qui renforce l'autonomie cognitive de l'élève, plutôt que de s'y substituer, tout en garantissant la confidentialité de ses données personnelles ?"***

**A** :
> *"Mais avant de se lancer tête baissée dans le code, on est d'abord allés voir ce que dit la science."*

*(A se tourne naturellement vers C.)*

---

### ⏱️ 1:45 → 2:30 — ÉTAT DE L'ART & HYPOTHÈSES (C)

**C** *(s'avance, distribue des impressions couleurs des études au jury)* :
> *"Deux études récentes ont complètement orienté notre approche. Vous les avez sous les yeux."*

> *"La première vient du MIT Media Lab : en 2025, les chercheuses Pattie Maes et Nataliya Kosmyna ont mesuré par EEG l'activité cérébrale d'étudiants utilisant ChatGPT. Le résultat est sans appel : quand l'IA fournit la réponse directe, l'activité neuronale chute brutalement. Les chercheurs appellent ça l'accumulation de « dette cognitive ». Le cerveau de l'élève s'éteint."*

> *"Mais la deuxième étude, venue d'Harvard, montre exactement l'inverse. Quand une IA est configurée comme un tuteur — elle ne donne jamais la réponse, elle guide — les étudiants progressent deux fois plus vite."*

> *"Autrement dit : le problème n'est pas l'IA elle-même. C'est la façon dont elle interagit avec l'élève. C'est de là que viennent nos quatre hypothèses :"*

**C** *(compte sur ses doigts)* :
> *"**H1** : une posture socratique — guider par le questionnement sans livrer la réponse — améliore la rétention des connaissances."*
>
> *"**H2** : un traitement local, directement sur l'appareil de l'élève, renforce la confiance et la confidentialité."*
>
> *"**H3** : un modèle de 4 milliards de paramètres, optimisé, peut tourner de façon fluide sur un smartphone standard, sans Internet."*
>
> *"**H4** : l'intégration de cette IA dans un écosystème scolaire concret — connecté aux vrais cours de l'élève et enrichi par la gamification — favorise l'adoption et l'usage régulier."*

**C** :
> *"Ces quatre hypothèses, il fallait les tester. Et pour ça, il fallait construire le système de A à Z."*

*(C se tourne vers B.)*

---

### ⏱️ 2:30 → 5:45 — NOTRE DÉMARCHE, ÉTAPE PAR ÉTAPE (B + C)

**B** *(s'avance, naturel)* :
> *"Pour comprendre comment on en est arrivés là, il faut revenir au point de départ. Septembre 2025. Nous sommes quatre élèves de Terminale au Lycée Henri Matisse. On sort de spécialité NSI, certains d'entre nous ont participé aux Trophées NSI — on sait coder, on a des bases en IA, mais on n'a jamais construit un système complet."*

> *"Notre constat est simple : Pronote est ennuyeux, mais il contient des données précieuses — les vrais cours de chaque élève. Et ChatGPT est partout dans nos classes, mais il donne les réponses au lieu de faire réfléchir. On se dit : et si on combinait les deux ? Les données Pronote pour le contexte, et une IA qui guide au lieu de répondre."*

**C** :
> *"C'est l'idée de départ. Mais entre l'idée et la réalité, il y a eu six étapes — et à chaque fois, c'est une de nos hypothèses qui a guidé les choix."*

#### 🔧 Étape 1 — Le socle de données *(H2 : confidentialité)*

**B** :
> *"Pour que l'IA connaisse les cours de l'élève, il faut d'abord récupérer ses données Pronote. Notre premier réflexe a été de développer un serveur proxy en Python. Le principe : l'app interroge notre serveur, qui interroge Pronote. En pratique, un paquet sur deux n'arrivait pas — et surtout, les données de l'élève transitaient par notre infrastructure. Pour notre hypothèse H2 — la confidentialité —, c'était un problème fondamental."*

> *"On a alors découvert une librairie open-source issue de Papillon, une application scolaire reconnue. On l'a intégrée directement dans notre app. Résultat : les données ne quittent plus jamais le téléphone de l'élève. C'est ce qu'on appelle notre RAG Pronote — l'IA utilise les vrais cours, devoirs et notes de l'élève comme contexte. C'est le cœur du projet, et c'est le premier jalon de H2."*

#### 🎨 Étape 2 — Le test de H4 *(adoption et engagement)*

**C** :
> *"Techniquement, ça fonctionnait. L'IA générait des quiz à partir des vrais cours, elle pouvait aider aux devoirs. Mais personne ne téléchargeait notre application."*

**B** :
> *"On avait construit un outil puissant dans une interface austère. Exactement comme Pronote. C'est là qu'on a compris que notre hypothèse H4 — l'adoption — ne dépendait pas seulement de l'IA. Elle dépendait de l'expérience complète."*

> *"On a tout redesigné : dark mode, animations, identité visuelle premium. Et surtout, un système de gamification : points d'expérience pour chaque quiz, niveaux, badges, classement entre camarades. Après le redesign, les téléchargements ont commencé. H4 commençait à se valider sur le terrain."*

#### ⚡ Étape 3 — Tester H2 et H3 *(inférence locale)*

**B** :
> *"Jusqu'ici, notre IA fonctionnait via l'API Gemini de Google — dans le cloud. Chaque question posée par un élève de 14 ans partait sur un serveur à l'étranger. Pour nos hypothèses H2 et H3, il fallait que l'IA tourne directement dans le téléphone, sans aucune connexion."*

> *"Nous avons commencé avec Llama 3, un modèle de 8 milliards de paramètres. Sur le papier, c'était le bon candidat."*

**C** *(secoue la tête)* :
> *"En pratique, H3 était invalidée : plus de 15 secondes par réponse, la RAM saturée, le téléphone qui surchauffait. Un modèle « fluide sur un smartphone standard », ce n'était pas ça."*

**B** :
> *"Il a fallu tout remettre à plat. Nous avons changé le modèle — Qwen 3.5, deux fois plus compact avec 4 milliards de paramètres, compressé en 4-bit — et le moteur d'inférence, en passant de llama.cpp à MLC LLM, optimisé pour les puces mobiles. Résultat : 30 tokens par seconde sur un iPhone 14. H3 était enfin validée. Et H2 avec elle : zéro donnée ne sort du téléphone."*

> *"Mais un nouveau problème est apparu : la qualité."*

#### 🧠 Étape 4 — Tester H1 *(posture socratique)*

*[A lève l'ardoise vers le jury. Écrit dessus : « Napoléon est mort en 1999. »]*

**B** :
> *"Un modèle de 4 milliards de paramètres est généraliste. Il ne sait pas enseigner. Et il hallucine — il invente des faits avec aplomb. Notre hypothèse H1 dit qu'une posture socratique améliore la rétention. Encore fallait-il que le modèle adopte cette posture."*

> *"Pour ça, on a agi sur deux leviers. D'abord, les system prompts : des instructions précises qui cadrent le comportement de l'IA à chaque interaction — lui interdire de donner la réponse, l'obliger à poser des questions, à reformuler. Mais un prompt seul ne suffit pas : le modèle le contourne dès que la question se complexifie. Il fallait ancrer la posture plus profondément."*

> *"C'est là qu'intervient QLoRA, une méthode de fine-tuning. Le principe : on gèle le modèle et on entraîne uniquement de petites matrices d'adaptation. Avec un rang de 16, on ne modifie que 0,1% des paramètres."*

*[C s'avance et tend à B l'épaisse pile de fiches bristol.]*

**B** *(prend la pile et la montre au jury)* :
> *"Et voilà ce sur quoi il a appris. Avec nos professeurs, nous avons d'abord rédigé 1 000 paires question-réponse socratiques, à la main. Mais mille, ce n'est pas assez. Alors nous avons construit Lucid Labs, notre plateforme interne, et utilisé la distillation de connaissances : un modèle puissant génère des exemples de qualité, que nos enseignants valident ensuite un par un. Total : 10 000 paires supervisées."*

> *"Et ce paramétrage n'est pas arbitraire : à rang 4, le modèle ne posait pas de questions. À rang 64, il répétait les exemples mot pour mot. Le rang 16, avec une perte finale de 0,87, c'est le point d'équilibre. H1 commençait à prendre forme."*

#### 📚 Étape 5 — Ancrer H1 dans la réalité des programmes

**B** :
> *"Le fine-tuning lui a appris comment enseigner. Mais il ne lui dit pas quoi enseigner."*

*[D s'avance et lâche un gros manuel scolaire sur la table — bruit sourd.]*

**B** :
> *"Depuis le début, notre IA utilisait les données Pronote de l'élève. Mais on s'est heurtés à un problème : les professeurs ne mettent pas toujours assez de contenu dans Pronote. Pour certains cours, le cahier de texte ne contenait qu'une ligne. L'IA manquait de matière."*

> *"On a donc ajouté une deuxième source : les manuels scolaires libres, de la 6ème à la Terminale, indexés en vecteurs. Quand l'élève pose une question, le système associe automatiquement ses vrais cours Pronote avec le programme officiel correspondant. C'est notre RAG — Retrieval Augmented Generation. L'IA ne peut répondre qu'à partir de sources vérifiées."*

> *"Pour résumer avec une image :"*

*[A prend une pose théâtrale, main au menton.]*

> *"Notre modèle est un acteur de talent. Le fine-tuning lui a appris son rôle : le professeur socratique. Mais sans texte, il improvise — et il raconte n'importe quoi."*

*[C s'approche de A et lui met le gros manuel dans les mains.]*

> *"Le RAG et les données Pronote, c'est le script qui lui interdit d'improviser. L'un donne le comportement. L'autre garantit la vérité."*

#### 🚪 Étape 6 — Confirmer H2 face aux institutions

**C** *(ton sobre)* :
> *"En parallèle, il a fallu publier et protéger. Nous avons déposé un brevet à l'INPI avec notre partenaire AxePI. Et quand nous avons soumis l'application sur l'App Store, Apple nous a refusés : non-conformité COPPA et RGPD. Notre hypothèse H2 ne devait pas seulement être vraie techniquement — elle devait être validée juridiquement. Il a fallu réécrire notre politique de confidentialité, renforcer les contrôles parentaux, et resoumettre."*

> *"Ces obstacles ne sont pas des échecs. Ce sont des itérations scientifiques. Et chacune a renforcé H2."*

**B** *(distribue une fiche plastifiée à chaque membre du jury)* :
> *"Pour résumer tout ce que je viens de vous raconter, voici une fiche que vous pouvez garder. D'un côté, l'architecture complète de LUCID. De l'autre, un résumé du projet. Aujourd'hui, LUCID embarque cinq assistants IA — tuteur socratique, quiz, flashcards, fiches de révision, aide aux devoirs — le tout alimenté par les vrais cours Pronote de l'élève et enrichi par la gamification. Cinq outils, une seule philosophie : l'élève travaille, l'IA guide."*

> *"Voilà huit mois de travail et quatre hypothèses testées sur le terrain. Maintenant, la vraie question : est-ce que ça marche ? Plutôt que de vous le dire, on va vous le montrer."*

---

### ⏱️ 5:45 → 7:00 — DÉMO LIVE : LE DUEL (D)

**[🚨 Démo Live : Le Duel (~1 min 15)]**

*[D sort deux téléphones, les tient côte à côte. Il passe une carte « Question Piège » imprimée au jury.]*

**D** :
> *"Vous avez devant vous une question piège que nous avons préparée. Prenez le temps de la lire."*

*[Le jury lit. D attend patiemment.]*

> *"Je pose exactement la même question à ChatGPT et à LUCID. Simultanément."*

*[D tape sur les deux écrans. Silence pendant que les IA répondent.]*

**D** *(commente en direct)* :
> *"ChatGPT donne la réponse complète, immédiatement. Il ne détecte même pas le piège. LUCID refuse. Il demande : 'D'où sors-tu cette formule ? Peux-tu m'expliquer ton raisonnement ?'"*

**D** *(sourire)* :
> *"C'est notre hypothèse H1 en direct. ChatGPT donne le poisson. LUCID apprend à pêcher."*

---

### ⏱️ 7:00 → 9:00 — RÉSULTATS, IMPACT & PERSPECTIVES (C + A)

**C** *(enchaîne directement après la démo)* :
> *"Ce que vous venez de voir en direct, nous l'avons aussi mesuré de façon rigoureuse avec deux protocoles."*

> *"**Premier protocole : un benchmark pédagogique.** 40 questions de Seconde et de Première, dans cinq matières, soumises à trois systèmes : ChatGPT, un modèle Llama 3.2 brut, et LUCID. Deux correcteurs indépendants — notre professeur encadrant et un enseignant volontaire — ont évalué chaque réponse à l'aveugle, sur cinq critères : pertinence, rigueur scientifique, adaptation aux programmes, posture pédagogique, fonctionnement hors-ligne."*

> *"Résultat : LUCID obtient un score global de **4,4 sur 5**. ChatGPT : **2,6**. Llama brut : **2,4**."*

**C** *(ton nuancé)* :
> *"Et le détail mérite qu'on s'y arrête. ChatGPT est meilleur que nous sur la pertinence brute : 4,5 contre 4. Son modèle est bien plus massif. Mais il s'effondre sur la posture pédagogique : 1,6 sur 5, parce qu'il livre systématiquement la réponse toute crue. LUCID, grâce au fine-tuning socratique, atteint 4,6 sur ce critère. Et ChatGPT obtient 0 sur le hors-ligne."*

> *"**Deuxième protocole : une enquête de terrain.** 47 lycéens de notre établissement ont utilisé LUCID pendant deux semaines en conditions réelles, puis rempli un questionnaire structuré."*

> *"89% recommandent LUCID. 74% le préfèrent à ChatGPT pour réviser. 78% déclarent mieux retenir leurs cours. Et un écart qui nous a marqués : 87% font confiance à LUCID pour protéger leurs données, contre seulement 19% pour ChatGPT."*

**C** *(récapitule)* :
> *"Nos quatre hypothèses sont confirmées. H1, posture socratique : validée, 4,6/5 contre 1,6 pour ChatGPT. H2, confidentialité : validée, 87% de confiance. H3, hors-ligne : validée, 30 tokens par seconde sur un iPhone standard. H4, adoption : validée, 89% de recommandation et les élèves actifs sur le leaderboard reviennent deux fois plus souvent."*

**C** *(change de ton, plus posé)* :
> *"Mais nous connaissons les limites de notre travail. 47 testeurs dans un seul établissement, c'est un signal, pas une preuve généralisable. Notre fine-tuning couvre cinq matières — les langues et les arts sont exclus. Et les smartphones de moins de 3 Go de RAM ne supportent pas encore notre modèle. Ce sont des axes d'amélioration concrets pour la suite."*

**A** *(reprend, transition fluide)* :
> *"Ce parcours, on ne l'a pas fait seuls. Les enseignants-chercheurs de **Polytech Nice Sophia** ont validé notre architecture locale et nos paramètres de fine-tuning. **AxePI** nous a accompagnés pour le dépôt de brevet à l'INPI. **Lucarne Pro** a fourni le compte Apple Developer. La **Fondation CGénial** a contribué au financement. Et les **professeurs du Lycée Henri Matisse** ont co-construit et validé les 10 000 paires de notre dataset."*

> *"Au-delà de la technique, LUCID porte un enjeu social. Le rapport PISA 2022 révèle un écart de 100 points entre élèves favorisés et défavorisés. Un professeur particulier coûte 40 euros de l'heure. LUCID met un tuteur IA gratuit dans la poche de chaque élève — y compris sur un téléphone à 150 euros, même sans Internet."*

> *"Il y a aussi un enjeu environnemental. Un appel à ChatGPT sollicite des GPU massifs dans des datacenters. Avec LUCID, chaque session de révision se fait sur la puce du téléphone, sans aucun serveur. Et un enjeu de confidentialité : les notes, l'emploi du temps, les devoirs — rien ne sort du téléphone de l'élève. Les identifiants Pronote sont chiffrés localement. Notre proxy de connexion est open-source. C'est de la transparence totale."*

---

### ⏱️ 9:00 → 10:00 — CONCLUSION (A, tous regroupés)

*[Les 4 se regroupent au centre. A devant. Silence de 3 secondes.]*

**A** *(calme, balaye le jury du regard)* :
> *"Nous sommes partis d'un constat documenté : les IA grand public créent de la dette cognitive. Nous avons formulé quatre hypothèses. Pour les tester, nous avons construit un système complet et 100% local : un modèle de 4 milliards de paramètres, compressé en 4-bit, spécialisé par QLoRA sur 10 000 paires construites avec nos professeurs, ancré dans les vrais cours Pronote de l'élève, et intégré dans un écosystème de cinq outils pédagogiques gamifiés. Le tout tourne directement dans le téléphone."*

> *"Nos quatre hypothèses sont validées. Score pédagogique : 4,4 sur 5. L'application est publiée sur l'App Store, près de 200 élèves l'utilisent, et une demande de brevet a été déposée."*

> *"Nous connaissons nos limites : un échantillon restreint, une couverture incomplète, un modèle perfectible. Ce prototype est un premier pas."*

*[Pause de 2 secondes.]*

**A** :
> *"LUCID, ce n'est pas un projet d'élèves qui ont utilisé l'IA."*

*[Silence.]*

> *"C'est un projet d'élèves qui ont **conçu un système d'intelligence artificielle complet**. Et qui lui ont interdit de donner les réponses."*

> *"Merci."*

*[Les 4 restent immobiles. Fin.]*

---

## 🛠️ Triggers Accessoires (Rappel Rapide)

* **T= 0:40 (D)** : Duel téléphone (ChatGPT) vs téléphone (LUCID en mode avion).
* **T= 1:45 (A/C)** : Distribution des rapports imprimés (PISA + étude MIT).
* **T= 2:30 (B)** : Récit du proxy Python → librairie Pawnote (Papillon).
* **T= 3:00 (C)** : Personne ne télécharge → redesign + gamification.
* **T= 3:30 (B)** : Llama 3 = échec → pivot Qwen 3.5 + MLC LLM.
* **T= 4:00 (A)** : Ardoise « Napoléon est mort en 1999 ».
* **T= 4:15 (C→B)** : Pile de fiches bristol (dataset 10 000 paires).
* **T= 4:45 (D)** : Manuel scolaire lâché sur la table — BAM (RAG).
* **T= 5:00 (A+C)** : Pose théâtrale acteur + manuel dans les mains.
* **T= 5:15 (C)** : Brevet INPI + rejet Apple Store.
* **T= 5:30 (B)** : Distribution des fiches plastifiées "Architecture Locale / Résumé LUCID".
* **T= 5:45 (D)** : Duel double téléphone + carte question piège.
