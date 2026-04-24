# 🚀 DevOps et CI/CD — LUCID

---

## 1. Processus Actuel

> **Note :** LUCID est un projet early-stage avec une petite équipe (2 fondateurs). Le processus DevOps est pragmatique et minimaliste, en adéquation avec le stade de développement.

---

## 2. Versioning (Git)

| Élément | Détail |
|---|---|
| **Plateforme** | GitHub |
| **Organisation** | NovaVibeCoding |
| **Repository App Mobile** | Privé (repo séparé pour l'app React Native / Expo) |
| **Repository Sites** | LUCID_WORKSPACE (npm workspaces pour les sites satellites) |
| **Stratégie de branches** | Trunk-based (main) |
| **Repos annexes** | `pronotebackend` (proxy Pronote, open-source) |

> ⚠️ L'app mobile et les sites web sont dans des **repositories séparés**, ce n'est PAS un monorepo unique.

### .gitignore

Les éléments suivants sont exclus du versioning :
- `node_modules/`
- `.next/`
- `dist/`
- `.env.local` (secrets)
- `*.log` (fichiers de log de développement)
- `.DS_Store`

---

## 3. Déploiement — Sites Web (Vercel)

### 3.1. Configuration

Chaque site satellite est déployé indépendamment sur Vercel avec un `vercel.json` :

```json
{
  "buildCommand": "cd ../.. && npm install && npm run build --workspace=sites/{project_name}",
  "installCommand": "echo skip"
}
```

### 3.2. Workflow de Déploiement

```
Développeur → git push main
                    ↓
              GitHub Webhook → Vercel
                    ↓
              Build automatique (npm run build)
                    ↓
              Preview URL (pour les branches non-main)
              OU Production URL (pour main)
                    ↓
              Déploiement Edge (serverless functions + static)
```

### 3.3. URLs de Production

| Site | URL estimée |
|---|---|
| lucid_official_website | `lucid-official-website.vercel.app` / custom domain |
| lucid_labs | `lucid-labs.vercel.app` |
| lucid_dashboard | `lucid-admin.vercel.app` |
| lucid_prof | `lucid-prof.vercel.app` |
| lucid_hub | `lucid-hub.vercel.app` |
| lucid_roadmap | `lucid-roadmap.vercel.app` |
| lucid_finance | `linxea-dashboard.vercel.app` |
| lucid_media_tracker | `lucid-media-tracker.vercel.app` |
| lucid_redirect | `lucid-redirect.vercel.app` |

---

## 4. Déploiement — Application Mobile (Expo / EAS)

### 4.1. Expo Application Services (EAS)

| Phase | Commande | Usage |
|---|---|---|
| **Build** | `eas build --platform ios` | Build de l'archive iOS (.ipa) |
| **Submit** | `eas submit --platform ios` | Soumission sur l'App Store |
| **Update (OTA)** | `eas update` | Mise à jour JavaScript sans rebuild natif |

### 4.2. Distribution

| Canal | Statut |
|---|---|
| iOS App Store | ✅ Publié (ID: `id6757653389`) |
| Android APK (via Expo) | ⚙️ Distribution interne (lien direct) |
| Google Play Store | 🔜 En préparation |

---

## 5. Tests

### 5.1. Statut Actuel

> ⚠️ **Honnêtement :** Il n'y a pas encore de suite de tests automatisés complète. Les tests sont principalement manuels.

### 5.2. Tests Manuels

| Type | Fréquence | Quoi |
|---|---|---|
| **Test Fonctionnel** | À chaque feature | Vérification manuelle du comportement attendu |
| **Test IA (Benchmark)** | Ponctuel | Mode benchmark dans Lucid Labs pour comparer les sorties |
| **Test de Régression** | Avant chaque release | Vérification que les features existantes n'ont pas cassé |
| **Test Cross-Device** | Avant soumission App Store | Test sur iPhone réel |

### 5.3. Tests Automatisés (Roadmap)

| Type | Outil Prévu | Statut |
|---|---|---|
| Unit Tests | Jest / Vitest | 🔜 À implémenter |
| E2E Mobile | Detox / Maestro | 🔜 À implémenter |
| Lint | ESLint | ✅ Configuré sur tous les projets |
| Type Check | TypeScript (`tsc`) | ✅ Compilateur strict |
| Schema Validation | Zod | ✅ Utilisé pour les schémas IA |

---

## 6. Monitoring

### 6.1. Monitoring Actuel

| Outil | Usage |
|---|---|
| **Vercel Analytics** | Métriques de déploiement, temps de build |
| **Supabase Dashboard** | Nombre de requêtes, taille DB, logs Edge Functions |
| **Console Logs** | `console.warn` / `console.error` dans le code (non centralisé) |
| **dev_*.log** | Fichiers de log locaux pour Lucid Labs (développement) |

### 6.2. Monitoring Prévu

| Outil | Usage Prévu | Phase |
|---|---|---|
| **Sentry** | Crash reporting + error tracking | Phase 2 |
| **PostHog** | Analytics produit (funnel, retention) | Phase 2 |
| **Uptime Robot** | Monitoring uptime des sites | Phase 1 |
| **Supabase Alerts** | Alertes sur les quotas DB | Phase 1 |

---

## 7. Sécurité CI/CD

| Mesure | Implémentation |
|---|---|
| **Secrets** | Variables d'environnement Vercel (encrypted) |
| **Env Local** | `.env.local` non versionné (`.gitignore`) |
| **Service Role Key** | Jamais exposée côté client |
| **Preview Deployments** | Pas de secrets de production dans les previews |
| **Branch Protection** | À configurer (pas encore en place) |

---

## 8. Processus de Release (App Mobile)

```
1. 🛠️ Développement
   └─ Feature branch ou directement sur main
   
2. ✅ Test Manuel
   └─ Test sur simulateur iOS + device réel
   
3. 📦 Build
   └─ eas build --platform ios --profile production
   
4. 📤 Submit
   └─ eas submit --platform ios
   
5. 🍎 Review Apple
   └─ App Review (1-3 jours)
   
6. 🚀 Publication
   └─ Release sur l'App Store
   
7. 📢 Communication
   └─ Post Instagram + notification in-app
```

---

## 9. Coûts Infrastructure

| Service | Plan | Coût |
|---|---|---|
| Vercel | Hobby (gratuit) | 0€ |
| Supabase | Free tier | 0€ |
| Gemini API | Free tier (multi-clés) | ~0€ (ou ~$20-30 pour le dataset) |
| Expo / EAS | Free (builds limités) | 0€ |
| VPS Proxy Pronote | Scaleway/OVH | ~5-10€/mois |
| Apple Developer | Programme annuel | 99€/an |
| Domaines | Variables | ~10-20€/an |
| **TOTAL** | | **~120-150€/an** |

> 💡 L'infrastructure est optimisée pour un coût quasi-nul grâce aux free tiers de Supabase, Vercel et Gemini.
