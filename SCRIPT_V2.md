# 🎤 LUCID — Script Oral V2 (Format Concours Scientifique)

*Durée visée : 10 minutes / 4 Présentateurs*
*Concours : C'Génial 2026 / Faites de la Science*

---

## 🎭 1. Rôles et Placement

**A (Coordinateur)** : Ouvre et ferme la présentation. Gère les transitions entre les parties. Porte la problématique et la conclusion.
**B (Architecte technique)** : Explique les choix techniques et l'architecture hybride. Gère les supports visuels (Panneau Plexiglas, LEDs, dominos).
**C (Responsable Recherche & Évaluation)** : Présente les fondements scientifiques, le protocole d'évaluation et la discussion critique (limites).
**D (Démonstrateur)** : Gère les démonstrations live sur les téléphones. Apporte les preuves expérimentales en temps réel.

> **Note :** Si seulement 2 présentateurs, A absorbe C et B absorbe D.

---

## 🎬 2. Le Script

---

### ⏱️ 0:00 → 1:30 — PROBLÉMATIQUE

**[A s'approche du jury. D tient un téléphone, écran tourné vers le jury. L'icône Mode Avion est visible.]**

**A** *(calme, posé)* :
> *"En France, 60% des élèves déclarent ne pas savoir organiser efficacement leurs révisions. Ce chiffre vient du rapport PISA 2022 de l'OCDE. Et l'arrivée de ChatGPT dans les classes n'a rien arrangé."*

**[D tape une question sur le téléphone. Le texte s'affiche token par token. Le jury voit l'écran.]**

**A** :
> *"Observez cet écran. Ce téléphone est en mode avion. Il est complètement déconnecté. Pourtant, une intelligence artificielle est en train de répondre. L'intégralité du traitement se déroule ici, sur la puce de ce téléphone. Aucune donnée ne quitte cet appareil."*

*[Pause. A laisse le jury observer.]*

**A** :
> *"Ce que vous voyez là, c'est le résultat de notre recherche. Nous sommes quatre lycéens du Lycée Henri Matisse à Vence, et pendant huit mois, nous avons travaillé sur une question précise :"*

**A** *(articule lentement)* :
> ***"Comment concevoir un assistant scolaire basé sur l'intelligence artificielle qui renforce l'autonomie cognitive de l'élève, plutôt que de s'y substituer, tout en garantissant la confidentialité de ses données personnelles ?"***

**A** :
> *"C'est notre problématique. Et pour y répondre, nous avons formulé quatre hypothèses de travail que nous allons vous présenter, puis vérifier devant vous."*

---

### ⏱️ 1:30 → 2:15 — HYPOTHÈSES & ÉTAT DE L'ART

**C** *(s'avance)* :
> *"Avant de construire quoi que ce soit, nous sommes partis de la littérature scientifique. L'étude du MIT Media Lab de Pattie Maes et Nataliya Kosmyna, publiée en 2025, a mesuré par EEG l'activité cérébrale d'étudiants utilisant ChatGPT. Le résultat est net : l'activité neuronale chute drastiquement lorsqu'une IA fournit la réponse directe. Les chercheurs appellent cela l'accumulation de « dette cognitive »."*

> *"Mais une étude d'Harvard, sur l'assistant PS2 PAL, montre l'inverse : quand l'IA est configurée en tuteur, sans jamais donner la réponse, les étudiants progressent deux fois plus vite."*

> *"Ces deux études ont fondé nos quatre hypothèses :"*

**C** *(en les comptant sur ses doigts)* :
> *"Premièrement : **H1**, une posture socratique, où l'IA guide par le questionnement sans jamais livrer la réponse, améliore la rétention des connaissances.*
> *Deuxièmement : **H2**, un traitement local des données, sur l'appareil de l'élève, renforce la confiance et garantit la confidentialité.*
> *Troisièmement : **H3**, un modèle de 4 milliards de paramètres, correctement optimisé, peut fonctionner de façon fluide sur un smartphone standard, sans connexion Internet.*
> *Quatrièmement : **H4**, un système d'orchestration intelligent peut basculer de façon transparente entre un modèle local et un modèle cloud, sans que l'élève ne perçoive la transition."*

---

### ⏱️ 2:15 → 4:30 — MÉTHODE & RÉALISATION

**A** :
> *"Pour tester ces hypothèses, il a fallu construire le système. Notre développement s'est étalé sur quatre phases, de septembre 2025 à mars 2026."*

*(A désigne B.)*

**B** *(s'approche du Panneau Plexiglas)* :
> *"LUCID repose sur une architecture hybride à deux moteurs d'inférence."*

*[B allume la LED verte.]*

**B** :
> *"**Premier moteur : local.** Un modèle Qwen 3.5 de 4 milliards de paramètres, compressé en 4-bit via quantification NF4 et exécuté directement sur le NPU du téléphone grâce au moteur MLC LLM."*

*[B déplace les dominos en bois un par un sur le panneau.]*

> *"Pour comprendre comment ça fonctionne : quand l'élève pose une question, le modèle découpe sa phrase en unités sémantiques, les tokens. Chaque token évalue sa pertinence par rapport aux autres grâce au mécanisme d'Attention des transformers."*

*[B montre les fils de laine tendus entre les dominos.]*

> *"Le token « suites » regarde « maths ». Il ignore « moi ». C'est ce calcul qui produit la réponse. Et tout cela se déroule en local. Nos mesures donnent 30 tokens par seconde sur un iPhone 14 et 7 tokens par seconde sur les tablettes Lenovo de la Région Sud. Dans les deux cas, l'expérience est fluide."*

*[B allume la LED bleue.]*

**B** :
> *"**Deuxième moteur : cloud souverain.** Pour les requêtes complexes ou les appareils moins puissants, nous avons déployé un modèle Qwen 14B sur un Mac Mini M4, physiquement hébergé chez notre partenaire AxePI. Le serveur est exposé via Cloudflare Tunnel, sans IP publique. Résultat : 58 tokens par seconde, avec une souveraineté totale des données. Le système d'orchestration bascule automatiquement entre les deux moteurs en moins de 800 millisecondes, sans interruption pour l'élève. C'est notre hypothèse H4."*

**B** :
> *"Mais la vraie difficulté était ailleurs : un modèle de 4 milliards de paramètres est généraliste. Il ne sait pas enseigner, et surtout, il hallucine."*

*[A lève silencieusement l'ardoise. Il y est écrit : « Napoléon est mort en 1999. »]*

**B** :
> *"En classe, c'est inacceptable. Nous avons attaqué ce problème sur deux fronts."*

> *"**Front 1 : le comportement.** On a utilisé la méthode QLoRA. Le principe : au lieu de ré-entraîner les 4 milliards de paramètres, ce qui est impossible sur notre matériel, on gèle le modèle et on n'entraîne que de petites matrices d'adaptation. Avec un rang de 16, on ne modifie que 0,1% des paramètres. Le modèle apprend comment enseigner : guider par le questionnement, jamais donner la réponse."*

*[C s'avance et tend à B l'épaisse pile de fiches bristol.]*

**B** :
> *"Et ça, c'est notre dataset. En collaboration avec les professeurs du Lycée Henri Matisse, nous avons d'abord élaboré 1 000 paires question-réponse socratiques à la main. Puis, grâce à Lucid Labs, notre plateforme interne, nous avons généré 9 000 exemples supplémentaires par distillation de connaissances, tous validés individuellement par les enseignants via notre outil Lucid Professeur. Total : 10 000 paires supervisées."*

> *"Un détail important : le choix du rang r = 16 n'est pas arbitraire. Nous avons testé r = 4, mais le modèle n'adoptait pas une posture socratique stable. Et r = 64 provoquait du sur-apprentissage. La perte finale sur notre dataset est de 0,87, ce qui confirme une bonne spécialisation."*

*[D s'avance et lâche lourdement un énorme manuel scolaire sur la table.]*

**B** :
> *"**Front 2 : la véracité.** Le Fine-Tuning apprend au modèle comment enseigner. Mais il ne lui dit pas quoi enseigner. Pour cela, nous avons développé une architecture RAG, Retrieval Augmented Generation."*

> *"Tous les manuels libres de la 6ème à la Terminale sont embarqués dans le téléphone, indexés en vecteurs via un modèle d'embedding. Avant chaque réponse, le système récupère les passages pertinents du manuel et les injecte dans le contexte. Le modèle est contraint de sourcer ses réponses uniquement dans cette base de connaissances vérifiée."*

> *"Pour résumer avec une analogie : le modèle est un acteur de talent."*

*[A prend une pose théâtrale, main au menton.]*

> *"Le fine-tuning lui apprend l'attitude : comment jouer le rôle du professeur socratique. Mais sans texte, il improvise, et il dit n'importe quoi."*

*[C s'approche de A et lui met le gros manuel dans les mains.]*

> *"Le RAG, c'est le script qui lui dicte la vérité. L'un donne le comportement, l'autre donne le contenu. C'est cette combinaison qui a fait disparaître les hallucinations de notre évaluation."*

---

### ⏱️ 4:30 → 6:45 — RÉSULTATS & VALIDATION EXPÉRIMENTALE

**A** :
> *"L'architecture étant en place, nous devions vérifier nos quatre hypothèses. Nous avons mis en place deux protocoles d'évaluation."*

*(A désigne C.)*

**C** :
> *"**Premier protocole : un benchmark technique.** Nous avons soumis 40 questions de Seconde et de Première, dans cinq matières, à trois systèmes : ChatGPT, un modèle Llama 3.2 brut, et LUCID. Deux correcteurs indépendants, notre professeur encadrant et un collègue volontaire, ont évalué chaque réponse à l'aveugle, sur 5 critères : pertinence, rigueur scientifique, adaptation aux programmes, posture pédagogique, et fonctionnement hors-ligne."*

> *"Résultat : LUCID obtient un score global de **4,4 sur 5**. ChatGPT : **2,6 sur 5**. Llama brut : **2,4 sur 5**."*

> *"Le détail est révélateur. ChatGPT est meilleur que nous sur la pertinence brute, avec 4,5 contre 4. Mais il s'effondre sur la posture pédagogique : 1,6 sur 5, parce qu'il livre systématiquement la réponse directe. LUCID, grâce au fine-tuning socratique, atteint 4,6 sur 5 sur ce même critère. Et évidemment, ChatGPT obtient 0 sur le fonctionnement hors-ligne."*

**C** :
> *"**Deuxième protocole : une enquête de terrain.** 47 lycéens bêta-testeurs ont utilisé LUCID pendant deux semaines en conditions réelles, puis ont rempli un questionnaire structuré."*

> *"89% recommandent LUCID. 74% le préfèrent à ChatGPT pour réviser. 78% déclarent mieux retenir leurs cours. Et sur la confiance dans la protection des données : 87% font confiance à LUCID, contre seulement 19% pour ChatGPT."*

**[D sort deux téléphones.]**

**A** :
> *"Les chiffres, c'est bien. Mais nous allons maintenant vous le prouver en direct."*

**[🚨 Démo : Le Duel (1 min 30)]**

**D** :
> *"Je vais poser la même question à ChatGPT et à LUCID, simultanément."*

*[D passe une carte « Question Piège » imprimée au jury.]*

> *"Lisez cette question, s'il vous plaît. Je la tape sur les deux téléphones."*

*[D tape en miroir sur les deux écrans.]*

> *"Observez la différence. ChatGPT fournit la réponse complète immédiatement. Il ne détecte pas le piège dans l'énoncé. LUCID, lui, refuse de répondre directement. Il demande à l'élève : 'D'où sors-tu cette formule ? Est-ce que tu peux m'expliquer ton raisonnement ?'"*

> *"Voilà notre hypothèse H1 en action. ChatGPT donne le poisson. LUCID apprend à pêcher."*

**C** :
> *"Nous pouvons maintenant confirmer la validation de nos quatre hypothèses. H1, posture socratique : validée, score pédagogique 4,6/5 contre 1,6 pour ChatGPT. H2, confidentialité : validée, 87% de confiance. H3, fonctionnement hors-ligne : validée, 30 tokens par seconde sur iPhone, 7 sur tablette Lenovo. H4, orchestration transparente : validée, basculement en moins de 800 millisecondes."*

---

### ⏱️ 6:45 → 8:00 — DISCUSSION CRITIQUE : LIMITES & OBSTACLES

**A** :
> *"Nos résultats sont encourageants. Mais nous devons être honnêtes sur les limites de notre travail."*

**C** :
> *"**Première limite : la taille de notre échantillon.** 47 testeurs dans un seul établissement, c'est un résultat indicatif, pas une preuve statistique robuste. Les élèves étaient volontaires, ce qui introduit un biais de sélection : ils étaient probablement plus motivés que la moyenne. Pour consolider ces résultats, il faudrait une étude multi-établissements avec un recrutement aléatoire stratifié."*

> *"**Deuxième limite : la couverture des matières.** Notre fine-tuning couvre cinq matières. Les langues vivantes et les arts sont exclus. Le modèle est nettement moins fiable dans ces domaines."*

**B** :
> *"**Troisième limite : les appareils anciens.** Les modèles de plus de 4 milliards de paramètres sont incompatibles avec les smartphones disposant de moins de 3 Go de RAM. Nous explorons actuellement la quantification 2-bit et les modèles distillés pour résoudre cela."*

**C** :
> *"**Quatrième point, et c'est un obstacle que nous avons surmonté :** notre premier choix de modèle, Llama 3 avec 8 milliards de paramètres, était inutilisable. La latence dépassait 15 secondes par réponse et la RAM saturait à plus de 4 Go. Nous avons dû abandonner ce modèle et migrer vers Qwen 3.5, divisant la latence par cinq. De même, Apple a refusé notre première soumission sur l'App Store pour non-conformité COPPA et RGPD. Nous avons dû renforcer nos contrôles parentaux et notre politique de confidentialité avant d'être acceptés."*

---

### ⏱️ 8:00 → 9:15 — PARTENARIATS & IMPACT

**A** :
> *"Ce projet n'aurait pas existé sans un écosystème de partenaires qui ont chacun joué un rôle précis."*

> *"Les enseignants-chercheurs de **Polytech Nice Sophia** ont validé notre choix d'architecture hybride et nos paramètres de fine-tuning. L'entreprise **AxePI** nous a accompagnés juridiquement pour le dépôt de notre demande de brevet auprès de l'INPI, et héberge physiquement notre serveur sur son infrastructure réseau. **Lucarne Pro** nous a fourni le Mac Mini M4 et le compte développeur Apple pour la publication. La **Fondation CGénial** a contribué au financement du serveur. Et bien sûr, les **professeurs du Lycée Henri Matisse** ont co-construit et validé l'intégralité de notre dataset de 10 000 paires."*

**C** :
> *"Au-delà du produit, LUCID porte un enjeu de société. La France présente un écart de près de 100 points entre élèves favorisés et défavorisés au rapport PISA 2022. Un professeur particulier coûte 40 euros de l'heure. LUCID place un tuteur IA gratuit et hors-ligne dans la poche de chaque élève, y compris sur un téléphone à 150 euros."*

> *"L'approche Edge Computing a aussi un impact environnemental mesurable. Un modèle local de 4 milliards de paramètres consomme une fraction infime de l'énergie requise par une requête cloud, qui nécessite des datacenters refroidis à grande eau. Notre Mac Mini M4 consomme 40 watts maximum, contre des centaines de watts pour les GPU de datacenter."*

> *"LUCID a d'ailleurs été distingué au Concours Science Factor 2026 par deux prix : le Prix Lycée et le Prix Orange Numérique, qui récompense la solution numérique la plus utile pour la société civile."*

---

### ⏱️ 9:15 → 10:00 — CONCLUSION & PERSPECTIVES

*[Les 4 se regroupent au centre. A devant.]*

*[3 secondes de silence.]*

**A** :
> *"Nous sommes partis d'un constat scientifique : l'IA grand public crée de la dette cognitive chez les élèves. Nous avons formulé quatre hypothèses. Pour les tester, nous avons construit un système complet : un modèle de 4 milliards de paramètres, quantifié en 4-bit, spécialisé par QLoRA sur 10 000 paires co-construites avec nos professeurs, protégé par un RAG ancré dans les manuels officiels, et déployé de façon autonome dans un téléphone grâce à MLC LLM."*

> *"Nos quatre hypothèses sont validées. Le score pédagogique est de 4,4 sur 5. L'application est publiée sur l'App Store. Près de 200 élèves l'utilisent. Une demande de brevet a été déposée auprès de l'INPI."*

> *"Nous connaissons nos limites : notre échantillon est restreint, notre couverture des matières est incomplète, et notre modèle reste perfectible sur les raisonnements les plus complexes. Ce prototype est un premier pas."*

*[Pause.]*

**A** :
> *"LUCID, ce n'est pas un projet d'élèves qui ont utilisé l'IA. C'est un projet d'élèves qui ont construit une IA. Et qui lui ont interdit de donner les réponses."*

> *"Merci."*

*[Silence. Rester immobiles.]*

---

## 🛠️ Triggers Accessoires (Rappel Rapide)

* **T= 0:00 (A+D)** : Téléphone en mode avion, écran vers le jury. Texte qui s'affiche.
* **T= 2:15 (B)** : LED verte, dominos tokens, fils de laine (Attention).
* **T= 3:00 (B)** : LED bleue, pointe l'architecture cloud souveraine.
* **T= 3:30 (A)** : Ardoise « Napoléon est mort en 1999 ».
* **T= 3:45 (C)** : Pile de fiches bristol (dataset).
* **T= 4:00 (D)** : Manuel scolaire lâché sur la table (RAG).
* **T= 4:15 (A)** : Pose théâtrale (analogie acteur/prompteur).
* **T= 5:30 (D)** : Duel double téléphone + carte question piège au jury.
* **BONUS (sur la table)** : Maquette éclatée, éprouvette, dé 20 faces.

---

## 📊 Comparatif V1 → V2

| Critère Jury | Script V1 (Startup) | Script V2 (Scientifique) |
|:---|:---|:---|
| Problématique formulée | ❌ | ✅ Phrase mot pour mot |
| Hypothèses explicites | ❌ | ✅ H1, H2, H3, H4 |
| Protocole d'évaluation détaillé | ⚠️ Chiffres seuls | ✅ Double protocole (benchmark + terrain) |
| Résultats contextualisés | ⚠️ Style marketing | ✅ Avec taille d'échantillon et nuances |
| Limites et échecs | ❌ Absent | ✅ 4 limites + 2 obstacles surmontés |
| Rôle des partenaires | ⚠️ Mentionnés vaguement | ✅ Rôle concret de chacun |
| Ton | Marketing / Keynote | Scientifique avec énergie |
| Accessoires spectaculaires | ✅ | ✅ Tous conservés |
| Démos live | 3 démos (trop long) | 1 démo ciblée (le duel, la plus percutante) |
| Durée estimée | ~15 min | ~10 min |
