# 🎨 Design System — LUCID

---

## 1. Identité Visuelle

### 1.1. Philosophie de Design
LUCID adopte un design **dark-mode premium**, inspiré du **glassmorphism**, avec des accents vibrants néon. L'objectif est de donner l'impression d'une application haut de gamme, futuriste et captivante — à l'opposé de l'austérité de Pronote.

**Mots-clés :** Premium, Envoûtant, Futuriste, Dark, Glassmorphism, Néon

### 1.2. Logo
- **Typographie :** Le mot "LUCID" en majuscules, lettre par lettre
- **Style :** Ultra-bold, tracking serré, gradient blanc → gris (dégradé vertical)
- **Taille Hero :** `text-7xl md:text-[14rem]` — Impact massif sur la home page

---

## 2. Palette de Couleurs

### 2.1. Variables CSS (Source de vérité)

```css
:root {
  --bg-color: #0d0415;          /* Very dark violet — Background principal */
  --text-color: #f8fafc;        /* Blanc slate — Texte principal */
  --primary-color: #e024ce;     /* Rose Violet — Couleur d'accent primaire */
  --secondary-color: #9d4edd;   /* Deep Violet — Couleur d'accent secondaire */
  --accent-color: #db2777;      /* Deep Rose — Accent tertiaire */
  --glass-bg: rgba(25, 12, 35, 0.4);       /* Fond glassmorphism */
  --glass-border: rgba(224, 36, 206, 0.25); /* Bordure glassmorphism */
  --glass-blur: 12px;           /* Intensité du blur */
}
```

### 2.2. Tailwind Config

```js
colors: {
  primary: '#e024ce',   // Rose Violet
  secondary: '#9d4edd', // Deep Violet  
  accent: '#db2777',    // Deep Rose
  dark: '#0d0415',      // Very dark violet background
}
```

### 2.3. Couleurs Sémantiques

| Nom | Hex | Usage |
|---|---|---|
| `primary` | `#e024ce` | CTA principaux, glow, bordures actives, badges |
| `secondary` | `#9d4edd` | Dégradés secondaires, liens, accents |
| `accent` | `#db2777` | Gamification, trophées, alertes positives |
| `dark` | `#0d0415` | Background global |
| `glass-bg` | `rgba(25,12,35,0.4)` | Fond des panneaux transparents |
| `glass-border` | `rgba(224,36,206,0.25)` | Bordure des panneaux glass |
| Text Primary | `#f8fafc` | Texte principal (blanc) |
| Text Secondary | `#9ca3af` | Texte secondaire (gray-400) |
| Text Muted | `#6b7280` | Texte discret (gray-500) |

### 2.4. Gradients Récurrents

| Nom | CSS | Usage |
|---|---|---|
| Gradient Primary | `from-primary via-white to-secondary` | Titres Hero |
| Gradient Accent | `from-primary to-secondary` | Boutons, badges |
| Gradient Gold | `from-yellow-300 to-yellow-600` | Classement #1 |
| Gradient Silver | `from-slate-300 to-slate-400` | Classement #2 |
| Gradient Bronze | `from-orange-400 to-orange-600` | Classement #3 |

---

## 3. Typographie

### 3.1. Police Principale
```css
--font-main: 'Inter', system-ui, -apple-system, sans-serif;
```

- **Family :** Inter (Google Fonts)
- **Fallback :** system-ui, -apple-system, sans-serif
- **Lissage :** `-webkit-font-smoothing: antialiased`

### 3.2. Échelle Typographique

| Rôle | Classes Tailwind | Poids |
|---|---|---|
| Hero Title | `text-7xl md:text-[14rem]` | `font-black` (900) |
| Section Title | `text-4xl md:text-6xl` | `font-black` (900) |
| Subtitle | `text-3xl md:text-5xl` | `font-bold` (700) |
| Body Large | `text-xl md:text-2xl` | `font-light` (300) |
| Body | `text-lg` | `font-normal` (400) |
| Caption | `text-sm` | `font-semibold` (600) |
| Overline | `text-xs` | `font-black uppercase tracking-[0.3em]` |

---

## 4. Composants UI

### 4.1. Glass Panel (Composant principal)

```css
.glass-panel {
  background: rgba(25, 12, 35, 0.4);      /* Fond semi-transparent */
  backdrop-filter: blur(12px);               /* Flou de fond */
  -webkit-backdrop-filter: blur(12px);      
  border: 1px solid rgba(224, 36, 206, 0.25); /* Bordure subtile primary */
  border-radius: 1rem;                      /* Coins arrondis */
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1); /* Ombre diffuse */
  position: relative;
  overflow: hidden;
}
```

### 4.2. Glass Card (Carte interactive)

```css
.glass-card {
  background: rgba(255, 255, 255, 0.03);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1.5rem;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.glass-card:hover {
  background: rgba(255, 255, 255, 0.05);
  border-color: rgba(224, 36, 206, 0.4);
  transform: translateY(-5px);
  box-shadow: 0 30px 60px rgba(0, 0, 0, 0.5), 
              0 0 20px rgba(224, 36, 206, 0.15);
}
```

### 4.3. Boutons

| Type | Style |
|---|---|
| CTA Principal | `glass-panel bg-white/5 hover:bg-white/10 border-white/20 hover:border-primary/60` + gradient sweep animation |
| CTA Secondaire | `glass-panel border-primary/40 hover:border-primary hover:bg-primary/20` |
| Disabled | `glass-panel border-white/10 text-gray-500 cursor-not-allowed opacity-60 grayscale` |
| Badge/Tag | `rounded-full bg-primary/10 border border-primary/40 text-primary text-sm font-bold uppercase tracking-widest` |

### 4.4. Glow Effects

| Effet | CSS |
|---|---|
| Shadow Glow Primary | `shadow-[0_0_20px_rgba(224,36,206,0.3)]` |
| Shadow Glow XP | `drop-shadow-[0_0_10px_rgba(255,0,127,0.5)]` |
| Text Glow | `drop-shadow-[0_0_20px_rgba(255,0,127,0.5)]` |
| Background Glow | `bg-primary/20 rounded-full blur-[150px]` |

---

## 5. Animations & Micro-Interactions

### 5.1. Bibliothèque : Framer Motion

| Animation | Usage | Config |
|---|---|---|
| Fade-in + Scale | Premier chargement Hero | `initial={{ opacity: 0, scale: 0.95 }}` → `animate={{ opacity: 1, scale: 1 }}` |
| Slide-in | Éléments entrant dans le viewport | `initial={{ opacity: 0, y: 30 }}` → `whileInView={{ opacity: 1, y: 0 }}` |
| Hover Scale | Boutons, cartes | `whileHover={{ scale: 1.05, y: -5 }}` + `whileTap={{ scale: 0.95 }}` |
| Gradient Sweep | CTA principal au hover | `translate-x-[-100%] → translate-x-[100%] duration-1000` |
| Pulse | Glow backgrounds décoratifs | `animate-pulse` (CSS natif) |
| Bounce | Couronne du classement #1 | `animate-bounce` |

### 5.2. Transitions
- **Durée standard :** `0.4s cubic-bezier(0.4, 0, 0.2, 1)`
- **Ease Hero :** `duration: 1.2, ease: [0.16, 1, 0.3, 1]`
- **Delay séquentiel :** `delay: index * 0.2` pour les listes

---

## 6. Iconographie

- **Bibliothèque :** Lucide React (`lucide-react`)
- **Taille standard :** `size={16-24}` pour les icônes inline, `size={32-64}` pour les features
- **Couleur :** Hérite de la couleur du texte parent ou colorée par Tailwind

### Icônes Principales

| Icône | Contexte |
|---|---|
| `Trophy` | Gamification, classement |
| `Star` | XP, récompenses |
| `Zap` | Badges, énergie |
| `ShieldCheck` | Sécurité, brevet |
| `Lightbulb` | Innovation, IA |
| `Apple` / `Play` | Store buttons |
| `Crown` | Champion #1 |
| `Instagram` | Réseaux sociaux |

---

## 7. Responsive Design

| Breakpoint | Comportement |
|---|---|
| Mobile (<768px) | Stack vertical, padding réduit, tailles texte réduites |
| Tablet (768-1024px) | Grille 2 colonnes, textes intermédiaires |
| Desktop (>1024px) | Layout complet, grille 3-4 colonnes, tailles Hero max |

---

## 8. Scrollbar Custom

```css
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: #0d0415; }
::-webkit-scrollbar-thumb { background: rgba(224, 36, 206, 0.25); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: #e024ce; }
```

---

## 9. Background Patterns

### Noise Overlay
```css
.noise-bg::before {
  content: "";
  /* SVG fractalNoise filter overlay */
  opacity: 0.03;
  pointer-events: none;
  z-index: 1;
}
```

### Decorative Blurs
- Blobs `bg-primary/20 blur-[150px]` positionnés en absolute
- Gradient subtles `from-transparent via-primary/5 to-transparent`
- Skewed geometric shapes `skew-x-[-12deg] shadow-[0_0_100px_rgba(0,0,0,0.8)]`
