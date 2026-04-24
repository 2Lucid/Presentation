# 💰 Pricing et Tiers — LUCID

---

## 1. Modèle : Freemium → Pro → Enterprise

> **Statut actuel :** L'application est 100% gratuite. Le modèle Freemium est prévu pour la Phase 2.

---

## 2. Offres Prévues

### 2.1. 🆓 LUCID Free (Gratuit)

| Fonctionnalité | Limite |
|---|---|
| Hub scolaire (notes, EDT, devoirs) | ✅ Illimité |
| Connexion Pronote | ✅ |
| Gamification (XP, niveaux, badges) | ✅ Illimité |
| Leaderboard | ✅ |
| Ajout d'amis | ✅ |
| Quiz IA | ❌ 3/jour |
| Flashcards IA | ❌ 2/jour |
| Fiches de Révision IA | ❌ 1/jour |
| Aide aux Devoirs IA | ❌ 2/jour |
| Tuteur Socratique IA | ❌ 5 min/jour |
| Export calendrier | ✅ |
| Publicités | 🟡 Bannières discrètes (éventuel) |

### 2.2. ⭐ LUCID Pro (4.99€/mois ou 39.99€/an)

| Fonctionnalité | Limite |
|---|---|
| Tout ce qui est dans Free | ✅ |
| Quiz IA | ✅ **Illimité** |
| Flashcards IA | ✅ **Illimité** |
| Fiches de Révision IA | ✅ **Illimité** |
| Aide aux Devoirs IA | ✅ **Illimité** |
| Tuteur Socratique IA | ✅ **Illimité** |
| Badge "Pro" sur le profil | ✅ |
| Thèmes exclusifs | ✅ |
| Support prioritaire | ✅ |
| Sans publicité | ✅ |
| Accès anticipé aux nouvelles features | ✅ |

**Prix annuel = 33% de réduction** par rapport au mensuel (39.99€ vs 59.88€)

### 2.3. 🏫 LUCID Enterprise (Sur devis)

| Fonctionnalité | Détail |
|---|---|
| Toutes les features Pro | ✅ Pour tous les élèves de l'établissement |
| Dashboard établissement | ✅ Métriques d'engagement par classe |
| Lucid Prof intégré | ✅ Plateforme de création pour les enseignants |
| Support dédié | ✅ Interlocuteur unique |
| Personnalisation | ✅ Branding établissement possible |
| Formation | ✅ Onboarding profs et admin |
| SLA | ✅ Temps de réponse garanti |
| Facturation | Annuelle, par élève |
| **Prix indicatif** | 2-5€/élève/an |

---

## 3. Logique de Pricing

### 3.1. Pourquoi ce prix ?

| Critère | Justification |
|---|---|
| **4.99€/mois** | Inférieur à un café par semaine — accessible pour un lycéen/étudiant |
| **Comparable Kartable** | Kartable premium = 9.99€/mois → LUCID est 50% moins cher |
| **Valeur perçue** | IA personnalisée (vs contenu générique) justifie le paiement |
| **Seuil psychologique** | <5€ = achat impulsif, pas besoin de demander aux parents |

### 3.2. Monétisation Alternative Envisagée

| Option | Statut | Commentaire |
|---|---|---|
| Publicité in-app | 🟡 Peut-être | Bannières discrètes uniquement, jamais intrusif |
| In-App Purchase (items) | ❌ Rejeté | Pas de pay-to-win, contraire aux valeurs |
| Data selling | ❌ Jamais | Contraire au RGPD et à nos principes |

---

## 4. Paiement

### 4.1. iOS
- **Méthode :** Apple In-App Purchase (obligatoire sur iOS)
- **Commission Apple :** 30% la première année, 15% après (Small Business Program)
- **Gestion :** Via StoreKit 2 / RevenueCat (à implémenter)

### 4.2. Android (futur)
- **Méthode :** Google Play Billing
- **Commission :** 15% (Small Business Program)

### 4.3. Web (Lucid Prof Enterprise)
- **Méthode prévue :** Stripe
- **Statut :** Non implémenté

---

## 5. Projections de Revenus

### Hypothèses

| Variable | Valeur |
|---|---|
| Base utilisateurs Free (Y1) | 5 000 |
| Taux de conversion Free → Pro | 5% |
| Prix moyen/mois | 4.99€ |
| Commission Apple | 15% (après Y1) |

### Projection

| Mois | Users Free | Users Pro | MRR Brut | MRR Net (après Apple) |
|---|---|---|---|---|
| M6 | 1 000 | 50 | 250€ | 212€ |
| M12 | 5 000 | 250 | 1 250€ | 1 062€ |
| M18 | 10 000 | 500 | 2 500€ | 2 125€ |
| M24 | 20 000 | 1 000 | 5 000€ | 4 250€ |

> 💡 Ces projections sont conservatrices. Un taux de conversion de 5% est bas pour une app avec une forte proposition de valeur IA.
