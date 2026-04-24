with open("raw_script.html", "r") as f:
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
    ("un tuteur — elle ne donne jamais la réponse, elle guide — les étudiants", "un tuteur (elle ne donne jamais la réponse, elle guide), les étudiants"),
    ("posture socratique — guider par le questionnement sans livrer la réponse — améliore", "posture socratique (guider par le questionnement sans livrer la réponse) améliore"),
    ("données précieuses — les vrais cours", "données précieuses : les vrais cours"),
    ("guide au lieu de répondre — pas seulement", "guide au lieu de répondre. Pas seulement"),
    ("cinq étapes — et à chaque fois", "cinq étapes, et à chaque fois"),
    ("Pour notre hypothèse H2 — la confidentialité —, c'était", "Pour notre hypothèse H2 (la confidentialité), c'était"),
    ("notre RAG Pronote — l'IA utilise", "notre RAG Pronote : l'IA utilise"),
    ("COPPA et RGPD — les réglementations de protection des mineurs", "COPPA et RGPD (les réglementations de protection des mineurs)"),
    ("de Google — dans le cloud", "de Google, dans le cloud"),
    ("changé le modèle — Qwen 3.5, deux fois plus compact avec 4 milliards de paramètres, compressé en 4-bit — et le moteur", "changé le modèle (Qwen 3.5, deux fois plus compact avec 4 milliards de paramètres, compressé en 4-bit) et le moteur"),
    ("l'aide aux devoirs — partout", "l'aide aux devoirs, partout"),
    ("chaque interaction — lui interdire", "chaque interaction : lui interdire"),
    ("0,1% des paramètres — mais ce 0,1%", "0,1% des paramètres, mais ce 0,1%"),
    ("bien entraîné, hallucine — il invente", "bien entraîné, hallucine : il invente"),
    ("RAG — Retrieval Augmented Generation", "RAG (Retrieval Augmented Generation)"),
    ("cours, il improvise — et il raconte", "cours, il improvise, et il raconte"),
    ("cinq assistants IA — tuteur socratique, quiz, flashcards, fiches de révision, aide aux devoirs — le tout", "cinq assistants IA (tuteur socratique, quiz, flashcards, fiches de révision, aide aux devoirs), le tout"),
    ("indépendants — notre professeur encadrant et un enseignant volontaire — ont évalué", "indépendants (notre professeur encadrant et un enseignant volontaire) ont évalué"),
    ("enseigne mieux — on a construit", "enseigne mieux : on a construit"),
    ("cinq matières — les langues et les arts sont exclus", "cinq matières (les langues et les arts sont exclus)"),
    ("un constat — les IA grand public créent de la dette cognitive — et nous avons", "un constat (les IA grand public créent de la dette cognitive) et nous avons"),
]

for old, new in replacements:
    text = text.replace(old, new)

with open("raw_script.html", "w") as f:
    f.write(text)
