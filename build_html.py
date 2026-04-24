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
                background-color: transparent;
                border-left: 3px solid #000;
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
    {content}
</body>
</html>
"""

final_html = template.replace("{content}", content)

with open("LUCID_Script_Oral_Final.html", "w") as f:
    f.write(final_html)
