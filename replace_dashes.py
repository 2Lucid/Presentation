import re

with open("SCRIPT_V4.md", "r") as f:
    text = f.read()

# Heading replacements
text = text.replace("LUCID — Script Oral", "LUCID : Script Oral")
text = text.replace("0:00 → 1:45 — PROBLÉMATIQUE", "0:00 → 1:45 : PROBLÉMATIQUE")
text = text.replace("1:45 → 2:30 — ÉTAT", "1:45 → 2:30 : ÉTAT")
text = text.replace("2:30 → 5:45 — NOTRE", "2:30 → 5:45 : NOTRE")
text = text.replace("Étape 1 — Le socle", "Étape 1 : Le socle")
text = text.replace("Étape 2 — Le test", "Étape 2 : Le test")
text = text.replace("Étape 3 — Tester", "Étape 3 : Tester")
text = text.replace("Étape 4 — Tester", "Étape 4 : Tester")
text = text.replace("Étape 5 — Ancrer", "Étape 5 : Ancrer")
text = text.replace("5:45 → 7:00 — DÉMO", "5:45 → 7:00 : DÉMO")
text = text.replace("7:00 → 10:00 — RÉSULTATS", "7:00 → 10:00 : RÉSULTATS")
text = text.replace("table — bruit sourd", "table (bruit sourd)")
text = text.replace("table — BAM", "table : BAM")

# In-text replacements
replacements = [
    ("ne révisent plus du tout — ils recopient", "ne révisent plus du tout, ils recopient"),
    ("solution, LUCID — en mode avion", "solution, LUCID, en mode avion"),
    ("un tuteur — elle ne donne jamais", "un tuteur (elle ne donne jamais la réponse, elle guide), les étudiants"), # manual
    ("posture socratique — guider", "posture socratique (guider par le questionnement sans livrer la réponse) améliore"), # manual
    ("données précieuses — les vrais cours", "données précieuses : les vrais cours"),
    ("guide au lieu de répondre — pas seulement", "guide au lieu de répondre. Pas seulement"),
    ("cinq étapes — et à chaque fois", "cinq étapes, et à chaque fois"),
    ("Pour notre hypothèse H2 — la confidentialité —, c'était", "Pour notre hypothèse H2 (la confidentialité), c'était"),
    ("notre RAG Pronote — l'IA utilise", "notre RAG Pronote : l'IA utilise"),
    ("COPPA et RGPD — les réglementations", "COPPA et RGPD (les réglementations de protection des mineurs)"),
    ("de Google — dans le cloud", "de Google, dans le cloud"),
    ("changé le modèle — Qwen 3.5", "changé le modèle (Qwen 3.5, deux fois plus compact avec 4 milliards de paramètres, compressé en 4-bit) et le moteur"),
    ("l'aide aux devoirs — partout", "l'aide aux devoirs, partout"),
    ("chaque interaction — lui interdire", "chaque interaction : lui interdire"),
    ("0,1% des paramètres — mais ce 0,1%", "0,1% des paramètres, mais ce 0,1%"),
    ("bien entraîné, hallucine — il invente", "bien entraîné, hallucine : il invente"),
    ("RAG — Retrieval Augmented Generation", "RAG (Retrieval Augmented Generation)"),
    ("cours, il improvise — et il raconte", "cours, il improvise et il raconte"),
    ("cinq assistants IA — tuteur", "cinq assistants IA (tuteur socratique, quiz, flashcards, fiches de révision, aide aux devoirs), le tout"),
    ("indépendants — notre professeur encadrant et un enseignant volontaire — ont évalué", "indépendants (notre professeur encadrant et un enseignant volontaire) ont évalué"),
    ("enseigne mieux — on a construit", "enseigne mieux : on a construit"),
    ("cinq matières — les langues", "cinq matières (les langues et les arts sont exclus)"),
    ("un constat — les IA grand", "un constat (les IA grand public créent de la dette cognitive) et nous avons"),
]

for old, new in replacements:
    text = text.replace(old, new)

# Some fixes for trailing stuff
text = text.replace("un tuteur (elle ne donne jamais la réponse, elle guide), les étudiants", "un tuteur (elle ne donne jamais la réponse, elle guide), les étudiants")
text = text.replace("posture socratique (guider par le questionnement sans livrer la réponse) améliore", "posture socratique (guider par le questionnement sans livrer la réponse) améliore")
text = text.replace("COPPA et RGPD (les réglementations de protection des mineurs) de protection des mineurs", "COPPA et RGPD (les réglementations de protection des mineurs)")
text = text.replace("compressé en 4-bit) et le moteur d'inférence, en passant de llama.cpp à MLC LLM, optimisé pour les puces mobiles. Résultat : 30 tokens par seconde sur un iPhone 14. H3 était enfin validée. Et H2 avec elle : zéro donnée ne sort du téléphone.\"*", "compressé en 4-bit) et le moteur d'inférence, en passant de llama.cpp à MLC LLM, optimisé pour les puces mobiles. Résultat : 30 tokens par seconde sur un iPhone 14. H3 était enfin validée. Et H2 avec elle : zéro donnée ne sort du téléphone.\"*")

# Manual tricky ones:
text = re.sub(r"un tuteur — elle ne donne jamais la réponse, elle guide — les étudiants", r"un tuteur (elle ne donne jamais la réponse, elle guide), les étudiants", text)
text = re.sub(r"posture socratique — guider par le questionnement sans livrer la réponse — améliore", r"posture socratique (guider par le questionnement sans livrer la réponse) améliore", text)
text = re.sub(r"Pour notre hypothèse H2 — la confidentialité —, c'était", r"Pour notre hypothèse H2 (la confidentialité), c'était", text)
text = re.sub(r"COPPA et RGPD — les réglementations de protection des mineurs", r"COPPA et RGPD (les réglementations de protection des mineurs)", text)
text = re.sub(r"changé le modèle — Qwen 3\.5, deux fois plus compact avec 4 milliards de paramètres, compressé en 4-bit — et le moteur", r"changé le modèle (Qwen 3.5, deux fois plus compact avec 4 milliards de paramètres, compressé en 4-bit) et le moteur", text)
text = re.sub(r"indépendants — notre professeur encadrant et un enseignant volontaire — ont évalué", r"indépendants (notre professeur encadrant et un enseignant volontaire) ont évalué", text)
text = re.sub(r"cinq assistants IA — tuteur socratique, quiz, flashcards, fiches de révision, aide aux devoirs — le tout", r"cinq assistants IA (tuteur socratique, quiz, flashcards, fiches de révision, aide aux devoirs), le tout", text)
text = re.sub(r"un constat — les IA grand public créent de la dette cognitive — et nous avons", r"un constat (les IA grand public créent de la dette cognitive) et nous avons", text)
text = re.sub(r"cinq matières — les langues et les arts sont exclus\.", r"cinq matières (les langues et les arts sont exclus).", text)

with open("SCRIPT_V4.md", "w") as f:
    f.write(text)

print("Done")
