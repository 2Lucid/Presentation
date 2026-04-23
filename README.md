# 🎤 LUCID — Fiche Orale Répétition

*Durée visée : 10-12 minutes / 4 Présentateurs*

## 🎭 1. Rôles et Placement

**A (Leader / Storyteller)** : À gauche. Ouvre le bal, gère les transitions, pose la punchline de fin.
**D (Démonstrateur)** : Au centre. Showman, tient les téléphones, gère toutes les démos live.
**B (Tech Lead)** : À droite. Gère l'explication archi et le *Panneau Cerveau* + *Poster Alliance*.
**C (Expet Impact)** : En léger retrait (vers *Balance*). Axe sociétal, PISA, anti-triche et écologie.

---

## 🎬 2. Le Script Mot pour Mot

### ⏱️ 0:00 → 2:00 — L'OUVERTURE CHOC

**[A s'approche face au jury avec une boîte transparente. D y dépose un téléphone.]**

**A :**
> *"On s'imagine toujours que l'Intelligence Artificielle flotte quelque part, très loin de nous, cachée sur d'immenses serveurs virtuels."*

**[A tape silencieusement sur l'écran et le tourne vers le jury. L'icône Mode Avion est ostensiblement visible. Le texte s'affiche tout seul, token par token.]**

**A :**
> *"Et pourtant, regardez bien cet écran. Ce téléphone est en mode avion. Il est totalement déconnecté du reste du monde. La phrase qui s'écrit sous vos yeux n'existe sur aucun serveur de la planète. L'intelligence n'est pas dans le Cloud. Elle est là, prisonnière dans cette boîte."*

*[Pause de 3 secondes. A sourit.]*

**A** : "Si vous demandez à ChatGPT de faire un devoir, il le fera. Tous les jours, les médias nous répètent que l'IA détruit l'éducation et que l'école a perdu la bataille. Mais nous, on a décidé de prendre le problème de face. Plutôt que de fuir, on a décidé de hacker cette arme. On a forgé l'IA la plus désagréable du monde pour un tricheur. Une IA qui refuse *obstinément* de donner la réponse."

*[A fait un signe à D. D reprend le téléphone en main.]*

**D** *(Montre l'écran)* : "Connexion Pronote... Cours du lendemain détectés... Un quiz sur-mesure est généré. Sans Internet."

**A** : "Son nom est LUCID." *(A marque une micro-pause et sourit)* "Avec une simple connexion Pronote, l'application synchronise le profil complet de l'élève en quelques secondes : son emploi du temps, ses devoirs à faire, ses notes. À partir de cette base de données personnelle, LUCID déploie un écosystème d'intelligences artificielles : génération de quiz sur-mesure, flashcards interactives, duels de connaissances, et tuteur conversationnel.
Et le plus fou, c'est ce qu'il se passe en ce moment même. Ce matin à 8h, près de 200 élèves ont sorti leur téléphone, non pas pour TikTok, mais pour réviser. On a mené une vraie démarche de recherche avec 47 bêta-testeurs : questionnaires formels, grilles d'évaluation, benchmarks techniques. Toutes les données que vous entendrez aujourd'hui viennent d'eux, de leurs retours terrain. On a compilé tout ça dans un papier de recherche. Résultat : 89% recommandent l'app et 74% la préfèrent à ChatGPT. Nous avons été audités par Apple, l'app est publiée sur l'App Store grâce à notre partenaire Lucarne Pro. Ce qu'on va vous montrer aujourd'hui, ce n'est pas une maquette bricolée, c'est un produit global, fini et vivant. Mais pour le comprendre, il faut ouvrir le capot. Et c'est lui qui a construit le moteur." *(A désigne B et recule)*

---

### ⏱️ 2:00 → 4:00 — LA MACHINE (Architecte B)

**B** *(Pointe la Maquette Décortiquée)* : "Merci. LUCID repose sur une architecture hybride. Deux cerveaux."

*[B s'approche du Panneau Plexiglas, allume la LED Verte]*

**B** : "**Premier cerveau : local.** Un modèle Qwen 3.5 de 4 milliards de paramètres, quantifié en 4-bit au format NF4. Quand l'élève tape 'Explique-moi les suites', le modèle ne lit pas des mots. Il découpe la phrase en tokens."
*[B déplace les dominos en bois un par un sur le panneau]*
"Chaque token calcule mathématiquement sa pertinence avec les autres."
*[B montre les fils de laine tendus (Attention)]*
"Le token 'suites' regarde 'maths'. Il ignore 'moi'. C'est le pur calcul du mécanisme d'Attention : l'équation **Softmax(Q·K^T / √d_k) · V**. Et cette algèbre linéaire tourne en local via MLC LLM, directement sur le NPU et le GPU du téléphone. On a mesuré : 30 tokens par seconde sur un iPhone 14, le texte s'affiche au rythme naturel de la lecture."

*[B allume la LED Bleue]*

**B** : "**Deuxième cerveau : le Cloud souverain.** On n'impose pas le local. Même sur les tablettes Lenovo fournies par la Région Sud, que la majorité des lycéens ont à disposition, LUCID tourne : on descend à 7 tokens par seconde, c'est utilisable. Mais pour plus de fluidité, on propose un modèle Qwen 14B hébergé sur notre propre Mac Mini M4, fourni par Lucarne Pro et physiquement hébergé chez notre partenaire AxePI, via Cloudflare Tunnel. L'avantage : 58 tokens par seconde, plus rapide. L'inconvénient : le coût serveur, donc le lycéen sera limité en nombre de requêtes quotidiennes, alors que le modèle local est totalement gratuit et illimité. Mais même en Cloud, on fait les choses bien. La requête passe par notre proxy sécurisé via Cloudflare Tunnel. 87% de nos bêta-testeurs font confiance à LUCID pour protéger leurs données, contre seulement 19% pour ChatGPT."

*[B pointe le grand poster]*

**B** : "Faire tourner un Small Model en éducation, c'est risqué. Dans un premier temps, on a travaillé le comportement : le **Fine-Tuning** via QLoRA. Au lieu d'entraîner les 4 milliards de paramètres, ce qui serait impossible pour des lycéens, on gèle le modèle original et on n'entraîne que de petites matrices de bas-rang. La formule : **ΔW = B·A**, où le rang r = 16, soit seulement 0,1% des paramètres. On a entraîné sur 3 époques complètes avec un taux d'apprentissage de 2×10⁻⁴."

*[C s'avance et tend à B une épaisse pile de fiches bristol]*

**B** : "Et ces fiches, c'est notre dataset. En partenariat avec les professeurs du Lycée Henri Matisse, on a collecté 1 000 exemples pédagogiques socratiques écrits à la main. Puis, grâce à notre plateforme Lucid Labs, on a généré 9 000 exemples supplémentaires par distillation de connaissances, validés un par un par les enseignants via notre outil Lucid Professeur. Total : **10 000 paires question-réponse** ancrées dans les programmes officiels. L'IA a appris *comment* guider, pas donner la réponse. Sa perte finale sur notre dataset : 0,87, ce qui confirme la spécialisation sans sur-apprentissage. Mais il y avait un gros problème : les petits modèles hallucinent."

*[A lève silencieusement une ardoise. Il est écrit dessus : "Napoléon est mort en 1999."]*

**B** : "Voilà. En classe, c'est impensable. Alors on a développé un **RAG** extrême. C'est le QUOI."

*[D s'avance et lâche lourdement un énorme manuel scolaire sur la table (Bruit sourd "BAM")]*

**B** : "L'Open Education : tous les manuels libres de la 6ème à la Terminale embarqués dans le téléphone, indexés en vecteurs via un modèle d'embedding. Le RAG verrouille l'IA strictement dans cette base de connaissances vérifiées pour bloquer toute aberration historique ou scientifique.

Pour résumer : l'IA est un acteur de génie."

*[A dépose l'ardoise et prend une pose théâtrale (ex: main au menton, penseur)]*

**B** : "Le Fine-Tuning lui apprend l'attitude. Mais s'il n'a pas de texte, il improvise."

*[C s'approche de A, et lui plante le gros manuel scolaire dans les mains]*

**B** : "Le RAG, c'est le prompteur qui lui dicte la stricte vérité. L'un donne l'attitude, l'autre donne la vérité. L'inventivité trompeuse a totalement disparu."

---

### ⏱️ 4:00 → 6:30 — L'IMPACT (Expert C)

**A** *(Revient)* : "L'architecture, c'est le comment. La pédagogie, c'est le pourquoi. Et les résultats parlent d'eux-mêmes : nos correcteurs ont évalué 40 réponses sur 5 critères. LUCID obtient un score pédagogique de 4,4 sur 5, contre seulement 2,6 pour ChatGPT. Parce qu'une IA qui donne les réponses toutes faites ne sert à rien. Pourquoi LUCID refuse de tricher ?" *(A désigne C)*

**C** *(Avance près de la balance, regard assombri, très solennel)* : "Regardez nos classes. Le véritable mur de notre génération, ce n'est pas la difficulté des programmes... c'est la solitude face à l'échec. Selon le rapport PISA 2022 de l'OCDE, la France présente un écart de près de 100 points entre un élève favorisé et un élève défavorisé."

*[C pointe lentement le jury du doigt]*

**C** : "Si vos parents ont de l'argent, ils vous paient un professeur particulier à 40€ de l'heure. S'ils n'en ont pas, ou ne sont pas là... vous rentrez le soir, seul dans votre chambre, face à un exercice de maths ou d'histoire incompréhensible. Cette détresse silencieuse brise des dizaines de milliers d'avenirs par an. LUCID répare cette fracture. On a pris ce prof à 40€ de l'heure, et on l'a mis dans la poche de TOUS nos camarades. Gratuitement. Hors ligne. Même sur un téléphone cassé à 150€."

*[C attrape les cartes Privacy ("CLOUD" et "LOCAL"). Il jette lourdement les cartes LOCAL sur le plateau droit, qui s'enfonce violemment.]*

**C** : "Mais la vraie urgence, c'est ce naufrage d'intelligence." *(Il regarde le jury dans les yeux)* "Quand les IA grand public sont sorties, on a vu le désastre dans les couloirs. L'élève prend la photo, la machine crache la réponse magique, le cerveau de l'élève s'éteint. La chercheuse de Harvard Maes a documenté ce phénomène : l'accumulation de dette cognitive. On fabrique une génération sous perfusion intellectuelle." 

**[C se déplace vers l'affiche des 6 catégories de Paul & Elder, et la frappe sèchement du poing]**

**C :**
> *"LUCID est là pour empêcher ce naufrage. Notre solution ne sort pas de notre imagination, elle sort de la littérature scientifique. L'IA est enchaînée aux travaux du chercheur Richard Paul sur la Maïeutique Socratique. Au lieu de livrer une réponse morte, elle déconstruit l'élève sur 6 dimensions... Demandez-lui la dérivée de x², et l'IA, intraitable, refusera de vous la donner. Elle ciblera votre faille : 'Que sais-tu du taux de variation ?'. LUCID force le lycéen à réactiver le mouvement de sa propre pensée."*

**C :**
> *"L'impact est planétaire. De récentes études scientifiques des universités californiennes, dirigées par Shaolei Ren, ont révélé un fait terrifiant. Aujourd'hui, lorsqu'un élève fait ses devoirs sur ChatGPT, sa question traverse des câbles sous-marins et demande l'évaporation de près d'un demi-litre d'eau douce par session, juste pour refroidir les serveurs ! C'est une folie environnementale pour réviser un cours de Terminale.*
>
> *Le choix politique de LUCID, c'est le triomphe du Edge Computing. Aucune eau ne bout. La facture énergétique est divisée par 100 parce que l'IA tourne localement, sur cette banale puce électronique que l'élève gardait de toute façon dans sa poche pour s'abrutir sur TikTok.*
>
> *Le choix que propose LUCID n'est pas technologique. C'est le seul choix de société durable que nous puissions léguer à notre génération."*

---

### ⏱️ 6:30 → 11:00 — LES 3 DÉMOS LIVE (Démonstrateur D)

**A** *(Revient au centre)* : "Vous avez vu la science. Vous avez vu l'impact. Maintenant... On va vous prouver que ça marche. Sans filet." *(Fait signe à D)*

**[🚨 Démo 1 : Mode Avion (1 min)]**
**D** : "Preuve numéro 1." *(Montre le téléphone LUCID)* "Je vais activer le mode avion. Plus de Wi-Fi, plus de 4G." *(Il swipe et tape).* "Je pose ma question. Observez. 3 milliards de paramètres, 2Go en inférence... L'IA me répond. Aucune donnée ne sort de cette salle."

*[A tape silencieusement sur l'écran. (NOTE TECHNIQUE : Prévoir connexion téléphone vers Mac pour répliquer l'écran et mieux y voir). L'icône Mode Avion est ostensiblement visible par le jury. Le texte s'affiche tout seul, token par token.]*

**[🚨 Démo 2 : Le Duel (1.5 min)]**
**D** : "Deuxième preuve. ChatGPT contre LUCID." *(Il sort un 2ème téléphone avec ChatGPT et passe la 'Question Piège imprimée' au jury).* "Lisez-la s'il vous plaît... Je pose la même question aux deux."
*[D tape en miroir]* 
"ChatGPT donne tout de suite la réponse. Et ne détecte pas le hors-sujet. LUCID... s'arrête. LUCID vous demande 'D'où sors-tu cette formule ?' ChatGPT distribue des poissons, LUCID apprend à pêcher."

**[🚨 Démo 3 : Jury Maker (1.5 min)]**
**D** *(Se tourne vers le jury)* : "Dernière preuve : c'est vous qui choisissez. Donnez-moi un thème de cours de votre choix. Histoire, maths, philo ?"
"Je demande un quiz de 5 questions sur [Sujet du Jury]. En direct... Et voilà. Oubliez ChatGPT. Si vous vous trompez à ce quiz, LUCID vous expliquera gentiment pourquoi."

---

### ⏱️ 11:00 → 12:00 — LA CLÉ DE VOÛTE (Clôture)

*[Les 4 se regroupent au centre, A devant.]*

*[3 secondes de silence]*

**A** : "On nous dit que l'IA va creuser les inégalités. 
Nous on est 4 lycéens. On a pris un modèle Qwen de 4 milliards de paramètres.
On l'a quantifié en 4-bit NF4.
On l'a spécialisé avec QLoRA sur un dataset de 10 000 paires forgées avec nos professeurs.
On l'a déployé de façon autonome dans un téléphone grâce à MLC LLM.
Et on lui a INTERDIT de donner les réponses.

Résultat : un tuteur gratuit, privé, écologique, noté 4,4 sur 5 par nos correcteurs, qui tourne sur un téléphone standard sans Internet. 

Une demande de brevet a été déposée sur notre architecture, accompagnée par AxePI. Les enseignants-chercheurs de Polytech Nice Sophia ont validé notre choix d'architecture hybride.

LUCID, ce n'est pas un projet d'élèves qui ont *utilisé* l'IA.
C'est un projet d'élèves qui ont **construit** une IA. 

Merci."

*[Coupure nette. Rester immobiles. C'est gagné.]*

---

## 🛠️ Triggers Accessoires (Rappel Rapide)
* **T= 0:00 (A)** : Lève le smartphone.
* **T= 1:00 (D)** : Écran Pronote live.
* **T= 2:30 (B)** : LED verte locale, dominos tokens, lanières Attention.
* **T= 3:30 (B)** : LED Bleue cloud, pointe Poster RAG+FineTuning.
* **T= 5:00 (C)** : Place les poids/cartes sur la Balance.
* **T= 6:00 (C)** : Pointe Affiche Paul & Elder (Socrate).
* **T= 7:00 (D)** : Swipe mode avion et montre la génération de tokens.
* **T= 8:00 (D)** : Double téléphone duel + Cartes Piège lues par Jury.
* **T= 9:30 (D)** : Prompt live selon le mot imposé par le jury.
* **BONUS** : Sur la table de secours : la maquette éclatée, l'éprouvette (2L = modèle compressé), le dé 20 faces (température Softmax).
