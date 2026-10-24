# -*- coding: utf-8 -*-
"""
Multi-Page Platform Generator for BioTwin Labs.
Separates each service into its own dedicated, clean, focused page:
1. Home Services Catalog & Search Hub (/)
2. Camera Optical BP & Sugar Scanner (/camera-checkup)
3. Zero-Report 2-Min Longevity Assessment (/zero-report-quiz)
4. Old Report Time Machine Projector (/old-report-projector)
5. Full 72+ Biomarker Panel (/full-biomarker-analysis)
6. At-Home Blood Test Booking (/book-blood-test)
7. Private Founder CRM (/founder-crm)
"""

import os

TEMPLATES_DIR = r"c:\Users\B-WOI\OneDrive\Desktop\BioTwin-Platform\web\templates"
os.makedirs(TEMPLATES_DIR, exist_ok=True)

# Common Header & Style Snippet for templates
COMMON_HEAD = '''
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #05070c;
            --surface: #0a0f1a;
            --surface-card: #111827;
            --surface-hover: #192236;
            --border: #1f293d;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --text-dim: #64748b;
            --accent: #38bdf8;
            --accent-glow: rgba(56, 189, 248, 0.25);
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: var(--bg);
            color: var(--text-main);
            line-height: 1.5;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        .navbar {
            display: flex; justify-content: space-between; align-items: center;
            padding: 16px 36px; background: rgba(10, 15, 26, 0.96); backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 1000;
        }
        .brand-box { display: flex; align-items: center; gap: 12px; text-decoration: none; color: inherit; }
        .brand-icon {
            width: 42px; height: 42px; background: linear-gradient(135deg, #38bdf8, #818cf8);
            border-radius: 12px; display: flex; align-items: center; justify-content: center;
            font-weight: 900; font-size: 22px; color: #000; box-shadow: 0 0 20px var(--accent-glow);
        }
        .brand-text h1 { font-size: 19px; font-weight: 800; }
        .brand-text span { font-size: 10px; text-transform: uppercase; letter-spacing: 1.5px; color: var(--accent); font-weight: 700; display: block; }
        .nav-controls { display: flex; align-items: center; gap: 16px; }
        .lang-switch { display: flex; gap: 6px; background: var(--surface-card); padding: 4px; border-radius: 8px; border: 1px solid var(--border); }
        .lang-btn {
            background: transparent; border: none; color: var(--text-muted); padding: 5px 10px;
            border-radius: 6px; font-size: 11px; font-weight: 700; cursor: pointer; transition: all 0.2s;
        }
        .lang-btn.active, .lang-btn:hover { background: var(--accent); color: #000; }
        .btn-nav-action {
            background: var(--surface-card); border: 1px solid var(--border); color: #fff; text-decoration: none;
            padding: 8px 16px; border-radius: 8px; font-size: 12px; font-weight: 700; transition: all 0.2s;
            display: flex; align-items: center; gap: 6px;
        }
        .btn-nav-action:hover { border-color: var(--accent); color: var(--accent); }
        .main-content { flex: 1; max-width: 1280px; width: 100%; margin: 0 auto; padding: 32px 24px 60px; }
        .page-badge {
            display: inline-flex; align-items: center; gap: 6px; background: rgba(56, 189, 248, 0.1);
            border: 1px solid rgba(56, 189, 248, 0.25); color: var(--accent); font-size: 11px; font-weight: 800;
            padding: 4px 12px; border-radius: 999px; text-transform: uppercase; margin-bottom: 12px;
        }
        .page-title { font-size: 28px; font-weight: 800; margin-bottom: 8px; }
        .page-desc { font-size: 14px; color: var(--text-muted); max-width: 750px; line-height: 1.6; margin-bottom: 28px; }
        .btn-main {
            background: linear-gradient(135deg, #38bdf8, #2563eb); color: #fff; border: none;
            padding: 14px 24px; border-radius: 12px; font-size: 14px; font-weight: 800; cursor: pointer;
            transition: all 0.2s; box-shadow: 0 4px 15px rgba(56, 189, 248, 0.3); display: inline-flex;
            align-items: center; justify-content: center; gap: 8px; text-decoration: none;
        }
        .btn-main:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(56, 189, 248, 0.45); }
        .footer {
            border-top: 1px solid var(--border); background: var(--surface); padding: 24px 36px;
            font-size: 12px; color: var(--text-dim); text-align: center;
        }
    </style>
'''

print("Generating clean multi-page architecture...")
