# 📋 Backlog et Features Futures — LUCID

---

## Légende Priorité
- 🔴 **P0** — Critique (prochaine release)
- 🟡 **P1** — Important (3-6 mois)
- 🟢 **P2** — Nice to have (6-12 mois)
- 🔵 **P3** — Exploration (1 an+)

---

## 1. Application Mobile

| # | Feature | Priorité | Description | Complexité |
|---|---|---|---|---|
| M1 | Support Android (Google Play) | 🔴 P0 | Packaging et publication de l'app Expo sur le Play Store | Moyenne |
| M2 | Carte Mentale IA | 🟡 P1 | Génération de cartes mentales à partir des cours (exclus du MVP pour complexité de rendu) | Élevée |
| M3 | Mode Multi-Joueur (Défis) | 🟡 P1 | Défis en temps réel entre amis (quiz head-to-head) | Élevée |
| M4 | Notifications Push Intelligentes | 🟡 P1 | Rappels de devoirs, objectifs XP quotidiens, alertes de classement | Moyenne |
| M5 | Mode hors-ligne IA (inférence locale) | ✅ Intégré | Modèle Gemma E2B/E4B embarqué pour quiz sans internet (cœur du produit) | Élevée |
| M6 | Widget iOS (Today Extension) | 🟢 P2 | Widget home screen avec emploi du temps + note la plus récente | Moyenne |
| M7 | Streaks quotidiens | 🟡 P1 | Compteur de jours consécutifs d'utilisation avec bonus XP | Faible |
| M8 | Thèmes custom (skins) | 🟢 P2 | Personnalisation du thème de l'app (débloquable via XP) | Faible |
| M9 | Import OCR (notes manuscrites) | 🔵 P3 | Scanner un cours manuscrit → OCR → IA pédagogique | Très élevée |
| M10 | Dark/Light mode toggle | 🟢 P2 | Permettre un mode clair pour les utilisateurs qui préfèrent | Faible |
| M11 | Calendrier unifié devoirs + emploi du temps | 🟡 P1 | Vue calendrier mensuelle combinée | Moyenne |
| M12 | Support École Directe | 🟡 P1 | 2ème ENT de France — étendre la couverture marché | Élevée |
| M13 | Tableau de bord parental | 🟢 P2 | Vue simplifiée pour que les parents suivent la progression | Moyenne |
| M14 | Mode examen (révision chronométrée) | 🟢 P2 | Quiz avec timer + conditions d'examen simulées | Faible |
| M15 | Badges partageables (story Instagram) | 🟡 P1 | Partager ses succès sur Instagram/Snapchat (viral loop) | Faible |

---

## 2. IA & Modèle

| # | Feature | Priorité | Description | Complexité |
|---|---|---|---|---|
| A1 | Déploiement modèles edge Gemma E2B/E4B | 🔴 P0 | Finaliser le fine-tuning et le déploiement des modèles Gemma on-device | Élevée |
| A2 | RAG on-device | 🔴 P0 | Implémenter le RAG pour l'injection de contexte scolaire local | Élevée |
| A3 | AB Testing IA (Benchmark Mode) | 🟡 P1 | Comparaison automatisée des réponses Gemini vs modèle Gemma edge | Moyenne |
| A4 | Mémoire long-terme du Tuteur | 🟢 P2 | Le tuteur se souvient des sessions précédentes de l'élève (via RAG étendu) | Élevée |
| A5 | Détection automatique de lacunes | 🟢 P2 | Analyser les patterns d'erreurs de l'élève pour recommander des révisions ciblées | Élevée |
| A6 | Génération de devoirs types (prépa DS) | 🟡 P1 | L'IA génère un devoir type complet simulant un contrôle | Moyenne |
| A7 | Correction automatique de copies | 🔵 P3 | Photo de copie → OCR → correction IA | Très élevée |
| A8 | Résumé audio de cours (TTS) | 🔵 P3 | Conversion des fiches de révision en audio écoutables | Moyenne |

---

## 3. Plateformes Web (Sites)

| # | Feature | Priorité | Description | Complexité |
|---|---|---|---|---|
| W1 | Lucid Prof — Beta publique | 🟡 P1 | Ouvrir la plateforme professeur à 10+ enseignants pilotes | Moyenne |
| W2 | Lucid Prof — Import PDF | 🟢 P2 | Upload de PDF de cours → parsing → génération automatique d'exercices | Élevée |
| W3 | Lucid Prof — Marketplace | 🔵 P3 | Les profs partagent/vendent leurs modules pédagogiques | Très élevée |
| W4 | Lucid Dashboard — IA Analyst Automatisé | 🟡 P1 | Rapports hebdomadaires automatiques par email (cron Vercel) | Faible |
| W5 | Lucid Dashboard — Carte mondiale d'activité | 🟢 P2 | Visualisation en temps réel de l'activité LUCID sur une carte | Élevée |
| W6 | Lucid Live | 🔵 P3 | Compteur live de quiz, XP et devoirs en cours sur le réseau mondial | Élevée |
| W7 | Site officiel — Simulations 3D interactives | 🔵 P3 | Intégrer des démos 3D dans le site vitrine | Très élevée |

---

## 4. Infrastructure & DevOps

| # | Feature | Priorité | Description | Complexité |
|---|---|---|---|---|
| I1 | Monitoring + Alerting (Sentry/DataDog) | 🟡 P1 | Tracking des crash et erreurs en production | Moyenne |
| I2 | Analytics d'usage (PostHog/Mixpanel) | 🟡 P1 | Tracking des événements utilisateur pour optimiser la rétention | Moyenne |
| I3 | CDN pour assets statiques | 🟢 P2 | Distribution optimale des images et vidéos | Faible |
| I4 | Supabase Edge Functions → API Gateway | 🟢 P2 | Centraliser les appels API derrière un gateway unifié | Moyenne |
| I5 | Tests E2E automatisés (Detox/Maestro) | 🟡 P1 | Tests automatiques sur l'app mobile avant chaque release | Élevée |

---

## 5. Business & Marketing

| # | Feature | Priorité | Description | Complexité |
|---|---|---|---|---|
| B1 | Modèle Freemium activé | 🟡 P1 | Limites quotidiennes sur les fonctionnalités IA gratuites | Moyenne |
| B2 | Apple In-App Purchase | 🟡 P1 | Intégration des paiements in-app pour l'offre Pro | Élevée |
| B3 | Landing page SEO-friendly | 🔴 P0 | Optimisation du site officiel pour le référencement | Faible |
| B4 | Programme de parrainage | 🟢 P2 | "Invite un ami → gagne des XP bonus" | Faible |
| B5 | Kit Presse 3.0 | 🟡 P1 | Export PDF automatique depuis Lucid Media Tracker | Faible |
| B6 | Campagne publicité TikTok | 🟢 P2 | Contenus vidéo courts démontrant les fonctionnalités | Moyenne |

---

## 6. Idées en Exploration (Icebox)

> Ces idées ne sont pas planifiées mais méritent d'être gardées.

- 💡 **Mode Pomodoro intégré** — Timer de révision avec pauses XP
- 💡 **Challenges saisonniers** — Événements spéciaux (challenge vacances, semaine de révisions)
- 💡 **Lucid Academy** — Parcours d'apprentissage structurés par matière
- 💡 **Reconnaissance d'écriture manuscrite** — L'IA lit les notes prises en cours
- 💡 **Connexion avec Google Classroom** — Élargir au-delà de Pronote
- 💡 **API publique Lucid** — Permettre aux développeurs tiers de construire sur Lucid
- 💡 **Pack Famille** — Abonnement partagé parent + enfants
- 💡 **Lucid for Teachers** — Version standalone pour les profs sans élèves sur Lucid
