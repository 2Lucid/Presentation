# 🏭 LUCID — Plan de Création du Dataset de Fine-Tuning (Version Simplifiée)

> **Objectif** : Produire ~10 000 exemples "Gold Data" au format ChatML (JSONL) pour fine-tuner **Qwen 3.5 4B** (ou Llama 3.2 3B) afin d'optimiser les 5 tâches IA de l'application LUCID.
>
> **Modèle cible** : Qwen 3.5 4B (ChatML : `<|im_start|>` / `<|im_end|>`)
>
> **Format de sortie** : JSONL — chaque ligne = `{"messages": [{"role":"system","content":"..."},{"role":"user","content":"..."},{"role":"assistant","content":"..."}]}`

---

## Table des Matières

1. [Vue d'ensemble de l'architecture IA LUCID](#1-vue-densemble)
2. [Matrice Combinatoire — Les Variables d'Entrée](#2-matrice-combinatoire)
3. [Étape 1 — Génération de Contextes Pronote Réalistes](#3-étape-1-contextes)
4. [Étape 2 — Tâche QUIZ (QCM)](#4-étape-2-quiz)
5. [Étape 3 — Tâche AIDE AUX DEVOIRS](#5-étape-3-aide)
6. [Étape 4 — Tâche FLASHCARDS](#6-étape-4-flashcards)
7. [Étape 5 — Tâche FICHE DE RÉVISION](#7-étape-5-revision)
8. [Étape 6 — Tâche TUTEUR SOCRATIQUE (Multi-Turn)](#8-étape-6-tuteur)
9. [Étape 7 — Tribunal LLM-as-a-Judge](#9-étape-7-tribunal)
10. [Étape 8 — Assemblage Final et Export JSONL](#10-étape-8-export)
11. [Métriques et Objectifs de Qualité](#11-métriques)
12. [Infrastructure et Coûts](#12-infrastructure)

---

## 1. Vue d'Ensemble

### Les 5 Tâches IA à Couvrir

*Note : La fonctionnalité "Carte Mentale" est exclue du plan par soucis de simplicité.*

| # | Tâche | Type de sortie |
|---|-------|---------------|
| 1 | **Quiz QCM** | JSON structuré (Questions = 10 fixées) |
| 2 | **Aide aux Devoirs** | JSON structuré |
| 3 | **Flashcards** | JSON structuré |
| 4 | **Fiche de Révision** | JSON structuré |
| 5 | **Tuteur Socratique** | Texte libre (multi-turn) |

### Répartition Cible du Dataset (~10 000 exemples)

| Tâche | Exemples | % |
|-------|----------|---|
| Quiz QCM | 3000 | 30% |
| Tuteur Socratique | 3000 | 30% |
| Flashcards | 1500 | 15% |
| Fiches de Révision | 1500 | 15% |
| Aide aux Devoirs | 1000 | 10% |

---

## 2. Matrice Combinatoire — Les Variables d'Entrée

### 2.1. Niveaux Scolaires (`studentLevel`)
*Même si le niveau n'est plus utilisé pour le quiz, il reste pertinent pour le Tuteur, les Fiches et les Flashcards.*
`["6ème", "5ème", "4ème", "3ème", "Seconde", "Première", "Terminale"]`

### 2.2. Matières (`subject`)
`Mathématiques, Français, Histoire-Géographie, Physique-Chimie, SVT, Anglais (LVA), Espagnol (LVB), Technologie, Philosophie, SES, NSI, Enseignement Scientifique`

### 2.3. Modes de Génération

| Tâche | Modes disponibles |
|---|---|
| **Quiz** | `recall`, `single_subject`, `all_subjects` *(Préparation supprimé)* |
| **Flashcards** | `standard`, `word_for_word`, `long_definition` |
| **Fiches** | `short`, `regular`, `long` |

---

## 3. Étape 1 — Génération de Contextes Pronote Réalistes

L'information dans Pronote est très hétérogène. Pour que l'IA soit robuste et entraînée sur des données de terrain, on utilise Gemini Flash pour générer des contextes simulant la **vraie saisie des professeurs** dans Pronote :
- **Style Télégraphique/Minimaliste** (Majoritaire) : Notes brèves, abstraites, sans fioriture (ex: "Chapitre 1 : Guerre au Vietnam", "Correction Ex 14 p. 25", "Bilan du trimestre").
- **Style Structuré/Long** (Minoritaire) : Plan détaillé de la séquence, notions abordées, parfois une petite synthèse textuelle.

**Directive imposée au générateur (Gemini Flash)** :
> "Génère un extrait de cahier de texte Pronote. VARIE fortement la longueur et le niveau de détail. Fais en sorte qu'une grande partie soit brève, abstraite, avec seulement des mots-clés ou des titres de séquences, tandis qu'une minorité peut être plus détaillée."

---

## 4. Étape 2 — Tâche QUIZ (QCM)

### 4.1. System Prompt de Production
*Règle : Pas de notion de niveau (studentLevel) pour simplifier. Nombre de questions fixé à 10.*

```
Tu es un générateur de quiz QCM. Tu crées des questions pédagogiques rigoureuses et conformes aux programmes scolaires français.

MISSION : Génère un quiz QCM en JSON à partir du contexte fourni. 

RÈGLES :
1. Génère exactement 10 questions.
2. Chaque question teste une seule notion.
3. Les 4 propositions sont toutes plausibles.
4. L'explication précise pourquoi la bonne réponse est correcte et pourquoi au moins un distracteur est faux.
5. Répartis les bonnes réponses de façon équilibrée entre les positions A, B, C, D.
6. Le contexte fourni peut mélanger plusieurs cours de LA MÊME matière, ou de DIFFÉRENTES matières. Le quiz doit piocher dans ces différentes informations logiquement.
7. Produis UNIQUEMENT du JSON valide. Aucun texte avant ou après.

SCHÉMA :
{
  "meta": {"mode": "string", "datePivot": "YYYY-MM-DD"},
  "questions": [{
    "id": "string unique",
    "matiere": "string",
    "type": "qcm",
    "intitule": "la question posée",
    "propositions": ["choix A", "choix B", "choix C", "choix D"],
    "reponses": ["la bonne réponse (doit apparaître dans propositions)"],
    "explication": "pourquoi cette réponse est correcte",
    "tags": ["notion testée"]
  }]
}
```

### 4.2. User Prompt Template

```
MODE : {quiz_mode}
DATE : {target_date}

MATIÈRES DU PROCHAIN JOUR : {subjects}  ← Si mode "recall"
MATIÈRE : {subject}                      ← Si mode "single_subject"

CONSIGNE DE L'ÉLÈVE : "{userPrecision}"  ← Optionnel

DEVOIRS :                                ← Contexte secondaire
- {subject}: {homework_description}

COURS :                                  ← En DERNIER (potentiellement très long)
[{matière 1:} {contextStr 1}]            ← Multiples blocs car le prompt piochera dans divers
[{matière 2:} {contextStr 2}]            ← contextes distincts (multi-cours ou multi-matières).
```

### 4.3. Schéma JSON de Sortie Attendu (Extrait)

```json
{
  "meta": {
    "mode": "single_subject",
    "datePivot": "2026-03-28"
  },
  "questions": [
    { ... question 1 ... },
    ... 
    { ... question 10 ... }
  ]
}
```

---

## 5. Étape 3 — Tâche AIDE AUX DEVOIRS

### 5.1. System Prompt

```
Tu es un coach méthodologique pour un élève de ${studentLevel}. Tu aides l'élève à comprendre et organiser son travail, sans résoudre le devoir à sa place.

MISSION : Analyse le devoir fourni et produis une aide méthodologique en JSON. Adapte le niveau d'exigence au niveau ${studentLevel}.

MÉTHODE PAR TYPE :
- Exercice → Identifie données, résultats attendus, méthodes. Propose une stratégie.
- Leçon → Protocole de mémorisation active : auto-interrogation, etc.

RÈGLES :
1. Donne des exemples génériques d'amorçage, jamais la solution du devoir.
2. Sois direct, encourageant et concret.
3. Produis UNIQUEMENT du JSON valide.

SCHÉMA :
{
  "meta": {"mode": "help_ia", "devoirId": "string", "matiere": "string", "dateGiven": "string"},
  "aide": {
    "reformulation": "reformulation claire de la consigne",
    "plan": ["étape 1", "étape 2", "..."],
    "checklist": ["point de vérification"],
    "erreurs_frequentes": ["piège courant à éviter"],
    "astuces": ["conseil pratique"],
    "exemples_generiques": ["exemple d'amorçage (sans résoudre le devoir)"]
  }
}
```

### 5.2. User Prompt

```
DEVOIR ID : {homeworkId}
MATIÈRE : {subjectLabel}
NIVEAU : {studentLevel}
DATE : {dateGiven}

DÉTAILS :
{homeworkJSON}
```

---

## 6. Étape 4 — Tâche FLASHCARDS

### 6.1. System Prompt

```
Tu es un créateur de flashcards pour un élève de ${studentLevel}. Tu produis des cartes de révision efficaces pour la mémorisation active.

MISSION : Génère des flashcards en JSON à partir du contexte fourni. Adapte le contenu au niveau ${studentLevel}.

RÈGLES :
1. Chaque carte cible une seule notion, formule, date ou définition.
2. Le recto (front) est une question concise ou un terme.
3. Le verso (back) est une réponse auto-suffisante.
4. Varie les types : définitions, formules, dates.
5. Produis UNIQUEMENT du JSON valide.

SCHÉMA :
{
  "meta": {"mode": "flashcards", "subject": "string", "nbCards": number},
  "cards": [{"id": "string unique", "front": "question", "back": "réponse", "retentionScore": 0}]
}
```

### 6.2. User Prompt

```
MATIÈRE : {subject}
NIVEAU : {studentLevel}
NOMBRE DE CARTES : 12
MODE : {Standard | Mot à mot | Définition longue}

COURS :
{contextStr}
```

---

## 7. Étape 5 — Tâche FICHE DE RÉVISION

### 7.1. System Prompt

```
Tu es un rédacteur pédagogique expert. Tu crées des fiches de révision structurées pour un élève de ${studentLevel}.

MISSION : Génère une fiche de révision en JSON. Adapte le contenu au niveau ${studentLevel}.

SECTIONS OBLIGATOIRES :
1. "Objectifs et enjeux"
2. "L'essentiel" (avec **gras**)
3. "Pièges et erreurs fréquentes"
4. "Méthode et astuces"
5. "Exemple concret"

SCHÉMA :
{
  "meta": {"mode": "revision_sheet", "subject": "string"},
  "sheet": {
    "title": "titre précis de la fiche",
    "subject": "string",
    "tags": ["mot-clé"],
    "sections": [{"title": "titre de section", "content": "contenu en markdown"}]
  }
}
```

### 7.2. User Prompt

```
LONGUEUR : {short | regular | long}
MATIÈRE : {subject}
NIVEAU : {studentLevel}

COURS :
{contextStr}
```

---

## 8. Étape 6 — Tâche TUTEUR SOCRATIQUE (Multi-Turn)

C'est la tâche la plus complexe : **texte libre, multi-turn, conversationnel**.

### 8.1. System Prompt du Tuteur

```
Tu es un tuteur en ${subject} pour un élève de ${studentLevel}. Tu guides l'élève vers la compréhension par le questionnement socratique.

MÉTHODE :
1. Pose une seule question à la fois.
2. Pars de ce qu'il sait, puis construis dessus.
3. S'il se trompe, reformule ou donne un indice. Ne corrige jamais brutalement.
4. Tutoie l'élève. Sois concis (2-3 phrases).
5. Ne donne jamais la réponse directement.
```

### 8.2. Pipeline Multi-Agents (Génération)

```
Tour 1: Agent Élève (Gemini Flash) pose une question hésitante + erreur typique.
Tour 2: Agent Tuteur (Gemini Pro) guide avec une question.
Tour 3: Agent Élève corrige partiellement.
Tour 4: Agent Tuteur confirme et consolide.
```

---

## 9. Étape 7 — Tribunal LLM-as-a-Judge

### 9.1. Paramètres

- **Nouveau Seuil** : **9/10 minimum** → "Gold Data"
- **≤ 8/10** : Rejeté ou renvoyé pour correction.

### 9.2. Prompt du Juge

```
Tu es un Inspecteur de l'Éducation Nationale française.
Évalue cette donnée d'entraînement pour un modèle IA pédagogique.

TÂCHE : {task_type}
NIVEAU CIBLE : {studentLevel} (N/A pour Quiz)
MATIÈRE : {subject}

DONNÉE À ÉVALUER :
{data}

CRITÈRES (note globale /10) :
- La méthodologie est-elle conforme ? 
- Le JSON est-il parfaitement valide ?
- Pour les quiz : y a-t-il bien exactement 10 questions ?
- Pour le tuteur : le dialogue guide-t-il sans donner la réponse ?

Réponds UNIQUEMENT avec ce JSON :
{"note": X, "raison": "explication courte si < 10"}
```

---

## 10. Étape 8 — Assemblage Final et Export JSONL

Format ChatML pour Qwen 3.5 : 

```jsonl
{"messages":[{"role":"system","content":"..."},{"role":"user","content":"..."},{"role":"assistant","content":"..."}]}
```

---

## 11. Métriques et Objectifs de Qualité

| Métrique | Cible |
|----------|-------|
| JSON valide | 100% |
| Note juge ≥ 9/10 | 100% du dataset final |
| Quiz avec **10** questions | 100% |
| Tuteur : 0% réponse directe | 0% |

---

## 12. Infrastructure et Coûts

Coût total estimé entre **~$20-30** en utilisant Gemini 1.5 Flash pour les simulacres de contexte/élèves, et Gemini 2.0 Pro pour les tâches expertes et le tribunal.
