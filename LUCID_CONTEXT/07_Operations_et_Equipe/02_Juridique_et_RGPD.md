# ⚖️ Juridique et RGPD — LUCID

---

## 1. Statut Juridique

| Élément | Détail |
|---|---|
| **Forme juridique actuelle** | Projet non-incorporé (association de fait) |
| **Structure prévue** | SAS (Phase 3, avec premiers revenus) |
| **Siège** | France (Vence, 06) |
| **Responsable de traitement (RGPD)** | Pierre Aboussouan (contact : pierre.aboussouan@ac-nice.fr) |
| **Encadrement** | Lycée Henri Matisse |

---

## 2. Propriété Intellectuelle

### 2.1. Dépôt de Brevet
- **Objet :** Système de gamification scolaire (méthode d'engagement des élèves via XP, niveaux, badges liés aux données scolaires)
- **Cabinet :** AXEPI (www.axepi.com) — Leader dans l'accompagnement à l'innovation et la PI
- **Statut :** Dépôt en cours
- **Protection :** Le brevet protège la méthode innovante d'analyse et de gamification du parcours scolaire

### 2.2. Code Source
- **App mobile (lucid_app)** : Propriétaire (non open-source)
- **Sites web (lucid_*)** : Propriétaire
- **Proxy Pronote (pronotebackend)** : Open-source sur GitHub (transparence RGPD)
- **Dataset (Gold Data)** : Propriétaire (10 000 exemples générés par Lucid Labs)

### 2.3. Marque
- **Nom :** LUCID
- **Protection marque :** À déposer (INPI)

---

## 3. Conformité RGPD

### 3.1. Principes Appliqués

| Principe RGPD | Implémentation LUCID |
|---|---|
| **Licéité** | Consentement explicite lors de la connexion Pronote |
| **Minimisation** | Seules les données strictement nécessaires sont traitées |
| **Limitation de conservation** | Données supprimables sur demande (<30 jours) |
| **Intégrité et confidentialité** | Chiffrement HTTPS/TLS, SecureStore, RLS |
| **Droits des personnes** | Accès, rectification, suppression |
| **Transparence** | Politique de confidentialité publique et détaillée |

### 3.2. Données Traitées

| Donnée | Stockage | Finalité | Durée |
|---|---|---|---|
| **Identifiants Pronote** | Local uniquement (Expo SecureStore, chiffré) | Authentification | Jusqu'à déconnexion |
| **Données Pronote** | Local uniquement (AsyncStorage, cache) | Affichage + RAG pour l'IA edge | Jusqu'à déconnexion |
| **Inférence IA** | **Local uniquement (Gemma on-device)** | Génération quiz/flashcards/fiches | Non conservée |
| **Nom d'affichage** | Supabase (profiles) | Profil social + leaderboard | Jusqu'à suppression du compte |
| **XP, Niveaux, Badges** | Supabase (profiles) + Local (AsyncStorage) | Gamification | Jusqu'à suppression du compte |
| **Avatar** | Supabase Storage | Profil social | Jusqu'à suppression du compte |
| **Amis** | Supabase (profiles) | Fonctionnalité sociale | Jusqu'à suppression du compte |
| **Logs IA** | **Non conservés** (inférence locale) | — | N/A |

> 💡 **Avantage RGPD clé :** L'architecture edge AI signifie que les données scolaires de l'élève ne quittent JAMAIS son téléphone pour l'IA. L'inférence est locale, pas de transit cloud.

### 3.3. Données NON traitées

| Donnée | Statut |
|---|---|
| Géolocalisation | ❌ Jamais collectée |
| Contacts du téléphone | ❌ Jamais accédés |
| Photos / Caméra | ❌ Pas accédé |
| Historique de navigation | ❌ Jamais collecté |
| Adresse email personnelle | ❌ Pas collectée (sauf si inscription newsletter volontaire) |
| Données vendues à des tiers | ❌ **JAMAIS** |

### 3.4. Architecture de Confidentialité

```
Données Pronote          Données Profil
(sensibles)              (gamification)
     │                        │
     ▼                        ▼
┌──────────┐           ┌──────────┐
│  LOCAL   │           │ SUPABASE │
│  ONLY    │           │  CLOUD   │
│          │           │          │
│ SecureStore          │ profiles │
│ (identifiants)       │ (XP,     │
│                      │  badges, │
│ AsyncStorage         │  amis)   │
│ (notes, EDT,         │          │
│  devoirs)            │  RLS ✅  │
│                      └──────────┘
│ Gemma E2B/E4B
│ (IA edge, inférence
│  100% locale)
└──────────┘
     ↑                                
     │                            
  JAMAIS                          
  transmis                        
  au cloud                        
```

### 3.5. Droits des Utilisateurs

| Droit | Comment l'exercer |
|---|---|
| **Droit d'accès** | Demande via email (réponse <30 jours) |
| **Droit de rectification** | Modification directe dans l'app (profil) |
| **Droit de suppression** | Paramètres → Supprimer mon compte (exécutée <30 jours) |
| **Droit à la portabilité** | Export des données sur demande (format JSON) |
| **Droit d'opposition** | Désactiver les notifications, se déconnecter |

---

## 4. Conditions Générales d'Utilisation (CGU)

### 4.1. Points Clés

- L'application est réservée aux élèves et étudiants
- L'utilisateur est responsable de la confidentialité de ses identifiants Pronote
- LUCID n'est pas responsable de la disponibilité du service Pronote
- L'IA fournit une aide pédagogique, pas de garantie de résultat scolaire
- Toute exploitation abusive (bots, scripts, multi-comptes) est interdite et peut entraîner un ban
- L'utilisation de l'XP généré par des moyens frauduleux est interdite (cf. règlement du concours)

### 4.2. Pages Légales

| Page | Route | Contenu |
|---|---|---|
| Politique de Confidentialité | `/privacy` | Détail RGPD complet |
| Conditions Générales d'Utilisation | `/cgu` | CGU détaillées |
| Mentions Légales | `/mentions-legales` | Informations légales éditeur |

---

## 5. Conformité Spécifique (Mineur)

> ⚠️ La majorité des utilisateurs sont **mineurs** (<18 ans). Cela implique des obligations supplémentaires :

| Obligation | Implémentation |
|---|---|
| Consentement parental | Les identifiants Pronote sont déjà sous responsabilité parentale |
| Langage adapté | Politique de confidentialité rédigée clairement |
| Pas de collecte excessive | Minimisation des données stricte |
| Pas de publicité ciblée | Aucune publicité ciblée (pas de tracking publicitaire) |
| Pas de manipulation | Gamification éthique (pas de dark patterns) |

---

## 6. Contrats et Partenariats

| Partenaire | Type | Statut |
|---|---|---|
| **AXEPI** | Cabinet PI (dépôt de brevet) | ✅ Actif |
| **Lycée Henri Matisse** | Établissement d'accueil | ✅ Actif |
| **Vercel** | Hébergement (Terms of Service) | ✅ Accepté |
| **Supabase** | BaaS (Terms of Service) | ✅ Accepté |
| **Apple** | Developer Program (licence annuelle) | ✅ Actif (99€/an) |
| **Google** | Gemini API (Terms of Use) | ✅ Accepté |
