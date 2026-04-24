# 📊 KPIs et Métriques — LUCID

---

## 1. Métriques Business (North Star)

| KPI | Définition | Objectif Phase 1 | Objectif Phase 3 |
|---|---|---|---|
| **MAU** (Monthly Active Users) | Utilisateurs actifs par mois | 500+ | 20 000+ |
| **MRR** (Monthly Recurring Revenue) | Revenus récurrents mensuels (abonnements Pro) | 0€ (gratuit) | 5 000€+ |
| **Churn Rate** | % d'utilisateurs qui arrêtent l'app par mois | <10% | <5% |

---

## 2. Métriques Produit

### 2.1. Acquisition

| KPI | Définition | Comment le Mesurer |
|---|---|---|
| **Installations** | Nombre total de téléchargements | App Store Connect / Play Console |
| **CPI** (Cost per Install) | Coût pour chaque installation | Dépenses Ads / Installations |
| **Source d'acquisition** | D'où viennent les utilisateurs | UTM tags (lucid_redirect), Instagram Insights |
| **Conversion QR→Install** | % des scans QR qui installent | lucid_redirect analytics |

### 2.2. Activation

| KPI | Définition | Seuil de Succès |
|---|---|---|
| **Onboarding complété** | % des installeurs qui connectent Pronote | >70% |
| **Première action IA** | % qui utilisent un quiz/flashcard dans les 24h | >30% |
| **Time to first value** | Temps entre l'install et le premier "wow moment" | <5 min |

### 2.3. Engagement

| KPI | Définition | Objectif |
|---|---|---|
| **DAU** (Daily Active Users) | Utilisateurs actifs par jour | >30% du MAU |
| **DAU/MAU** | Ratio d'engagement quotidien | >30% (excellent >40%) |
| **Sessions/jour** | Nombre moyen de sessions par utilisateur par jour | >1.5 |
| **Durée de session** | Temps moyen passé par session | >3 min |
| **Quiz complétés/jour** | Nombre moyen de quiz terminés par user actif | >1 |
| **XP gagné/jour moyen** | XP moyen par utilisateur actif | Mesurer la tendance |

### 2.4. Rétention

| KPI | Définition | Objectif |
|---|---|---|
| **D1 Retention** | % des installeurs actifs le lendemain | >50% |
| **D7 Retention** | % des installeurs actifs après 7 jours | >30% |
| **D30 Retention** | % des installeurs actifs après 30 jours | >20% |
| **Reactivation Rate** | % des churned users qui reviennent | Mesurer |

### 2.5. Revenus (Futur)

| KPI | Définition | Objectif |
|---|---|---|
| **Conversion Free→Pro** | % des utilisateurs gratuits qui upgraden | >5% |
| **ARPU** (Average Revenue Per User) | Revenu moyen par utilisateur (tous users) | >0.25€/mois |
| **ARPPU** (Average Revenue Per Paying User) | Revenu moyen par abonné Pro | ~4.99€/mois |
| **LTV** (Lifetime Value) | Valeur totale d'un utilisateur sur sa durée de vie | >30€ |
| **CAC** (Customer Acquisition Cost) | Coût total pour acquérir un utilisateur | <5€ |
| **LTV/CAC Ratio** | Retour sur l'acquisition | >3x |

---

## 3. Métriques Techniques

### 3.1. Performance App

| KPI | Objectif |
|---|---|
| **Temps de lancement** (cold start) | <2s |
| **Crash rate** | <1% |
| **API Latency (Supabase)** | <200ms |
| **API Latency (Gemini — beta)** | <3s |
| **Edge AI Latency (Gemma — target)** | <500ms |
| **Taille du bundle** | <80MB (incluant le modèle Gemma) |

### 3.2. Infrastructure

| KPI | Objectif |
|---|---|
| **Uptime sites web** | >99.5% |
| **Supabase DB size** | Surveiller (free tier = 500MB) |
| **Gemini API usage/day** | Surveiller les quotas |
| **Build success rate (Vercel)** | >95% |

---

## 4. Métriques IA (Lucid Labs)

| KPI | Définition | Objectif |
|---|---|---|
| **Total Examples** | Exemples générés au total | 10 000+ |
| **Gold Data** | Exemples avec score juge ≥ 9/10 | 10 000 (100% du dataset final) |
| **Judge Pass Rate** | % des exemples qui passent le juge | >85% |
| **Gold Rate by Task** | % de gold par type de tâche | >80% pour chaque |
| **JSON Validity** | % de JSON valide dans les sorties IA | 100% |
| **Tokens/Example** | Consommation moyenne de tokens par exemple | Optimiser (minimiser le coût) |
| **Quiz 10Q Compliance** | % des quiz ayant exactement 10 questions | 100% |
| **Tutor No-Answer Rate** | % des conversations tuteur où l'IA ne donne pas la réponse | 100% |
| **Edge vs Cloud Quality** | Score de qualité du modèle Gemma edge vs Gemini API | >95% de parité |
| **Gemma Inference Time** | Temps de réponse on-device moyen | <500ms |

---

## 5. Métriques Gamification

| KPI | Définition | Ce qu'on surveille |
|---|---|---|
| **XP total distribué** | Somme de tous les XP de tous les users | Croissance |
| **Niveau moyen** | Niveau moyen des utilisateurs actifs | Progression |
| **Badges débloqués** | Nombre total de badges débloqués | Engagement features |
| **Leaderboard actifs** | Nombre d'utilisateurs dans le top 50 | Compétition |
| **XP sync errors** | Erreurs de synchronisation bidirectionnelle | <0.1% |

---

## 6. Outils de Mesure

| Métrique | Outil Actuel | Outil Prévu |
|---|---|---|
| Installations | App Store Connect | + PostHog |
| Engagement | Supabase Dashboard (manuel) | PostHog / Mixpanel |
| Revenus | Apple App Store Connect | + RevenueCat |
| Performance | Console.log (pas idéal) | Sentry |
| IA Metrics | Lucid Labs Dashboard (custom) | ✅ Déjà en place |
| Uptime | Manuel | Uptime Robot |
| SEO | — | Google Search Console |

---

## 7. Dashboard de Suivi (Lucid Dashboard)

Le `lucid_dashboard` affiche déjà :
- 📊 Nombre total d'utilisateurs
- 📈 Nouvelles inscriptions par période
- 🏆 Top utilisateurs par XP
- 📍 Carte d'implantation géographique
- 🤖 Rapports d'analyse IA (via Gemini) automatisés
- 📧 Programmation de rapports par email (via Resend)
