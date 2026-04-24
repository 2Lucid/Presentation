# 🎤 LUCID — Script Oral V3 (Final)

*Durée visée : 10 minutes / 4 Présentateurs*
*Concours : C'Génial 2026 / Faites de la Science*

---

## 🎭 1. Rôles et Placement

**A (Coordinateur)** : Ouvre et ferme la présentation. Porte la problématique, les transitions et la conclusion.
**B (Architecte technique)** : Explique les choix techniques et l'architecture hybride. Gère les supports visuels (Panneau Plexiglas, LEDs, dominos).
**C (Responsable Recherche & Évaluation)** : Présente les fondements scientifiques, le protocole d'évaluation et la discussion critique (limites).
**D (Démonstrateur)** : Gère les démonstrations live sur les téléphones. Apporte les preuves expérimentales en temps réel.

> **Note :** Si seulement 2 présentateurs, A absorbe C et B absorbe D.

---

## 🎬 2. Le Script

---

### ⏱️ 0:00 → 1:45 — PROBLÉMATIQUE (A + D)

**[A s'approche du jury. D est en retrait, téléphone en main, prêt.]**

**A** *(naturel, regarde le jury dans les yeux)* :
> *"On a tous vu la même scène dans nos classes. L'élève sort son téléphone sous la table, prend en photo l'exercice, le colle dans ChatGPT, et recopie la réponse. C'est rapide, c'est efficace, et c'est un désastre éducatif. Le rapport PISA 2022 de l'OCDE confirme ce qu'on voit tous les jours : 60% des élèves français ne savent pas organiser leurs révisions. Avec ChatGPT, ils ne révisent plus du tout — ils recopient."*

*[Pause. A change de ton.]*

**A** :
> *"Alors on s'est posé une question simple. Et si l'intelligence artificielle, au lieu de faire le travail à la place de l'élève, le forçait à réfléchir par lui-même ? Et si on construisait une IA qui refuse obstinément de donner la réponse ?"*

*[A fait un signe à D. D active le Mode Avion bien visiblement devant le jury, puis tape une question. Le texte commence à s'afficher token par token. A pointe l'écran.]*

**A** :
> *"Ce téléphone est en mode avion. Aucune connexion. Et pourtant, observez : une IA est en train de répondre — en direct, sur la puce de ce téléphone. Aucune donnée ne sort de cet appareil."*

*[A laisse 2 secondes au jury pour observer.]*

**A** :
> *"Ce que vous voyez là, c'est le résultat de huit mois de recherche. Nous sommes quatre lycéens du Lycée Henri Matisse à Vence, et nous nous sommes attaqués à une problématique précise :"*

**A** *(articule lentement)* :
> ***"Comment concevoir un assistant scolaire basé sur l'intelligence artificielle qui renforce l'autonomie cognitive de l'élève, plutôt que de s'y substituer, tout en garantissant la confidentialité de ses données personnelles ?"***

**A** :
> *"Mais avant de se lancer tête baissée dans le code, on est d'abord allés voir ce que dit la science."*

*(A se tourne naturellement vers C.)*

---

### ⏱️ 1:45 → 2:30 — ÉTAT DE L'ART & HYPOTHÈSES (C)

**C** *(s'avance, prend le relais sans rupture)* :
> *"Deux études récentes ont complètement orienté notre approche."*

> *"La première vient du MIT Media Lab : en 2025, les chercheuses Pattie Maes et Nataliya Kosmyna ont mesuré par EEG l'activité cérébrale d'étudiants utilisant ChatGPT. Le résultat est sans appel : quand l'IA fournit la réponse directe, l'activité neuronale chute brutalement. Les chercheurs appellent ça l'accumulation de « dette cognitive ». Le cerveau de l'élève, en quelque sorte, s'éteint."*

> *"Mais la deuxième étude, venue d'Harvard, montre exactement l'inverse. Quand une IA est configurée comme un tuteur — elle ne donne jamais la réponse, elle guide — les étudiants progressent deux fois plus vite."*

> *"Autrement dit : le problème n'est pas l'IA elle-même. C'est la façon dont elle interagit avec l'élève. C'est de là que viennent nos quatre hypothèses :"*

**C** *(compte sur ses doigts)* :
> *"**H1** : une posture socratique — guider par le questionnement sans livrer la réponse — améliore la rétention des connaissances."*
>
> *"**H2** : un traitement local, directement sur l'appareil de l'élève, renforce la confiance et la confidentialité."*
>
> *"**H3** : un modèle de 4 milliards de paramètres, optimisé, peut tourner de façon fluide sur un smartphone standard, sans Internet."*
>
> *"**H4** : un système d'orchestration peut basculer de façon transparente entre un moteur local et un moteur cloud."*

**C** :
> *"Ces quatre hypothèses, il fallait les tester. Et pour ça, il fallait construire le système de A à Z."*

*(C se tourne vers B.)*

---

### ⏱️ 2:30 → 4:45 — MÉTHODE & RÉALISATION (B)

**B** *(s'approche du Panneau Plexiglas)* :
> *"Le développement s'est étalé sur quatre phases, de septembre 2025 à mars 2026. LUCID repose sur une architecture hybride : deux moteurs d'inférence qui se complètent."*

*[B allume la LED verte.]*

**B** :
> *"**Premier moteur : local.** Un modèle Qwen 3.5 de 4 milliards de paramètres, compressé en 4-bit et exécuté directement sur le NPU du téléphone via le moteur MLC LLM. C'est ce que vous avez vu à l'instant sur le téléphone en mode avion."*

> *"Pour comprendre ce qui se passe à l'intérieur :"*

*[B déplace les dominos en bois un par un sur le panneau.]*

> *"Quand l'élève pose une question, le modèle découpe sa phrase en unités sémantiques : les tokens. Ensuite, chaque token évalue sa pertinence par rapport à tous les autres. C'est le mécanisme d'Attention des transformers."*

*[B montre les fils de laine tendus entre les dominos.]*

> *"Le token « suites » regarde « maths ». Il ignore « moi ». C'est ce calcul, répété sur des dizaines de couches, qui produit la réponse. Et tout ça tourne en local. Nos benchmarks donnent 30 tokens par seconde sur un iPhone 14 : le texte s'affiche au rythme naturel de la lecture."*

*[B allume la LED bleue.]*

**B** :
> *"**Deuxième moteur : cloud souverain.** Tous les téléphones ne sont pas des iPhone. Même les tablettes Lenovo fournies par la Région Sud à nos camarades doivent pouvoir utiliser LUCID. Pour ça, nous avons déployé un modèle plus puissant — Qwen 14B — sur un Mac Mini M4, hébergé physiquement chez notre partenaire AxePI, exposé via Cloudflare Tunnel. 58 tokens par seconde, et une souveraineté totale : les données ne transitent jamais par des serveurs tiers. Le système d'orchestration bascule entre les deux moteurs en moins de 800 millisecondes, sans que l'élève s'en rende compte. C'est notre hypothèse H4."*

**B** *(change de ton, plus lent)* :
> *"Faire tourner un modèle sur un téléphone, ça, c'est un défi technique. Mais le vrai problème est beaucoup plus profond."*

*[A lève l'ardoise vers le jury. Écrit dessus : « Napoléon est mort en 1999. »]*

**B** :
> *"Un modèle de 4 milliards de paramètres est généraliste. Il ne sait pas enseigner. Et il hallucine. En classe, c'est inacceptable. Nous avons attaqué ce problème sur deux fronts."*

> *"**Front 1 : lui apprendre à enseigner.** Nous avons utilisé QLoRA, une méthode de fine-tuning. Le principe : au lieu de ré-entraîner les 4 milliards de paramètres, ce qui est hors de portée sur notre matériel, on gèle le modèle et on entraîne uniquement de petites matrices d'adaptation. Avec un rang de 16, on ne modifie que 0,1% des paramètres."*

*[C s'avance et tend à B l'épaisse pile de fiches bristol.]*

**B** *(prend la pile et la montre au jury)* :
> *"Et voilà ce sur quoi il a appris. Avec les professeurs de notre lycée, nous avons d'abord rédigé 1 000 paires question-réponse socratiques, à la main. Puis, via Lucid Labs, notre plateforme interne, nous avons généré 9 000 exemples supplémentaires par distillation de connaissances, tous validés un par un par les enseignants via un outil dédié : Lucid Professeur. Total : 10 000 paires supervisées."*

> *"Et ce paramétrage n'est pas arbitraire : à r = 4, le modèle n'adoptait pas la posture socratique. À r = 64, il sur-apprenait. Le rang 16, avec une perte finale de 0,87, c'est le point d'équilibre."*

**B** :
> *"Mais il restait un problème. Le fine-tuning lui apprend comment enseigner. Mais il ne lui dit pas quoi enseigner."*

*[D s'avance et lâche un gros manuel scolaire sur la table — bruit sourd.]*

**B** :
> *"**Front 2 : lui donner la vérité.** C'est le rôle de notre RAG — Retrieval Augmented Generation. Tous les manuels libres de la 6ème à la Terminale sont embarqués dans le téléphone, indexés en vecteurs. Avant chaque réponse, le système récupère les passages pertinents du manuel et les injecte dans le contexte. Le modèle est contraint de sourcer ses réponses uniquement dans cette base vérifiée."*

> *"Pour résumer avec une image :"*

*[A prend une pose théâtrale, main au menton.]*

> *"Notre modèle est un acteur de talent. Le fine-tuning lui a appris son rôle : le professeur socratique. Mais sans texte, il improvise — et il raconte n'importe quoi."*

*[C s'approche de A et lui met le gros manuel dans les mains.]*

> *"Le RAG, c'est le script qui lui interdit d'improviser. L'un donne le comportement. L'autre garantit la vérité."*

**B** :
> *"Voilà le système. Maintenant la vraie question : est-ce que ça marche ?"*

---

### ⏱️ 4:45 → 6:45 — RÉSULTATS & VALIDATION EXPÉRIMENTALE (C + D)

**C** *(reprend naturellement après la question de B)* :
> *"Pour le savoir, nous avons mis en place deux protocoles d'évaluation."*

> *"**Premier protocole : un benchmark pédagogique.** 40 questions de Seconde et de Première, dans cinq matières, soumises à trois systèmes : ChatGPT, un modèle Llama 3.2 brut, et LUCID. Deux correcteurs indépendants — notre professeur encadrant et un enseignant volontaire — ont évalué chaque réponse à l'aveugle, sur cinq critères : pertinence, rigueur scientifique, adaptation aux programmes, posture pédagogique, fonctionnement hors-ligne."*

> *"Résultat : LUCID obtient un score global de **4,4 sur 5**. ChatGPT : **2,6**. Llama brut : **2,4**."*

**C** *(ton nuancé)* :
> *"Et le détail mérite qu'on s'y arrête. ChatGPT est meilleur que nous sur la pertinence brute : 4,5 contre 4. Son modèle est bien plus massif. Mais il s'effondre sur la posture pédagogique : 1,6 sur 5, parce qu'il livre systématiquement la réponse toute crue. LUCID, grâce au fine-tuning socratique, atteint 4,6 sur ce critère. Et ChatGPT obtient 0 sur le hors-ligne."*

> *"**Deuxième protocole : une enquête de terrain.** 47 lycéens de notre établissement ont utilisé LUCID pendant deux semaines en conditions réelles, puis rempli un questionnaire structuré."*

> *"89% recommandent LUCID. 74% le préfèrent à ChatGPT pour réviser. 78% déclarent mieux retenir leurs cours. Et un écart qui nous a marqués : 87% font confiance à LUCID pour protéger leurs données, contre seulement 19% pour ChatGPT."*

**C** :
> *"Voilà pour les chiffres. Mais plutôt que de vous demander de nous croire sur parole, on va vous le montrer."*

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

**C** *(récapitule en enchaînant directement)* :
> *"Avec ce duel et nos deux protocoles, nous confirmons la validation des quatre hypothèses. H1, posture socratique : validée, 4,6/5 contre 1,6 pour ChatGPT. H2, confidentialité : validée, 87% de confiance. H3, hors-ligne : validée, 7 à 30 tokens par seconde selon l'appareil. H4, orchestration : validée, basculement en moins de 800 millisecondes."*

**C** :
> *"Nos résultats sont encourageants. Mais il serait malhonnête de s'arrêter là."*

---

### ⏱️ 6:45 → 8:00 — DISCUSSION CRITIQUE (C + B)

**C** *(enchaîne sans rupture, le ton devient plus posé)* :
> *"Nous connaissons les limites de notre travail, et nous pensons qu'elles sont importantes à partager."*

> *"**Première limite : l'échantillon.** 47 testeurs dans un seul établissement, c'est un signal, pas une preuve statistique généralisable. Et nos testeurs étaient volontaires — donc probablement plus motivés que la moyenne. Pour consolider, il faudrait une étude sur au moins 200 élèves, dans plusieurs lycées, avec un recrutement aléatoire."*

> *"**Deuxième limite : la couverture.** Notre fine-tuning couvre cinq matières. Les langues vivantes et les arts sont exclus. Sur ces sujets, le modèle est moins fiable."*

**B** :
> *"**Troisième limite : le matériel.** Les smartphones de moins de 3 Go de RAM ne supportent pas notre modèle. Nous explorons la quantification 2-bit et les modèles distillés pour y remédier."*

**C** :
> *"Nous voulons aussi mentionner les obstacles qui ont façonné ce projet. Notre premier modèle, Llama 3 avec 8 milliards de paramètres, était inutilisable : plus de 15 secondes par réponse et une RAM saturée. Nous avons dû l'abandonner et migrer vers Qwen 3.5, ce qui a divisé la latence par cinq. Et Apple a refusé notre première soumission sur l'App Store pour non-conformité COPPA et RGPD. Il a fallu réécrire notre politique de confidentialité et renforcer les contrôles parentaux avant d'être acceptés."*

**C** :
> *"Ces épreuves ne sont pas des échecs. Ce sont des données. Et elles ont rendu le projet meilleur."*

---

### ⏱️ 8:00 → 9:15 — PARTENARIATS & IMPACT (A + C)

**A** *(reprend, transition fluide)* :
> *"Ce parcours, on ne l'a pas fait seuls. Chaque partenaire a joué un rôle concret."*

> *"Les enseignants-chercheurs de **Polytech Nice Sophia** ont validé notre architecture hybride et nos paramètres de fine-tuning. **AxePI** nous a accompagnés pour le dépôt de brevet à l'INPI et héberge physiquement notre serveur. **Lucarne Pro** a fourni le Mac Mini M4 et le compte Apple pour la publication. La **Fondation CGénial** a contribué au financement. Et les **professeurs du Lycée Henri Matisse** ont co-construit et validé les 10 000 paires de notre dataset."*

**A** :
> *"Mais au-delà de la technique, LUCID porte un enjeu plus large."*

**C** :
> *"Le rapport PISA 2022 révèle un écart de 100 points entre élèves favorisés et défavorisés en France. Un professeur particulier coûte 40 euros de l'heure. LUCID met un tuteur IA gratuit dans la poche de chaque élève — y compris sur un téléphone à 150 euros, même sans Internet."*

> *"Il y a aussi un enjeu environnemental. Notre Mac Mini M4 consomme 40 watts maximum. Un GPU de datacenter en consomme des centaines. En choisissant le traitement local, on réduit considérablement l'empreinte de chaque session de révision."*

> *"LUCID a d'ailleurs été distingué au Concours Science Factor 2026 par un double prix : le Prix Lycée et le Prix Orange Numérique, qui récompense la solution numérique la plus utile à la société civile."*

**A** *(transition vers la conclusion)* :
> *"Voilà où nous en sommes. Essayons de résumer."*

---

### ⏱️ 9:15 → 10:00 — CONCLUSION & PERSPECTIVES (A, tous regroupés)

*[Les 4 se regroupent au centre. A devant. Silence de 3 secondes.]*

**A** *(calme, balaye le jury du regard)* :
> *"Nous sommes partis d'un constat documenté : les IA grand public créent de la dette cognitive. Nous avons formulé quatre hypothèses. Pour les tester, nous avons construit un système complet : un modèle de 4 milliards de paramètres, compressé en 4-bit, spécialisé par QLoRA sur 10 000 paires construites avec nos professeurs, protégé par un RAG ancré dans les manuels officiels, et déployé dans un téléphone."*

> *"Nos quatre hypothèses sont validées. Score pédagogique : 4,4 sur 5. L'application est publiée sur l'App Store, près de 200 élèves l'utilisent, et une demande de brevet a été déposée."*

> *"Nous connaissons nos limites : un échantillon restreint, une couverture incomplète, un modèle perfectible. Ce prototype est un premier pas."*

*[Pause de 2 secondes.]*

**A** :
> *"LUCID, ce n'est pas un projet d'élèves qui ont utilisé l'IA."*

*[Silence.]*

> *"C'est un projet d'élèves qui ont **construit** une IA. Et qui lui ont interdit de donner les réponses."*

> *"Merci."*

*[Les 4 restent immobiles. Fin.]*

---

## 🛠️ Triggers Accessoires (Rappel Rapide)

* **T= 0:15 (A)** : Décrit le problème ChatGPT en classe.
* **T= 0:40 (D)** : Active le mode avion devant le jury, tape la question.
* **T= 2:30 (B)** : LED verte, dominos tokens, fils de laine (Attention).
* **T= 3:15 (B)** : LED bleue (cloud souverain).
* **T= 3:45 (A)** : Ardoise « Napoléon est mort en 1999 ».
* **T= 4:00 (C→B)** : Pile de fiches bristol (dataset 10 000 paires).
* **T= 4:20 (D)** : Manuel scolaire lâché sur la table — BAM (RAG).
* **T= 4:35 (A+C)** : Pose théâtrale acteur + manuel dans les mains.
* **T= 5:45 (D)** : Duel double téléphone + carte question piège.
* **BONUS (sur la table)** : Maquette éclatée, éprouvette, dé 20 faces.
