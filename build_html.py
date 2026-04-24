import sys

with open("raw_script.html", "r") as f:
    content = f.read()

template = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LUCID — Script Oral</title>
    <style>
        :root {
            --primary: #2563eb;
            --text-main: #1f2937;
            --text-muted: #6b7280;
            --bg: #ffffff;
            --bg-accent: #f3f4f6;
            --border: #e5e7eb;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: var(--text-main);
            background-color: var(--bg);
            max-width: 850px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        
        .editor-notice {
            background-color: #eff6ff;
            color: #1e3a8a;
            padding: 10px 15px;
            border-radius: 6px;
            font-size: 0.9rem;
            margin-bottom: 2em;
            border-left: 4px solid #3b82f6;
        }
        
        @media print {
            .editor-notice {
                display: none;
            }
        }

        h1 {
            font-size: 2.5rem;
            color: var(--text-main);
            border-bottom: 2px solid var(--primary);
            padding-bottom: 10px;
            margin-bottom: 0.5em;
        }

        h2 {
            font-size: 1.8rem;
            color: var(--primary);
            margin-top: 2em;
            border-bottom: 1px solid var(--border);
            padding-bottom: 8px;
        }

        h3 {
            font-size: 1.3rem;
            color: #4b5563;
            margin-top: 1.8em;
            background: var(--bg-accent);
            padding: 8px 12px;
            border-radius: 6px;
            border-left: 4px solid var(--primary);
        }

        h4 {
            font-size: 1.1rem;
            color: #374151;
            margin-top: 1.5em;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        p {
            margin-bottom: 1.2em;
        }

        strong {
            color: #111827;
        }

        em {
            color: var(--text-muted);
            font-style: italic;
        }

        blockquote {
            margin: 1.5em 0;
            padding: 15px 20px;
            background-color: #f9fafb;
            border-left: 4px solid #9ca3af;
            border-radius: 0 6px 6px 0;
            font-size: 1.05rem;
            line-height: 1.7;
        }

        blockquote p {
            margin: 0;
            color: #374151;
            font-style: italic;
        }

        ul {
            margin-bottom: 1.5em;
            padding-left: 20px;
        }

        li {
            margin-bottom: 0.5em;
        }

        hr {
            border: 0;
            height: 1px;
            background: var(--border);
            margin: 2em 0;
        }

        #editable-content {
            outline: none;
        }

        /* Print optimization */
        @media print {
            body {
                padding: 0;
                max-width: 100%;
                font-size: 12pt;
            }
            h2, h3 {
                page-break-after: avoid;
            }
            p, blockquote {
                page-break-inside: avoid;
            }
            blockquote {
                /* Let JS styling apply during print if enabled, otherwise fallback */
                border-left-width: 4px !important;
            }
            h3 {
                background: transparent;
                border: 1px solid #000;
                border-left: 4px solid #000;
            }
            @page {
                margin: 2cm;
            }
        }
    </style>
</head>
<body>
    <div class="editor-notice" contenteditable="false">
        <strong>Mode Édition Activé :</strong> Vous pouvez cliquer n'importe où dans le texte ci-dessous pour le modifier directement.<br>
        Vos modifications sont sauvegardées automatiquement dans votre navigateur (elles ne s'effaceront pas si vous rafraîchissez la page).
        <div style="margin-top: 12px; display: flex; gap: 10px;">
            <button onclick="downloadHTML()" style="padding: 6px 12px; background: #3b82f6; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: 500;">📥 Télécharger le fichier modifié</button>
            <button onclick="resetContent()" style="padding: 6px 12px; background: #ef4444; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: 500;">🔄 Réinitialiser au script original</button>
        </div>
    </div>
    <div id="editable-content" contenteditable="true" spellcheck="false">
        {content}
    </div>

    <script>
        function applyColors() {
            const colors = {
                'A': { bg: 'rgba(59, 130, 246, 0.1)', border: '#3b82f6' },
                'B': { bg: 'rgba(16, 185, 129, 0.1)', border: '#10b981' },
                'C': { bg: 'rgba(139, 92, 246, 0.1)', border: '#8b5cf6' },
                'D': { bg: 'rgba(245, 158, 11, 0.1)', border: '#f59e0b' }
            };

            let currentSpeaker = null;
            const contentDiv = document.getElementById('editable-content');

            contentDiv.childNodes.forEach(node => {
                if (node.nodeType === 1) { 
                    if (node.tagName.match(/^H[1-6]$/) || node.tagName === 'HR') {
                        currentSpeaker = null;
                    } 
                    else if (node.tagName === 'P') {
                        const strong = node.querySelector('strong');
                        if (strong) {
                            const text = strong.textContent.trim();
                            const match = text.match(/^([ABCD])(\s|\(|$)/);
                            if (match && !text.includes('Note')) {
                                currentSpeaker = match[1];
                                strong.style.color = colors[currentSpeaker].border;
                            }
                        }
                    } 
                    else if (node.tagName === 'BLOCKQUOTE' && currentSpeaker) {
                        node.style.backgroundColor = colors[currentSpeaker].bg;
                        node.style.borderLeftColor = colors[currentSpeaker].border;
                    }
                }
            });
        }

        document.addEventListener("DOMContentLoaded", () => {
            const contentDiv = document.getElementById('editable-content');
            
            // On load: check if there's a saved version
            const saved = localStorage.getItem('lucid_script_saved');
            if (saved) {
                contentDiv.innerHTML = saved;
            } else {
                applyColors();
                localStorage.setItem('lucid_script_original', contentDiv.innerHTML); // Save original state once with colors
            }

            // Auto-save on every edit
            contentDiv.addEventListener('input', () => {
                localStorage.setItem('lucid_script_saved', contentDiv.innerHTML);
            });
        });

        function downloadHTML() {
            let htmlContent = "<!DOCTYPE html>\\n" + document.documentElement.outerHTML;
            const blob = new Blob([htmlContent], {type: "text/html;charset=utf-8"});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = "index.html";
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }

        function resetContent() {
            if (confirm("Voulez-vous vraiment annuler toutes vos modifications et revenir au script original ?")) {
                localStorage.removeItem('lucid_script_saved');
                const original = localStorage.getItem('lucid_script_original');
                if (original) {
                    document.getElementById('editable-content').innerHTML = original;
                } else {
                    location.reload(); // Fallback
                }
            }
        }
    </script>
</body>
</html>
"""

final_html = template.replace("{content}", content)

with open("index.html", "w") as f:
    f.write(final_html)
