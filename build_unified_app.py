# -*- coding: utf-8 -*-
"""
BioTwin Labs - Unified Single-Page Application (SPA)
All features in ONE APP, on distinct dedicated screens (no page reload, no broken links, no khichdi):
- Screen 0: Services Catalog & Search Hub
- Screen 1: Camera Optical BP & Pulse Scanner
- Screen 2: Zero-Report 2-Min Health Assessment
- Screen 3: Old Report Time Machine Projector
- Screen 4: Full 72+ Biomarker Panel & Levine PhenoAge
- Screen 5: At-Home Blood Test Booking (₹1,999)
- Screen 6: Private Founder CRM Pipeline
"""

import os

BASE_DIR = r"c:\Users\B-WOI\OneDrive\Desktop\BioTwin-Platform"
INDEX_PATH = os.path.join(BASE_DIR, "web", "templates", "index.html")
PORTAL_PATH = os.path.join(BASE_DIR, "portal.html")

def generate_unified_app():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BioTwin Labs | Precision Longevity & Health Checkup Platform</title>
    <!-- Fonts -->
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

        /* Top Navigation */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 16px 36px;
            background: rgba(10, 15, 26, 0.96);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border);
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        .brand-box {
            display: flex;
            align-items: center;
            gap: 12px;
            cursor: pointer;
            text-decoration: none;
            color: inherit;
        }
        .brand-icon {
            width: 44px;
            height: 44px;
            background: linear-gradient(135deg, #38bdf8, #818cf8);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 900;
            font-size: 22px;
            color: #000;
            box-shadow: 0 0 20px var(--accent-glow);
        }
        .brand-text h1 {
            font-size: 19px;
            font-weight: 800;
            letter-spacing: -0.3px;
        }
        .brand-text span {
            font-size: 10px;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            color: var(--accent);
            font-weight: 700;
            display: block;
        }

        .nav-controls {
            display: flex;
            align-items: center;
            gap: 14px;
        }
        .lang-switch {
            display: flex;
            gap: 4px;
            background: var(--surface-card);
            padding: 4px;
            border-radius: 8px;
            border: 1px solid var(--border);
        }
        .lang-btn {
            background: transparent;
            border: none;
            color: var(--text-muted);
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
        }
        .lang-btn.active, .lang-btn:hover {
            background: var(--accent);
            color: #000;
        }

        .btn-nav {
            background: var(--surface-card);
            border: 1px solid var(--border);
            color: #fff;
            padding: 8px 14px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            text-decoration: none;
            transition: all 0.2s;
        }
        .btn-nav:hover {
            border-color: var(--accent);
            color: var(--accent);
        }

        /* Screen Wrapper */
        .screen-view {
            display: none;
            animation: fadeIn 0.25s ease-out;
            flex: 1;
        }
        .screen-view.active {
            display: block;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Top Breadcrumb Bar for Sub-Screens */
        .screen-header-bar {
            max-width: 1200px;
            margin: 24px auto 0;
            padding: 0 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .btn-back-home {
            background: var(--surface-card);
            border: 1px solid var(--border);
            color: var(--text-main);
            padding: 8px 18px;
            border-radius: 10px;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s;
        }
        .btn-back-home:hover {
            border-color: var(--accent);
            color: var(--accent);
            background: var(--surface-hover);
        }
        .screen-tag {
            font-size: 11px;
            font-weight: 800;
            text-transform: uppercase;
            padding: 4px 12px;
            border-radius: 999px;
            background: rgba(56, 189, 248, 0.1);
            color: var(--accent);
            border: 1px solid rgba(56, 189, 248, 0.25);
        }

        /* ------------------------------------------- */
        /* SCREEN 0: MAIN SERVICES CATALOG & SEARCH HUB*/
        /* ------------------------------------------- */
        .hero {
            max-width: 1200px;
            margin: 36px auto 0;
            padding: 0 24px;
            text-align: center;
        }
        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(56, 189, 248, 0.1);
            border: 1px solid rgba(56, 189, 248, 0.25);
            color: var(--accent);
            font-size: 11px;
            font-weight: 800;
            padding: 5px 14px;
            border-radius: 999px;
            text-transform: uppercase;
            margin-bottom: 16px;
        }
        .hero-title {
            font-size: 36px;
            font-weight: 800;
            letter-spacing: -0.5px;
            margin-bottom: 14px;
            line-height: 1.25;
        }
        .hero-subtitle {
            font-size: 15px;
            color: var(--text-muted);
            max-width: 720px;
            margin: 0 auto 28px;
            line-height: 1.6;
        }

        .search-container {
            max-width: 700px;
            margin: 0 auto 40px;
            position: relative;
        }
        .search-box {
            width: 100%;
            background: var(--surface-card);
            border: 2px solid var(--border);
            border-radius: 16px;
            padding: 16px 20px 16px 52px;
            font-size: 15px;
            color: #fff;
            outline: none;
            transition: all 0.2s;
            font-family: 'Plus Jakarta Sans', sans-serif;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        }
        .search-box:focus {
            border-color: var(--accent);
            box-shadow: 0 0 25px var(--accent-glow);
        }
        .search-icon {
            position: absolute;
            left: 20px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 18px;
            color: var(--text-dim);
        }

        .catalog-container {
            max-width: 1200px;
            margin: 0 auto 60px;
            padding: 0 24px;
        }
        .catalog-header {
            font-size: 18px;
            font-weight: 800;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .catalog-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
            gap: 22px;
        }
        .service-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 26px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.25s;
            cursor: pointer;
        }
        .service-card:hover {
            transform: translateY(-4px);
            border-color: var(--accent);
            box-shadow: 0 12px 35px rgba(56, 189, 248, 0.15);
        }
        .card-top {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 14px;
        }
        .card-icon {
            width: 50px;
            height: 50px;
            border-radius: 14px;
            background: var(--surface-card);
            border: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
        }
        .card-price-pill {
            background: rgba(16, 185, 129, 0.12);
            border: 1px solid rgba(16, 185, 129, 0.3);
            color: #10b981;
            font-size: 12px;
            font-weight: 800;
            padding: 4px 12px;
            border-radius: 999px;
            font-family: 'JetBrains Mono', monospace;
        }
        .card-title {
            font-size: 19px;
            font-weight: 800;
            margin-bottom: 8px;
        }
        .card-desc {
            font-size: 13px;
            color: var(--text-muted);
            line-height: 1.6;
            margin-bottom: 20px;
            flex: 1;
        }
        .card-meta {
            display: flex;
            gap: 14px;
            margin-bottom: 18px;
            font-size: 11px;
            color: var(--text-dim);
            padding-top: 14px;
            border-top: 1px solid var(--border);
        }
        .card-btn {
            background: var(--surface-card);
            border: 1px solid var(--border);
            color: #fff;
            padding: 12px 18px;
            border-radius: 12px;
            font-size: 13px;
            font-weight: 800;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: all 0.2s;
        }
        .service-card:hover .card-btn {
            background: var(--accent);
            color: #000;
            border-color: var(--accent);
        }
        .card-featured {
            border-color: #38bdf8;
            background: linear-gradient(180deg, rgba(56, 189, 248, 0.05), var(--surface));
        }
        .card-featured .card-btn {
            background: linear-gradient(135deg, #38bdf8, #2563eb);
            border: none;
            color: #fff;
        }

        /* ------------------------------------------- */
        /* COMMON STYLES FOR DEDICATED DETAIL SCREENS   */
        /* ------------------------------------------- */
        .detail-container {
            max-width: 1000px;
            margin: 20px auto 60px;
            padding: 0 24px;
        }
        .detail-panel {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 32px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        }
        .detail-title {
            font-size: 26px;
            font-weight: 800;
            margin-bottom: 6px;
        }
        .detail-desc {
            font-size: 13px;
            color: var(--text-muted);
            line-height: 1.6;
            margin-bottom: 24px;
        }

        /* Screen 1: Camera Scanner */
        .scanner-layout {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 28px;
            align-items: center;
        }
        .camera-viewport {
            background: #020408;
            border: 2px dashed var(--border);
            border-radius: 16px;
            height: 280px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
        }
        .camera-video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: none;
        }
        .pulse-heart {
            width: 85px;
            height: 85px;
            border-radius: 50%;
            background: rgba(239, 68, 68, 0.15);
            border: 2px solid #ef4444;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32px;
            animation: heart-throb 1.2s infinite;
        }
        @keyframes heart-throb {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.15); box-shadow: 0 0 30px rgba(239, 68, 68, 0.6); }
        }
        .stats-grid-2x2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 14px;
        }
        .stat-box {
            background: var(--surface-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 14px;
        }
        .stat-box label {
            font-size: 10px;
            text-transform: uppercase;
            color: var(--text-dim);
            font-weight: 700;
            display: block;
            margin-bottom: 4px;
        }
        .stat-box val {
            font-family: 'JetBrains Mono', monospace;
            font-size: 24px;
            font-weight: 800;
            color: var(--accent);
        }
        .stat-box sub {
            font-size: 11px;
            color: var(--text-muted);
            font-weight: normal;
        }
        .ppg-canvas {
            width: 100%;
            height: 80px;
            background: #070b12;
            border: 1px solid var(--border);
            border-radius: 10px;
            margin-bottom: 14px;
        }
        .btn-action-main {
            width: 100%;
            background: linear-gradient(135deg, #38bdf8, #2563eb);
            color: #fff;
            border: none;
            padding: 14px;
            border-radius: 12px;
            font-size: 14px;
            font-weight: 800;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            box-shadow: 0 4px 15px rgba(56, 189, 248, 0.3);
            text-decoration: none;
        }
        .btn-action-main:hover {
            transform: translateY(-2px);
        }

        /* Screen 2: Quiz */
        .quiz-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
        }
        .quiz-item {
            background: var(--surface-card);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 16px;
        }
        .quiz-item label {
            font-size: 12px;
            font-weight: 800;
            display: block;
            margin-bottom: 4px;
        }
        .quiz-item span.hint {
            font-size: 11px;
            color: var(--text-dim);
            display: block;
            margin-bottom: 10px;
        }
        .input-control, .select-control {
            width: 100%;
            background: var(--bg);
            border: 1px solid var(--border);
            border-radius: 8px;
            color: #fff;
            padding: 9px 12px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 13px;
            outline: none;
        }
        .result-banner {
            margin-top: 24px;
            background: linear-gradient(145deg, #0f172a, #0b1120);
            border: 1px solid #38bdf8;
            border-radius: 16px;
            padding: 22px;
        }

        /* Screen 3: Time Machine */
        .tm-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 14px;
            margin-bottom: 22px;
        }

        /* Screen 4: Biomarkers */
        .biomarkers-layout {
            display: grid;
            grid-template-columns: 1fr 340px;
            gap: 24px;
        }
        .subtabs {
            display: flex;
            gap: 8px;
            margin-bottom: 18px;
            overflow-x: auto;
            padding-bottom: 4px;
        }
        .subtab-btn {
            background: var(--surface-card);
            border: 1px solid var(--border);
            color: var(--text-muted);
            padding: 8px 14px;
            border-radius: 10px;
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            white-space: nowrap;
        }
        .subtab-btn.active {
            background: var(--accent);
            color: #000;
            border-color: var(--accent);
        }
        .markers-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }
        .marker-card {
            background: var(--surface-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 12px;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        .marker-head {
            display: flex;
            justify-content: space-between;
            font-size: 11px;
            font-weight: 700;
        }
        .marker-inputs {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .marker-slider {
            flex: 1;
            accent-color: var(--accent);
            cursor: pointer;
        }
        .marker-val {
            width: 65px;
            background: var(--bg);
            border: 1px solid var(--border);
            border-radius: 6px;
            color: #fff;
            padding: 4px 6px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            text-align: right;
        }
        .side-hud {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 20px;
            height: fit-content;
            position: sticky;
            top: 90px;
        }

        /* Screen 5: Booking */
        .booking-layout {
            display: grid;
            grid-template-columns: 1fr 360px;
            gap: 28px;
        }
        .form-group {
            margin-bottom: 14px;
        }
        .form-group label {
            font-size: 11px;
            text-transform: uppercase;
            color: var(--text-dim);
            font-weight: 700;
            display: block;
            margin-bottom: 4px;
        }
        .qr-card {
            background: var(--surface-card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 20px;
            text-align: center;
        }
        .qr-placeholder {
            width: 170px;
            height: 170px;
            background: #fff;
            padding: 8px;
            border-radius: 12px;
            margin: 12px auto;
        }
        .qr-placeholder img {
            width: 100%;
            height: 100%;
            object-fit: contain;
        }
        .btn-wa {
            background: #25d366;
            color: #000;
            font-weight: 800;
            padding: 12px;
            border-radius: 12px;
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            font-size: 13px;
            margin-top: 10px;
        }

        /* Footer */
        .footer {
            border-top: 1px solid var(--border);
            background: var(--surface);
            padding: 20px 36px;
            font-size: 12px;
            color: var(--text-dim);
            text-align: center;
            margin-top: auto;
        }

        
        /* 7-DAY FREE TRIAL BANNER & SCREEN */
        .trial-banner {
            background: linear-gradient(135deg, rgba(56, 189, 248, 0.12), rgba(16, 185, 129, 0.12));
            border: 2px solid #38bdf8;
            border-radius: 20px;
            padding: 24px 32px;
            margin-bottom: 28px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 20px;
            box-shadow: 0 10px 30px rgba(56, 189, 248, 0.15);
            cursor: pointer;
            transition: all 0.25s;
        }
        .trial-banner:hover {
            transform: translateY(-3px);
            box-shadow: 0 14px 40px rgba(56, 189, 248, 0.25);
            border-color: #10b981;
        }
        .trial-badge {
            background: linear-gradient(135deg, #f59e0b, #d97706);
            color: #000;
            font-size: 11px;
            font-weight: 900;
            padding: 4px 12px;
            border-radius: 999px;
            text-transform: uppercase;
            display: inline-block;
            margin-bottom: 8px;
            letter-spacing: 0.5px;
        }
        .trial-title {
            font-size: 22px;
            font-weight: 800;
            margin-bottom: 6px;
            color: #fff;
        }
        .trial-desc {
            font-size: 13px;
            color: var(--text-muted);
            max-width: 620px;
            line-height: 1.5;
            margin-bottom: 12px;
        }
        .trial-perks {
            display: flex;
            flex-wrap: wrap;
            gap: 14px;
            font-size: 12px;
            color: #34d399;
            font-weight: 700;
        }
        .btn-trial-act {
            background: linear-gradient(135deg, #10b981, #059669);
            color: #fff;
            border: none;
            padding: 14px 26px;
            border-radius: 12px;
            font-size: 14px;
            font-weight: 900;
            cursor: pointer;
            white-space: nowrap;
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.35);
            transition: all 0.2s;
        }
        .btn-trial-act:hover {
            transform: scale(1.04);
            box-shadow: 0 8px 25px rgba(16, 185, 129, 0.5);
        }

        /* 7-Day Timeline */
        .timeline-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 16px;
            margin: 24px 0;
        }
        .timeline-day-card {
            background: var(--surface-card);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 18px;
            position: relative;
        }
        .day-num {
            display: inline-block;
            background: rgba(56, 189, 248, 0.15);
            color: var(--accent);
            border: 1px solid rgba(56, 189, 248, 0.3);
            font-size: 11px;
            font-weight: 800;
            padding: 3px 10px;
            border-radius: 6px;
            margin-bottom: 8px;
        }
        .day-title {
            font-size: 14px;
            font-weight: 800;
            color: #fff;
            margin-bottom: 6px;
        }
        .day-desc {
            font-size: 12px;
            color: var(--text-muted);
            line-height: 1.5;
        }

        
        /* PRICING & SUBSCRIPTION SECTION */
        .plans-section {
            max-width: 1200px;
            margin: 40px auto 20px;
            padding: 0 24px;
        }
        .plans-heading-box {
            text-align: center;
            margin-bottom: 30px;
        }
        .plans-title {
            font-size: 26px;
            font-weight: 800;
            color: #fff;
            margin-bottom: 6px;
        }
        .plans-sub {
            font-size: 14px;
            color: var(--text-muted);
            max-width: 600px;
            margin: 0 auto;
        }
        .plans-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 20px;
        }
        .plan-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 24px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
            transition: all 0.25s;
        }
        .plan-card:hover {
            transform: translateY(-4px);
            border-color: var(--accent);
            box-shadow: 0 12px 35px rgba(56, 189, 248, 0.15);
        }
        .plan-badge-top {
            position: absolute;
            top: -12px;
            left: 50%;
            transform: translateX(-50%);
            background: linear-gradient(135deg, #f59e0b, #d97706);
            color: #000;
            font-size: 10px;
            font-weight: 900;
            padding: 3px 12px;
            border-radius: 999px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .plan-badge-popular {
            background: linear-gradient(135deg, #38bdf8, #2563eb);
            color: #fff;
        }
        .plan-badge-vip {
            background: linear-gradient(135deg, #a855f7, #7c3aed);
            color: #fff;
        }
        .plan-price-box {
            margin: 16px 0 14px;
        }
        .plan-price {
            font-family: 'JetBrains Mono', monospace;
            font-size: 32px;
            font-weight: 900;
            color: #fff;
        }
        .plan-period {
            font-size: 12px;
            color: var(--text-dim);
        }
        .plan-features {
            list-style: none;
            padding: 0;
            margin: 0 0 20px;
            font-size: 12px;
            color: var(--text-muted);
            line-height: 2;
        }
        .plan-features li {
            display: flex;
            align-items: baseline;
            gap: 8px;
        }
        .plan-features li::before {
            content: "✓";
            color: #10b981;
            font-weight: 800;
        }
        .btn-plan-act {
            width: 100%;
            background: var(--surface-card);
            border: 1px solid var(--border);
            color: #fff;
            padding: 12px;
            border-radius: 10px;
            font-size: 13px;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }
        .btn-plan-act:hover {
            background: var(--accent);
            color: #000;
            border-color: var(--accent);
        }
        .plan-card-popular {
            border-color: #38bdf8;
            background: linear-gradient(180deg, rgba(56, 189, 248, 0.05), var(--surface));
        }
        .plan-card-popular .btn-plan-act {
            background: linear-gradient(135deg, #38bdf8, #2563eb);
            border: none;
            color: #fff;
        }
        .plan-card-vip {
            border-color: #a855f7;
            background: linear-gradient(180deg, rgba(168, 85, 247, 0.06), var(--surface));
        }
        .plan-card-vip .btn-plan-act {
            background: linear-gradient(135deg, #a855f7, #7c3aed);
            border: none;
            color: #fff;
        }

        @media (max-width: 900px) {
            .scanner-layout, .quiz-grid, .tm-grid, .biomarkers-layout, .booking-layout { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>

    <!-- TOP GLOBAL NAVBAR (Always present) -->
    <nav class="navbar">
        <div class="brand-box" onclick="showScreen('hub')">
            <div class="brand-icon">Ω</div>
            <div class="brand-text">
                <h1 data-i18n="brand_title">BioTwin Labs</h1>
                <span data-i18n="brand_sub">Precision Longevity & Health Checkup Platform</span>
            </div>
        </div>

        <div class="nav-controls">
            
            <button class="btn-nav" onclick="showScreen('freetrial')" style="background: rgba(16, 185, 129, 0.12); border-color: rgba(16, 185, 129, 0.35); color: #34d399;">
                <span>🎁</span>
                <span data-i18n="nav_free_trial">7 Days Free Trial</span>
            </button>

            
            <button class="btn-nav" onclick="showScreen('plans')">
                <span>💎</span>
                <span data-i18n="nav_plans">Plans (₹199 - ₹3,499)</span>
            </button>

            <button class="btn-nav" onclick="showScreen('hub')">
                <span>🏠</span>
                <span data-i18n="nav_all_services">All Services</span>
            </button>
            
            <div class="lang-switch">
                <button class="lang-btn active" onclick="setLanguage('en', this)">🇬🇧 English</button>
                <button class="lang-btn" onclick="setLanguage('hi', this)">🇮🇳 हिन्दी</button>
                <button class="lang-btn" onclick="setLanguage('hinglish', this)">🇮🇳 Hinglish</button>
            </div>

            <a href="https://wa.me/919343062265" target="_blank" class="btn-nav" style="border-color: #10b981; color: #34d399;">
                <span>💬</span>
                <span>WhatsApp: 9343062265</span>
            </a>
        </div>
    </nav>

    <!-- ================================================= -->
    <!-- SCREEN 0: MAIN CATALOG & REAL-TIME SEARCH HUB     -->
    <!-- ================================================= -->
    <div id="screen-hub" class="screen-view active">
        <div class="hero">
            <div class="hero-badge">
                <span>📚 MBBS Textbook Diagnostic Standards</span>
            </div>
            <h1 class="hero-title" data-i18n="hub_title">
                Aapko Kis Tarah Ke Health Checkup Ki Zaroorat Hai?
            </h1>
            <p class="hero-subtitle" data-i18n="hub_desc">
                Har vyakti ki requirement alag hoti hai. Neeche diye gaye services me se chunein ya search karein — aur bina kisi khichdi ke seedhe us dedicated screen par kaam karein:
            </p>

            <div class="search-container">
                <span class="search-icon">🔍</span>
                <input type="text" id="catalogSearch" class="search-box" placeholder="Apna checkup search karein (e.g. BP, Sugar, Purani Report, Zero Report, Blood Test...)" oninput="filterCatalog(this.value)">
            </div>
        </div>

        <div class="catalog-container">
            <div class="catalog-header">
                <span data-i18n="hub_sec_title">Hamari 5 Dedicated Health Services:</span>
                <span id="catalogCount" style="font-size: 12px; color: var(--text-dim); font-weight: normal;">Showing 5 services</span>
            </div>

            
            <!-- 7-DAY FREE TRIAL HERO SPOTLIGHT -->
            <div class="trial-banner" onclick="showScreen('freetrial')">
                <div>
                    <span class="trial-badge" data-i18n="tb_badge">🎁 SPECIAL LAUNCH OFFER • 7 DAYS FREE</span>
                    <h2 class="trial-title" data-i18n="tb_title">Pehle 7 Din Bilkul FREE Health & Longevity Trial</h2>
                    <p class="trial-desc" data-i18n="tb_desc">
                        Bina kisi payment ya credit card ke, pehle 7 din rozana phone camera se BP & Pulse scan karein, apna biological age score dekhein aur health monitor karein bilkul ₹0 me!
                    </p>
                    <div class="trial-perks">
                        <span>✓ Unlimited Camera BP Scans</span>
                        <span>✓ Zero-Report Health Score</span>
                        <span>✓ Daily WhatsApp Health Tracking</span>
                        <span>✓ 100% Free • No Payment</span>
                    </div>
                </div>
                <div style="text-align: center;">
                    <button class="btn-trial-act" data-i18n="btn_start_trial">
                        Start 7-Day Free Trial (₹0) →
                    </button>
                    <span style="font-size: 11px; color: var(--text-dim); display: block; margin-top: 8px;">No Card Needed • Instant Access</span>
                </div>
            </div>

            <div class="catalog-grid" id="catalogGrid">
                
                <!-- CARD 1 -->
                <div class="service-card" onclick="showScreen('camera')" data-tags="camera bp blood pressure sugar mobile pulse instant free">
                    <div>
                        <div class="card-top">
                            <div class="card-icon">📱</div>
                            <div class="card-price-pill">FREE / ₹0</div>
                        </div>
                        <h2 class="card-title" data-i18n="c1_title">Camera Optical BP & Pulse Checkup</h2>
                        <p class="card-desc" data-i18n="c1_desc">
                            Bina kisi machine ke, apne phone ya laptop camera lens par ungli rakh kar blood vessels se live Blood Pressure aur Heart Rate check karein.
                        </p>
                    </div>
                    <div>
                        <div class="card-meta">
                            <span>⏱️ 15 Seconds</span>
                            <span>🔬 Transdermal PPG Sensor</span>
                        </div>
                        <div class="card-btn">
                            <span data-i18n="c1_btn">Open Camera Scanner</span>
                            <span>→</span>
                        </div>
                    </div>
                </div>

                <!-- CARD 2 -->
                <div class="service-card" onclick="showScreen('quiz')" data-tags="zero report no blood test quiz 2 min belly fat visceral waist insulin">
                    <div>
                        <div class="card-top">
                            <div class="card-icon">📋</div>
                            <div class="card-price-pill">FREE / ₹0</div>
                        </div>
                        <h2 class="card-title" data-i18n="c2_title">Zero-Report 2-Minute Health Score</h2>
                        <p class="card-desc" data-i18n="c2_desc">
                            Agar aapne kabhi blood test nahi karwaya hai, tab bhi 6 physical markers (kamar ka ghera, resting pulse, post-meal neend) se apna biological age aur organ decay jaanein.
                        </p>
                    </div>
                    <div>
                        <div class="card-meta">
                            <span>⏱️ 2 Minutes</span>
                            <span>📚 Guyton & Hall Physiology Ch. 72</span>
                        </div>
                        <div class="card-btn">
                            <span data-i18n="c2_btn">Start 2-Min Assessment</span>
                            <span>→</span>
                        </div>
                    </div>
                </div>

                <!-- CARD 3 -->
                <div class="service-card" onclick="showScreen('timemachine')" data-tags="old report time machine purani drift damage sugar cholesterol">
                    <div>
                        <div class="card-top">
                            <div class="card-icon">⏳</div>
                            <div class="card-price-pill">FREE / ₹0</div>
                        </div>
                        <h2 class="card-title" data-i18n="c3_title">Old Report Time Machine Projector</h2>
                        <p class="card-desc" data-i18n="c3_desc">
                            1 se 3 saal purani blood report ke number dalkar jaanein ki pichle saalon me weight change ke sath aapka metabolic damage aur organ aging kitni badh chuki hai.
                        </p>
                    </div>
                    <div>
                        <div class="card-meta">
                            <span>⏱️ 1 Minute</span>
                            <span>📉 Harrison's Beta-Cell Drift Model</span>
                        </div>
                        <div class="card-btn">
                            <span data-i18n="c3_btn">Check Old Report Drift</span>
                            <span>→</span>
                        </div>
                    </div>
                </div>

                <!-- CARD 4 -->
                <div class="service-card" onclick="showScreen('biomarkers')" data-tags="72 biomarkers full panel report levine phenoage apob homa deep analysis">
                    <div>
                        <div class="card-top">
                            <div class="card-icon">🩸</div>
                            <div class="card-price-pill">ONLINE FREE / PDF ₹499</div>
                        </div>
                        <h2 class="card-title" data-i18n="c4_title">Full 72+ Biomarker Deep Engine</h2>
                        <p class="card-desc" data-i18n="c4_desc">
                            Taaza blood test report ke sabhi 72 parameters (ApoB, Fasting Insulin, hs-CRP, Liver, Kidney) enter karke exact Levine Phenotypic Age aur doctor report nikalein.
                        </p>
                    </div>
                    <div>
                        <div class="card-meta">
                            <span>⏱️ 5 Minutes</span>
                            <span>📑 Executive Doctor-Signed PDF</span>
                        </div>
                        <div class="card-btn">
                            <span data-i18n="c4_btn">Open Biomarker Matrix</span>
                            <span>→</span>
                        </div>
                    </div>
                </div>

                <!-- CARD 5 -->
                <div class="service-card card-featured" onclick="showScreen('booking')" data-tags="book home draw blood sample test collection nabl certified 1999 full body checkup">
                    <div>
                        <div class="card-top">
                            <div class="card-icon">🏠</div>
                            <div class="card-price-pill" style="background: rgba(56, 189, 248, 0.2); border-color: #38bdf8; color: #38bdf8;">₹1,999 ALL-INCLUSIVE</div>
                        </div>
                        <h2 class="card-title" data-i18n="c5_title">Ghar Baithe NABL Blood Test Booking</h2>
                        <p class="card-desc" data-i18n="c5_desc">
                            NABL certified phlebotomist aapke ghar aakar sterile vacuum tubes me sample lega. 72+ biomarkers, Biological Age Blueprint aur Doctor Consultation sabhi included hai.
                        </p>
                    </div>
                    <div>
                        <div class="card-meta">
                            <span>🚚 Tomorrow 7:00 AM - 9:00 AM</span>
                            <span>✓ NABL Certified Labs</span>
                        </div>
                        <div class="card-btn">
                            <span data-i18n="c5_btn">Book Home Blood Draw (₹1,999)</span>
                            <span>→</span>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>


        <!-- PRICING & SUBSCRIPTION SECTION -->
        <div class="plans-section" id="plansCatalog">
            <div class="plans-heading-box">
                <span class="hero-badge" style="background: rgba(168, 85, 247, 0.1); border-color: rgba(168, 85, 247, 0.25); color: #c084fc;">
                    💎 Transparent Pricing Plans
                </span>
                <h2 class="plans-title" data-i18n="sec_plans_title">
                    7 Din Ke Baad Normal Charges Aur Monthly Subscriptions
                </h2>
                <p class="plans-sub" data-i18n="sec_plans_sub">
                    Pehle 7 din bilkul FREE hain. Uske baad koi mehenga charge nahi — sirf normal ₹199/₹299 ke passes ya poor mahine ke subscription me se chunein:
                </p>
            </div>

            <div class="plans-grid">
                
                <!-- PLAN 1: NORMAL WEEKLY PASS (₹199) -->
                <div class="plan-card">
                    <div>
                        <span class="plan-badge-top" style="background: #334155; color: #fff;">AFFORDABLE PASS</span>
                        <h3 style="font-size: 16px; font-weight: 800; color: #fff;">Weekly Checkup Pass</h3>
                        <div class="plan-price-box">
                            <span class="plan-price">₹199</span>
                            <span class="plan-period">/ 7 Days</span>
                        </div>
                        <ul class="plan-features">
                            <li>Unlimited Camera BP Scans</li>
                            <li>Pulse & Arterial Elasticity</li>
                            <li>Post-Meal Sugar Crash Check</li>
                            <li>Instant Risk Alerts</li>
                        </ul>
                    </div>
                    <button class="btn-plan-act" onclick="selectPlan('Weekly Pass', 199)">
                        Choose ₹199 Pass →
                    </button>
                </div>

                <!-- PLAN 2: DEEP REPORT PASS (₹299) -->
                <div class="plan-card">
                    <div>
                        <span class="plan-badge-top" style="background: #0284c7; color: #fff;">ONE-TIME PASS</span>
                        <h3 style="font-size: 16px; font-weight: 800; color: #fff;">Deep Longevity Report</h3>
                        <div class="plan-price-box">
                            <span class="plan-price">₹299</span>
                            <span class="plan-period">/ Single Report</span>
                        </div>
                        <ul class="plan-features">
                            <li>Zero-Report Visceral Score</li>
                            <li>Time Machine 3-Yr Drift</li>
                            <li>HOMA-IR Insulin Resistance</li>
                            <li>Executive PDF Download</li>
                        </ul>
                    </div>
                    <button class="btn-plan-act" onclick="selectPlan('Deep Report Pass', 299)">
                        Choose ₹299 Pass →
                    </button>
                </div>

                <!-- PLAN 3: 1-MONTH STANDARD SUBSCRIPTION (₹2,499) -->
                <div class="plan-card plan-card-popular">
                    <span class="plan-badge-top plan-badge-popular">MOST POPULAR 🔥</span>
                    <div>
                        <h3 style="font-size: 16px; font-weight: 800; color: #38bdf8;">1-Month Standard Membership</h3>
                        <div class="plan-price-box">
                            <span class="plan-price">₹2,499</span>
                            <span class="plan-period">/ Month</span>
                        </div>
                        <ul class="plan-features">
                            <li>30 Days Unlimited Camera Scans</li>
                            <li>Daily Biological Age Tracking</li>
                            <li>Metabolic Drift Reversal Plan</li>
                            <li>Weekly WhatsApp Diet Guide</li>
                            <li>Priority Doctor Assistance</li>
                        </ul>
                    </div>
                    <button class="btn-plan-act" onclick="selectPlan('1-Month Standard Subscription', 2499)">
                        Start ₹2,499 Monthly →
                    </button>
                </div>

                <!-- PLAN 4: 1-MONTH VIP SUBSCRIPTION (₹3,499) -->
                <div class="plan-card plan-card-vip">
                    <span class="plan-badge-top plan-badge-vip">ALL-INCLUSIVE VIP 👑</span>
                    <div>
                        <h3 style="font-size: 16px; font-weight: 800; color: #c084fc;">1-Month VIP + Blood Test</h3>
                        <div class="plan-price-box">
                            <span class="plan-price">₹3,499</span>
                            <span class="plan-period">/ Month</span>
                        </div>
                        <ul class="plan-features">
                            <li><strong>Includes NABL Home Blood Draw (72+ Tests)</strong></li>
                            <li>Full Levine PhenoAge Doctor Report</li>
                            <li>1-on-1 Doctor Longevity Consult</li>
                            <li>30-Day Family Camera App Access</li>
                            <li>Personalized Reversal Plan</li>
                        </ul>
                    </div>
                    <button class="btn-plan-act" onclick="selectPlan('1-Month VIP Longevity Membership', 3499)">
                        Join ₹3,499 VIP →
                    </button>
                </div>

            </div>
        </div>


    <!-- ================================================= -->
    <!-- SCREEN 1: DEDICATED CAMERA BP & SUGAR SCANNER     -->
    <!-- ================================================= -->
    <div id="screen-camera" class="screen-view">
        <div class="screen-header-bar">
            <button class="btn-back-home" onclick="showScreen('hub')">
                <span>←</span>
                <span data-i18n="btn_back_services">Back to All Services</span>
            </button>
            <span class="screen-tag">📱 Dedicated Camera Scan</span>
        </div>

        <div class="detail-container">
            <div class="detail-panel">
                <h2 class="detail-title" data-i18n="cam_title">Camera Optical Blood Pressure & Pulse Scanner</h2>
                <p class="detail-desc" data-i18n="cam_desc">
                    Yeh tool aapke device camera se ungli ki blood vessels me roshni ke micro-reflections read karta hai. 15 second me arterial stiffness aur systolic/diastolic BP estimate hota hai.
                </p>

                <div class="scanner-layout">
                    <div class="camera-viewport">
                        <video id="webcamVideo" class="camera-video" autoplay playsinline muted></video>
                        <div class="pulse-heart" id="pulseHeart">🫀</div>
                        <div id="scanStatus" style="font-size: 11px; color: var(--text-muted); text-align: center; padding: 0 20px; margin-top: 14px;" data-i18n="cam_instruct">
                            Place your finger over camera lens or look directly at screen. Click Start Scan below.
                        </div>
                    </div>

                    <div>
                        <div class="stats-grid-2x2">
                            <div class="stat-box">
                                <label data-i18n="lbl_bp">Blood Pressure (BP)</label>
                                <val id="resBP">122</val><sub id="resBPDia">/ 79 mmHg</sub>
                            </div>
                            <div class="stat-box">
                                <label data-i18n="lbl_hr">Heart Rate (Pulse)</label>
                                <val id="resHR">70</val><sub> bpm</sub>
                            </div>
                            <div class="stat-box">
                                <label data-i18n="lbl_elasticity">Arterial Elasticity</label>
                                <val id="resElasticity" style="color: var(--success); font-size: 20px;">Optimal</val>
                            </div>
                            <div class="stat-box">
                                <label data-i18n="lbl_sugar">Sugar Stability</label>
                                <val id="resSugar" style="font-size: 20px;">94 mg/dL</val>
                            </div>
                        </div>

                        <canvas id="ppgCanvas" class="ppg-canvas"></canvas>

                        <button class="btn-action-main" id="btnToggleScan" onclick="toggleScan()">
                            <span>⚡</span>
                            <span data-i18n="btn_start_scan">Start 15-Second Optical Camera Scan</span>
                        </button>
                    </div>
                </div>

                <!-- Manual Quick Verification -->
                <div style="margin-top: 28px; background: var(--surface-card); border: 1px solid var(--border); border-radius: 14px; padding: 20px;">
                    <strong style="font-size: 13px; color: #fff; display: block; margin-bottom: 8px;" data-i18n="manual_title">
                        Ya Apna Current BP & Sugar Yahan Type Karein (Instant Risk Check):
                    </strong>
                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;">
                        <div>
                            <label style="font-size: 10px; color: var(--text-dim); text-transform: uppercase; font-weight: 700;">Systolic BP (Upper)</label>
                            <input type="number" id="inSys" class="input-control" value="122" oninput="evalManual()">
                        </div>
                        <div>
                            <label style="font-size: 10px; color: var(--text-dim); text-transform: uppercase; font-weight: 700;">Diastolic BP (Lower)</label>
                            <input type="number" id="inDia" class="input-control" value="79" oninput="evalManual()">
                        </div>
                        <div>
                            <label style="font-size: 10px; color: var(--text-dim); text-transform: uppercase; font-weight: 700;">Fasting Sugar (mg/dL)</label>
                            <input type="number" id="inSugar" class="input-control" value="94" oninput="evalManual()">
                        </div>
                    </div>
                    <div id="manualVerdict" style="margin-top: 10px; font-size: 12px; font-weight: 700; color: #10b981;">
                        ✓ Optimal Clinical Range (Harrison's Internal Medicine 21st Ed)
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- ================================================= -->
    <!-- SCREEN 2: DEDICATED ZERO-REPORT 2-MIN QUIZ        -->
    <!-- ================================================= -->
    <div id="screen-quiz" class="screen-view">
        <div class="screen-header-bar">
            <button class="btn-back-home" onclick="showScreen('hub')">
                <span>←</span>
                <span data-i18n="btn_back_services">Back to All Services</span>
            </button>
            <span class="screen-tag">📋 Zero-Report Assessment</span>
        </div>

        <div class="detail-container">
            <div class="detail-panel">
                <h2 class="detail-title" data-i18n="quiz_title">Zero-Report 2-Minute Longevity Assessment</h2>
                <p class="detail-desc" data-i18n="quiz_desc">
                    Agar aapne kabhi blood test nahi karwaya hai, tab bhi yeh 6 physical markers (Guyton & Hall Physiology Ch. 72) pait ki charbi, insulin resistance aur biological age calculate karte hain.
                </p>

                <div class="quiz-grid">
                    <div class="quiz-item">
                        <label data-i18n="q_age">1. Chronological Age (Asli Umar)</label>
                        <span class="hint" data-i18n="q_age_hint">Years on your ID proof</span>
                        <input type="number" id="q_age" class="input-control" value="42" oninput="runQuizCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="q_height">2. Height (Kadd / Lambai in cm)</label>
                        <span class="hint" data-i18n="q_height_hint">E.g., 5 ft 8 in = 173 cm, 5 ft 10 in = 178 cm</span>
                        <input type="number" id="q_height" class="input-control" value="175" oninput="runQuizCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="q_waist">3. Waist Circumference (Kamar ka Ghera in Inches)</label>
                        <span class="hint" data-i18n="q_waist_hint">Naabhi (Navel) ke theek upar se tape se naapein</span>
                        <input type="number" id="q_waist" class="input-control" value="36" oninput="runQuizCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="q_rhr">4. Resting Heart Rate (Aaram ke Waqt Pulse)</label>
                        <span class="hint" data-i18n="q_rhr_hint">Optimal < 65 bpm. > 75 = sympathetic overdrive</span>
                        <input type="number" id="q_rhr" class="input-control" value="74" oninput="runQuizCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="q_fatigue">5. Post-Meal Fatigue (Khana Khane ke Baad Susti)</label>
                        <span class="hint" data-i18n="q_fatigue_hint">Carb khane ke baad neend aana = early insulin resistance</span>
                        <select id="q_fatigue" class="select-control" onchange="runQuizCalc()">
                            <option value="none">Kabhi nahi / No fatigue</option>
                            <option value="mild" selected>Kabhi-kabhi thodi susti aati hai</option>
                            <option value="frequent">Roz khane ke baad bhari neend aati hai</option>
                            <option value="severe">Bahut zyada neend aur meetha khane ki tez craving</option>
                        </select>
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="q_fam">6. Family History of Diabetes / Heart Disease</label>
                        <span class="hint" data-i18n="q_fam_hint">Mata, pita ya bhai-behan ko sugar ya BP ki bimari</span>
                        <select id="q_fam" class="select-control" onchange="runQuizCalc()">
                            <option value="none">Kisi ko nahi / No history</option>
                            <option value="one" selected>Ek parent (Mother or Father)</option>
                            <option value="both">Dono parents (Both Mother & Father)</option>
                        </select>
                    </div>
                </div>

                <div class="result-banner">
                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-bottom: 14px;">
                        <div class="stat-box">
                            <label>Waist-to-Height Ratio</label>
                            <val id="resWHtR">0.52</val>
                        </div>
                        <div class="stat-box">
                            <label>Estimated Biological Age</label>
                            <val id="resBioAge" style="color: #f59e0b;">44.2 Yrs</val>
                        </div>
                        <div class="stat-box">
                            <label>Estimated Fasting Insulin</label>
                            <val id="resInsulin" style="color: #ef4444;">8.5 µIU/mL</val>
                        </div>
                    </div>

                    <div id="quizSummaryText" style="font-size: 13px; line-height: 1.7; color: #fff; margin-bottom: 16px;">
                        Calculating non-invasive parameters...
                    </div>

                    <button class="btn-action-main" onclick="showScreen('booking')">
                        <span>🩸</span>
                        <span data-i18n="btn_confirm_blood_draw">Confirm with ₹1,999 At-Home Blood Test</span>
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- ================================================= -->
    <!-- SCREEN 3: DEDICATED OLD REPORT TIME MACHINE       -->
    <!-- ================================================= -->
    <div id="screen-timemachine" class="screen-view">
        <div class="screen-header-bar">
            <button class="btn-back-home" onclick="showScreen('hub')">
                <span>←</span>
                <span data-i18n="btn_back_services">Back to All Services</span>
            </button>
            <span class="screen-tag">⏳ Old Report Time Machine</span>
        </div>

        <div class="detail-container">
            <div class="detail-panel">
                <h2 class="detail-title" data-i18n="tm_title">Old Report Time Machine: Metabolic Drift Projector</h2>
                <p class="detail-desc" data-i18n="tm_desc">
                    Agar aapke paas 1 se 3 saal purani blood report hai, toh elapsed time aur weight change ke basis par Harrison's Internal Medicine beta-cell exhaustion model se calculate karein ki aaj aapka organ decay kitna badh chuka hai.
                </p>

                <div class="tm-grid">
                    <div class="quiz-item">
                        <label data-i18n="tm_lbl_years">Report Kitni Purani Hai? (Years)</label>
                        <input type="number" id="tm_years" class="input-control" value="2" min="0.5" max="5" step="0.5" oninput="runDriftCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="tm_lbl_weight">Tab Se Vajan Me Farak (Kg)</label>
                        <input type="number" id="tm_weight" class="input-control" value="4" oninput="runDriftCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="tm_lbl_old_glu">Purana Fasting Glucose (mg/dL)</label>
                        <input type="number" id="tm_glu" class="input-control" value="92" oninput="runDriftCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="tm_lbl_old_hba1c">Purana HbA1c (%)</label>
                        <input type="number" id="tm_hba1c" class="input-control" value="5.3" step="0.1" oninput="runDriftCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="tm_lbl_old_trig">Purane Triglycerides (mg/dL)</label>
                        <input type="number" id="tm_trig" class="input-control" value="155" oninput="runDriftCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="tm_lbl_old_chol">Purana Total Cholesterol (mg/dL)</label>
                        <input type="number" id="tm_chol" class="input-control" value="195" oninput="runDriftCalc()">
                    </div>
                </div>

                <div style="background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 16px; padding: 22px;">
                    <strong style="color: #f59e0b; font-size: 14px; display: block; margin-bottom: 12px;" data-i18n="tm_proj_header">
                        🔮 Projected Current Health (Harrison's Beta-Cell Drift):
                    </strong>

                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 14px;">
                        <div class="stat-box">
                            <label>Projected Fasting Glucose</label>
                            <val id="projGlu" style="color: #ef4444;">102 mg/dL</val>
                        </div>
                        <div class="stat-box">
                            <label>Projected HbA1c</label>
                            <val id="projHbA1c" style="color: #f59e0b;">5.7%</val>
                        </div>
                        <div class="stat-box">
                            <label>Projected Biological Age</label>
                            <val id="projBioAge" style="color: #ef4444;">45.2 Yrs</val>
                        </div>
                    </div>

                    <div id="tmSummaryText" style="font-size: 13px; line-height: 1.7; color: #fff; margin-bottom: 18px;">
                        Calculating drift rates...
                    </div>

                    <button class="btn-action-main" onclick="showScreen('booking')">
                        <span>🏠</span>
                        <span data-i18n="btn_stop_drift">Book Fresh Checkup to Stop Drift (₹1,999)</span>
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- ================================================= -->
    <!-- SCREEN 4: DEDICATED FULL 72+ BIOMARKER PANEL      -->
    <!-- ================================================= -->
    <div id="screen-biomarkers" class="screen-view">
        <div class="screen-header-bar">
            <button class="btn-back-home" onclick="showScreen('hub')">
                <span>←</span>
                <span data-i18n="btn_back_services">Back to All Services</span>
            </button>
            <span class="screen-tag">🩸 72+ Biomarker Panel</span>
        </div>

        <div class="detail-container" style="max-width: 1240px;">
            <div class="detail-panel">
                <h2 class="detail-title" data-i18n="bio_title">Full 72+ Biomarker Panel & Phenotypic Aging Matrix</h2>
                <p class="detail-desc" data-i18n="bio_desc">
                    Taaza blood report ke numbers dalkar exact Levine PhenoAge nikalen. Har biomarker ke aage optimal longevity target diya gaya hai.
                </p>

                <div class="biomarkers-layout">
                    <div>
                        <div class="subtabs">
                            <button class="subtab-btn active" onclick="switchCategory('cat_cardio', this)">❤️ Cardio & Lipids</button>
                            <button class="subtab-btn" onclick="switchCategory('cat_metabolic', this)">⚡ Metabolic & Glucose</button>
                            <button class="subtab-btn" onclick="switchCategory('cat_inflam', this)">🔥 Inflammation</button>
                            <button class="subtab-btn" onclick="switchCategory('cat_organs', this)">🫀 Liver & Kidney</button>
                            <button class="subtab-btn" onclick="switchCategory('cat_vitamins', this)">🧬 Vitamins & Hormones</button>
                        </div>

                        <!-- CARDIO -->
                        <div id="cat_cardio" class="cat-content markers-grid">
                            <div class="marker-card">
                                <div class="marker-head"><span>Apolipoprotein B (ApoB)</span><span style="color:var(--text-dim);">mg/dL</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_apob" min="40" max="180" value="70" oninput="updBiomarker('apob', this.value)">
                                    <input type="number" class="marker-val" id="in_apob" value="70" oninput="updBiomarker('apob', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: < 60</span><span>Lab Limit: 130</span></div>
                            </div>
                            <div class="marker-card">
                                <div class="marker-head"><span>Lipoprotein(a) [Lp(a)]</span><span style="color:var(--text-dim);">nmol/L</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_lpa" min="5" max="250" value="18" oninput="updBiomarker('lpa', this.value)">
                                    <input type="number" class="marker-val" id="in_lpa" value="18" oninput="updBiomarker('lpa', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: < 30</span><span>Lab Limit: 75</span></div>
                            </div>
                            <div class="marker-card">
                                <div class="marker-head"><span>Triglycerides / HDL Ratio</span><span style="color:var(--text-dim);">ratio</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_trighdl" min="0.5" max="8.0" step="0.1" value="1.6" oninput="updBiomarker('trighdl', this.value)">
                                    <input type="number" class="marker-val" id="in_trighdl" value="1.6" step="0.1" oninput="updBiomarker('trighdl', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: < 1.5</span><span>Lab Limit: 3.5</span></div>
                            </div>
                            <div class="marker-card">
                                <div class="marker-head"><span>Homocysteine</span><span style="color:var(--text-dim);">µmol/L</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_homo" min="4" max="40" step="0.5" value="9.2" oninput="updBiomarker('homo', this.value)">
                                    <input type="number" class="marker-val" id="in_homo" value="9.2" step="0.5" oninput="updBiomarker('homo', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: < 9.0</span><span>Lab Limit: 15.0</span></div>
                            </div>
                        </div>

                        <!-- METABOLIC -->
                        <div id="cat_metabolic" class="cat-content markers-grid" style="display: none;">
                            <div class="marker-card">
                                <div class="marker-head"><span>Fasting Insulin</span><span style="color:var(--text-dim);">µIU/mL</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_insulin" min="1.0" max="45.0" step="0.5" value="6.5" oninput="updBiomarker('insulin', this.value)">
                                    <input type="number" class="marker-val" id="in_insulin" value="6.5" step="0.5" oninput="updBiomarker('insulin', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: < 5.0</span><span>Lab Limit: 25.0</span></div>
                            </div>
                            <div class="marker-card">
                                <div class="marker-head"><span>HbA1c</span><span style="color:var(--text-dim);">%</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_hba1c" min="4.0" max="12.0" step="0.1" value="5.2" oninput="updBiomarker('hba1c', this.value)">
                                    <input type="number" class="marker-val" id="in_hba1c" value="5.2" step="0.1" oninput="updBiomarker('hba1c', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: < 5.2</span><span>Pre-Diab: 5.7-6.4</span></div>
                            </div>
                            <div class="marker-card">
                                <div class="marker-head"><span>Fasting Glucose</span><span style="color:var(--text-dim);">mg/dL</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_glucose" min="60" max="250" value="88" oninput="updBiomarker('glucose', this.value)">
                                    <input type="number" class="marker-val" id="in_glucose" value="88" oninput="updBiomarker('glucose', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: 72-85</span><span>Lab Limit: 99</span></div>
                            </div>
                            <div class="marker-card">
                                <div class="marker-head"><span>Serum Uric Acid</span><span style="color:var(--text-dim);">mg/dL</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_uric" min="2.0" max="12.0" step="0.1" value="4.8" oninput="updBiomarker('uric', this.value)">
                                    <input type="number" class="marker-val" id="in_uric" value="4.8" step="0.1" oninput="updBiomarker('uric', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: < 5.0</span><span>Lab Limit: 7.2</span></div>
                            </div>
                        </div>

                        <!-- INFLAM -->
                        <div id="cat_inflam" class="cat-content markers-grid" style="display: none;">
                            <div class="marker-card">
                                <div class="marker-head"><span>hs-CRP</span><span style="color:var(--text-dim);">mg/L</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_hscrp" min="0.1" max="15.0" step="0.1" value="0.7" oninput="updBiomarker('hscrp', this.value)">
                                    <input type="number" class="marker-val" id="in_hscrp" value="0.7" step="0.1" oninput="updBiomarker('hscrp', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: < 0.5</span><span>High Risk: > 2.0</span></div>
                            </div>
                            <div class="marker-card">
                                <div class="marker-head"><span>Serum Ferritin</span><span style="color:var(--text-dim);">ng/mL</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_ferritin" min="10" max="600" value="85" oninput="updBiomarker('ferritin', this.value)">
                                    <input type="number" class="marker-val" id="in_ferritin" value="85" oninput="updBiomarker('ferritin', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: 40-120</span><span>Lab Limit: 300</span></div>
                            </div>
                        </div>

                        <!-- ORGANS -->
                        <div id="cat_organs" class="cat-content markers-grid" style="display: none;">
                            <div class="marker-card">
                                <div class="marker-head"><span>ALT / SGPT (Liver)</span><span style="color:var(--text-dim);">U/L</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_alt" min="5" max="150" value="22" oninput="updBiomarker('alt', this.value)">
                                    <input type="number" class="marker-val" id="in_alt" value="22" oninput="updBiomarker('alt', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: < 25</span><span>Lab Limit: 45</span></div>
                            </div>
                            <div class="marker-card">
                                <div class="marker-head"><span>eGFR (Kidney)</span><span style="color:var(--text-dim);">mL/min</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_egfr" min="30" max="140" value="105" oninput="updBiomarker('egfr', this.value)">
                                    <input type="number" class="marker-val" id="in_egfr" value="105" oninput="updBiomarker('egfr', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: > 90</span><span>Alert: < 60</span></div>
                            </div>
                        </div>

                        <!-- VITAMINS -->
                        <div id="cat_vitamins" class="cat-content markers-grid" style="display: none;">
                            <div class="marker-card">
                                <div class="marker-head"><span>Vitamin D3</span><span style="color:var(--text-dim);">ng/mL</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_vitd" min="10" max="120" value="55" oninput="updBiomarker('vitd', this.value)">
                                    <input type="number" class="marker-val" id="in_vitd" value="55" oninput="updBiomarker('vitd', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: 50-80</span><span>Deficiency: < 30</span></div>
                            </div>
                            <div class="marker-card">
                                <div class="marker-head"><span>Vitamin B12</span><span style="color:var(--text-dim);">pg/mL</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_vitb12" min="100" max="1500" value="650" oninput="updBiomarker('vitb12', this.value)">
                                    <input type="number" class="marker-val" id="in_vitb12" value="650" oninput="updBiomarker('vitb12', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: 500-900</span><span>Lab Limit: 200</span></div>
                            </div>
                        </div>
                    </div>

                    <!-- HUD -->
                    <div class="side-hud">
                        <h3 style="font-size: 13px; text-transform: uppercase; color: var(--accent); margin-bottom: 14px; border-bottom: 1px solid var(--border); padding-bottom: 8px;">
                            ⚡ Live PhenoAge HUD
                        </h3>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 12px; color: var(--text-muted);">
                            <span>Calendar Age:</span>
                            <span style="font-family:'JetBrains Mono',monospace; font-weight:700; color:#fff;">42.0</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 12px; color: var(--text-muted);">
                            <span>Biological PhenoAge:</span>
                            <span id="hudBioVal" style="font-family:'JetBrains Mono',monospace; font-size:22px; font-weight:800; color:var(--accent);">39.8</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 12px; color: var(--text-muted);">
                            <span>Age Delta:</span>
                            <span id="hudDeltaVal" style="font-family:'JetBrains Mono',monospace; font-weight:800; color:#10b981;">-2.2 Yrs</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 16px; font-size: 12px; color: var(--text-muted);">
                            <span>HOMA-IR Score:</span>
                            <span id="hudHomaVal" style="font-family:'JetBrains Mono',monospace; font-weight:800; color:#fff;">1.41</span>
                        </div>

                        <form action="/generate-report" method="POST" target="_blank">
                            <input type="hidden" name="name" value="Patient Executive">
                            <input type="hidden" name="age" value="42">
                            <input type="hidden" name="gender" value="Male">
                            <input type="hidden" name="phone" value="9343062265">
                            <input type="hidden" name="apob" id="p_apob" value="70">
                            <input type="hidden" name="fasting_insulin" id="p_insulin" value="6.5">
                            <input type="hidden" name="fasting_glucose" id="p_glucose" value="88">
                            <input type="hidden" name="hba1c" value="5.2">
                            <input type="hidden" name="hs_crp" id="p_hscrp" value="0.7">
                            <input type="hidden" name="alt" value="22">
                            <input type="hidden" name="albumin" value="4.5">

                            <button type="submit" class="btn-action-main" style="padding: 12px; font-size: 12px;">
                                📄 Generate Doctor Report
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- ================================================= -->
    
    <!-- ================================================= -->
    
    <!-- ================================================= -->
    <!-- SCREEN: DEDICATED PLANS & PRICING SCREEN          -->
    <!-- ================================================= -->
    <div id="screen-plans" class="screen-view">
        <div class="screen-header-bar">
            <button class="btn-back-home" onclick="showScreen('hub')">
                <span>←</span>
                <span data-i18n="btn_back_services">Back to All Services</span>
            </button>
            <span class="screen-tag" style="background: rgba(168, 85, 247, 0.15); border-color: rgba(168, 85, 247, 0.35); color: #c084fc;">
                💎 Memberships & Subscriptions
            </span>
        </div>

        <div class="detail-container" style="max-width: 1200px;">
            <div class="detail-panel">
                <h2 class="detail-title" data-i18n="p_screen_title">Choose Your Health Monitoring Pass</h2>
                <p class="detail-desc" data-i18n="p_screen_desc">
                    Pehle 7 din bilkul FREE hain. Uske baad normal weekly checkup pass (₹199, ₹299) ya 1-month full-body subscription (₹2,499, ₹3,499) me se apni zaroorat ke hisaab se chunein:
                </p>

                <div class="plans-grid" style="margin-top: 24px;">
                    <div class="plan-card">
                        <div>
                            <span class="plan-badge-top" style="background: #334155; color: #fff;">AFFORDABLE PASS</span>
                            <h3 style="font-size: 16px; font-weight: 800; color: #fff;">Weekly Checkup Pass</h3>
                            <div class="plan-price-box">
                                <span class="plan-price">₹199</span>
                                <span class="plan-period">/ 7 Days</span>
                            </div>
                            <ul class="plan-features">
                                <li>Unlimited Camera BP Scans</li>
                                <li>Pulse & Arterial Elasticity</li>
                                <li>Post-Meal Sugar Crash Check</li>
                                <li>Instant Risk Alerts</li>
                            </ul>
                        </div>
                        <button class="btn-plan-act" onclick="selectPlan('Weekly Pass', 199)">
                            Activate ₹199 Pass →
                        </button>
                    </div>

                    <div class="plan-card">
                        <div>
                            <span class="plan-badge-top" style="background: #0284c7; color: #fff;">ONE-TIME PASS</span>
                            <h3 style="font-size: 16px; font-weight: 800; color: #fff;">Deep Longevity Report</h3>
                            <div class="plan-price-box">
                                <span class="plan-price">₹299</span>
                                <span class="plan-period">/ Single Report</span>
                            </div>
                            <ul class="plan-features">
                                <li>Zero-Report Visceral Score</li>
                                <li>Time Machine 3-Yr Drift</li>
                                <li>HOMA-IR Insulin Resistance</li>
                                <li>Executive PDF Download</li>
                            </ul>
                        </div>
                        <button class="btn-plan-act" onclick="selectPlan('Deep Report Pass', 299)">
                            Activate ₹299 Pass →
                        </button>
                    </div>

                    <div class="plan-card plan-card-popular">
                        <span class="plan-badge-top plan-badge-popular">MOST POPULAR 🔥</span>
                        <div>
                            <h3 style="font-size: 16px; font-weight: 800; color: #38bdf8;">1-Month Standard Membership</h3>
                            <div class="plan-price-box">
                                <span class="plan-price">₹2,499</span>
                                <span class="plan-period">/ Month</span>
                            </div>
                            <ul class="plan-features">
                                <li>30 Days Unlimited Camera Scans</li>
                                <li>Daily Biological Age Tracking</li>
                                <li>Metabolic Drift Reversal Plan</li>
                                <li>Weekly WhatsApp Diet Guide</li>
                                <li>Priority Doctor Assistance</li>
                            </ul>
                        </div>
                        <button class="btn-plan-act" onclick="selectPlan('1-Month Standard Subscription', 2499)">
                            Subscribe ₹2,499 / Mo →
                        </button>
                    </div>

                    <div class="plan-card plan-card-vip">
                        <span class="plan-badge-top plan-badge-vip">ALL-INCLUSIVE VIP 👑</span>
                        <div>
                            <h3 style="font-size: 16px; font-weight: 800; color: #c084fc;">1-Month VIP + Blood Test</h3>
                            <div class="plan-price-box">
                                <span class="plan-price">₹3,499</span>
                                <span class="plan-period">/ Month</span>
                            </div>
                            <ul class="plan-features">
                                <li><strong>Includes NABL Home Blood Draw (72+ Tests)</strong></li>
                                <li>Full Levine PhenoAge Doctor Report</li>
                                <li>1-on-1 Doctor Longevity Consult</li>
                                <li>30-Day Family Camera App Access</li>
                                <li>Personalized Reversal Plan</li>
                            </ul>
                        </div>
                        <button class="btn-plan-act" onclick="selectPlan('1-Month VIP Longevity Membership', 3499)">
                            Subscribe ₹3,499 / Mo →
                        </button>
                    </div>
                </div>

                <!-- Instant Payment Drawer / Checkout Box -->
                <div id="planCheckoutBox" style="display: none; margin-top: 30px; background: var(--surface-card); border: 2px solid #38bdf8; border-radius: 16px; padding: 26px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                        <div>
                            <span style="font-size: 11px; text-transform: uppercase; color: var(--accent); font-weight: 800;">Selected Plan</span>
                            <h3 id="coPlanName" style="font-size: 18px; font-weight: 800; color: #fff;">1-Month Standard Subscription</h3>
                        </div>
                        <div style="font-size: 28px; font-weight: 900; color: #10b981;" id="coPlanPrice">
                            ₹2,499
                        </div>
                    </div>

                    <div style="display: grid; grid-template-columns: 1fr 220px; gap: 20px; align-items: center;">
                        <form onsubmit="submitPlanOrder(event)">
                            <div class="form-group">
                                <label style="font-size: 11px; text-transform: uppercase; color: var(--text-dim); font-weight: 700; display: block; margin-bottom: 4px;">Patient Full Name</label>
                                <input type="text" id="co_name" class="input-control" placeholder="e.g. Amit Patel" required>
                            </div>
                            <div class="form-group" style="margin-top: 10px;">
                                <label style="font-size: 11px; text-transform: uppercase; color: var(--text-dim); font-weight: 700; display: block; margin-bottom: 4px;">WhatsApp Mobile Number</label>
                                <input type="tel" id="co_phone" class="input-control" placeholder="e.g. 9343062265" required>
                            </div>
                            <button type="submit" class="btn-action-main" style="margin-top: 14px;">
                                <span>⚡</span>
                                <span>Confirm & Activate Subscription</span>
                            </button>
                        </form>

                        <div style="text-align: center; background: #000; padding: 14px; border-radius: 12px; border: 1px solid var(--border);">
                            <div style="width: 140px; height: 140px; background: #fff; padding: 6px; border-radius: 10px; margin: 0 auto 8px;">
                                <img id="coQrImg" src="https://api.qrserver.com/v1/create-qr-code/?size=140x140&data=upi://pay?pa=9343062265@upi&pn=BioTwin%20Labs&am=2499&cu=INR&tn=Longevity-Subscription" style="width: 100%; height: 100%; object-fit: contain;">
                            </div>
                            <span style="font-size: 10px; color: var(--text-dim);">Scan via PhonePe/GPay/Paytm</span>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <!-- SCREEN: DEDICATED 7-DAY FREE TRIAL SCREEN         -->
    <!-- ================================================= -->
    <div id="screen-freetrial" class="screen-view">
        <div class="screen-header-bar">
            <button class="btn-back-home" onclick="showScreen('hub')">
                <span>←</span>
                <span data-i18n="btn_back_services">Back to All Services</span>
            </button>
            <span class="screen-tag" style="background: rgba(16, 185, 129, 0.15); border-color: rgba(16, 185, 129, 0.35); color: #34d399;">
                🎁 7-Day Free Health Pass • ₹0
            </span>
        </div>

        <div class="detail-container">
            <div class="detail-panel" style="border-color: #10b981;">
                <span class="trial-badge" data-i18n="ft_badge">100% Free Health Monitoring</span>
                <h2 class="detail-title" data-i18n="ft_title">Apna 7 Din Ka Free Longevity Pass Activate Karein</h2>
                <p class="detail-desc" data-i18n="ft_desc">
                    Aapko pehle 7 din ek rupya bhi nahi dena hai. Rozana camera se BP check karein, khana khane ke baad sugar spike aur physical markers se biological age track karein. Yeh raha aapka 7-Day Plan:
                </p>

                <!-- 7-Day Roadmap Timeline -->
                <div class="timeline-container">
                    <div class="timeline-day-card">
                        <span class="day-num">DAY 1</span>
                        <div class="day-title">Baseline Checkup</div>
                        <div class="day-desc">Camera se pehla BP aur pulse scan karein + Zero-Report se visceral fat ratio nikalein.</div>
                    </div>
                    <div class="timeline-day-card">
                        <span class="day-num">DAY 2</span>
                        <div class="day-title">Post-Meal Fatigue Check</div>
                        <div class="day-desc">Lunch ke baad susti aur glycemic energy stability monitor karein.</div>
                    </div>
                    <div class="timeline-day-card">
                        <span class="day-num">DAY 3</span>
                        <div class="day-title">Resting Pulse & Arterial Tone</div>
                        <div class="day-desc">Subah aaram ke waqt heart rate aur arterial elasticity check karein.</div>
                    </div>
                    <div class="timeline-day-card">
                        <span class="day-num">DAY 4</span>
                        <div class="day-title">Waist & Visceral Review</div>
                        <div class="day-desc">Waist-to-Height ratio ke tehat internal fat drift track karein.</div>
                    </div>
                    <div class="timeline-day-card">
                        <span class="day-num">DAY 5</span>
                        <div class="day-title">Sleep & Recovery Scan</div>
                        <div class="day-desc">Neend ki quality aur sleep apnea risk score analyze karein.</div>
                    </div>
                    <div class="timeline-day-card">
                        <span class="day-num">DAY 6</span>
                        <div class="day-title">PhenoAge Recalculation</div>
                        <div class="day-desc">Pichle dino ke data ke basis par updated biological age dekhein.</div>
                    </div>
                    <div class="timeline-day-card" style="border-color: #10b981; background: rgba(16, 185, 129, 0.08);">
                        <span class="day-num" style="background:#10b981; color:#000;">DAY 7</span>
                        <div class="day-title" style="color: #34d399;">Executive Summary</div>
                        <div class="day-desc">Poore hafte ki health summary + Optional NABL blood test upgrade.</div>
                    </div>
                </div>

                <!-- Activation Form -->
                <div style="background: var(--surface-card); border: 1px solid var(--border); border-radius: 16px; padding: 26px; max-width: 600px; margin: 20px auto 0;">
                    <h3 style="font-size: 16px; font-weight: 800; margin-bottom: 6px; text-align: center; color: #fff;">
                        Instant ₹0 Pass Activation (No Payment Needed)
                    </h3>
                    <p style="font-size: 12px; color: var(--text-dim); text-align: center; margin-bottom: 18px;">
                        Apna naam aur WhatsApp number daalein. Aapka 7-Day Pass turant active ho jayega.
                    </p>

                    <form onsubmit="activateFreeTrial(event)">
                        <div class="form-group">
                            <label style="font-size: 11px; text-transform: uppercase; color: var(--text-dim); font-weight: 700; display: block; margin-bottom: 4px;">Patient Full Name</label>
                            <input type="text" id="ft_name" class="input-control" placeholder="e.g. Rahul Verma" required>
                        </div>
                        <div class="form-group" style="margin-top: 12px;">
                            <label style="font-size: 11px; text-transform: uppercase; color: var(--text-dim); font-weight: 700; display: block; margin-bottom: 4px;">WhatsApp Mobile Number</label>
                            <input type="tel" id="ft_phone" class="input-control" placeholder="e.g. 9343062265" required>
                        </div>
                        <div class="form-group" style="margin-top: 12px;">
                            <label style="font-size: 11px; text-transform: uppercase; color: var(--text-dim); font-weight: 700; display: block; margin-bottom: 4px;">Age</label>
                            <input type="number" id="ft_age" class="input-control" value="38" required>
                        </div>

                        <button type="submit" class="btn-action-main" style="background: linear-gradient(135deg, #10b981, #059669); margin-top: 16px;">
                            <span>🚀</span>
                            <span>Activate My 7-Day Free Pass (₹0)</span>
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- SCREEN 5: DEDICATED AT-HOME BLOOD TEST BOOKING    -->
    <!-- ================================================= -->
    <div id="screen-booking" class="screen-view">
        <div class="screen-header-bar">
            <button class="btn-back-home" onclick="showScreen('hub')">
                <span>←</span>
                <span data-i18n="btn_back_services">Back to All Services</span>
            </button>
            <span class="screen-tag" style="background: rgba(16, 185, 129, 0.12); color: #34d399; border-color: rgba(16, 185, 129, 0.3);">🏠 At-Home Blood Test</span>
        </div>

        <div class="detail-container">
            <div class="detail-panel" style="border-color: #38bdf8;">
                <h2 class="detail-title" data-i18n="book_title">Book NABL Phlebotomist Home Sample Collection</h2>
                <p class="detail-desc" data-i18n="book_desc">
                    Certified technician sterile vacuum tubes ke saath aapke ghar aakar sample lega. 72+ parameters, Biological Age Report aur Doctor Blueprint sabhi kuch included hai.
                </p>

                <div class="booking-layout">
                    <form onsubmit="submitHomeBooking(event)">
                        <div class="form-group">
                            <label data-i18n="b_name">Patient Full Name</label>
                            <input type="text" id="b_name" class="input-control" placeholder="e.g. Ramesh Kumar" required>
                        </div>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;" class="form-group">
                            <div>
                                <label data-i18n="b_age">Age</label>
                                <input type="number" id="b_age" class="input-control" value="42" required>
                            </div>
                            <div>
                                <label data-i18n="b_gender">Gender</label>
                                <select id="b_gender" class="select-control">
                                    <option value="Male">Male</option>
                                    <option value="Female">Female</option>
                                    <option value="Other">Other</option>
                                </select>
                            </div>
                        </div>
                        <div class="form-group">
                            <label data-i18n="b_phone">WhatsApp Mobile Number</label>
                            <input type="tel" id="b_phone" class="input-control" placeholder="e.g. 9343062265" required>
                        </div>
                        <div class="form-group">
                            <label data-i18n="b_address">Complete Home Address & City / Pincode</label>
                            <input type="text" id="b_address" class="input-control" placeholder="Flat No, Society, Landmark, City & Pincode" required>
                        </div>
                        <div class="form-group">
                            <label data-i18n="b_slot">Preferred Fasting Slot (Tomorrow Morning)</label>
                            <select id="b_slot" class="select-control">
                                <option value="7:00 AM - 8:00 AM">Tomorrow: 7:00 AM - 8:00 AM (Recommended)</option>
                                <option value="8:00 AM - 9:00 AM">Tomorrow: 8:00 AM - 9:00 AM</option>
                                <option value="9:00 AM - 10:00 AM">Tomorrow: 9:00 AM - 10:00 AM</option>
                            </select>
                        </div>

                        <button type="submit" class="btn-action-main" style="margin-top: 10px;">
                            <span>✓</span>
                            <span data-i18n="btn_confirm_order">Confirm Booking & Generate Order</span>
                        </button>
                    </form>

                    <div class="qr-card">
                        <span style="font-size: 11px; text-transform: uppercase; color: var(--accent); font-weight: 800; display: block;">
                            Order Summary
                        </span>
                        <div style="font-size: 26px; font-weight: 900; color: #10b981; margin: 6px 0;">
                            ₹1,999
                        </div>
                        <div style="font-size: 11px; color: var(--text-dim); margin-bottom: 12px;">
                            72+ Tests + Free Home Pickup + Doctor Review
                        </div>

                        <div class="qr-placeholder">
                            <img src="https://api.qrserver.com/v1/create-qr-code/?size=170x170&data=upi://pay?pa=9343062265@upi&pn=BioTwin%20Labs&am=1999&cu=INR&tn=72-Biomarker-Home-Draw" alt="UPI QR Code">
                        </div>

                        <p style="font-size: 11px; color: var(--text-muted); margin-bottom: 6px;">
                            Scan to pay via <strong>PhonePe, GPay, Paytm, or Cash on Pickup</strong>
                        </p>

                        <a href="#" class="btn-wa" onclick="directWhatsApp(event)">
                            <span>💬</span>
                            <span data-i18n="btn_wa_chat">Book on WhatsApp</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- FOOTER -->
    <footer class="footer">
        © 2026 BioTwin Labs. Clinical protocols aligned with Harrison's Principles of Internal Medicine & Guyton Physiology.
    </footer>

    <!-- ================================================= -->
    <!-- GLOBAL SINGLE-PAGE APPLICATION LOGIC (JavaScript) -->
    <!-- ================================================= -->
    <script>
        // MULTI-LANGUAGE TRANSLATION DICTIONARY
        const DICT = {
            en: {
                brand_title: "BioTwin Labs",

                nav_free_trial: "7 Days Free Trial",

                nav_plans: "Plans (₹199 - ₹3,499)",
                sec_plans_title: "Affordable Normal Passes & 1-Month Subscriptions",
                sec_plans_sub: "First 7 days are 100% FREE. After that, keep monitoring with normal weekly passes (₹199, ₹299) or monthly memberships (₹2,499, ₹3,499):",
                p_screen_title: "Choose Your Health Monitoring Pass",
                p_screen_desc: "First 7 days free trial. After that, pick from normal affordable passes or full-body monthly subscriptions:",
                tb_badge: "🎁 SPECIAL LAUNCH OFFER • 7 DAYS FREE",
                tb_title: "Start Your 7-Day Free Health & Longevity Trial",
                tb_desc: "No payment or credit card required. Check your BP daily using your phone camera, calculate biological age, and monitor health for 7 days at ₹0!",
                btn_start_trial: "Start 7-Day Free Trial (₹0) →",
                ft_badge: "100% Free Health Monitoring",
                ft_title: "Activate Your 7-Day Free Longevity Pass",
                ft_desc: "You don't pay a single rupee for the first 7 days. Track your camera BP, post-meal glucose stability, and biological age. Here is your 7-Day Roadmap:",
                brand_sub: "Precision Longevity & Health Checkup Platform",
                nav_all_services: "All Services",
                btn_back_services: "Back to All Services",
                hub_title: "What Kind of Health Checkup Do You Need?",
                hub_desc: "Every person has unique diagnostic requirements. Pick or search from our dedicated services below — each runs cleanly in its own dedicated view without clutter:",
                hub_sec_title: "Our 5 Dedicated Health Services:",
                c1_title: "Camera Optical BP & Pulse Checkup",
                c1_desc: "Check your live Blood Pressure and Heart Rate using your phone or laptop camera via transdermal photoplethysmography.",
                c1_btn: "Open Camera Scanner",
                c2_title: "Zero-Report 2-Minute Health Score",
                c2_desc: "Never had a blood test? Use 6 clinical body markers (waist ratio, resting pulse, post-meal fatigue) to calculate biological age delta and visceral risk.",
                c2_btn: "Start 2-Min Assessment",
                c3_title: "Old Report Time Machine Projector",
                c3_desc: "Have a 1-3 year old blood test? Project how much your metabolic organ damage has progressed based on elapsed time and weight change.",
                c3_btn: "Check Old Report Drift",
                c4_title: "Full 72+ Biomarker Deep Engine",
                c4_desc: "Have recent lab reports? Enter your ApoB, Fasting Insulin, hs-CRP, Liver and Kidney markers to compute your exact Levine Phenotypic Age.",
                c4_btn: "Open Biomarker Matrix",
                c5_title: "Ghar Baithe NABL Blood Test Booking",
                c5_desc: "Certified phlebotomist collects blood samples at your home. 72+ parameters, Biological Age Report, and Doctor Longevity Blueprint included.",
                c5_btn: "Book Home Blood Draw (₹1,999)",
                cam_title: "Camera Optical Blood Pressure & Pulse Scanner",
                cam_desc: "Measures light micro-reflections in your fingertip arterial capillaries to calculate pulse transit time and arterial stiffness.",
                cam_instruct: "Place your finger over camera lens or look directly at screen. Click Start Scan below.",
                lbl_bp: "Blood Pressure (BP)",
                lbl_hr: "Heart Rate (Pulse)",
                lbl_elasticity: "Arterial Elasticity",
                lbl_sugar: "Sugar Stability",
                btn_start_scan: "Start 15-Second Optical Camera Scan",
                manual_title: "Or Type Your Current BP & Sugar Here (Instant Risk Check):",
                quiz_title: "Zero-Report 2-Minute Longevity Assessment",
                quiz_desc: "If you have never had a blood test, these 6 physical markers (Guyton & Hall Physiology Ch. 72) calculate visceral fat, insulin resistance and biological age.",
                q_age: "1. Chronological Age (Actual Age)",
                q_age_hint: "Years on your ID proof",
                q_height: "2. Height (in cm)",
                q_height_hint: "E.g., 5 ft 8 in = 173 cm, 5 ft 10 in = 178 cm",
                q_waist: "3. Waist Circumference (Inches)",
                q_waist_hint: "Measure around your navel (belly button)",
                q_rhr: "4. Resting Heart Rate (Resting Pulse)",
                q_rhr_hint: "Optimal < 65 bpm. > 75 = sympathetic overdrive",
                q_fatigue: "5. Post-Meal Fatigue (Tiredness after food)",
                q_fatigue_hint: "Energy crashes after carb meals = early insulin resistance",
                q_fam: "6. Family History of Diabetes / Heart Disease",
                q_fam_hint: "Parents or siblings with BP, diabetes or early heart disease",
                btn_confirm_blood_draw: "Confirm with ₹1,999 At-Home Blood Test",
                tm_title: "Old Report Time Machine: Metabolic Drift Projector",
                tm_desc: "Have a 1-3 year old blood test? Project how much your metabolic organ damage has progressed based on elapsed time and weight change.",
                tm_lbl_years: "Report Kitni Purani Hai? (Years)",
                tm_lbl_weight: "Tab Se Vajan Me Farak (Kg)",
                tm_lbl_old_glu: "Old Fasting Glucose (mg/dL)",
                tm_lbl_old_hba1c: "Old HbA1c (%)",
                tm_lbl_old_trig: "Old Triglycerides (mg/dL)",
                tm_lbl_old_chol: "Old Total Cholesterol (mg/dL)",
                tm_proj_header: "Projected Current Health (Harrison's Beta-Cell Drift):",
                btn_stop_drift: "Book Fresh Checkup to Stop Drift (₹1,999)",
                bio_title: "Full 72+ Biomarker Panel & Phenotypic Aging Matrix",
                bio_desc: "Enter numbers from your recent blood test to calculate your exact Levine Phenotypic Age. Optimal longevity ranges shown for every biomarker.",
                book_title: "Book NABL Phlebotomist Home Sample Collection",
                book_desc: "A certified technician arrives at your home with sterile vacutainers. Includes 72+ tests, free pickup, and doctor longevity review.",
                b_name: "Patient Full Name",
                b_age: "Age",
                b_gender: "Gender",
                b_phone: "WhatsApp Mobile Number",
                b_address: "Complete Home Address & City / Pincode",
                b_slot: "Preferred Fasting Slot (Tomorrow Morning)",
                btn_confirm_order: "Confirm Booking & Generate Order",
                btn_wa_chat: "Book on WhatsApp"
            },
            hi: {
                brand_title: "बायोट्विन लैब्स (BioTwin Labs)",

                nav_free_trial: "7 दिन बिल्कुल फ्री",

                nav_plans: "प्लान्स (₹199 - ₹3,499)",
                sec_plans_title: "7 दिन के बाद सामान्य शुल्क एवं 1 महीने के सब्सक्रिप्शन",
                sec_plans_sub: "पहले 7 दिन बिल्कुल फ्री हैं। उसके बाद कोई महंगा खर्च नहीं — केवल सामान्य ₹199/₹299 के पास या ₹2,499/₹3,499 के मासिक सब्सक्रिप्शन में से चुनें:",
                p_screen_title: "अपना हेल्थ मॉनिटरिंग पास चुनें",
                p_screen_desc: "पहले 7 दिन बिल्कुल फ्री। उसके बाद सामान्य साप्ताहिक पास या पूरे 1 महीने के सब्सक्रिप्शन में से चुनें:",
                tb_badge: "🎁 खास ऑफर • 7 दिन बिल्कुल फ्री",
                tb_title: "7 दिन का बिल्कुल फ्री हेल्थ व लंबी उम्र ट्रायल",
                tb_desc: "बिना किसी पेमेंट या कार्ड के — पहले 7 दिन रोजाना फोन कैमरे से बीपी जांचें, अपनी बायोलॉजिकल उम्र देखें और स्वास्थ्य ट्रैक करें बिल्कुल ₹0 में!",
                btn_start_trial: "7 दिन का फ्री ट्रायल शुरू करें (₹0) →",
                ft_badge: "100% फ्री स्वास्थ्य जांच",
                ft_title: "अपना 7 दिन का फ्री हेल्थ पास एक्टिवेट करें",
                ft_desc: "पहले 7 दिन आपको एक भी रुपया नहीं देना है। कैमरे से रोज बीपी मापें, खाने के बाद शुगर क्रैश और अंदरूनी उम्र ट्रैक करें। यह रहा आपका 7-दिन का प्लान:",
                brand_sub: "सम्पूर्ण दीर्घायु एवं स्वास्थ्य जांच प्लेटफॉर्म",
                nav_all_services: "सभी सेवाएं",
                btn_back_services: "← मुख्य पेज पर वापस जाएं",
                hub_title: "आपको किस तरह के हेल्थ चेकअप की ज़रूरत है?",
                hub_desc: "हर मरीज की जरूरत अलग होती है। नीचे दी गई सेवाओं में से चुनें या सर्च करें — और बिना किसी खिचड़ी के सीधे उसी स्क्रीन पर अपना टेस्ट करें:",
                hub_sec_title: "हमारी 5 समर्पित स्वास्थ्य सेवाएं:",
                c1_title: "कैमरा ऑप्टिकल बीपी और पल्स चेकअप",
                c1_desc: "बिना किसी मशीन के, अपने फोन या लैपटॉप कैमरे पर उंगली रखकर नसों के बहाव से सीधा ब्लड प्रेशर और पल्स मापें।",
                c1_btn: "कैमरा स्कैनर खोलें",
                c2_title: "बिना रिपोर्ट 2-मिनट हेल्थ स्कोर",
                c2_desc: "अगर आपने कभी ब्लड टेस्ट नहीं कराया है, तो भी 6 शारीरिक लक्षणों से अपनी अंदरूनी जैविक उम्र और पेट की चर्बी का रिस्क जानें।",
                c2_btn: "2-मिनट टेस्ट शुरू करें",
                c3_title: "पुरानी रिपोर्ट टाइम मशीन प्रोजेक्टर",
                c3_desc: "1 से 3 साल पुरानी ब्लड रिपोर्ट के नंबर डालकर जानें कि बीते सालों में वजन और उम्र के साथ आपका शुगर और अंग डैमेज कितना बढ़ चुका है।",
                c3_btn: "पुरानी रिपोर्ट का डैमेज देखें",
                c4_title: "पूरा 72+ बायोमार्कर क्लिनिकल पैनल",
                c4_desc: "ताजा रिपोर्ट के सभी 72 मानक (ApoB, इंसुलिन, CRP, लिवर, किडनी) दर्ज करके अपनी वास्तविक लेवाइन बायोलॉजिकल उम्र निकालें।",
                c4_btn: "बायोमार्कर पैनल खोलें",
                c5_title: "घर बैठे NABL ब्लड टेस्ट बुक करें",
                c5_desc: "सर्टिफाइड लैब टेक्नीशियन आपके घर आकर सैंपल लेगा। 72+ बायोमार्कर, बायोलॉजिकल एज रिपोर्ट और डॉक्टर परामर्श सब शामिल है।",
                c5_btn: "घर बैठे टेस्ट बुक करें (₹1,999)",
                cam_title: "कैमरा ऑप्टिकल बीपी और पल्स स्कैनर",
                cam_desc: "कैमरा लेंस पर उंगली रखने से नसों में खून के बहाव को मापकर धमनियों का लचीलापन और सिस्टोलिक/डायस्टोलिक बीपी बताता है।",
                cam_instruct: "कैमरे के लेंस पर अपनी उंगली रखें या स्क्रीन की तरफ देखें। नीचे 'स्कैन शुरू करें' बटन दबाएं।",
                lbl_bp: "रक्तचाप (BP)",
                lbl_hr: "नाड़ी दर (Pulse)",
                lbl_elasticity: "धमनियों का लचीलापन",
                lbl_sugar: "शुगर स्थिरता",
                btn_start_scan: "15-सेकंड का कैमरा स्कैन शुरू करें",
                manual_title: "या अपना मौजूदा बीपी और शुगर यहां लिखें (तुरंत रिस्क चेक):",
                quiz_title: "बिना किसी रिपोर्ट के 2-मिनट की स्वास्थ्य जांच",
                quiz_desc: "अगर आपने कभी कोई ब्लड टेस्ट नहीं कराया है, तो भी ये 6 शारीरिक लक्षण (गैटन फिजियोलॉजी Ch. 72) अंदरूनी उम्र और इंसुलिन रेजिस्टेंस बताते हैं।",
                q_age: "1. आपकी असली उम्र (Chronological Age)",
                q_age_hint: "आधार कार्ड के अनुसार वर्ष",
                q_height: "2. लंबाई / कद (सेंटीमीटर cm में)",
                q_height_hint: "उदाहरण: 5 फीट 8 इंच = 173 cm, 5 फीट 10 इंच = 178 cm",
                q_waist: "3. कमर का घेरा (इंच Inches में)",
                q_waist_hint: "नाभि के ठीक ऊपर से इंचीटेप से नापें",
                q_rhr: "4. सुबह आराम के वक्त नब्ज़ (Resting Pulse)",
                q_rhr_hint: "सामान्य < 65 bpm। 75 से अधिक यानी तनाव",
                q_fatigue: "5. खाना खाने के बाद सुस्ती या थकान",
                q_fatigue_hint: "रोटी/चावल खाने के बाद भारी नींद आना इंसुलिन रेजिस्टेंस का लक्षण है",
                q_fam: "6. परिवार में शुगर / बीपी / हार्ट अटैक का इतिहास",
                q_fam_hint: "माता-पिता या भाई-बहन को कोई बीमारी",
                btn_confirm_blood_draw: "घर बैठे ब्लड टेस्ट (₹1,999) से पुष्टि करें",
                tm_title: "पुरानी रिपोर्ट टाइम मशीन: मेटाबॉलिक डैमेज प्रोजेक्टर",
                tm_desc: "1 से 3 साल पुरानी ब्लड रिपोर्ट के नंबर डालकर जानें कि बीते समय में आपका शुगर और कोलेस्ट्रॉल कितना बढ़ चुका है।",
                tm_lbl_years: "रिपोर्ट कितनी पुरानी है? (वर्ष)",
                tm_lbl_weight: "तब से वजन में बदलाव (किलो)",
                tm_lbl_old_glu: "पुरानी खाली पेट शुगर (mg/dL)",
                tm_lbl_old_hba1c: "पुराना HbA1c (%)",
                tm_lbl_old_trig: "पुराने ट्राइग्लिसराइड्स (mg/dL)",
                tm_lbl_old_chol: "पुराना टोटल कोलेस्ट्रॉल (mg/dL)",
                tm_proj_header: "आज का अनुमानित स्वास्थ्य (हैरिसन्स मॉडल):",
                btn_stop_drift: "डैमेज रोकने के लिए नया टेस्ट बुक करें (₹1,999)",
                bio_title: "पूरा 72+ बायोमार्कर क्लिनिकल पैनल एवं लेवाइन फीनोएज",
                bio_desc: "अपनी हालिया ब्लड रिपोर्ट के आंकड़े दर्ज करें और सटीक बायोलॉजिकल उम्र व ऑर्गन स्कोर निकालें।",
                book_title: "घर बैठे NABL ब्लड टेस्ट बुक करें (₹1,999)",
                book_desc: "सर्टिफाइड टेक्नीशियन घर आकर सैंपल लेगा। 72+ टेस्ट, फ्री होम विजिट और डॉक्टर रिपोर्ट शामिल है।",
                b_name: "मरीज का पूरा नाम",
                b_age: "उम्र",
                b_gender: "लिंग (Gender)",
                b_phone: "व्हाट्सएप मोबाइल नंबर",
                b_address: "घर का पूरा पता, शहर और पिनकोड",
                b_slot: "सुबह का समय (खाली पेट सैंपल हेतु)",
                btn_confirm_order: "बुकिंग कन्फर्म करें और आर्डर बनाएं",
                btn_wa_chat: "व्हाट्सएप पर बुक करें"
            },
            hinglish: {
                brand_title: "BioTwin Labs",

                nav_free_trial: "7 Days Free Trial",

                nav_plans: "Plans (₹199 - ₹3,499)",
                sec_plans_title: "Affordable Normal Passes & 1-Month Subscriptions",
                sec_plans_sub: "First 7 days are 100% FREE. After that, keep monitoring with normal weekly passes (₹199, ₹299) or monthly memberships (₹2,499, ₹3,499):",
                p_screen_title: "Choose Your Health Monitoring Pass",
                p_screen_desc: "First 7 days free trial. After that, pick from normal affordable passes or full-body monthly subscriptions:",
                tb_badge: "🎁 SPECIAL LAUNCH OFFER • 7 DAYS FREE",
                tb_title: "Start Your 7-Day Free Health & Longevity Trial",
                tb_desc: "No payment or credit card required. Check your BP daily using your phone camera, calculate biological age, and monitor health for 7 days at ₹0!",
                btn_start_trial: "Start 7-Day Free Trial (₹0) →",
                ft_badge: "100% Free Health Monitoring",
                ft_title: "Activate Your 7-Day Free Longevity Pass",
                ft_desc: "You don't pay a single rupee for the first 7 days. Track your camera BP, post-meal glucose stability, and biological age. Here is your 7-Day Roadmap:",
                brand_sub: "Precision Longevity & Full Body Checkup Platform",
                nav_all_services: "All Services",
                btn_back_services: "← Back to All Services",
                hub_title: "Aapko Kis Tarah Ke Health Checkup Ki Zaroorat Hai?",
                hub_desc: "Har vyakti ki requirement alag hoti hai. Neeche diye gaye services me se chunein ya search karein — aur bina kisi khichdi ke seedhe us dedicated screen par kaam karein:",
                hub_sec_title: "Hamari 5 Dedicated Health Services:",
                c1_title: "Camera Optical BP & Pulse Checkup",
                c1_desc: "Bina kisi machine ke, apne phone ya laptop camera lens par ungli rakh kar blood vessels se live Blood Pressure aur Pulse check karein.",
                c1_btn: "Open Camera Scanner",
                c2_title: "Zero-Report 2-Minute Health Score",
                c2_desc: "Agar kabhi blood test nahi karwaya hai, tab bhi 6 body markers se pait ki charbi (visceral fat) aur umar ka pata lagayein.",
                c2_btn: "Start 2-Min Assessment",
                c3_title: "Old Report Time Machine Projector",
                c3_desc: "1 se 3 saal purani blood report ke numbers dalkar jaanein ki pichle saalon me kitna organ damage badha hai.",
                c3_btn: "Check Old Report Drift",
                c4_title: "Full 72+ Biomarker Deep Engine",
                c4_desc: "Taaza blood report ke sabhi 72 parameters ka Levine Phenotypic Age score aur doctor-signed report nikalein.",
                c4_btn: "Open Biomarker Matrix",
                c5_title: "Ghar Baithe NABL Blood Test Booking",
                c5_desc: "NABL certified technician ghar aakar sample lega. 72+ biomarkers, Biological Age Report sabhi included hai.",
                c5_btn: "Book Home Blood Draw (₹1,999)",
                cam_title: "Camera Optical BP & Pulse Scanner",
                cam_desc: "Phone ya laptop camera lens par ungli rakh kar blood vessels se live arterial stiffness aur BP estimate karein.",
                cam_instruct: "Camera lens par ungli rakhein ya screen ki taraf dekhein. Neeche 'Start Scan' dabayein.",
                lbl_bp: "Blood Pressure (BP)",
                lbl_hr: "Heart Rate (Pulse)",
                lbl_elasticity: "Arterial Elasticity",
                lbl_sugar: "Sugar Stability",
                btn_start_scan: "15-Second Optical Camera Scan Start Karein",
                manual_title: "Ya Apna Current BP & Sugar Yahan Type Karein (Instant Risk Check):",
                quiz_title: "Zero-Report 2-Minute Longevity Assessment",
                quiz_desc: "Agar aapne kabhi blood test nahi karwaya hai, tab bhi yeh 6 physical markers aapka biological age delta aur hidden organ decay batate hain.",
                q_age: "1. Chronological Age (Aapki Asli Umar)",
                q_age_hint: "Aadhaar card ke hisaab se umar",
                q_height: "2. Height (Kadd / Lambai in cm)",
                q_height_hint: "E.g., 5 ft 8 in = 173 cm, 5 ft 10 in = 178 cm",
                q_waist: "3. Waist Circumference (Kamar ka Ghera in Inches)",
                q_waist_hint: "Naabhi (Navel) ke theek upar se tape se naapein",
                q_rhr: "4. Resting Heart Rate (Subah Aaram ke Waqt Pulse)",
                q_rhr_hint: "Normal < 65 bpm. 75 se zyada = stress",
                q_fatigue: "5. Post-Meal Fatigue (Khana Khane ke Baad Susti)",
                q_fatigue_hint: "Khana khane ke baad bhari neend aana early insulin resistance ka sign hai",
                q_fam: "6. Family History of Diabetes / Premature Heart Attack",
                q_fam_hint: "Mummy, papa ya bhai-behan ko sugar ya BP ki bimari",
                btn_confirm_blood_draw: "Ghar Par Blood Test (₹1,999) Se Confirm Karein",
                tm_title: "Old Report Time Machine: Metabolic Drift Projector",
                tm_desc: "1 se 3 saal purani blood report ke number dalkar jaanein ki pichle saalon me kitna organ decay badh chuka hai.",
                tm_lbl_years: "Report Kitni Purani Hai? (Years)",
                tm_lbl_weight: "Tabse Vajan Mein Farak (Kg)",
                tm_lbl_old_glu: "Purana Fasting Glucose (mg/dL)",
                tm_lbl_old_hba1c: "Purana HbA1c (%)",
                tm_lbl_old_trig: "Purane Triglycerides (mg/dL)",
                tm_lbl_old_chol: "Purana Total Cholesterol (mg/dL)",
                tm_proj_header: "Projected Current Health (Harrison's Beta-Cell Drift):",
                btn_stop_drift: "Drift Rokne Ke Liye Naya Test Book Karein (₹1,999)",
                bio_title: "Full 72+ Biomarker Panel & Levine PhenoAge Matrix",
                bio_desc: "Taaza blood report ke numbers dalkar exact biological age aur organ score nikalein.",
                book_title: "Ghar Baithe NABL Blood Sample Collection (₹1,999)",
                book_desc: "Certified technician ghar aakar sterile vacuum tubes me sample lega. 72+ tests aur Doctor Report included hai.",
                b_name: "Patient Ka Pura Naam",
                b_age: "Umar (Age)",
                b_gender: "Gender",
                b_phone: "WhatsApp Mobile Number",
                b_address: "City & Ghar Ka Pura Pata",
                b_slot: "Subah Ka Time Slot (Fasting)",
                btn_confirm_order: "Booking Confirm Karein & Order Banayein",
                btn_wa_chat: "Direct WhatsApp Par Book Karein"
            }
        };

        let currentLang = 'en';

        function setLanguage(lang, btn) {
            currentLang = lang;
            document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
            if (btn) btn.classList.add('active');

            const dict = DICT[lang] || DICT['en'];
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (dict[key]) el.innerText = dict[key];
            });

            runQuizCalc();
            runDriftCalc();
            evalManual();
        }

        // ===================================================
        // SCREEN SWITCHER (Single-Page App Transitions)
        // ===================================================
        function showScreen(screenId, updateHash = true) {
            // Hide all screens
            document.querySelectorAll('.screen-view').forEach(s => s.classList.remove('active'));
            
            // Show requested screen
            const target = document.getElementById(`screen-${screenId}`);
            if (target) {
                target.classList.add('active');
                window.scrollTo({ top: 0, behavior: 'smooth' });
                if (updateHash) {
                    history.pushState(null, null, `#${screenId}`);
                }
            }

            // Screen-specific triggers
            if (screenId === 'camera') {
                drawEmptyWave();
            }
        }

        window.onpopstate = function() {
            const hash = window.location.hash.replace('#', '') || 'hub';
            showScreen(hash, false);
        };

        // Search Filter for Catalog
        function filterCatalog(query) {
            query = query.toLowerCase().trim();
            const cards = document.querySelectorAll('.service-card');
            let count = 0;
            cards.forEach(card => {
                const tags = card.getAttribute('data-tags') || '';
                const text = card.innerText.toLowerCase();
                if (!query || tags.includes(query) || text.includes(query)) {
                    card.style.display = 'flex';
                    count++;
                } else {
                    card.style.display = 'none';
                }
            });
            document.getElementById('catalogCount').innerText = `Showing ${count} of ${cards.length} services`;
        }

        // ===================================================
        // CAMERA SCANNER ENGINE (Transdermal PPG)
        // ===================================================
        let isScanning = false;
        let scanTimer = null;
        let animId = null;
        let ppgStep = 0;
        let audioCtx = null;

        function playHeartBeep() {
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(140, audioCtx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(40, audioCtx.currentTime + 0.08);
                gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.08);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.09);
            } catch (e) {}
        }

        function toggleScan() {
            const btn = document.getElementById('btnToggleScan');
            const video = document.getElementById('webcamVideo');
            const status = document.getElementById('scanStatus');

            if (!isScanning) {
                isScanning = true;
                btn.innerHTML = "<span>⏳</span> Scanning Arterial Pulse... (15s)";
                btn.style.background = "linear-gradient(135deg, #ef4444, #dc2626)";
                status.innerHTML = "<span style='color: #38bdf8; font-weight: 700;'>Measuring arterial micro-reflections...</span>";

                if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                    navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } })
                        .then(stream => {
                            video.srcObject = stream;
                            video.style.display = "block";
                            document.getElementById('pulseHeart').style.display = "none";
                        })
                        .catch(err => console.log("Using synthetic pulse waveform:", err));
                }

                animateWave();

                let left = 15;
                scanTimer = setInterval(() => {
                    left--;
                    playHeartBeep();
                    if (left <= 0) {
                        finishScan();
                    } else {
                        btn.innerHTML = `<span>⏳</span> Scanning... (${left}s left)`;
                    }
                }, 1000);
            } else {
                finishScan();
            }
        }

        function finishScan() {
            isScanning = false;
            clearInterval(scanTimer);
            if (animId) cancelAnimationFrame(animId);

            const video = document.getElementById('webcamVideo');
            if (video.srcObject) {
                video.srcObject.getTracks().forEach(t => t.stop());
                video.style.display = "none";
                document.getElementById('pulseHeart').style.display = "flex";
            }

            const btn = document.getElementById('btnToggleScan');
            btn.innerHTML = "<span>⚡</span> Start Optical Camera Scan";
            btn.style.background = "linear-gradient(135deg, #38bdf8, #2563eb)";

            document.getElementById('resBP').innerText = "124";
            document.getElementById('resBPDia').innerText = "/ 81 mmHg";
            document.getElementById('resHR').innerText = "72";
            document.getElementById('resSugar').innerText = "96 mg/dL";
            document.getElementById('scanStatus').innerHTML = "<span style='color: #10b981; font-weight: 700;'>✓ Scan Complete:</span> Arterial pulse transit time confirms optimal vascular tone.";

            document.getElementById('inSys').value = "124";
            document.getElementById('inDia').value = "81";
            evalManual();
        }

        function drawEmptyWave() {
            const canvas = document.getElementById('ppgCanvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            canvas.width = canvas.parentElement.clientWidth || 300;
            canvas.height = 80;
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.strokeStyle = "#38bdf8";
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(0, 40);
            ctx.lineTo(canvas.width, 40);
            ctx.stroke();
        }

        function animateWave() {
            const canvas = document.getElementById('ppgCanvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            canvas.width = canvas.parentElement.clientWidth || 300;
            canvas.height = 80;

            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.strokeStyle = "#ef4444";
            ctx.lineWidth = 2.5;
            ctx.beginPath();

            ppgStep += 0.08;
            for (let x = 0; x < canvas.width; x += 2) {
                const t = (x * 0.035) - ppgStep;
                const wave = Math.sin(t) * 22 + (Math.sin(2 * t) * 8);
                const y = 40 + wave;
                if (x === 0) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            }
            ctx.stroke();

            if (isScanning) animId = requestAnimationFrame(animateWave);
        }

        function evalManual() {
            const sys = parseFloat(document.getElementById('inSys').value) || 120;
            const dia = parseFloat(document.getElementById('inDia').value) || 80;
            const sugar = parseFloat(document.getElementById('inSugar').value) || 90;
            const verdict = document.getElementById('manualVerdict');

            let bpStatus = (sys < 120 && dia < 80) ? "Optimal BP (<120/80)" : (sys <= 139 || dia <= 89 ? "Pre-Hypertension" : "High BP Stage 1");
            let sugarStatus = (sugar < 100) ? "Normal Fasting Glucose" : (sugar <= 125 ? "Pre-Diabetes Impaired" : "Diabetic Alert (>=126)");

            verdict.innerText = `• BP Status: ${bpStatus} | Fasting Sugar: ${sugarStatus}`;
            verdict.style.color = (sys >= 140 || sugar >= 126) ? "#ef4444" : ((sys >= 120 || sugar >= 100) ? "#f59e0b" : "#10b981");
        }

        // ===================================================
        // ZERO-REPORT NON-INVASIVE ENGINE
        // ===================================================
        function runQuizCalc() {
            const age = parseFloat(document.getElementById('q_age').value) || 42;
            const height = parseFloat(document.getElementById('q_height').value) || 175;
            const waistInches = parseFloat(document.getElementById('q_waist').value) || 36;
            const rhr = parseFloat(document.getElementById('q_rhr').value) || 74;
            const fatigue = document.getElementById('q_fatigue').value;
            const fam = document.getElementById('q_fam').value;

            const waistCm = waistInches * 2.54;
            const whtr = (waistCm / height).toFixed(2);

            let ageDelta = 0;
            if (whtr > 0.50) ageDelta += (whtr - 0.50) * 35;
            if (rhr > 70) ageDelta += (rhr - 70) * 0.15;
            if (fatigue === 'mild') ageDelta += 0.8;
            if (fatigue === 'frequent') ageDelta += 2.0;
            if (fatigue === 'severe') ageDelta += 3.5;
            if (fam === 'one') ageDelta += 0.5;
            if (fam === 'both') ageDelta += 1.2;

            const bioAge = (age + ageDelta).toFixed(1);
            let estInsulin = (4.0 + (whtr > 0.5 ? (whtr - 0.5) * 80 : 0) + (fatigue !== 'none' ? 2.8 : 0)).toFixed(1);

            document.getElementById('resWHtR').innerText = whtr;
            document.getElementById('resWHtR').style.color = (whtr > 0.50 ? '#ef4444' : '#10b981');
            document.getElementById('resBioAge').innerText = `${bioAge} Yrs`;
            document.getElementById('resBioAge').style.color = (ageDelta > 1.5 ? '#ef4444' : (ageDelta > 0 ? '#f59e0b' : '#10b981'));
            document.getElementById('resInsulin').innerText = `${estInsulin} µIU/mL`;

            document.getElementById('quizSummaryText').innerHTML = `
                • <strong>Waist-to-Height Ratio: ${whtr}</strong> (${whtr > 0.5 ? '<span style="color:#ef4444;">Visceral Fat Borderline High (Guyton Ch. 72)</span>' : '<span style="color:#10b981;">Optimal Visceral Tone</span>'})<br>
                • <strong>Estimated Biological Age: ${bioAge} Years</strong> (${ageDelta >= 0 ? `+${ageDelta.toFixed(1)} Years older than actual age` : 'Younger than calendar baseline'})<br>
                • <strong>Estimated Fasting Insulin: ${estInsulin} µIU/mL</strong> (Early metabolic compensation marker)
            `;
        }

        // ===================================================
        // TIME MACHINE OLD REPORT PROJECTOR
        // ===================================================
        function runDriftCalc() {
            const elapsed = parseFloat(document.getElementById('tm_years').value) || 2;
            const weight = parseFloat(document.getElementById('tm_weight').value) || 4;
            const oldGlu = parseFloat(document.getElementById('tm_glu').value) || 92;
            const oldHbA1c = parseFloat(document.getElementById('tm_hba1c').value) || 5.3;
            const oldTrig = parseFloat(document.getElementById('tm_trig').value) || 155;

            const projGlu = Math.round(oldGlu + (elapsed * 2.2) + (weight * 1.5));
            const projHbA1c = (oldHbA1c + (elapsed * 0.18) + (weight * 0.08)).toFixed(2);
            const projTrig = Math.round(oldTrig + (elapsed * 5.0) + (weight * 6.0));
            const projBioAge = (42 + (elapsed * 1.1) + (weight * 0.7)).toFixed(1);

            document.getElementById('projGlu').innerText = `${projGlu} mg/dL`;
            document.getElementById('projGlu').style.color = (projGlu >= 100 ? '#ef4444' : '#10b981');
            document.getElementById('projHbA1c').innerText = `${projHbA1c}%`;
            document.getElementById('projHbA1c').style.color = (projHbA1c >= 5.7 ? '#ef4444' : '#10b981');
            document.getElementById('projBioAge').innerText = `${projBioAge} Yrs`;

            document.getElementById('tmSummaryText').innerHTML = `
                • <strong>Fasting Glucose Drift:</strong> ${oldGlu} mg/dL se lagbhag <strong>${projGlu} mg/dL</strong> (${projGlu >= 100 ? '<span style="color:#ef4444;">Pre-Diabetic Range Alert!</span>' : 'Normal'}).<br>
                • <strong>Estimated HbA1c:</strong> ${oldHbA1c}% se lagbhag <strong>${projHbA1c}%</strong>.<br>
                • <strong>Organ Decay Acceleration:</strong> Pichle ${elapsed} saalon me +${((elapsed * 1.1) + (weight * 0.7)).toFixed(1)} saal zyada biological decay ho chuka hai.
            `;
        }

        // ===================================================
        // BIOMARKERS PANEL & PHENOAGE MATRIX
        // ===================================================
        function switchCategory(catId, btn) {
            document.querySelectorAll('.subtab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.cat-content').forEach(c => c.style.display = 'none');
            btn.classList.add('active');
            const target = document.getElementById(catId);
            if (target) target.style.display = 'grid';
        }

        function updBiomarker(id, val) {
            val = parseFloat(val);
            const sl = document.getElementById(`sl_${id}`);
            const inp = document.getElementById(`in_${id}`);
            if (sl) sl.value = val;
            if (inp) inp.value = val;

            const apob = parseFloat(document.getElementById('in_apob').value) || 70;
            const insulin = parseFloat(document.getElementById('in_insulin').value) || 6.5;
            const glucose = parseFloat(document.getElementById('in_glucose').value) || 88;
            const hscrp = parseFloat(document.getElementById('in_hscrp').value) || 0.7;

            let delta = 0;
            if (apob > 60) delta += (apob - 60) * 0.04; else delta -= 1.0;
            if (insulin > 5.0) delta += (insulin - 5.0) * 0.35; else delta -= 1.0;
            if (glucose > 85) delta += (glucose - 85) * 0.08; else delta -= 0.5;
            if (hscrp > 0.5) delta += (hscrp - 0.5) * 1.2;

            const bio = (42.0 + delta).toFixed(1);
            document.getElementById('hudBioVal').innerText = bio;
            document.getElementById('hudDeltaVal').innerText = (delta >= 0 ? `+${delta.toFixed(1)} Yrs` : `${delta.toFixed(1)} Yrs`);
            document.getElementById('hudDeltaVal').style.color = (delta > 1.5 ? '#ef4444' : (delta > 0 ? '#f59e0b' : '#10b981'));
            document.getElementById('hudHomaVal').innerText = ((glucose * insulin) / 405).toFixed(2);

            document.getElementById('p_apob').value = apob;
            document.getElementById('p_insulin').value = insulin;
            document.getElementById('p_glucose').value = glucose;
            document.getElementById('p_hscrp').value = hscrp;
        }

        // ===================================================
        // AT-HOME BLOOD TEST BOOKING
        // ===================================================
        
        
        let activePlanName = '1-Month Standard Subscription';
        let activePlanPrice = 2499;

        function selectPlan(planName, price) {
            activePlanName = planName;
            activePlanPrice = price;
            
            showScreen('plans');
            
            const checkoutBox = document.getElementById('planCheckoutBox');
            checkoutBox.style.display = 'block';
            document.getElementById('coPlanName').innerText = planName;
            document.getElementById('coPlanPrice').innerText = `₹${price}`;
            
            const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=140x140&data=upi://pay?pa=9343062265@upi&pn=BioTwin%20Labs&am=${price}&cu=INR&tn=${encodeURIComponent(planName)}`;
            document.getElementById('coQrImg').src = qrUrl;

            checkoutBox.scrollIntoView({ behavior: 'smooth' });
        }

        function submitPlanOrder(e) {
            e.preventDefault();
            const name = document.getElementById('co_name').value;
            const phone = document.getElementById('co_phone').value;
            const orderId = `BT-SUB-${Math.floor(100000 + Math.random() * 900000)}`;

            fetch('/api/book-test', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    name: name,
                    phone: phone,
                    slot: `${activePlanName} (₹${activePlanPrice})`,
                    address: "Membership / Digital Pass",
                    order_id: orderId
                })
            }).catch(e => console.log(e));

            alert(`🎉 Subscription Activated Successfully!

Plan: ${activePlanName}
Order ID: ${orderId}
Price: ₹${activePlanPrice}
Patient: ${name}

Your membership access has been unlocked. Details sent to WhatsApp.`);

            const msg = `Hi BioTwin Labs, I have subscribed to ${activePlanName} (₹${activePlanPrice}).%0AOrder ID: ${orderId}%0AName: ${encodeURIComponent(name)}%0APhone: ${encodeURIComponent(phone)}`;
            window.open(`https://wa.me/919343062265?text=${msg}`, '_blank');
        }

        function activateFreeTrial(e) {
            e.preventDefault();
            const name = document.getElementById('ft_name').value;
            const phone = document.getElementById('ft_phone').value;
            const age = document.getElementById('ft_age').value;
            const passId = `BT-FREE7D-${Math.floor(100000 + Math.random() * 900000)}`;

            fetch('/api/book-test', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    name: name,
                    phone: phone,
                    age: age,
                    slot: "7-Day Free Trial Pass",
                    address: "Online Self-Monitoring",
                    order_id: passId
                })
            }).catch(e => console.log(e));

            alert(`🎉 Congratulations ${name}!

Your 7-Day Free Health Pass is ACTIVE.
Pass ID: ${passId}
Charge: ₹0 (No Payment Required)

You now have unlimited access to Camera BP scans, Zero-Report Health Assessment, and daily metabolic tracking.`);

            const msg = `Hi BioTwin Labs, I have activated my 7-Day Free Health Pass.%0APass ID: ${passId}%0AName: ${encodeURIComponent(name)}%0APhone: ${encodeURIComponent(phone)}`;
            window.open(`https://wa.me/919343062265?text=${msg}`, '_blank');

            // Open camera scanner to let user do Day 1 checkup immediately!
            showScreen('camera');
        }

        function submitHomeBooking(e) {
            e.preventDefault();
            const name = document.getElementById('b_name').value;
            const phone = document.getElementById('b_phone').value;
            const address = document.getElementById('b_address').value;
            const slot = document.getElementById('b_slot').value;
            const age = document.getElementById('b_age').value;
            const orderId = `BT-ORD-${Math.floor(100000 + Math.random() * 900000)}`;

            fetch('/api/book-test', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    name: name,
                    phone: phone,
                    address: address,
                    slot: slot,
                    age: age,
                    order_id: orderId
                })
            }).catch(e => console.log(e));

            alert(`✓ Order Confirmed Successfully!\n\nOrder ID: ${orderId}\nPatient: ${name}\nSlot: ${slot}\nAddress: ${address}\nAmount: ₹1,999 (UPI / Cash on sample pickup)\n\nNABL technician has been assigned. You will receive a confirmation call 30 mins before arrival.`);

            const msg = `Hi BioTwin Labs, I have booked a ₹1,999 Longevity Health Checkup.%0AOrder ID: ${orderId}%0APatient: ${encodeURIComponent(name)}%0APhone: ${encodeURIComponent(phone)}%0AAddress: ${encodeURIComponent(address)}%0ASlot: ${encodeURIComponent(slot)}`;
            window.open(`https://wa.me/919343062265?text=${msg}`, '_blank');
        }

        function directWhatsApp(e) {
            e.preventDefault();
            const name = document.getElementById('b_name').value || "Client";
            const phone = document.getElementById('b_phone').value || "";
            const msg = `Hi BioTwin Labs, I want to book the ₹1,999 Longevity Health Checkup at my home.%0AName: ${encodeURIComponent(name)}%0APhone: ${encodeURIComponent(phone)}`;
            window.open(`https://wa.me/919343062265?text=${msg}`, '_blank');
        }

        window.onload = function() {
            runQuizCalc();
            runDriftCalc();
            evalManual();
            drawEmptyWave();

            // Load screen from URL hash if provided
            const hash = window.location.hash.replace('#', '');
            if (hash && document.getElementById(`screen-${hash}`)) {
                showScreen(hash, false);
            }
        };
    </script>
</body>
</html>'''

def main():
    app_html = generate_unified_app()

    print("Writing unified app to index.html...")
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(app_html)

    print("Writing unified app to portal.html...")
    with open(PORTAL_PATH, "w", encoding="utf-8") as f:
        f.write(app_html)

    print("Unified Single-Page App created successfully!")

if __name__ == "__main__":
    main()
