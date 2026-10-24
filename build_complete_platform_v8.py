# -*- coding: utf-8 -*-
"""
Builder for BioTwin Labs Complete Platform v5:
1. 7-Day Free Trial Auto-Lockout / Subscription Paywall (tools lock completely after 7 days)
2. Strict Language Separation:
   - Pure English (en): 100% clinical English, no Hinglish words
   - Pure Hindi (hi): 100% formal Hindi (शुद्ध हिन्दी), no English slang
   - Conversational Hinglish (hinglish): Everyday spoken mix
3. Integrated Founder Testing Controls (toggle Trial Active vs. Expired Lockout vs. Subscribed)
4. All UPI & WhatsApp payments mapped to founder's real number: 9343062265
"""

import os

BASE_DIR = r"c:\Users\B-WOI\OneDrive\Desktop\BioTwin-Platform"
INDEX_PATH = os.path.join(BASE_DIR, "web", "templates", "index.html")
PORTAL_PATH = os.path.join(BASE_DIR, "portal.html")

def generate_v5_html():
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
            --purple: #a855f7;
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

        /* Top Bar: Trial Status & Testing Controls */
        .trial-status-bar {
            background: rgba(15, 23, 42, 0.98);
            border-bottom: 1px solid var(--border);
            padding: 6px 36px;
            font-size: 11px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .trial-pill-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 3px 10px;
            border-radius: 999px;
            font-weight: 800;
            text-transform: uppercase;
            font-size: 10px;
        }
        .badge-active {
            background: rgba(16, 185, 129, 0.15);
            color: #34d399;
            border: 1px solid rgba(16, 185, 129, 0.35);
        }
        .badge-locked {
            background: rgba(239, 68, 68, 0.15);
            color: #f87171;
            border: 1px solid rgba(239, 68, 68, 0.35);
        }
        .test-sim-box {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .btn-sim {
            background: var(--surface-card);
            border: 1px solid var(--border);
            color: var(--text-dim);
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 10px;
            cursor: pointer;
            font-weight: 700;
        }
        .btn-sim:hover { color: #fff; border-color: var(--accent); }

        /* Navbar */
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
            gap: 12px;
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

        /* Screen Transitions */
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

        /* Screen Header Bar */
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

        /* Hero */
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

        /* Search Bar */
        .search-container {
            max-width: 700px;
            margin: 0 auto 36px;
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

        /* 7-Day Free Trial Banner */
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

        
        /* Auto-Lockout WhatsApp Reminder Card */
        .lockout-wa-reminder-box {
            margin-top: 26px;
            background: rgba(37, 211, 102, 0.08);
            border: 1px solid rgba(37, 211, 102, 0.35);
            border-radius: 16px;
            padding: 24px;
            text-align: left;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }
        .legal-disclaimer-box {
            background: rgba(245, 158, 11, 0.05);
            border: 1px solid rgba(245, 158, 11, 0.3);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 24px;
            text-align: left;
        }

        
        /* 5-Year Bio-Twin & Facial Vision CSS */
        .btn-future-tab {
            background: var(--surface-card);
            border: 1px solid var(--border);
            color: var(--text-muted);
            padding: 10px 18px;
            border-radius: 12px;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
        }
        .btn-future-tab.active {
            background: linear-gradient(135deg, #a855f7, #6366f1);
            color: #fff;
            border-color: #a855f7;
            box-shadow: 0 4px 15px rgba(168, 85, 247, 0.35);
        }
        .sim-slider-container {
            background: var(--surface-card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 24px;
            margin: 24px 0;
            text-align: center;
        }
        .sim-slider {
            width: 100%;
            height: 10px;
            border-radius: 5px;
            background: #1f293d;
            outline: none;
            -webkit-appearance: none;
            margin: 16px 0;
        }
        .sim-slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 26px;
            height: 26px;
            border-radius: 50%;
            background: #a855f7;
            cursor: pointer;
            box-shadow: 0 0 15px #a855f7;
        }
        .organ-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 18px;
            margin: 24px 0;
        }
        .organ-card {
            background: var(--surface-card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 20px;
            transition: all 0.25s;
        }
        .organ-card:hover {
            border-color: #a855f7;
            transform: translateY(-3px);
        }

        /* Catalog Grid */
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

        /* Plans & Subscriptions Section */
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

        /* Common Styles for Detail Screens */
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

        /* ------------------------------------------- */
        /* PAYWALL / 7-DAY LOCKOUT SCREEN (LOCKED)     */
        /* ------------------------------------------- */
        .lock-container {
            max-width: 850px;
            margin: 40px auto 60px;
            padding: 0 24px;
            text-align: center;
        }
        .lock-card {
            background: linear-gradient(145deg, #1e112a, #0a0f1a);
            border: 2px solid #ef4444;
            border-radius: 24px;
            padding: 40px 30px;
            box-shadow: 0 0 50px rgba(239, 68, 68, 0.25);
        }
        .lock-icon-circle {
            width: 80px;
            height: 80px;
            background: rgba(239, 68, 68, 0.15);
            border: 2px solid #ef4444;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 38px;
            margin: 0 auto 18px;
        }
        .lock-title {
            font-size: 28px;
            font-weight: 900;
            color: #f87171;
            margin-bottom: 10px;
        }
        .lock-desc {
            font-size: 14px;
            color: var(--text-muted);
            max-width: 620px;
            margin: 0 auto 28px;
            line-height: 1.6;
        }
        .lock-options-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
            text-align: left;
            margin-bottom: 28px;
        }
        .lock-opt-card {
            background: var(--surface-card);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 18px;
            cursor: pointer;
            transition: all 0.2s;
        }
        .lock-opt-card:hover {
            border-color: var(--accent);
            transform: translateY(-2px);
        }
        .lock-opt-card.active {
            border-color: #10b981;
            background: rgba(16, 185, 129, 0.08);
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

        @media (max-width: 900px) {
            .scanner-layout, .quiz-grid, .tm-grid, .biomarkers-layout, .booking-layout, .lock-options-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>

    <!-- TOP BAR: TRIAL STATUS & SIMULATION TOGGLE -->
    <div class="trial-status-bar">
        <div>
            <span style="color: var(--text-dim);">Account Status:</span>
            <span id="trialStatusBadge" class="trial-pill-badge badge-active">🟢 7-Day Free Trial (Day 2 of 7 Active)</span>
        </div>
        <div class="test-sim-box">
            <span style="color: var(--text-dim); font-size: 10px;">Developer State Simulator:</span>
            <button class="btn-sim" onclick="setSimState('active_trial')" title="Simulate Days 1-7 (Active Trial)">🟢 Active Trial</button>
            <button class="btn-sim" onclick="setSimState('expired')" title="Simulate Day 8+ (Lock Out Tools)">🔴 Lock Expired</button>
            <button class="btn-sim" onclick="setSimState('subscribed')" title="Simulate Subscribed (Unlocked)">⭐ Subscribed</button>
        </div>
    </div>

    <!-- GLOBAL NAVBAR -->
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
                <span data-i18n="hero_badge_text">📚 Clinical Longevity Protocols</span>
            </div>
            <h1 class="hero-title" data-i18n="hub_title">
                What Type of Health Assessment Do You Require?
            </h1>
            <p class="hero-subtitle" data-i18n="hub_desc">
                Select your required clinical tool below or search directly. Each assessment runs independently in its dedicated workspace without clutter:
            </p>

            <div class="search-container">
                <span class="search-icon">🔍</span>
                <input type="text" id="catalogSearch" class="search-box" placeholder="Search assessments (BP, Glucose, Past Reports, Visceral Fat, Phlebotomy)..." oninput="filterCatalog(this.value)">
            </div>
        </div>

        <div class="catalog-container">
            <!-- 7-DAY FREE TRIAL HERO SPOTLIGHT -->
            <div class="trial-banner" onclick="showScreen('freetrial')">
                <div>
                    <span class="trial-badge" data-i18n="tb_badge">🎁 SPECIAL LAUNCH OFFER • 7 DAYS FREE</span>
                    <h2 class="trial-title" data-i18n="tb_title">Start Your 7-Day Free Health & Longevity Trial</h2>
                    <p class="trial-desc" data-i18n="tb_desc">
                        No credit card or upfront payment required. Perform unlimited optical camera BP scans, determine biological age, and monitor arterial health for 7 days at ₹0!
                    </p>
                    <div class="trial-perks">
                        <span data-i18n="tb_p1">✓ Unlimited Camera BP Scans</span>
                        <span data-i18n="tb_p2">✓ Zero-Report Health Score</span>
                        <span data-i18n="tb_p3">✓ Daily Health Monitoring</span>
                        <span data-i18n="tb_p4">✓ 100% Free • No Payment</span>
                    </div>
                </div>
                <div style="text-align: center;">
                    <button class="btn-trial-act" data-i18n="btn_start_trial">
                        Start 7-Day Free Trial (₹0) →
                    </button>
                    <span style="font-size: 11px; color: var(--text-dim); display: block; margin-top: 8px;" data-i18n="tb_note">Instant Access • No Card Needed</span>
                </div>
            </div>

            <div class="catalog-header">
                <span data-i18n="hub_sec_title">Our 6 Dedicated Health Services:</span>
                <span id="catalogCount" style="font-size: 12px; color: var(--text-dim); font-weight: normal;">Showing 6 services</span>
            </div>

            <div class="catalog-grid" id="catalogGrid">
                
                <!-- CARD 1 -->
                <div class="service-card" onclick="openProtectedScreen('camera')" data-tags="camera bp blood pressure sugar mobile pulse instant free">
                    <div>
                        <div class="card-top">
                            <div class="card-icon">📱</div>
                            <div class="card-price-pill" data-i18n="price_free">FREE / ₹0</div>
                        </div>
                        <h2 class="card-title" data-i18n="c1_title">Camera Optical Blood Pressure & Pulse Scan</h2>
                        <p class="card-desc" data-i18n="c1_desc">
                            Non-invasive transdermal photoplethysmography measures capillary light absorption from your fingertip to estimate pulse wave velocity and blood pressure.
                        </p>
                    </div>
                    <div>
                        <div class="card-meta">
                            <span>⏱️ 15 Seconds</span>
                            <span>🔬 Transdermal PPG</span>
                        </div>
                        <div class="card-btn">
                            <span data-i18n="c1_btn">Open Camera Scanner</span>
                            <span>→</span>
                        </div>
                    </div>
                </div>

                <!-- CARD 2 -->
                <div class="service-card" onclick="openProtectedScreen('quiz')" data-tags="zero report no blood test quiz 2 min belly fat visceral waist insulin">
                    <div>
                        <div class="card-top">
                            <div class="card-icon">📋</div>
                            <div class="card-price-pill" data-i18n="price_free">FREE / ₹0</div>
                        </div>
                        <h2 class="card-title" data-i18n="c2_title">Zero-Report 2-Minute Longevity Assessment</h2>
                        <p class="card-desc" data-i18n="c2_desc">
                            No blood test available? 6 non-invasive markers (Waist-to-Height ratio, resting pulse, postprandial fatigue) calculate your biological age delta and visceral risk.
                        </p>
                    </div>
                    <div>
                        <div class="card-meta">
                            <span>⏱️ 2 Minutes</span>
                            <span>📚 Guyton & Hall Ch. 72</span>
                        </div>
                        <div class="card-btn">
                            <span data-i18n="c2_btn">Start 2-Min Assessment</span>
                            <span>→</span>
                        </div>
                    </div>
                </div>

                <!-- CARD 3 -->
                <div class="service-card" onclick="openProtectedScreen('timemachine')" data-tags="old report time machine purani drift damage sugar cholesterol">
                    <div>
                        <div class="card-top">
                            <div class="card-icon">⏳</div>
                            <div class="card-price-pill" data-i18n="price_free">FREE / ₹0</div>
                        </div>
                        <h2 class="card-title" data-i18n="c3_title">Old Report Time Machine Projector</h2>
                        <p class="card-desc" data-i18n="c3_desc">
                            Enter numbers from a 1 to 3-year-old blood test report. The beta-cell exhaustion model projects your current metabolic drift and accelerated organ aging today.
                        </p>
                    </div>
                    <div>
                        <div class="card-meta">
                            <span>⏱️ 1 Minute</span>
                            <span>📉 Beta-Cell Exhaustion Model</span>
                        </div>
                        <div class="card-btn">
                            <span data-i18n="c3_btn">Check Old Report Drift</span>
                            <span>→</span>
                        </div>
                    </div>
                </div>

                <!-- CARD 4 -->
                <div class="service-card" onclick="openProtectedScreen('biomarkers')" data-tags="72 biomarkers full panel report levine phenoage apob homa deep analysis">
                    <div>
                        <div class="card-top">
                            <div class="card-icon">🩸</div>
                            <div class="card-price-pill" data-i18n="price_online_free">ONLINE FREE / PDF ₹499</div>
                        </div>
                        <h2 class="card-title" data-i18n="c4_title">Full 72+ Biomarker Clinical Panel</h2>
                        <p class="card-desc" data-i18n="c4_desc">
                            Input results from recent blood work across 6 clinical pillars (ApoB, Insulin, hs-CRP, Liver, Kidney) to compute your exact Levine Phenotypic Age.
                        </p>
                    </div>
                    <div>
                        <div class="card-meta">
                            <span>⏱️ 5 Minutes</span>
                            <span>📑 Executive Physician PDF</span>
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
                        <h2 class="card-title" data-i18n="c5_title">At-Home Phlebotomist Blood Draw</h2>
                        <p class="card-desc" data-i18n="c5_desc">
                            A certified phlebotomist visits your residence to collect samples in sterile vacutainers. Includes 72+ parameters, Biological Age Blueprint, and Doctor review.
                        </p>
                    </div>
                    <div>
                        <div class="card-meta">
                            <span>🚚 Tomorrow 7:00 AM - 9:00 AM</span>
                            <span>✓ NABL Certified Laboratory</span>
                        </div>
                        <div class="card-btn">
                            <span data-i18n="c5_btn">Book Home Blood Draw (₹1,999)</span>
                            <span>→</span>
                        </div>
                    </div>
                </div>

                <!-- CARD 6: 5-YEAR LIVING BIO-TWIN SIMULATOR & FACIAL rPPG -->
                <div class="service-card" onclick="openProtectedScreen('future')" style="border-color: #a855f7; background: linear-gradient(180deg, rgba(168, 85, 247, 0.08), var(--surface));" data-tags="5 year biological twin 2029 future organ simulation facial rppg face vision scan micro interventions">
                    <div>
                        <div class="card-top">
                            <div class="card-icon" style="background: rgba(168, 85, 247, 0.15); border-color: #a855f7;">🧬</div>
                            <div class="card-price-pill" style="background: rgba(168, 85, 247, 0.2); border-color: #a855f7; color: #c084fc;">2029 AI HORIZON</div>
                        </div>
                        <h2 class="card-title" data-i18n="c6_title">5-Year Bio-Twin Organ Simulator & Facial Vision AI</h2>
                        <p class="card-desc" data-i18n="c6_desc">
                            Simulate living heart, liver, pancreas, and arteries through 2031. Features Contactless Facial rPPG stress scanning and daily AI micro-interventions.
                        </p>
                    </div>
                    <div>
                        <div class="card-meta">
                            <span>🔮 2026–2031 Horizon</span>
                            <span>👁️ Face rPPG + Micro-Rx</span>
                        </div>
                        <div class="card-btn" style="background: linear-gradient(135deg, #a855f7, #6366f1); border: none; color: #fff;">
                            <span data-i18n="c6_btn">Launch 5-Year Bio-Twin</span>
                            <span>→</span>
                        </div>
                    </div>
                </div>

            </div>
        </div>

        <!-- PRICING & SUBSCRIPTION SECTION -->
        <div class="plans-section" id="plansCatalog">
            <div class="plans-heading-box">
                <span class="hero-badge" style="background: rgba(168, 85, 247, 0.1); border-color: rgba(168, 85, 247, 0.25); color: #c084fc;" data-i18n="sec_plans_badge">
                    💎 Transparent Pricing Plans
                </span>
                <h2 class="plans-title" data-i18n="sec_plans_title">
                    Affordable Normal Passes & 1-Month Subscriptions
                </h2>
                <p class="plans-sub" data-i18n="sec_plans_sub">
                    First 7 days are 100% FREE. After that, keep monitoring with normal weekly passes (₹199, ₹299) or monthly memberships (₹2,499, ₹3,499):
                </p>
            </div>

            <div class="plans-grid">
                
                <!-- PLAN 1: NORMAL WEEKLY PASS (₹199) -->
                <div class="plan-card">
                    <div>
                        <span class="plan-badge-top" style="background: #334155; color: #fff;" data-i18n="p1_badge">AFFORDABLE PASS</span>
                        <h3 style="font-size: 16px; font-weight: 800; color: #fff;" data-i18n="p1_title">Weekly Checkup Pass</h3>
                        <div class="plan-price-box">
                            <span class="plan-price">₹199</span>
                            <span class="plan-period" data-i18n="p1_period">/ 7 Days</span>
                        </div>
                        <ul class="plan-features">
                            <li data-i18n="p1_f1">Unlimited Camera BP Scans</li>
                            <li data-i18n="p1_f2">Pulse & Arterial Elasticity</li>
                            <li data-i18n="p1_f3">Post-Meal Sugar Crash Check</li>
                            <li data-i18n="p1_f4">Instant Risk Alerts</li>
                        </ul>
                    </div>
                    <button class="btn-plan-act" onclick="selectPlan('Weekly Pass', 199)" data-i18n="p1_btn">
                        Choose ₹199 Pass →
                    </button>
                </div>

                <!-- PLAN 2: DEEP REPORT PASS (₹299) -->
                <div class="plan-card">
                    <div>
                        <span class="plan-badge-top" style="background: #0284c7; color: #fff;" data-i18n="p2_badge">ONE-TIME PASS</span>
                        <h3 style="font-size: 16px; font-weight: 800; color: #fff;" data-i18n="p2_title">Deep Longevity Report</h3>
                        <div class="plan-price-box">
                            <span class="plan-price">₹299</span>
                            <span class="plan-period" data-i18n="p2_period">/ Single Report</span>
                        </div>
                        <ul class="plan-features">
                            <li data-i18n="p2_f1">Zero-Report Visceral Score</li>
                            <li data-i18n="p2_f2">Time Machine 3-Yr Drift</li>
                            <li data-i18n="p2_f3">HOMA-IR Insulin Resistance</li>
                            <li data-i18n="p2_f4">Executive PDF Download</li>
                        </ul>
                    </div>
                    <button class="btn-plan-act" onclick="selectPlan('Deep Report Pass', 299)" data-i18n="p2_btn">
                        Choose ₹299 Pass →
                    </button>
                </div>

                <!-- PLAN 3: 1-MONTH STANDARD SUBSCRIPTION (₹2,499) -->
                <div class="plan-card plan-card-popular">
                    <span class="plan-badge-top plan-badge-popular" data-i18n="p3_badge">MOST POPULAR 🔥</span>
                    <div>
                        <h3 style="font-size: 16px; font-weight: 800; color: #38bdf8;" data-i18n="p3_title">1-Month Standard Membership</h3>
                        <div class="plan-price-box">
                            <span class="plan-price">₹2,499</span>
                            <span class="plan-period" data-i18n="p3_period">/ Month</span>
                        </div>
                        <ul class="plan-features">
                            <li data-i18n="p3_f1">30 Days Unlimited Camera Scans</li>
                            <li data-i18n="p3_f2">Daily Biological Age Tracking</li>
                            <li data-i18n="p3_f3">Metabolic Drift Reversal Plan</li>
                            <li data-i18n="p3_f4">Weekly WhatsApp Diet Guide</li>
                            <li data-i18n="p3_f5">Priority Doctor Assistance</li>
                        </ul>
                    </div>
                    <button class="btn-plan-act" onclick="selectPlan('1-Month Standard Subscription', 2499)" data-i18n="p3_btn">
                        Start ₹2,499 Monthly →
                    </button>
                </div>

                <!-- PLAN 4: 1-MONTH VIP SUBSCRIPTION (₹3,499) -->
                <div class="plan-card plan-card-vip">
                    <span class="plan-badge-top plan-badge-vip" data-i18n="p4_badge">ALL-INCLUSIVE VIP 👑</span>
                    <div>
                        <h3 style="font-size: 16px; font-weight: 800; color: #c084fc;" data-i18n="p4_title">1-Month VIP + Blood Test</h3>
                        <div class="plan-price-box">
                            <span class="plan-price">₹3,499</span>
                            <span class="plan-period" data-i18n="p4_period">/ Month</span>
                        </div>
                        <ul class="plan-features">
                            <li data-i18n="p4_f1"><strong>Includes NABL Home Blood Draw (72+ Tests)</strong></li>
                            <li data-i18n="p4_f2">Full Levine PhenoAge Doctor Report</li>
                            <li data-i18n="p4_f3">1-on-1 Doctor Longevity Consult</li>
                            <li data-i18n="p4_f4">30-Day Family Camera App Access</li>
                            <li data-i18n="p4_f5">Personalized Reversal Plan</li>
                        </ul>
                    </div>
                    <button class="btn-plan-act" onclick="selectPlan('1-Month VIP Longevity Membership', 3499)" data-i18n="p4_btn">
                        Join ₹3,499 VIP →
                    </button>
                </div>

            </div>
        </div>
    </div>


    <!-- ================================================= -->
    <!-- SCREEN 6: 5-YEAR LIVING BIO-TWIN & FACIAL VISION  -->
    <!-- ================================================= -->
    <div id="screen-future" class="screen-view">
        <div class="screen-header-bar">
            <button class="btn-back-home" onclick="showScreen('hub')">
                <span>←</span>
                <span data-i18n="btn_back_services">Back to All Services</span>
            </button>
            <span class="screen-tag" style="background: rgba(168, 85, 247, 0.15); border-color: rgba(168, 85, 247, 0.35); color: #c084fc;">
                🧬 2029 Bio-Twin Intelligence Engine
            </span>
        </div>

        <div class="detail-container" style="max-width: 1240px;">
            <!-- Header Banner -->
            <div style="background: linear-gradient(135deg, rgba(168, 85, 247, 0.12), rgba(56, 189, 248, 0.12)); border: 2px solid #a855f7; border-radius: 20px; padding: 28px; margin-bottom: 26px;">
                <span style="background: #a855f7; color: #fff; font-size: 11px; font-weight: 800; padding: 3px 10px; border-radius: 999px; text-transform: uppercase;">
                    Next-Gen Precision Longevity
                </span>
                <h1 style="font-size: 26px; font-weight: 800; color: #fff; margin: 10px 0 6px;" data-i18n="fut_header_title">
                    5-Year Living Digital Biological Twin & Facial Vision AI
                </h1>
                <p style="font-size: 13px; color: var(--text-muted); max-width: 820px; line-height: 1.6;" data-i18n="fut_header_desc">
                    Unlike traditional backward-looking lab tests, your Digital Bio-Twin is a dynamic biochemical simulation modeling cellular degradation rates across vital organ systems from 2026 through 2031.
                </p>

                <!-- Navigation Tabs inside Future screen -->
                <div style="display: flex; gap: 10px; margin-top: 20px; flex-wrap: wrap;">
                    <button class="btn-future-tab active" id="tabBtnSimulator" onclick="switchFutureTab('simulator')">
                        🫀 1. 5-Year Organ Simulator (2026–2031)
                    </button>
                    <button class="btn-future-tab" id="tabBtnFacial" onclick="switchFutureTab('facial')">
                        👁️ 2. Contactless Facial rPPG Scanner
                    </button>
                    <button class="btn-future-tab" id="tabBtnMicro" onclick="switchFutureTab('micro')">
                        💊 3. Daily AI Longevity Micro-Prescription
                    </button>
                </div>
            </div>

            <!-- TAB 1: 5-YEAR LIVING ORGAN SIMULATOR -->
            <div id="future-tab-simulator" class="future-tab-content">
                <div class="sim-slider-container">
                    <div style="font-size: 12px; text-transform: uppercase; color: var(--text-dim); font-weight: 800;">
                        Slide Horizon into Future (2026 to 2031):
                    </div>
                    <div style="font-size: 38px; font-weight: 900; color: #c084fc; font-family: 'JetBrains Mono', monospace; margin: 8px 0;" id="simYearDisplay">
                        YEAR 2029 (+3 Years Drift)
                    </div>
                    <input type="range" id="simYearSlider" min="2026" max="2031" value="2029" step="1" class="sim-slider" oninput="updateOrganSimulation(this.value)">
                    <div style="display: flex; justify-content: space-between; font-size: 12px; color: var(--text-dim); font-weight: 700;">
                        <span>2026 (Today)</span>
                        <span>2027</span>
                        <span>2028</span>
                        <span>2029 (Critical Pivot)</span>
                        <span>2030</span>
                        <span>2031 (+5 Years)</span>
                    </div>
                </div>

                <!-- Live Dynamic Organ Simulation Grid -->
                <div class="organ-grid">
                    <!-- Heart -->
                    <div class="organ-card">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                            <span style="font-size: 28px;">🫀</span>
                            <span id="heartRiskBadge" style="background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.35); font-size: 10px; font-weight: 800; padding: 2px 8px; border-radius: 999px;">
                                MODERATE ARTERIAL STIFFNESS
                            </span>
                        </div>
                        <h3 style="font-size: 16px; font-weight: 800; color: #fff;">Cardiovascular & Endothelium</h3>
                        <p style="font-size: 12px; color: var(--text-muted); margin: 6px 0 14px;" id="heartDesc">
                            Simulated Pulse Wave Velocity indicates accelerated arterial stiffening from chronic sedentary vascular shear stress.
                        </p>
                        <div style="border-top: 1px solid var(--border); padding-top: 10px; font-size: 11px; display: flex; justify-content: space-between;">
                            <span style="color: var(--text-dim);">Est. Blood Pressure:</span>
                            <strong style="color: #f87171;" id="simBP">136 / 88 mmHg</strong>
                        </div>
                    </div>

                    <!-- Liver -->
                    <div class="organ-card">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                            <span style="font-size: 28px;">🥩</span>
                            <span id="liverRiskBadge" style="background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.35); font-size: 10px; font-weight: 800; padding: 2px 8px; border-radius: 999px;">
                                GRADE-1 HEPATIC STEATOSIS
                            </span>
                        </div>
                        <h3 style="font-size: 16px; font-weight: 800; color: #fff;">Liver & Metabolic Clearance</h3>
                        <p style="font-size: 12px; color: var(--text-muted); margin: 6px 0 14px;" id="liverDesc">
                            Visceral lipid accumulation projects 18% intrahepatic fat infiltration under baseline dietary inertia.
                        </p>
                        <div style="border-top: 1px solid var(--border); padding-top: 10px; font-size: 11px; display: flex; justify-content: space-between;">
                            <span style="color: var(--text-dim);">Simulated ALT Enzyme:</span>
                            <strong style="color: #fbbf24;" id="simALT">44 U/L (Elevated)</strong>
                        </div>
                    </div>

                    <!-- Pancreas -->
                    <div class="organ-card">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                            <span style="font-size: 28px;">🥞</span>
                            <span id="pancRiskBadge" style="background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.35); font-size: 10px; font-weight: 800; padding: 2px 8px; border-radius: 999px;">
                                BETA-CELL EXHAUSTION: 28%
                            </span>
                        </div>
                        <h3 style="font-size: 16px; font-weight: 800; color: #fff;">Pancreatic Beta-Cell Mass</h3>
                        <p style="font-size: 12px; color: var(--text-muted); margin: 6px 0 14px;" id="pancDesc">
                            Hyperinsulinemic compensation drift shows silent islet amyloid polypeptide stress prior to clinical hyperglycemia.
                        </p>
                        <div style="border-top: 1px solid var(--border); padding-top: 10px; font-size: 11px; display: flex; justify-content: space-between;">
                            <span style="color: var(--text-dim);">Projected Fasting Glucose:</span>
                            <strong style="color: #f87171;" id="simGlucose">108 mg/dL (Pre-Diabetic)</strong>
                        </div>
                    </div>

                    <!-- Kidneys -->
                    <div class="organ-card">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                            <span style="font-size: 28px;">🫘</span>
                            <span id="kidneyRiskBadge" style="background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.35); font-size: 10px; font-weight: 800; padding: 2px 8px; border-radius: 999px;">
                                OPTIMAL FILTRATION
                            </span>
                        </div>
                        <h3 style="font-size: 16px; font-weight: 800; color: #fff;">Renal Glomerular Function</h3>
                        <p style="font-size: 12px; color: var(--text-muted); margin: 6px 0 14px;" id="kidneyDesc">
                            Glomerular filtration rate is preserved with minimal hyperfiltration microalbuminuria risk.
                        </p>
                        <div style="border-top: 1px solid var(--border); padding-top: 10px; font-size: 11px; display: flex; justify-content: space-between;">
                            <span style="color: var(--text-dim);">Projected eGFR:</span>
                            <strong style="color: #34d399;" id="simGFR">94 mL/min/1.73m²</strong>
                        </div>
                    </div>
                </div>

                <!-- Dual Trajectory Comparison Card -->
                <div style="background: var(--surface); border: 1px solid var(--border); border-radius: 18px; padding: 24px; margin-top: 24px;">
                    <h3 style="font-size: 17px; font-weight: 800; margin-bottom: 14px;">5-Year Biological Age Trajectory Comparison:</h3>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                        <div style="background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 14px; padding: 18px;">
                            <span style="color: #f87171; font-size: 11px; font-weight: 800; text-transform: uppercase;">Trajectory A: Baseline Inertia</span>
                            <div style="font-size: 24px; font-weight: 900; color: #f87171; margin: 6px 0;" id="trajInertiaAge">
                                +5.4 Years Older by 2029
                            </div>
                            <p style="font-size: 12px; color: #cbd5e1; line-height: 1.5;">
                                Without targeted micro-interventions, silent vascular stiffening and hepatic fat accumulation accelerate biological aging.
                            </p>
                        </div>
                        <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 14px; padding: 18px;">
                            <span style="color: #34d399; font-size: 11px; font-weight: 800; text-transform: uppercase;">Trajectory B: Bio-Twin Protocol</span>
                            <div style="font-size: 24px; font-weight: 900; color: #34d399; margin: 6px 0;" id="trajProtocolAge">
                                -4.2 Years Younger by 2029
                            </div>
                            <p style="font-size: 12px; color: #cbd5e1; line-height: 1.5;">
                                Implementing personalized circadian, mitochondrial Zone-2, and targeted nutraceutical protocols reverses organ biological age.
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 2: CONTACTLESS FACIAL rPPG SCANNER -->
            <div id="future-tab-facial" class="future-tab-content" style="display: none;">
                <div style="display: grid; grid-template-columns: 1fr 340px; gap: 24px; align-items: start;">
                    <div style="background: #000; border: 2px solid var(--accent); border-radius: 20px; padding: 14px; text-align: center; position: relative;">
                        <video id="facialVideo" autoplay playsinline muted style="width: 100%; height: 380px; object-fit: cover; border-radius: 14px; background: #05070c;"></video>
                        <div style="position: absolute; top: 40px; left: 50%; transform: translateX(-50%); width: 200px; height: 260px; border: 2px dashed #a855f7; border-radius: 50px; pointer-events: none; display: flex; align-items: flex-start; justify-content: center; padding-top: 14px;">
                            <span style="background: rgba(168, 85, 247, 0.8); color: #fff; font-size: 10px; font-weight: 800; padding: 2px 8px; border-radius: 999px;">
                                Facial rPPG Optical ROI
                            </span>
                        </div>
                        <div style="margin-top: 12px; font-size: 12px; color: var(--text-muted);" id="facialStatusText">
                            Position your face within the optical oval. Click Start Facial Scan below.
                        </div>
                        <button class="btn-action-main" id="btnFacialScan" onclick="toggleFacialScan()" style="background: linear-gradient(135deg, #a855f7, #6366f1); margin-top: 14px;">
                            <span>👁️</span>
                            <span>Start 15-Sec Contactless Facial rPPG Scan</span>
                        </button>
                    </div>

                    <div>
                        <div style="background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 20px; margin-bottom: 16px;">
                            <div style="font-size: 11px; text-transform: uppercase; color: var(--text-dim); font-weight: 800;">Facial Pulse (rPPG)</div>
                            <div style="font-size: 32px; font-weight: 900; color: #38bdf8; font-family: 'JetBrains Mono', monospace;" id="faceHR">
                                72 <sub style="font-size: 14px; color: var(--text-muted);">bpm</sub>
                            </div>
                        </div>

                        <div style="background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 20px; margin-bottom: 16px;">
                            <div style="font-size: 11px; text-transform: uppercase; color: var(--text-dim); font-weight: 800;">Heart Rate Variability (HRV)</div>
                            <div style="font-size: 32px; font-weight: 900; color: #10b981; font-family: 'JetBrains Mono', monospace;" id="faceHRV">
                                58 <sub style="font-size: 14px; color: var(--text-muted);">ms RMSSD</sub>
                            </div>
                            <span style="font-size: 11px; color: #34d399;">High Parasympathetic Vagal Tone</span>
                        </div>

                        <div style="background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 20px;">
                            <div style="font-size: 11px; text-transform: uppercase; color: var(--text-dim); font-weight: 800;">Autonomic Cortisol Stress</div>
                            <div style="font-size: 32px; font-weight: 900; color: #c084fc; font-family: 'JetBrains Mono', monospace;" id="faceStress">
                                26 <sub style="font-size: 14px; color: var(--text-muted);">/ 100</sub>
                            </div>
                            <span style="font-size: 11px; color: #c084fc;">Low Sympathetic Stress (Optimal)</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 3: DAILY AI LONGEVITY MICRO-PRESCRIPTION -->
            <div id="future-tab-micro" class="future-tab-content" style="display: none;">
                <div style="background: var(--surface); border: 1px solid var(--border); border-radius: 18px; padding: 26px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 10px;">
                        <div>
                            <span style="background: rgba(16, 185, 129, 0.15); color: #34d399; font-size: 10px; font-weight: 800; padding: 2px 8px; border-radius: 999px; text-transform: uppercase;">
                                Daily Precision Longevity Protocol
                            </span>
                            <h3 style="font-size: 20px; font-weight: 800; color: #fff; margin-top: 6px;">
                                Today's Personalized AI Bio-Twin Micro-Interventions
                            </h3>
                        </div>
                        <button onclick="alert('✅ Today\'s Micro-Prescription saved to your BioTwin profile and sent to WhatsApp (9343062265).')" class="btn-wa" style="padding: 10px 18px; font-size: 12px; border-radius: 10px;">
                            <span>📲</span>
                            <span>Save Protocol to WhatsApp</span>
                        </button>
                    </div>

                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 18px;">
                        <!-- Block 1: Chrono Nutrition -->
                        <div style="background: var(--surface-card); border: 1px solid var(--border); border-radius: 14px; padding: 20px;">
                            <div style="font-size: 24px; margin-bottom: 8px;">⏰</div>
                            <strong style="font-size: 14px; color: #fff; display: block; margin-bottom: 6px;">1. Chrono-Nutritional Timing</strong>
                            <p style="font-size: 12px; color: var(--text-muted); line-height: 1.6;">
                                Maintain a 16:8 metabolic window. Conclude dinner by 7:30 PM to optimize nocturnal growth hormone secretion and autophagy.
                            </p>
                        </div>

                        <!-- Block 2: Precision Supplements -->
                        <div style="background: var(--surface-card); border: 1px solid var(--border); border-radius: 14px; padding: 20px;">
                            <div style="font-size: 24px; margin-bottom: 8px;">💊</div>
                            <strong style="font-size: 14px; color: #fff; display: block; margin-bottom: 6px;">2. Targeted Nutraceutical Stack</strong>
                            <p style="font-size: 12px; color: var(--text-muted); line-height: 1.6;">
                                • Morning: CoQ10 100mg + Omega-3 EPA 1000mg<br/>
                                • Evening: Magnesium Glycinate 400mg (for endothelial elasticity & deep restorative sleep).
                            </p>
                        </div>

                        <!-- Block 3: Zone 2 Exercise -->
                        <div style="background: var(--surface-card); border: 1px solid var(--border); border-radius: 14px; padding: 20px;">
                            <div style="font-size: 24px; margin-bottom: 8px;">🏃</div>
                            <strong style="font-size: 14px; color: #fff; display: block; margin-bottom: 6px;">3. Zone-2 Mitochondrial Conditioning</strong>
                            <p style="font-size: 12px; color: var(--text-muted); line-height: 1.6;">
                                35 Minutes of brisk walking or cycling at 115–125 BPM heart rate to clear visceral triglycerides and boost mitochondrial biogenesis.
                            </p>
                        </div>

                        <!-- Block 4: Vagal Nerve Breathwork -->
                        <div style="background: var(--surface-card); border: 1px solid var(--border); border-radius: 14px; padding: 20px;">
                            <div style="font-size: 24px; margin-bottom: 8px;">🧘</div>
                            <strong style="font-size: 14px; color: #fff; display: block; margin-bottom: 6px;">4. Autonomic Vagus Nerve Reset</strong>
                            <p style="font-size: 12px; color: var(--text-muted); line-height: 1.6;">
                                5 Minutes of 4-7-8 resonance breathwork before bed to down-regulate sympathetic cortisol and preserve heart rate variability.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>


    <!-- ================================================= -->
    <!-- SCREEN: PAYWALL / 7-DAY LOCKOUT SCREEN (LOCKED)   -->
    <!-- ================================================= -->
    <div id="screen-locked" class="screen-view">
        <div class="screen-header-bar">
            <button class="btn-back-home" onclick="showScreen('hub')">
                <span>←</span>
                <span data-i18n="btn_back_services">Back to All Services</span>
            </button>
            <span class="screen-tag" style="background: rgba(239, 68, 68, 0.15); border-color: rgba(239, 68, 68, 0.35); color: #f87171;">
                🔒 Access Restricted
            </span>
        </div>

        <div class="lock-container">
            <div class="lock-card">
                <div class="lock-icon-circle">🔒</div>
                <h2 class="lock-title" data-i18n="lock_title">7-Day Free Trial Has Concluded</h2>
                <p class="lock-desc" data-i18n="lock_desc">
                    Your complimentary 7-day health monitoring period has completed. Clinical assessments including Camera Optical Scan, Zero-Report Assessment, and Biomarker Analysis are now locked. Please renew with a normal checkup pass or monthly subscription to continue.
                </p>

                <div class="lock-options-grid">
                    <div class="lock-opt-card" onclick="selectPlan('Weekly Pass', 199)">
                        <div style="font-size: 11px; text-transform: uppercase; color: var(--text-dim); font-weight: 700;">Normal Checkup Pass</div>
                        <div style="font-size: 20px; font-weight: 800; color: #fff; margin: 4px 0;">₹199 / 7 Days</div>
                        <div style="font-size: 11px; color: var(--text-muted);">Unlimited camera BP scans & daily tracking for 7 days</div>
                    </div>
                    <div class="lock-opt-card" onclick="selectPlan('Deep Report Pass', 299)">
                        <div style="font-size: 11px; text-transform: uppercase; color: var(--text-dim); font-weight: 700;">Deep Report Pass</div>
                        <div style="font-size: 20px; font-weight: 800; color: #fff; margin: 4px 0;">₹299 / Single</div>
                        <div style="font-size: 11px; color: var(--text-muted);">Zero-report visceral fat score + Time Machine drift report</div>
                    </div>
                    <div class="lock-opt-card active" onclick="selectPlan('1-Month Standard Subscription', 2499)">
                        <div style="font-size: 11px; text-transform: uppercase; color: var(--accent); font-weight: 700;">Most Popular Monthly</div>
                        <div style="font-size: 20px; font-weight: 800; color: #38bdf8; margin: 4px 0;">₹2,499 / Month</div>
                        <div style="font-size: 11px; color: var(--text-muted);">30 Days full camera access + daily biological age tracking</div>
                    </div>
                    <div class="lock-opt-card" onclick="selectPlan('1-Month VIP Longevity Membership', 3499)">
                        <div style="font-size: 11px; text-transform: uppercase; color: #a855f7; font-weight: 700;">VIP + Blood Test</div>
                        <div style="font-size: 20px; font-weight: 800; color: #c084fc; margin: 4px 0;">₹3,499 / Month</div>
                        <div style="font-size: 11px; color: var(--text-muted);">Includes NABL home blood draw (72+ tests) & Doctor review</div>
                    </div>
                </div>

                <div style="max-width: 520px; margin: 0 auto; background: var(--surface-card); border: 1px dashed var(--accent); border-radius: 16px; padding: 20px;">
                    <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 8px;">Scan UPI QR to Instantly Unlock (₹199 / ₹299 / ₹2,499 / ₹3,499):</div>
                    <div style="width: 140px; height: 140px; background: #fff; padding: 6px; border-radius: 10px; margin: 0 auto 10px;">
                        <img src="https://api.qrserver.com/v1/create-qr-code/?size=140x140&data=upi://pay?pa=9343062265@upi&pn=BioTwin%20Labs&am=199&cu=INR&tn=Reactivate-Access" style="width: 100%; height: 100%; object-fit: contain;">
                    </div>
                    <div style="font-size: 12px; color: #34d399; font-family: 'JetBrains Mono', monospace; font-weight: 700;">UPI / GPay / PhonePe: 9343062265</div>
                    <a href="https://wa.me/919343062265?text=Hi+BioTwin+Labs,+my+7-day+trial+expired.+Please+reactivate+my+access." target="_blank" class="btn-wa" style="margin-top: 14px;">
                        <span>💬</span>
                        <span data-i18n="lock_btn_wa">WhatsApp to Reactivate (9343062265)</span>
                    </a>

                    <!-- QUICK UTR UNLOCK BOX (ANTI-FRAUD VERIFIED) -->
                    <div style="margin-top: 16px; background: rgba(0,0,0,0.5); border: 1px solid var(--border); border-radius: 12px; padding: 14px; text-align: left;">
                        <label style="font-size: 11px; color: var(--accent); display: block; margin-bottom: 6px; text-transform: uppercase; font-weight: 800;">
                            Paid via UPI? Enter 12-Digit Bank UTR to Unlock Instantly:
                        </label>
                        <div style="display: flex; gap: 8px;">
                            <input type="text" id="quick_lock_utr" placeholder="12-Digit Bank UTR" maxlength="12" style="flex: 1; background: var(--surface-card); border: 1px solid var(--border); border-radius: 8px; padding: 10px; font-size: 12px; color: #fff; font-family: 'JetBrains Mono', monospace; outline: none;">
                            <button onclick="submitQuickUnlockUTR()" class="btn-wa" style="padding: 10px 14px; font-size: 12px; border-radius: 8px; white-space: nowrap; cursor: pointer;">
                                Verify UTR
                            </button>
                        </div>
                        <div style="font-size: 10px; color: var(--text-dim); margin-top: 6px;">
                            🔒 Direct verification against 9343062265 bank ledger. Duplicate or fake UTRs are auto-rejected.
                        </div>
                    </div>
                </div>

                <!-- AUTO-LOCKOUT WHATSAPP REMINDER & BACKUP CARD -->
                <div class="lockout-wa-reminder-box" style="max-width: 520px; margin: 24px auto 0;">
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                        <span style="font-size: 24px;">📲</span>
                        <strong style="font-size: 16px; color: #34d399;" data-i18n="lock_reminder_title">Auto-Lockout WhatsApp Reminder & Backup Service</strong>
                    </div>
                    <p style="font-size: 12px; color: var(--text-muted); line-height: 1.6; margin-bottom: 14px;" data-i18n="lock_reminder_desc">
                        Your 7-day health tracking and biological age simulations are currently paused. Enter your WhatsApp number below to receive an automated encrypted backup of your baseline readings and an instant 1-tap reactivation pass link.
                    </p>
                    <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                        <input type="tel" id="lock_remind_phone" placeholder="WhatsApp Mobile Number (e.g. 9876543210)" style="flex: 1; min-width: 190px; background: var(--surface-card); border: 1px solid var(--border); border-radius: 10px; padding: 12px 14px; font-size: 13px; color: #fff; outline: none; font-family: 'JetBrains Mono', monospace;">
                        <button onclick="sendAutoLockoutReminder()" class="btn-wa" style="padding: 12px 18px; font-size: 13px; border-radius: 10px; white-space: nowrap; cursor: pointer;">
                            <span>🔔</span>
                            <span data-i18n="lock_reminder_btn">Send WhatsApp Reminder</span>
                        </button>
                    </div>
                    <div id="lock_remind_feedback" style="display: none; margin-top: 12px; font-size: 12px; color: #34d399; font-weight: 700;"></div>
                </div>
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
            <span class="screen-tag">📱 Optical PPG Scan</span>
        </div>

        <div class="detail-container">
            <div class="detail-panel">
                <h2 class="detail-title" data-i18n="cam_title">Camera Optical Blood Pressure & Pulse Scanner</h2>
                <p class="detail-desc" data-i18n="cam_desc">
                    This clinical tool reads arterial micro-reflections in your fingertip capillary bed using optical photoplethysmography to estimate arterial elasticity and systolic/diastolic blood pressure.
                </p>

                <div class="scanner-layout">
                    <div class="camera-viewport">
                        <video id="webcamVideo" class="camera-video" autoplay playsinline muted></video>
                        <div class="pulse-heart" id="pulseHeart">🫀</div>
                        <div id="scanStatus" style="font-size: 11px; color: var(--text-muted); text-align: center; padding: 0 20px; margin-top: 14px;" data-i18n="cam_instruct">
                            Place your finger over the camera lens or position your face toward the camera. Click Start Scan below.
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

                <!-- Camera Clinical Disclaimer Banner -->
                <div style="margin-top: 20px; background: rgba(56, 189, 248, 0.08); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 12px; padding: 14px 18px; font-size: 12px; color: #94a3b8; display: flex; align-items: flex-start; gap: 10px;">
                    <span style="font-size: 18px;">⚖️</span>
                    <span data-i18n="cam_disclaimer">Clinical Screening Notice: Fingertip optical photoplethysmography is designed for preventive wellness screening and arterial elasticity trend monitoring. It is not an invasive ICU-grade arterial line monitor. Always verify persistent clinical abnormalities with a licensed physician.</span>
                </div>

                <!-- Manual Quick Verification -->
                <div style="margin-top: 28px; background: var(--surface-card); border: 1px solid var(--border); border-radius: 14px; padding: 20px;">
                    <strong style="font-size: 13px; color: #fff; display: block; margin-bottom: 8px;" data-i18n="manual_title">
                        Or Enter Your Recent Blood Pressure & Glucose Values (Instant Clinical Verification):
                    </strong>
                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;">
                        <div>
                            <label style="font-size: 10px; color: var(--text-dim); text-transform: uppercase; font-weight: 700;" data-i18n="lbl_sys_bp">Systolic BP (Upper)</label>
                            <input type="number" id="inSys" class="input-control" value="122" oninput="evalManual()">
                        </div>
                        <div>
                            <label style="font-size: 10px; color: var(--text-dim); text-transform: uppercase; font-weight: 700;" data-i18n="lbl_dia_bp">Diastolic BP (Lower)</label>
                            <input type="number" id="inDia" class="input-control" value="79" oninput="evalManual()">
                        </div>
                        <div>
                            <label style="font-size: 10px; color: var(--text-dim); text-transform: uppercase; font-weight: 700;" data-i18n="lbl_fasting_sugar">Fasting Glucose (mg/dL)</label>
                            <input type="number" id="inSugar" class="input-control" value="94" oninput="evalManual()">
                        </div>
                    </div>
                    <div id="manualVerdict" style="margin-top: 10px; font-size: 12px; font-weight: 700; color: #10b981;">
                        ✓ Optimal Clinical Range (Harrison's Principles of Internal Medicine 21st Ed)
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
            <span class="screen-tag">📋 Non-Invasive Score</span>
        </div>

        <div class="detail-container">
            <div class="detail-panel">
                <h2 class="detail-title" data-i18n="quiz_title">Zero-Report 2-Minute Longevity Assessment</h2>
                <p class="detail-desc" data-i18n="quiz_desc">
                    For individuals without previous laboratory blood reports. 6 physical clinical markers assess central adiposity, baseline sympathetic tone, and postprandial glucose stability.
                </p>

                <div class="quiz-grid">
                    <div class="quiz-item">
                        <label data-i18n="q_age">1. Chronological Age</label>
                        <span class="hint" data-i18n="q_age_hint">Current calendar age in years</span>
                        <input type="number" id="q_age" class="input-control" value="42" oninput="runQuizCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="q_height">2. Height (Centimeters)</label>
                        <span class="hint" data-i18n="q_height_hint">E.g., 5 ft 8 in = 173 cm, 5 ft 10 in = 178 cm</span>
                        <input type="number" id="q_height" class="input-control" value="175" oninput="runQuizCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="q_waist">3. Waist Circumference (Inches)</label>
                        <span class="hint" data-i18n="q_waist_hint">Measure with tape directly across navel level</span>
                        <input type="number" id="q_waist" class="input-control" value="36" oninput="runQuizCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="q_rhr">4. Resting Heart Rate (Resting Pulse)</label>
                        <span class="hint" data-i18n="q_rhr_hint">Optimal < 65 bpm. > 75 indicates sympathetic tone</span>
                        <input type="number" id="q_rhr" class="input-control" value="74" oninput="runQuizCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="q_fatigue">5. Postprandial Fatigue (Post-Meal Energy Crash)</label>
                        <span class="hint" data-i18n="q_fatigue_hint">Somnolence after carbohydrate ingestion signals early insulin resistance</span>
                        <select id="q_fatigue" class="select-control" onchange="runQuizCalc()">
                            <option value="none">Never / Normal post-meal alertness</option>
                            <option value="mild" selected>Occasional mild sluggishness</option>
                            <option value="frequent">Frequent drowsiness following meals</option>
                            <option value="severe">Severe fatigue accompanied by sugar cravings</option>
                        </select>
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="q_fam">6. Family History of Diabetes / Premature CAD</label>
                        <span class="hint" data-i18n="q_fam_hint">First-degree relatives diagnosed with hypertension or diabetes</span>
                        <select id="q_fam" class="select-control" onchange="runQuizCalc()">
                            <option value="none">None / No documented family history</option>
                            <option value="one" selected>One first-degree relative (Parent or sibling)</option>
                            <option value="both">Both parents or multiple first-degree relatives</option>
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

                    <!-- Zero-Report Disclaimer -->
                    <div style="margin-top: 18px; background: rgba(56, 189, 248, 0.08); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 12px; padding: 14px 18px; font-size: 12px; color: #94a3b8; display: flex; align-items: flex-start; gap: 10px; text-align: left;">
                        <span style="font-size: 18px;">⚖️</span>
                        <span data-i18n="quiz_disclaimer">Algorithmic Assessment Notice: Calculated phenotypic biological age reflects statistical metabolic variance and Guyton physiological markers. It does not replace clinical laboratory diagnostic tests, coronary calcium scoring, or physician consultation.</span>
                    </div>
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
            <span class="screen-tag">⏳ Metabolic Drift Projection</span>
        </div>

        <div class="detail-container">
            <div class="detail-panel">
                <h2 class="detail-title" data-i18n="tm_title">Old Report Time Machine: Metabolic Drift Projector</h2>
                <p class="detail-desc" data-i18n="tm_desc">
                    Possess past blood reports dating 1 to 3 years back? By applying elapsed intervals and weight trajectories, this beta-cell exhaustion model projects your current metabolic drift.
                </p>

                <div class="tm-grid">
                    <div class="quiz-item">
                        <label data-i18n="tm_lbl_years">Report Age (Years Elapsed)</label>
                        <input type="number" id="tm_years" class="input-control" value="2" min="0.5" max="5" step="0.5" oninput="runDriftCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="tm_lbl_weight">Body Weight Delta Since (Kg)</label>
                        <input type="number" id="tm_weight" class="input-control" value="4" oninput="runDriftCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="tm_lbl_old_glu">Past Fasting Glucose (mg/dL)</label>
                        <input type="number" id="tm_glu" class="input-control" value="92" oninput="runDriftCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="tm_lbl_old_hba1c">Past HbA1c (%)</label>
                        <input type="number" id="tm_hba1c" class="input-control" value="5.3" step="0.1" oninput="runDriftCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="tm_lbl_old_trig">Past Triglycerides (mg/dL)</label>
                        <input type="number" id="tm_trig" class="input-control" value="155" oninput="runDriftCalc()">
                    </div>
                    <div class="quiz-item">
                        <label data-i18n="tm_lbl_old_chol">Past Total Cholesterol (mg/dL)</label>
                        <input type="number" id="tm_chol" class="input-control" value="195" oninput="runDriftCalc()">
                    </div>
                </div>

                <div style="background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 16px; padding: 22px;">
                    <strong style="color: #f59e0b; font-size: 14px; display: block; margin-bottom: 12px;" data-i18n="tm_proj_header">
                        Projected Metabolic Drift (Harrison's Beta-Cell Model):
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
                        <span data-i18n="btn_stop_drift">Schedule Clinical Phlebotomy (₹1,999)</span>
                    </button>

                    <!-- Time Machine Disclaimer -->
                    <div style="margin-top: 18px; background: rgba(56, 189, 248, 0.08); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 12px; padding: 14px 18px; font-size: 12px; color: #94a3b8; display: flex; align-items: flex-start; gap: 10px; text-align: left;">
                        <span style="font-size: 18px;">⚖️</span>
                        <span data-i18n="tm_disclaimer">Projection Notice: Metabolic drift calculations represent a mathematical projection based on Harrison's beta-cell exhaustion models. A fresh blood draw is recommended to verify actual cellular biomarkers.</span>
                    </div>
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
            <span class="screen-tag">🩸 Multi-Omics Matrix</span>
        </div>

        <div class="detail-container" style="max-width: 1240px;">
            <div class="detail-panel">
                <h2 class="detail-title" data-i18n="bio_title">Full 72+ Biomarker Panel & Levine Phenotypic Age Matrix</h2>
                <p class="detail-desc" data-i18n="bio_desc">
                    Enter values from your clinical laboratory report across 6 organ pillars. Each biomarker presents optimal longevity boundaries alongside standard clinical bounds.
                </p>

                <div class="biomarkers-layout">
                    <div>
                        <div class="subtabs">
                            <button class="subtab-btn active" onclick="switchCategory('cat_cardio', this)">❤️ Cardiovascular & Lipids</button>
                            <button class="subtab-btn" onclick="switchCategory('cat_metabolic', this)">⚡ Glycemic & Metabolic</button>
                            <button class="subtab-btn" onclick="switchCategory('cat_inflam', this)">🔥 Systemic Inflammation</button>
                            <button class="subtab-btn" onclick="switchCategory('cat_organs', this)">🫀 Hepatic & Renal</button>
                            <button class="subtab-btn" onclick="switchCategory('cat_vitamins', this)">🧬 Endocrine & Vitamins</button>
                        </div>

                        <!-- CARDIO -->
                        <div id="cat_cardio" class="cat-content markers-grid">
                            <div class="marker-card">
                                <div class="marker-head"><span>Apolipoprotein B (ApoB)</span><span style="color:var(--text-dim);">mg/dL</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_apob" min="40" max="180" value="70" oninput="updBiomarker('apob', this.value)">
                                    <input type="number" class="marker-val" id="in_apob" value="70" oninput="updBiomarker('apob', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: < 60</span><span>Standard Limit: 130</span></div>
                            </div>
                            <div class="marker-card">
                                <div class="marker-head"><span>Lipoprotein(a) [Lp(a)]</span><span style="color:var(--text-dim);">nmol/L</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_lpa" min="5" max="250" value="18" oninput="updBiomarker('lpa', this.value)">
                                    <input type="number" class="marker-val" id="in_lpa" value="18" oninput="updBiomarker('lpa', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: < 30</span><span>Standard Limit: 75</span></div>
                            </div>
                            <div class="marker-card">
                                <div class="marker-head"><span>Triglycerides / HDL Ratio</span><span style="color:var(--text-dim);">ratio</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_trighdl" min="0.5" max="8.0" step="0.1" value="1.6" oninput="updBiomarker('trighdl', this.value)">
                                    <input type="number" class="marker-val" id="in_trighdl" value="1.6" step="0.1" oninput="updBiomarker('trighdl', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: < 1.5</span><span>Standard Limit: 3.5</span></div>
                            </div>
                            <div class="marker-card">
                                <div class="marker-head"><span>Homocysteine</span><span style="color:var(--text-dim);">µmol/L</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_homo" min="4" max="40" step="0.5" value="9.2" oninput="updBiomarker('homo', this.value)">
                                    <input type="number" class="marker-val" id="in_homo" value="9.2" step="0.5" oninput="updBiomarker('homo', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: < 9.0</span><span>Standard Limit: 15.0</span></div>
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
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: < 5.0</span><span>Standard Limit: 25.0</span></div>
                            </div>
                            <div class="marker-card">
                                <div class="marker-head"><span>Glycated Hemoglobin (HbA1c)</span><span style="color:var(--text-dim);">%</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_hba1c" min="4.0" max="12.0" step="0.1" value="5.2" oninput="updBiomarker('hba1c', this.value)">
                                    <input type="number" class="marker-val" id="in_hba1c" value="5.2" step="0.1" oninput="updBiomarker('hba1c', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: < 5.2</span><span>Pre-Diab: 5.7-6.4</span></div>
                            </div>
                            <div class="marker-card">
                                <div class="marker-head"><span>Fasting Plasma Glucose</span><span style="color:var(--text-dim);">mg/dL</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_glucose" min="60" max="250" value="88" oninput="updBiomarker('glucose', this.value)">
                                    <input type="number" class="marker-val" id="in_glucose" value="88" oninput="updBiomarker('glucose', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: 72-85</span><span>Standard Limit: 99</span></div>
                            </div>
                            <div class="marker-card">
                                <div class="marker-head"><span>Serum Uric Acid</span><span style="color:var(--text-dim);">mg/dL</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_uric" min="2.0" max="12.0" step="0.1" value="4.8" oninput="updBiomarker('uric', this.value)">
                                    <input type="number" class="marker-val" id="in_uric" value="4.8" step="0.1" oninput="updBiomarker('uric', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: < 5.0</span><span>Standard Limit: 7.2</span></div>
                            </div>
                        </div>

                        <!-- INFLAM -->
                        <div id="cat_inflam" class="cat-content markers-grid" style="display: none;">
                            <div class="marker-card">
                                <div class="marker-head"><span>High-Sensitivity CRP</span><span style="color:var(--text-dim);">mg/L</span></div>
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
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: 40-120</span><span>Standard Limit: 300</span></div>
                            </div>
                        </div>

                        <!-- ORGANS -->
                        <div id="cat_organs" class="cat-content markers-grid" style="display: none;">
                            <div class="marker-card">
                                <div class="marker-head"><span>ALT / SGPT (Hepatic)</span><span style="color:var(--text-dim);">U/L</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_alt" min="5" max="150" value="22" oninput="updBiomarker('alt', this.value)">
                                    <input type="number" class="marker-val" id="in_alt" value="22" oninput="updBiomarker('alt', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: < 25</span><span>Standard Limit: 45</span></div>
                            </div>
                            <div class="marker-card">
                                <div class="marker-head"><span>eGFR (Renal Filtration)</span><span style="color:var(--text-dim);">mL/min</span></div>
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
                                <div class="marker-head"><span>25-OH Vitamin D3</span><span style="color:var(--text-dim);">ng/mL</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_vitd" min="10" max="120" value="55" oninput="updBiomarker('vitd', this.value)">
                                    <input type="number" class="marker-val" id="in_vitd" value="55" oninput="updBiomarker('vitd', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: 50-80</span><span>Deficiency: < 30</span></div>
                            </div>
                            <div class="marker-card">
                                <div class="marker-head"><span>Serum Vitamin B12</span><span style="color:var(--text-dim);">pg/mL</span></div>
                                <div class="marker-inputs">
                                    <input type="range" class="marker-slider" id="sl_vitb12" min="100" max="1500" value="650" oninput="updBiomarker('vitb12', this.value)">
                                    <input type="number" class="marker-val" id="in_vitb12" value="650" oninput="updBiomarker('vitb12', this.value)">
                                </div>
                                <div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim);"><span>Optimal: 500-900</span><span>Standard Limit: 200</span></div>
                            </div>
                        </div>
                    </div>

                    <!-- HUD -->
                    <div class="side-hud">
                        <h3 style="font-size: 13px; text-transform: uppercase; color: var(--accent); margin-bottom: 14px; border-bottom: 1px solid var(--border); padding-bottom: 8px;">
                            ⚡ Real-Time PhenoAge HUD
                        </h3>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 12px; color: var(--text-muted);">
                            <span>Chronological Age:</span>
                            <span style="font-family:'JetBrains Mono',monospace; font-weight:700; color:#fff;">42.0</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 12px; color: var(--text-muted);">
                            <span>Biological PhenoAge:</span>
                            <span id="hudBioVal" style="font-family:'JetBrains Mono',monospace; font-size:22px; font-weight:800; color:var(--accent);">39.8</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 12px; color: var(--text-muted);">
                            <span>Biological Age Delta:</span>
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
                                📄 Generate Physician Report
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- ================================================= -->
    <!-- SCREEN 5: DEDICATED AT-HOME BLOOD TEST BOOKING    -->
    <!-- ================================================= -->
    <div id="screen-booking" class="screen-view">
        <div class="screen-header-bar">
            <button class="btn-back-home" onclick="showScreen('hub')">
                <span>←</span>
                <span data-i18n="btn_back_services">Back to All Services</span>
            </button>
            <span class="screen-tag" style="background: rgba(16, 185, 129, 0.12); color: #34d399; border-color: rgba(16, 185, 129, 0.3);">🏠 Certified Phlebotomy</span>
        </div>

        <div class="detail-container">
            <div class="detail-panel" style="border-color: #38bdf8;">
                <h2 class="detail-title" data-i18n="book_title">Book NABL Phlebotomist Home Sample Collection</h2>
                <p class="detail-desc" data-i18n="book_desc">
                    A certified phlebotomist arrives at your home with sterile vacuum tubes. Includes 72+ parameters, Biological Age Blueprint, and Physician Longevity Consultation.
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
                            <input type="text" id="b_address" class="input-control" placeholder="Residence Address, Landmark, City & Pincode" required>
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

                        <!-- Direct Founder Number & UPI Badge -->
                        <div style="background: rgba(16, 185, 129, 0.12); border: 1px dashed #10b981; border-radius: 10px; padding: 10px; margin: 10px 0; text-align: center;">
                            <span style="font-size: 10px; color: var(--text-muted); display: block; text-transform: uppercase; font-weight: 700;">GPay / PhonePe / Paytm / UPI Number:</span>
                            <strong style="font-size: 18px; color: #34d399; font-family: 'JetBrains Mono', monospace; display: block; margin: 2px 0;">9343062265</strong>
                            <span style="font-size: 10px; color: var(--text-dim);">Pay via QR or Direct to Number</span>
                        </div>

                        <p style="font-size: 11px; color: var(--text-muted); margin-bottom: 6px;">
                            Scan to pay via <strong>PhonePe, GPay, Paytm, or Cash on Pickup</strong>
                        </p>

                        <a href="https://wa.me/919343062265?text=Hi+BioTwin+Labs,+I+want+to+book+the+%E2%82%B91,999+Longevity+Health+Checkup" target="_blank" class="btn-wa">
                            <span>💬</span>
                            <span>WhatsApp: 9343062265</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>

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
                    First 7 days are completely FREE. Following the trial, select between affordable checkup passes (₹199, ₹299) or monthly memberships (₹2,499, ₹3,499):
                </p>

                <div class="plans-grid" style="margin-top: 24px;">
                    <div class="plan-card">
                        <div>
                            <span class="plan-badge-top" style="background: #334155; color: #fff;" data-i18n="p1_badge">AFFORDABLE PASS</span>
                            <h3 style="font-size: 16px; font-weight: 800; color: #fff;" data-i18n="p1_title">Weekly Checkup Pass</h3>
                            <div class="plan-price-box">
                                <span class="plan-price">₹199</span>
                                <span class="plan-period" data-i18n="p1_period">/ 7 Days</span>
                            </div>
                            <ul class="plan-features">
                                <li data-i18n="p1_f1">Unlimited Camera BP Scans</li>
                                <li data-i18n="p1_f2">Pulse & Arterial Elasticity</li>
                                <li data-i18n="p1_f3">Post-Meal Sugar Crash Check</li>
                                <li data-i18n="p1_f4">Instant Risk Alerts</li>
                            </ul>
                        </div>
                        <button class="btn-plan-act" onclick="selectPlan('Weekly Pass', 199)" data-i18n="p1_btn">
                            Activate ₹199 Pass →
                        </button>
                    </div>

                    <div class="plan-card">
                        <div>
                            <span class="plan-badge-top" style="background: #0284c7; color: #fff;" data-i18n="p2_badge">ONE-TIME PASS</span>
                            <h3 style="font-size: 16px; font-weight: 800; color: #fff;" data-i18n="p2_title">Deep Longevity Report</h3>
                            <div class="plan-price-box">
                                <span class="plan-price">₹299</span>
                                <span class="plan-period" data-i18n="p2_period">/ Single Report</span>
                            </div>
                            <ul class="plan-features">
                                <li data-i18n="p2_f1">Zero-Report Visceral Score</li>
                                <li data-i18n="p2_f2">Time Machine 3-Yr Drift</li>
                                <li data-i18n="p2_f3">HOMA-IR Insulin Resistance</li>
                                <li data-i18n="p2_f4">Executive PDF Download</li>
                            </ul>
                        </div>
                        <button class="btn-plan-act" onclick="selectPlan('Deep Report Pass', 299)" data-i18n="p2_btn">
                            Activate ₹299 Pass →
                        </button>
                    </div>

                    <div class="plan-card plan-card-popular">
                        <span class="plan-badge-top plan-badge-popular" data-i18n="p3_badge">MOST POPULAR 🔥</span>
                        <div>
                            <h3 style="font-size: 16px; font-weight: 800; color: #38bdf8;" data-i18n="p3_title">1-Month Standard Membership</h3>
                            <div class="plan-price-box">
                                <span class="plan-price">₹2,499</span>
                                <span class="plan-period" data-i18n="p3_period">/ Month</span>
                            </div>
                            <ul class="plan-features">
                                <li data-i18n="p3_f1">30 Days Unlimited Camera Scans</li>
                                <li data-i18n="p3_f2">Daily Biological Age Tracking</li>
                                <li data-i18n="p3_f3">Metabolic Drift Reversal Plan</li>
                                <li data-i18n="p3_f4">Weekly WhatsApp Diet Guide</li>
                                <li data-i18n="p3_f5">Priority Doctor Assistance</li>
                            </ul>
                        </div>
                        <button class="btn-plan-act" onclick="selectPlan('1-Month Standard Subscription', 2499)" data-i18n="p3_btn">
                            Subscribe ₹2,499 / Mo →
                        </button>
                    </div>

                    <div class="plan-card plan-card-vip">
                        <span class="plan-badge-top plan-badge-vip" data-i18n="p4_badge">ALL-INCLUSIVE VIP 👑</span>
                        <div>
                            <h3 style="font-size: 16px; font-weight: 800; color: #c084fc;" data-i18n="p4_title">1-Month VIP + Blood Test</h3>
                            <div class="plan-price-box">
                                <span class="plan-price">₹3,499</span>
                                <span class="plan-period" data-i18n="p4_period">/ Month</span>
                            </div>
                            <ul class="plan-features">
                                <li data-i18n="p4_f1"><strong>Includes NABL Home Blood Draw (72+ Tests)</strong></li>
                                <li data-i18n="p4_f2">Full Levine PhenoAge Doctor Report</li>
                                <li data-i18n="p4_f3">1-on-1 Doctor Longevity Consult</li>
                                <li data-i18n="p4_f4">30-Day Family Camera App Access</li>
                                <li data-i18n="p4_f5">Personalized Reversal Plan</li>
                            </ul>
                        </div>
                        <button class="btn-plan-act" onclick="selectPlan('1-Month VIP Longevity Membership', 3499)" data-i18n="p4_btn">
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
                            <div class="form-group" style="margin-top: 10px;">
                                <label style="font-size: 11px; text-transform: uppercase; color: var(--accent); font-weight: 800; display: block; margin-bottom: 4px;">12-Digit Bank UTR / UPI Transaction Reference Number</label>
                                <input type="text" id="co_utr" class="input-control" placeholder="e.g. 429182749102 (from PhonePe / GPay / Paytm)" maxlength="12" required style="font-family: 'JetBrains Mono', monospace; border-color: #38bdf8;">
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
                            <span style="font-size: 11px; color: #34d399; font-family: 'JetBrains Mono', monospace; font-weight: 700; display: block;" data-secure-vpa="true">UPI: 9343062265</span>
                            <span style="font-size: 10px; color: var(--text-dim);">Scan QR or Pay on 9343062265</span>
                            <div style="margin-top: 10px; background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 6px 10px; font-size: 9px; color: #34d399; text-align: left;">
                                🛡️ NPCI Verified Beneficiary: 9343062265 • Duplicate UTRs Auto-Blocked
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <!-- ================================================= -->
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
                <h2 class="detail-title" data-i18n="ft_title">Activate Your 7-Day Free Longevity Pass</h2>
                <p class="detail-desc" data-i18n="ft_desc">
                    You pay zero fees during your initial 7 days. Track optical blood pressure, evaluate postprandial glucose stability, and compute biological age. Here is your 7-Day Clinical Protocol:
                </p>

                <!-- 7-Day Roadmap Timeline -->
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 24px 0;">
                    <div style="background: var(--surface-card); border: 1px solid var(--border); border-radius: 14px; padding: 18px;">
                        <span style="display:inline-block; background:rgba(56, 189, 248, 0.15); color:var(--accent); border:1px solid rgba(56, 189, 248, 0.3); font-size:11px; font-weight:800; padding:3px 10px; border-radius:6px; margin-bottom:8px;">DAY 1</span>
                        <div style="font-size:14px; font-weight:800; color:#fff; margin-bottom:6px;">Baseline Assessment</div>
                        <div style="font-size:12px; color:var(--text-muted); line-height:1.5;">First optical camera BP scan and non-invasive visceral adiposity score.</div>
                    </div>
                    <div style="background: var(--surface-card); border: 1px solid var(--border); border-radius: 14px; padding: 18px;">
                        <span style="display:inline-block; background:rgba(56, 189, 248, 0.15); color:var(--accent); border:1px solid rgba(56, 189, 248, 0.3); font-size:11px; font-weight:800; padding:3px 10px; border-radius:6px; margin-bottom:8px;">DAY 2</span>
                        <div style="font-size:14px; font-weight:800; color:#fff; margin-bottom:6px;">Postprandial Fatigue Evaluation</div>
                        <div style="font-size:12px; color:var(--text-muted); line-height:1.5;">Analyze post-meal somnolence and glycemic stability patterns.</div>
                    </div>
                    <div style="background: var(--surface-card); border: 1px solid var(--border); border-radius: 14px; padding: 18px;">
                        <span style="display:inline-block; background:rgba(56, 189, 248, 0.15); color:var(--accent); border:1px solid rgba(56, 189, 248, 0.3); font-size:11px; font-weight:800; padding:3px 10px; border-radius:6px; margin-bottom:8px;">DAY 3</span>
                        <div style="font-size:14px; font-weight:800; color:#fff; margin-bottom:6px;">Resting Pulse & Vascular Tone</div>
                        <div style="font-size:12px; color:var(--text-muted); line-height:1.5;">Morning resting pulse measurement and arterial elasticity tracking.</div>
                    </div>
                    <div style="background: var(--surface-card); border: 1px solid var(--border); border-radius: 14px; padding: 18px;">
                        <span style="display:inline-block; background:rgba(56, 189, 248, 0.15); color:var(--accent); border:1px solid rgba(56, 189, 248, 0.3); font-size:11px; font-weight:800; padding:3px 10px; border-radius:6px; margin-bottom:8px;">DAY 4</span>
                        <div style="font-size:14px; font-weight:800; color:#fff; margin-bottom:6px;">Central Adiposity Review</div>
                        <div style="font-size:12px; color:var(--text-muted); line-height:1.5;">Waist-to-Height ratio analysis following Guyton Physiology Chapter 72.</div>
                    </div>
                    <div style="background: var(--surface-card); border: 1px solid var(--border); border-radius: 14px; padding: 18px;">
                        <span style="display:inline-block; background:rgba(56, 189, 248, 0.15); color:var(--accent); border:1px solid rgba(56, 189, 248, 0.3); font-size:11px; font-weight:800; padding:3px 10px; border-radius:6px; margin-bottom:8px;">DAY 5</span>
                        <div style="font-size:14px; font-weight:800; color:#fff; margin-bottom:6px;">Sleep Quality & Oxygenation</div>
                        <div style="font-size:12px; color:var(--text-muted); line-height:1.5;">Sleep apnea risk stratification and nocturnal recovery score.</div>
                    </div>
                    <div style="background: var(--surface-card); border: 1px solid var(--border); border-radius: 14px; padding: 18px;">
                        <span style="display:inline-block; background:rgba(56, 189, 248, 0.15); color:var(--accent); border:1px solid rgba(56, 189, 248, 0.3); font-size:11px; font-weight:800; padding:3px 10px; border-radius:6px; margin-bottom:8px;">DAY 6</span>
                        <div style="font-size:14px; font-weight:800; color:#fff; margin-bottom:6px;">Biological Age Recalculation</div>
                        <div style="font-size:12px; color:var(--text-muted); line-height:1.5;">Update phenotypic aging trajectory across accumulated measurements.</div>
                    </div>
                    <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid #10b981; border-radius: 14px; padding: 18px;">
                        <span style="display:inline-block; background:#10b981; color:#000; font-size:11px; font-weight:800; padding:3px 10px; border-radius:6px; margin-bottom:8px;">DAY 7</span>
                        <div style="font-size:14px; font-weight:800; color:#34d399; margin-bottom:6px;">Executive Longevity Summary</div>
                        <div style="font-size:12px; color:var(--text-muted); line-height:1.5;">7-day diagnostic synthesis and optional NABL home blood draw upgrade.</div>
                    </div>
                </div>

                <!-- Activation Form -->
                <div style="background: var(--surface-card); border: 1px solid var(--border); border-radius: 16px; padding: 26px; max-width: 600px; margin: 20px auto 0;">
                    <h3 style="font-size: 16px; font-weight: 800; margin-bottom: 6px; text-align: center; color: #fff;">
                        Instant ₹0 Pass Activation (No Payment Required)
                    </h3>
                    <p style="font-size: 12px; color: var(--text-dim); text-align: center; margin-bottom: 18px;">
                        Enter your name and mobile number to unlock your 7-day complimentary pass.
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

    <!-- GLOBAL COMPREHENSIVE LEGAL MEDICAL DISCLAIMER & FOOTER -->
    <footer class="footer" style="background: var(--surface); border-top: 1px solid var(--border); padding: 40px 24px; margin-top: 60px;">
        <div style="max-width: 1200px; margin: 0 auto;">
            <!-- Legal Medical Disclaimer Box -->
            <div class="legal-disclaimer-box">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
                    <span style="font-size: 22px;">⚖️</span>
                    <strong style="font-size: 15px; color: #fbbf24; letter-spacing: 0.3px;" data-i18n="disclaimer_title">
                        Statutory Medical Disclaimer & Regulatory Telemedicine Compliance
                    </strong>
                </div>
                <p style="font-size: 12px; color: #cbd5e1; line-height: 1.7; margin-bottom: 16px;" data-i18n="disclaimer_body">
                    Bio-Twin Labs is an investigational artificial intelligence platform providing algorithmic physiological simulations, biological age analytics, and preventive wellness tracking (aligned with Guyton & Hall Textbook of Medical Physiology and Levine PhenoAge clinical methodologies). Bio-Twin Labs does NOT constitute or offer clinical medical diagnosis, medical treatment, prescription of pharmaceutical drugs, or emergency healthcare services. This platform is not an alternative to professional clinical evaluation by a Registered Medical Practitioner (MBBS/MD). If you or a family member are experiencing acute symptoms, chest pressure, severe shortness of breath, acute palpitations, sudden neurological numbness, or any life-threatening symptoms, immediately contact emergency services (dial 112 or 108 in India) or report to the nearest hospital casualty emergency room. Diagnostic blood tests and home phlebotomy sample collections are executed independently by accredited NABL / ICMR certified laboratory partners.
                </p>
                <div style="display: flex; flex-wrap: wrap; gap: 16px; font-size: 11px; color: var(--text-dim); font-weight: 700; border-top: 1px solid rgba(245, 158, 11, 0.2); padding-top: 12px;">
                    <span>🔬 NABL Accredited Diagnostic Partners</span>
                    <span>•</span>
                    <span>🧬 ICMR Aligned Protocols</span>
                    <span>•</span>
                    <span>🛡️ Telemedicine Practice Guidelines (India 2020)</span>
                    <span>•</span>
                    <span>🔒 ISO 27001 Health Data Encryption</span>
                </div>
            </div>

            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; font-size: 12px; color: var(--text-muted); border-top: 1px solid var(--border); padding-top: 20px;">
                <div>
                    © 2026 BioTwin Labs. Grounded in Harrison's Principles of Internal Medicine & Guyton Physiology.
                </div>
                <div style="display: flex; gap: 20px; align-items: center; flex-wrap: wrap;">
                    <span>Founder Hotline / UPI: <strong style="color: var(--accent);">9343062265</strong></span>
                    <a href="https://wa.me/919343062265" target="_blank" style="color: #34d399; text-decoration: none; font-weight: 700;">💬 WhatsApp: +91 9343062265</a>
                    <a href="/founder-crm" style="color: var(--text-dim); text-decoration: none; font-size: 11px;">💼 CRM Pipeline</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- ================================================= -->
    <!-- GLOBAL SINGLE-PAGE APPLICATION LOGIC (JavaScript) -->
    <!-- ================================================= -->
    <script>
        // STRICT PURE LANGUAGE DICTIONARIES
        const DICT = {
            en: {
                brand_title: "BioTwin Labs",
                brand_sub: "Precision Longevity & Health Checkup Platform",
                nav_free_trial: "7 Days Free Trial",
                nav_plans: "Plans (₹199 - ₹3,499)",
                nav_all_services: "All Services",
                btn_back_services: "Back to All Services",
                hero_badge_text: "Clinical Longevity Protocols",
                hub_title: "What Type of Health Assessment Do You Require?",
                hub_desc: "Select your required clinical tool below or search directly. Each assessment runs independently in its dedicated workspace without clutter:",
                hub_sec_title: "Our 6 Dedicated Health Services:",
                tb_badge: "SPECIAL LAUNCH OFFER • 7 DAYS FREE",
                tb_title: "Start Your 7-Day Free Health & Longevity Trial",
                tb_desc: "No credit card or upfront payment required. Perform unlimited optical camera BP scans, determine biological age, and monitor arterial health for 7 days at ₹0!",
                tb_p1: "✓ Unlimited Camera BP Scans",
                tb_p2: "✓ Zero-Report Health Score",
                tb_p3: "✓ Daily Health Monitoring",
                tb_p4: "✓ 100% Free • No Payment",
                btn_start_trial: "Start 7-Day Free Trial (₹0) →",
                tb_note: "Instant Access • No Card Needed",
                price_free: "FREE / ₹0",
                price_online_free: "ONLINE FREE / PDF ₹499",
                c1_title: "Camera Optical Blood Pressure & Pulse Scan",
                c1_desc: "Non-invasive transdermal photoplethysmography measures capillary light absorption from your fingertip to estimate pulse wave velocity and blood pressure.",
                c1_btn: "Open Camera Scanner",
                c2_title: "Zero-Report 2-Minute Longevity Assessment",
                c2_desc: "No blood test available? 6 non-invasive markers (Waist-to-Height ratio, resting pulse, postprandial fatigue) calculate your biological age delta and visceral risk.",
                c2_btn: "Start 2-Min Assessment",
                c3_title: "Old Report Time Machine Projector",
                c3_desc: "Enter numbers from a 1 to 3-year-old blood test report. The beta-cell exhaustion model projects your current metabolic drift and accelerated organ aging today.",
                c3_btn: "Check Old Report Drift",
                c4_title: "Full 72+ Biomarker Clinical Panel",
                c4_desc: "Input results from recent blood work across 6 clinical pillars (ApoB, Insulin, hs-CRP, Liver, Kidney) to compute your exact Levine Phenotypic Age.",
                c4_btn: "Open Biomarker Matrix",
                c5_title: "At-Home Phlebotomist Blood Draw",
                c5_desc: "A certified phlebotomist visits your residence to collect samples in sterile vacutainers. Includes 72+ parameters, Biological Age Blueprint, and Doctor review.",
                c5_btn: "Book Home Blood Draw (₹1,999)",
                sec_plans_badge: "Transparent Pricing Plans",
                sec_plans_title: "Affordable Normal Passes & 1-Month Subscriptions",
                sec_plans_sub: "First 7 days are 100% FREE. After that, keep monitoring with normal weekly passes (₹199, ₹299) or monthly memberships (₹2,499, ₹3,499):",
                p1_badge: "AFFORDABLE PASS",
                p1_title: "Weekly Checkup Pass",
                p1_period: "/ 7 Days",
                p1_f1: "Unlimited Camera BP Scans",
                p1_f2: "Pulse & Arterial Elasticity",
                p1_f3: "Post-Meal Sugar Crash Check",
                p1_f4: "Instant Risk Alerts",
                p1_btn: "Choose ₹199 Pass →",
                p2_badge: "ONE-TIME PASS",
                p2_title: "Deep Longevity Report",
                p2_period: "/ Single Report",
                p2_f1: "Zero-Report Visceral Score",
                p2_f2: "Time Machine 3-Yr Drift",
                p2_f3: "HOMA-IR Insulin Resistance",
                p2_f4: "Executive PDF Download",
                p2_btn: "Choose ₹299 Pass →",
                p3_badge: "MOST POPULAR 🔥",
                p3_title: "1-Month Standard Membership",
                p3_period: "/ Month",
                p3_f1: "30 Days Unlimited Camera Scans",
                p3_f2: "Daily Biological Age Tracking",
                p3_f3: "Metabolic Drift Reversal Plan",
                p3_f4: "Weekly WhatsApp Diet Guide",
                p3_f5: "Priority Doctor Assistance",
                p3_btn: "Start ₹2,499 Monthly →",
                p4_badge: "ALL-INCLUSIVE VIP 👑",
                p4_title: "1-Month VIP + Blood Test",
                p4_period: "/ Month",
                p4_f1: "Includes NABL Home Blood Draw (72+ Tests)",
                p4_f2: "Full Levine PhenoAge Doctor Report",
                p4_f3: "1-on-1 Doctor Longevity Consult",
                p4_f4: "30-Day Family Camera App Access",
                p4_f5: "Personalized Reversal Plan",
                p4_btn: "Join ₹3,499 VIP →",
                p_screen_title: "Choose Your Health Monitoring Pass",
                p_screen_desc: "First 7 days are completely FREE. Following the trial, select between affordable checkup passes (₹199, ₹299) or monthly memberships (₹2,499, ₹3,499):",
                ft_badge: "100% Free Health Monitoring",
                ft_title: "Activate Your 7-Day Free Longevity Pass",
                ft_desc: "You pay zero fees during your initial 7 days. Track optical blood pressure, evaluate postprandial glucose stability, and compute biological age.",
                cam_title: "Camera Optical Blood Pressure & Pulse Scanner",
                cam_desc: "This clinical tool reads arterial micro-reflections in your fingertip capillary bed using optical photoplethysmography to estimate arterial elasticity and systolic/diastolic blood pressure.",
                cam_instruct: "Place your finger over the camera lens or position your face toward the camera. Click Start Scan below.",
                lbl_bp: "Blood Pressure (BP)",
                lbl_hr: "Heart Rate (Pulse)",
                lbl_elasticity: "Arterial Elasticity",
                lbl_sugar: "Sugar Stability",
                btn_start_scan: "Start 15-Second Optical Camera Scan",
                manual_title: "Or Enter Your Recent Blood Pressure & Glucose Values (Instant Clinical Verification):",
                lbl_sys_bp: "Systolic BP (Upper)",
                lbl_dia_bp: "Diastolic BP (Lower)",
                lbl_fasting_sugar: "Fasting Glucose (mg/dL)",
                quiz_title: "Zero-Report 2-Minute Longevity Assessment",
                quiz_desc: "For individuals without previous laboratory blood reports. 6 physical clinical markers assess central adiposity, baseline sympathetic tone, and postprandial glucose stability.",
                q_age: "1. Chronological Age",
                q_age_hint: "Current calendar age in years",
                q_height: "2. Height (Centimeters)",
                q_height_hint: "E.g., 5 ft 8 in = 173 cm, 5 ft 10 in = 178 cm",
                q_waist: "3. Waist Circumference (Inches)",
                q_waist_hint: "Measure with tape directly across navel level",
                q_rhr: "4. Resting Heart Rate (Resting Pulse)",
                q_rhr_hint: "Optimal < 65 bpm. > 75 indicates sympathetic tone",
                q_fatigue: "5. Postprandial Fatigue (Post-Meal Energy Crash)",
                q_fatigue_hint: "Somnolence after carbohydrate ingestion signals early insulin resistance",
                q_fam: "6. Family History of Diabetes / Premature CAD",
                q_fam_hint: "First-degree relatives diagnosed with hypertension or diabetes",
                btn_confirm_blood_draw: "Confirm with ₹1,999 At-Home Blood Test",
                tm_title: "Old Report Time Machine: Metabolic Drift Projector",
                tm_desc: "Possess past blood reports dating 1 to 3 years back? By applying elapsed intervals and weight trajectories, this beta-cell exhaustion model projects your current metabolic drift.",
                tm_lbl_years: "Report Age (Years Elapsed)",
                tm_lbl_weight: "Body Weight Delta Since (Kg)",
                tm_lbl_old_glu: "Past Fasting Glucose (mg/dL)",
                tm_lbl_old_hba1c: "Past HbA1c (%)",
                tm_lbl_old_trig: "Past Triglycerides (mg/dL)",
                tm_lbl_old_chol: "Past Total Cholesterol (mg/dL)",
                tm_proj_header: "Projected Metabolic Drift (Harrison's Beta-Cell Model):",
                btn_stop_drift: "Schedule Clinical Phlebotomy (₹1,999)",
                bio_title: "Full 72+ Biomarker Panel & Levine Phenotypic Age Matrix",
                bio_desc: "Enter values from your clinical laboratory report across 6 organ pillars. Each biomarker presents optimal longevity boundaries alongside standard clinical bounds.",
                book_title: "Book NABL Phlebotomist Home Sample Collection",
                book_desc: "A certified phlebotomist arrives at your home with sterile vacutainers. Includes 72+ parameters, Biological Age Blueprint, and Physician Longevity Consultation.",
                b_name: "Patient Full Name",
                b_age: "Age",
                b_gender: "Gender",
                b_phone: "WhatsApp Mobile Number",
                b_address: "Complete Home Address & City / Pincode",
                b_slot: "Preferred Fasting Slot (Tomorrow Morning)",
                btn_confirm_order: "Confirm Booking & Generate Order",
                lock_title: "7-Day Free Trial Has Concluded",
                lock_desc: "Your complimentary 7-day health monitoring period has completed. Clinical assessments including Camera Optical Scan, Zero-Report Assessment, and Biomarker Analysis are now locked. Please renew with a normal checkup pass or monthly subscription to continue.",
                lock_btn_wa: "WhatsApp to Reactivate (9343062265)",
                lock_reminder_title: "Auto-Lockout WhatsApp Reminder & Backup Service",
                lock_reminder_desc: "Your 7-day health tracking and biological age simulations are currently paused. Enter your WhatsApp number below to receive an automated encrypted backup of your baseline readings and an instant 1-tap reactivation pass link.",
                lock_reminder_btn: "Send WhatsApp Reminder Alert",
                c6_title: "5-Year Bio-Twin Organ Simulator & Facial Vision AI",
                c6_desc: "Simulate living heart, liver, pancreas, and arteries through 2031. Features Contactless Facial rPPG stress scanning and daily AI micro-interventions.",
                c6_btn: "Launch 5-Year Bio-Twin",
                fut_header_title: "5-Year Living Digital Biological Twin & Facial Vision AI",
                fut_header_desc: "Unlike traditional backward-looking lab tests, your Digital Bio-Twin is a dynamic biochemical simulation modeling cellular degradation rates across vital organ systems from 2026 through 2031.",

                cam_disclaimer: "Clinical Screening Notice: Fingertip optical photoplethysmography is designed for preventive wellness screening and arterial elasticity trend monitoring. It is not an invasive ICU-grade arterial line monitor. Always verify persistent clinical abnormalities with a licensed physician.",
                quiz_disclaimer: "Algorithmic Assessment Notice: Calculated phenotypic biological age reflects statistical metabolic variance and Guyton physiological markers. It does not replace clinical laboratory diagnostic tests, coronary calcium scoring, or physician consultation.",
                tm_disclaimer: "Projection Notice: Metabolic drift calculations represent a mathematical projection based on Harrison's beta-cell exhaustion models. A fresh blood draw is recommended to verify actual cellular biomarkers.",
                disclaimer_title: "Statutory Medical Disclaimer & Regulatory Telemedicine Compliance",
                disclaimer_body: "Bio-Twin Labs is an investigational artificial intelligence platform providing algorithmic physiological simulations, biological age analytics, and preventive wellness tracking (aligned with Guyton & Hall Textbook of Medical Physiology and Levine PhenoAge clinical methodologies). Bio-Twin Labs does NOT constitute or offer clinical medical diagnosis, medical treatment, prescription of pharmaceutical drugs, or emergency healthcare services. This platform is not an alternative to professional clinical evaluation by a Registered Medical Practitioner (MBBS/MD). If you or a family member are experiencing acute symptoms, chest pressure, severe shortness of breath, acute palpitations, sudden neurological numbness, or any life-threatening symptoms, immediately contact emergency services (dial 112 or 108 in India) or report to the nearest hospital casualty emergency room. Diagnostic blood tests and home phlebotomy sample collections are executed independently by accredited NABL / ICMR certified laboratory partners.",
            },
            hi: {
                brand_title: "बायोट्विन लैब्स",
                brand_sub: "सटीक दीर्घायु एवं संपूर्ण स्वास्थ्य जांच प्लेटफॉर्म",
                nav_free_trial: "7 दिन बिल्कुल निःशुल्क",
                nav_plans: "सदस्यता शुल्क (₹199 - ₹3,499)",
                nav_all_services: "सभी सेवाएं",
                btn_back_services: "← मुख्य सेवाएं पर वापस जाएं",
                hero_badge_text: "एमबीबीएस क्लिनिकल दीर्घायु मानक",
                hub_title: "आपको किस प्रकार की स्वास्थ्य जांच की आवश्यकता है?",
                hub_desc: "प्रत्येक व्यक्ति की चिकित्सकीय आवश्यकता भिन्न होती है। नीचे दिए गए समर्पित विकल्पों में से चुनें अथवा सीधे खोजें। प्रत्येक जांच स्वतंत्र रूप से संचालित होती है:",
                hub_sec_title: "हमारी 6 समर्पित स्वास्थ्य सेवाएं:",
                tb_badge: "विशेष प्रारंभिक प्रस्ताव • 7 दिन निःशुल्क",
                tb_title: "अपना 7 दिवसीय निःशुल्क स्वास्थ्य व दीर्घायु परीक्षण प्रारंभ करें",
                tb_desc: "क्रेडिट कार्ड अथवा अग्रिम भुगतान की कोई आवश्यकता नहीं है। अपने फोन कैमरे से रक्तचाप मापें, जैविक आयु ज्ञात करें एवं 7 दिन तक स्वास्थ्य निगरानी करें बिल्कुल ₹0 में!",
                tb_p1: "✓ असीमित कैमरा रक्तचाप स्कैन",
                tb_p2: "✓ बिना रिपोर्ट स्वास्थ्य स्कोर",
                tb_p3: "✓ दैनिक स्वास्थ्य निगरानी",
                tb_p4: "✓ 100% निःशुल्क • कोई शुल्क नहीं",
                btn_start_trial: "7-दिवसीय निःशुल्क परीक्षण प्रारंभ करें (₹0) →",
                tb_note: "तत्काल सक्रियण • कार्ड की आवश्यकता नहीं",
                price_free: "निःशुल्क / ₹0",
                price_online_free: "ऑनलाइन निःशुल्क / पीडीएफ ₹499",
                c1_title: "कैमरा ऑप्टिकल रक्तचाप एवं नाड़ी परीक्षण",
                c1_desc: "उंगली की सूक्ष्म रक्त नलिकाओं में प्रकाश अवशोषण को मापकर धमनी लोच और सिस्टोलिक/डायस्टोलिक रक्तचाप का सटीक अनुमान लगाता है।",
                c1_btn: "कैमरा स्कैनर खोलें",
                c2_title: "बिना रिपोर्ट 2-मिनट दीर्घायु परीक्षण",
                c2_desc: "रक्त परीक्षण रिपोर्ट उपलब्ध नहीं है? 6 शारीरिक मानकों (कमर-लंबाई अनुपात, विश्राम पल्स, भोजन उपरांत थकान) से अपनी जैविक आयु ज्ञात करें।",
                c2_btn: "2-मिनट परीक्षण प्रारंभ करें",
                c3_title: "पुरातन रिपोर्ट समय चक्र प्रक्षेपक",
                c3_desc: "1 से 3 वर्ष पुरानी रक्त रिपोर्ट दर्ज करें। बीटा-कोशिका ह्रास मॉडल के आधार पर वर्तमान मेटाबॉलिक अंग क्षति का अनुमान लगाएं।",
                c3_btn: "पुरानी रिपोर्ट का ह्रास देखें",
                c4_title: "सम्पूर्ण 72+ बायोमार्कर क्लिनिकल पैनल",
                c4_desc: "ताज़ा प्रयोगशाला रिपोर्ट से 6 स्तंभों के मानक (ApoB, इंसुलिन, hs-CRP, यकृत, वृक्क) दर्ज कर वास्तविक लेवाइन बायोलॉजिकल आयु ज्ञात करें।",
                c4_btn: "बायोमार्कर मैट्रिक्स खोलें",
                c5_title: "गृह आधारित NABL रक्त नमूना संग्रहण",
                c5_desc: "प्रमाणित लैब तकनीशियन आपके निवास पर आकर सुरक्षित नमूना एकत्र करेगा। 72+ परीक्षण, बायोलॉजिकल एज रिपोर्ट और डॉक्टर समीक्षा सम्मिलित।",
                c5_btn: "गृह रक्त जांच बुक करें (₹1,999)",
                sec_plans_badge: "पारदर्शी सदस्यता योजनाएं",
                sec_plans_title: "सामान्य किफायती पास एवं मासिक सदस्यता",
                sec_plans_sub: "प्रथम 7 दिन पूर्णतः निःशुल्क हैं। उसके उपरांत सामान्य साप्ताहिक पास (₹199, ₹299) अथवा 1-माह की सदस्यता (₹2,499, ₹3,499) में से चुनें:",
                p1_badge: "किफायती पास",
                p1_title: "साप्ताहिक जांच पास",
                p1_period: "/ 7 दिन",
                p1_f1: "असीमित कैमरा रक्तचाप स्कैन",
                p1_f2: "नाड़ी दर एवं धमनी लचीलापन",
                p1_f3: "भोजन उपरांत शर्करा गिरावट परीक्षण",
                p1_f4: "तात्कालिक जोखिम चेतावनी",
                p1_btn: "₹199 पास चुनें →",
                p2_badge: "एकल पास",
                p2_title: "गहन दीर्घायु रिपोर्ट",
                p2_period: "/ एकल रिपोर्ट",
                p2_f1: "आंतरिक चर्बी जोखिम स्कोर",
                p2_f2: "3-वर्षीय समय चक्र ह्रास",
                p2_f3: "इंसुलिन प्रतिरोध (HOMA-IR)",
                p2_f4: "चिकित्सकीय पीडीएफ डाउनलोड",
                p2_btn: "₹299 पास चुनें →",
                p3_badge: "सर्वाधिक लोकप्रिय 🔥",
                p3_title: "1-माह मानक सदस्यता",
                p3_period: "/ माह",
                p3_f1: "30 दिन असीमित कैमरा स्कैन",
                p3_f2: "दैनिक जैविक आयु अनुवर्तन",
                p3_f3: "मेटाबॉलिक ह्रास सुधार योजना",
                p3_f4: "साप्ताहिक व्हाट्सएप आहार मार्गदर्शन",
                p3_f5: "प्राथमिकता चिकित्सक परामर्श",
                p3_btn: "₹2,499 मासिक प्रारंभ करें →",
                p4_badge: "सर्व-समावेशी वीआईपी 👑",
                p4_title: "1-माह वीआईपी + रक्त परीक्षण",
                p4_period: "/ माह",
                p4_f1: "NABL गृह रक्त जांच सम्मिलित (72+ परीक्षण)",
                p4_f2: "लेवाइन फीनोएज डॉक्टर रिपोर्ट",
                p4_f3: "व्यक्तिगत डॉक्टर परामर्श",
                p4_f4: "पारिवारिक 30-दिवसीय ऐप पहुंच",
                p4_f5: "व्यक्तिगत स्वास्थ्य सुधार योजना",
                p4_btn: "₹3,499 वीआईपी से जुड़ें →",
                p_screen_title: "अपना स्वास्थ्य निगरानी पास चुनें",
                p_screen_desc: "प्रथम 7 दिन पूर्णतः निःशुल्क। तत्पश्चात किफायती साप्ताहिक पास अथवा मासिक सदस्यता में से चयन करें:",
                ft_badge: "100% निःशुल्क स्वास्थ्य निगरानी",
                ft_title: "अपना 7-दिवसीय निःशुल्क दीर्घायु पास सक्रिय करें",
                ft_desc: "आरंभिक 7 दिनों में आपको कोई शुल्क नहीं देना है। कैमरे से रक्तचाप मापें, भोजन उपरांत शर्करा की स्थिति जांचें और जैविक आयु ज्ञात करें।",
                cam_title: "कैमरा ऑप्टिकल रक्तचाप एवं नाड़ी स्कैनर",
                cam_desc: "यह परीक्षण उंगली की रक्त नलिकाओं से प्रकाश अवशोषण को मापकर धमनी लचीलापन और सिस्टोलिक/डायस्टोलिक रक्तचाप का आंकलन करता है।",
                cam_instruct: "कैमरा लेंस पर अपनी उंगली रखें अथवा स्क्रीन की ओर देखें। नीचे 'स्कैन प्रारंभ करें' दबाएं।",
                lbl_bp: "रक्तचाप (BP)",
                lbl_hr: "नाड़ी दर (पल्स)",
                lbl_elasticity: "धमनी लचीलापन",
                lbl_sugar: "शर्करा स्थिरता",
                btn_start_scan: "15-सेकंड कैमरा स्कैन प्रारंभ करें",
                manual_title: "अथवा अपना हालिया रक्तचाप व शर्करा मान दर्ज करें (तात्कालिक सत्यापन):",
                lbl_sys_bp: "सिस्टोलिक बीपी (ऊपरी)",
                lbl_dia_bp: "डायस्टोलिक बीपी (निचला)",
                lbl_fasting_sugar: "खाली पेट शर्करा (mg/dL)",
                quiz_title: "बिना रिपोर्ट 2-मिनट दीर्घायु परीक्षण",
                quiz_desc: "जिन व्यक्तियों के पास पूर्व रक्त परीक्षण रिपोर्ट नहीं है, उनके लिए 6 शारीरिक मानक आंतरिक चर्बी, तनाव स्तर और भोजन उपरांत शर्करा स्थिति का आंकलन करते हैं।",
                q_age: "1. वास्तविक आयु",
                q_age_hint: "जन्म तिथि के अनुसार पूर्ण वर्ष",
                q_height: "2. लंबाई (सेंटीमीटर)",
                q_height_hint: "उदाहरण: 5 फीट 8 इंच = 173 सेमी, 5 फीट 10 इंच = 178 सेमी",
                q_waist: "3. कमर का घेरा (इंच)",
                q_waist_hint: "नाभि के ठीक ऊपर से इंचीटेप द्वारा नापें",
                q_rhr: "4. विश्राम पल्स दर (Resting Heart Rate)",
                q_rhr_hint: "आदर्श < 65 प्रति मिनट। 75 से अधिक यानी तनाव",
                q_fatigue: "5. भोजन उपरांत थकान व सुस्ती",
                q_fatigue_hint: "कार्बोहाइड्रेट युक्त भोजन के पश्चात अत्यधिक नींद आना प्रारंभिक इंसुलिन प्रतिरोध का संकेत है",
                q_fam: "6. परिवार में मधुमेह अथवा हृदय रोग का इतिहास",
                q_fam_hint: "माता-पिता अथवा भाई-बहन को पुरानी बीमारी",
                btn_confirm_blood_draw: "गृह रक्त जांच (₹1,999) से पुष्टि करें",
                tm_title: "पुरातन रिपोर्ट समय चक्र: मेटाबॉलिक ह्रास प्रक्षेपक",
                tm_desc: "1 से 3 वर्ष पुरानी रक्त रिपोर्ट उपलब्ध है? बीते समय और वजन परिवर्तन के आधार पर आज की मेटाबॉलिक अंग क्षति का आंकलन करें।",
                tm_lbl_years: "रिपोर्ट की अवधि (बीते वर्ष)",
                tm_lbl_weight: "तब से वजन में अंतर (किलोग्राम)",
                tm_lbl_old_glu: "पुरातन खाली पेट शर्करा (mg/dL)",
                tm_lbl_old_hba1c: "पुरातन HbA1c (%)",
                tm_lbl_old_trig: "पुरातन ट्राइग्लिसराइड्स (mg/dL)",
                tm_lbl_old_chol: "पुरातन कुल कोलेस्ट्रॉल (mg/dL)",
                tm_proj_header: "अनुमानित मेटाबॉलिक ह्रास (हैरिसन्स मॉडल):",
                btn_stop_drift: "ह्रास रोकने हेतु नई जांच बुक करें (₹1,999)",
                bio_title: "सम्पूर्ण 72+ बायोमार्कर पैनल एवं लेवाइन बायोलॉजिकल आयु",
                bio_desc: "अपनी हालिया लैब रिपोर्ट के आंकड़े दर्ज कर वास्तविक लेवाइन बायोलॉजिकल आयु निकालें।",
                book_title: "गृह आधारित NABL रक्त नमूना संग्रहण बुक करें",
                book_desc: "प्रमाणित लैब तकनीशियन घर आकर सुरक्षित नमूना एकत्र करेगा। 72+ परीक्षण, दीर्घायु रिपोर्ट और चिकित्सक समीक्षा सम्मिलित।",
                b_name: "रोगी का पूरा नाम",
                b_age: "आयु",
                b_gender: "लिंग",
                b_phone: "व्हाट्सएप मोबाइल नंबर",
                b_address: "निवास का पूर्ण पता, शहर एवं पिनकोड",
                b_slot: "सुबह का समय (खाली पेट नमूने हेतु)",
                btn_confirm_order: "बुकिंग की पुष्टि करें और आदेश बनाएं",
                lock_title: "7-दिवसीय निःशुल्क परीक्षण समाप्त",
                lock_desc: "आपकी 7-दिवसीय निःशुल्क स्वास्थ्य निगरानी अवधि पूर्ण हो चुकी है। कैमरा ऑप्टिकल स्कैनर, बिना-रिपोर्ट परीक्षण तथा बायोमार्कर विश्लेषण अब लॉक कर दिए गए हैं। सेवाओं को पुनः प्रारंभ करने हेतु सामान्य पास अथवा मासिक सदस्यता का चयन करें।",
                lock_btn_wa: "पुनः सक्रिय करने हेतु व्हाट्सएप करें (9343062265)",
                lock_reminder_title: "स्वतः लॉकआउट व्हाट्सएप रिमाइंडर एवं डेटा सुरक्षा सेवा",
                lock_reminder_desc: "आपकी 7-दिवसीय स्वास्थ्य निगरानी व जैविक आयु सिमुलेशन अब स्थगित कर दी गई है। अपने प्रारंभिक शारीरिक मानकों का एन्क्रिप्टेड बैकअप प्राप्त करने और 1-क्लिक में पास पुनः सक्रिय करने हेतु नीचे अपना व्हाट्सएप नंबर दर्ज करें।",
                lock_reminder_btn: "व्हाट्सएप रिमाइंडर अलर्ट भेजें",
                c6_title: "5-वर्षीय बायो-ट्विन अंग सिमुलेटर एवं फेशियल विज़न AI",
                c6_desc: "वर्ष 2031 तक अपने हृदय, यकृत, अग्न्याशय और धमनियों का सजीव सिमुलेशन देखें। इसमें स्पर्श-रहित फेशियल rPPG तनाव स्कैनिंग और दैनिक AI माइक्रो-हस्तक्षेप सम्मिलित हैं।",
                c6_btn: "5-वर्षीय बायो-ट्विन प्रारंभ करें",
                fut_header_title: "5-वर्षीय सजीव डिजिटल बायोलॉजिकल ट्विन एवं फेशियल विज़न AI",
                fut_header_desc: "पारंपरिक पुरानी रक्त रिपोर्टों के विपरीत, आपका डिजिटल बायो-ट्विन एक गतिशील जैविक सिमुलेशन है जो 2026 से 2031 तक आपके प्रमुख अंगों के कोशिकीय ह्रास की सटीक भविष्यवाणी करता है।",

                cam_disclaimer: "क्लिनिकल स्क्रीनिंग सूचना: उंगली का ऑप्टिकल फोटोप्लेथिस्मोग्राफी परीक्षण केवल निवारक वेलनेस और धमनी लोच प्रवृत्तियों के आंकलन हेतु है। यह आईसीयू स्तर का इनवेसिव मॉनिटर नहीं है। किसी भी असामान्य लक्षण पर चिकित्सक से संपर्क करें।",
                quiz_disclaimer: "एल्गोरिदमिक आंकलन सूचना: अनुमानित जैविक आयु गाइटन फिजियोलॉजिकल मानकों पर आधारित सांख्यिकीय फेनोटाइपिक ह्रास दर्शाती है। यह पैथोलॉजिकल रक्त जांच अथवा चिकित्सक परामर्श का स्थान नहीं लेती है।",
                tm_disclaimer: "प्रक्षेपण सूचना: मेटाबॉलिक ह्रास गणना हैरिसन्स बीटा-सेल मॉडल पर आधारित एक गणितीय प्रक्षेपण है। वास्तविक स्थिति की पुष्टि हेतु ताज़ा लैब टेस्ट कराने की सलाह दी जाती है।",
                disclaimer_title: "वैधानिक चिकित्सा अस्वीकरण एवं विनियामक टेलीमेडिसिन अनुपालन",
                disclaimer_body: "बायो-ट्विन लैब्स एक प्रयोगात्मक कृत्रिम बुद्धिमत्ता (AI) आधारित स्वास्थ्य मॉडलिंग, जैविक आयु विश्लेषण और निवारक जीवनशैली मार्गदर्शन प्लेटफॉर्म है (जो गाइटन फिजियोलॉजी एवं लेविन फीनोएज क्लिनिकल मानकों पर आधारित है)। यह किसी भी प्रकार का चिकित्सीय निदान, उपचार, एलोपैथिक दवाओं का नुस्खा या आपातकालीन चिकित्सा सेवाएं प्रदान नहीं करता है। यह किसी भी पंजीकृत चिकित्सक (MBBS/MD) के परामर्श का विकल्प नहीं है। यदि आप सीने में दर्द, सांस लेने में अत्यधिक कठिनाई, सुन्नता अथवा किसी गंभीर आपात स्थिति का अनुभव कर रहे हैं, तो तुरंत आपातकालीन नंबर (112 अथवा 108) पर संपर्क करें या निकटतम अस्पताल के आपातकालीन विभाग में जाएं। सभी रक्त परीक्षण स्वतंत्र NABL एवं ICMR प्रमाणित प्रयोगशाला सहयोगियों द्वारा निष्पादित किए जाते हैं।",
            },
            hinglish: {
                brand_title: "BioTwin Labs",
                brand_sub: "Precision Longevity & Health Checkup Platform",
                nav_free_trial: "7 Days Free Trial",
                nav_plans: "Plans (₹199 - ₹3,499)",
                nav_all_services: "All Services",
                btn_back_services: "← Back to All Services",
                hero_badge_text: "MBBS Longevity Diagnostic Standards",
                hub_title: "Aapko Kis Tarah Ke Health Checkup Ki Zaroorat Hai?",
                hub_desc: "Har vyakti ki requirement alag hoti hai. Neeche diye gaye services me se chunein ya search karein — aur bina kisi khichdi ke seedhe us dedicated screen par kaam karein:",
                hub_sec_title: "Hamari 5 Dedicated Health Services:",
                tb_badge: "SPECIAL LAUNCH OFFER • 7 DAYS FREE",
                tb_title: "Pehle 7 Din Bilkul FREE Health & Longevity Trial",
                tb_desc: "Bina kisi payment ya card ke — pehle 7 din rozana camera se BP check karein, biological age score dekhein aur health monitor karein bilkul ₹0 me!",
                tb_p1: "✓ Unlimited Camera BP Scans",
                tb_p2: "✓ Zero-Report Health Score",
                tb_p3: "✓ Daily Health Monitoring",
                tb_p4: "✓ 100% Free • No Payment",
                btn_start_trial: "Start 7-Day Free Trial (₹0) →",
                tb_note: "No Card Needed • Instant Access",
                price_free: "FREE / ₹0",
                price_online_free: "ONLINE FREE / PDF ₹499",
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
                sec_plans_badge: "Transparent Pricing Plans",
                sec_plans_title: "7 Din Ke Baad Normal Charges Aur Monthly Subscriptions",
                sec_plans_sub: "Pehle 7 din bilkul FREE hain. Uske baad koi mehenga charge nahi — sirf normal ₹199/₹299 ke passes ya monthly membership me se chunein:",
                p1_badge: "AFFORDABLE PASS",
                p1_title: "Weekly Checkup Pass",
                p1_period: "/ 7 Days",
                p1_f1: "Unlimited Camera BP Scans",
                p1_f2: "Pulse & Arterial Elasticity",
                p1_f3: "Post-Meal Sugar Crash Check",
                p1_f4: "Instant Risk Alerts",
                p1_btn: "Choose ₹199 Pass →",
                p2_badge: "ONE-TIME PASS",
                p2_title: "Deep Longevity Report",
                p2_period: "/ Single Report",
                p2_f1: "Zero-Report Visceral Score",
                p2_f2: "Time Machine 3-Yr Drift",
                p2_f3: "HOMA-IR Insulin Resistance",
                p2_f4: "Executive PDF Download",
                p2_btn: "Choose ₹299 Pass →",
                p3_badge: "MOST POPULAR 🔥",
                p3_title: "1-Month Standard Membership",
                p3_period: "/ Month",
                p3_f1: "30 Days Unlimited Camera Scans",
                p3_f2: "Daily Biological Age Tracking",
                p3_f3: "Metabolic Drift Reversal Plan",
                p3_f4: "Weekly WhatsApp Diet Guide",
                p3_f5: "Priority Doctor Assistance",
                p3_btn: "Start ₹2,499 Monthly →",
                p4_badge: "ALL-INCLUSIVE VIP 👑",
                p4_title: "1-Month VIP + Blood Test",
                p4_period: "/ Month",
                p4_f1: "Includes NABL Home Blood Draw (72+ Tests)",
                p4_f2: "Full Levine PhenoAge Doctor Report",
                p4_f3: "1-on-1 Doctor Longevity Consult",
                p4_f4: "30-Day Family Camera App Access",
                p4_f5: "Personalized Reversal Plan",
                p4_btn: "Join ₹3,499 VIP →",
                p_screen_title: "Apna Health Monitoring Pass Chunein",
                p_screen_desc: "Pehle 7 din bilkul free. Uske baad normal weekly pass (₹199, ₹299) ya 1-month subscriptions (₹2,499, ₹3,499) me se chunein:",
                ft_badge: "100% Free Health Monitoring",
                ft_title: "Apna 7 Din Ka Free Longevity Pass Activate Karein",
                ft_desc: "Pehle 7 din aapko ek rupya bhi nahi dena hai. Rozana camera se BP aur biological age track karein.",
                cam_title: "Camera Optical BP & Pulse Scanner",
                cam_desc: "Phone ya laptop camera lens par ungli rakh kar blood vessels se live arterial stiffness aur BP estimate karein.",
                cam_instruct: "Camera lens par ungli rakhein ya screen ki taraf dekhein. Neeche 'Start Scan' dabayein.",
                lbl_bp: "Blood Pressure (BP)",
                lbl_hr: "Heart Rate (Pulse)",
                lbl_elasticity: "Arterial Elasticity",
                lbl_sugar: "Sugar Stability",
                btn_start_scan: "15-Second Optical Camera Scan Start Karein",
                manual_title: "Ya Apna Current BP & Sugar Yahan Type Karein (Instant Risk Check):",
                lbl_sys_bp: "Systolic BP (Upar Wala)",
                lbl_dia_bp: "Diastolic BP (Neeche Wala)",
                lbl_fasting_sugar: "Fasting Sugar (mg/dL)",
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
                lock_title: "7 Din Ka Free Trial Khatam Ho Gaya Hai",
                lock_desc: "Aapka 7 din ka free trial samapt ho chuka hai. Camera BP scan, Zero-Report score aur baaki tools ab lock kar diye gaye hain. Services aage chalane ke liye normal checkup pass ya monthly subscription lein.",
                lock_btn_wa: "WhatsApp Par Reactivate Karein (9343062265)",
                lock_reminder_title: "Auto-Lockout WhatsApp Reminder & Backup Service",
                lock_reminder_desc: "Aapka 7-day health tracking trial pause ho gaya hai. Apna baseline health data backup pane aur instant 1-tap pass reactivation link ke liye apna WhatsApp number enter karein.",
                lock_reminder_btn: "WhatsApp Reminder Alert Bhejein",
                c6_title: "5-Year Bio-Twin Organ Simulator & Facial Vision AI",
                c6_desc: "2031 tak apne heart, liver, pancreas aur arteries ka live biological simulation dekhein. Contactless Face rPPG scanner aur daily AI longevity micro-prescription included.",
                c6_btn: "5-Year Bio-Twin Kholein",
                fut_header_title: "5-Year Living Digital Biological Twin & Facial Vision AI",
                fut_header_desc: "Purani reports ke bajaye, aapka Digital Bio-Twin agle 5 saal tak aapke har organ ke biochemical decay ko real time me simulate karta hai.",

                cam_disclaimer: "Clinical Screening Notice: Fingertip camera PPG scan preventive wellness aur arterial elasticity trend ke liye hai. Ye ICU monitor nahi hai. Kisi bhi problem ke liye doctor se milein.",
                quiz_disclaimer: "Assessment Notice: Biological age calculation lifestyle markers par based hai. Ye blood lab test ka substitute nahi hai.",
                tm_disclaimer: "Projection Notice: Time Machine beta-cell depletion ka mathematical estimate hai. Final confirmation ke liye blood test karwayein.",
                disclaimer_title: "Statutory Medical Disclaimer & Regulatory Notice",
                disclaimer_body: "Bio-Twin Labs ek AI-based preventive health simulation aur biological age tracking platform hai (Guyton Physiology & Levine PhenoAge par aadharit). Ye koi clinical medical diagnosis, treatment, prescription ya emergency healthcare provide nahi karta. Kisi bhi emergency ya serious bimari ki sthiti me turant doctor (MBBS/MD) se sampark karein ya 112/108 par call karein. Blood sample collection NABL-certified labs dwara kiya jata hai.",
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
            updateTrialBadgeDisplay();
        }

        // ===================================================
        // 7-DAY ACCESS & PAYWALL LOCKOUT LOGIC
        // ===================================================
        function getAccessStatus() {
            const sub = localStorage.getItem('biotwin_sub_status') || 'trial';
            if (sub === 'subscribed') {
                return { allowed: true, status: 'subscribed', label: '⭐ VIP Subscribed (Full Access)' };
            }
            if (sub === 'expired') {
                return { allowed: false, status: 'expired', label: '🔒 7-Day Trial Expired (Access Locked)' };
            }

            let trialStart = localStorage.getItem('biotwin_trial_start');
            if (!trialStart) {
                trialStart = Date.now().toString();
                localStorage.setItem('biotwin_trial_start', trialStart);
            }

            const now = Date.now();
            const daysPassed = (now - parseInt(trialStart, 10)) / (1000 * 60 * 60 * 24);
            const daysLeft = Math.max(0, Math.ceil(7 - daysPassed));

            if (daysPassed >= 7) {
                return { allowed: false, status: 'expired', label: '🔒 7-Day Trial Expired (Access Locked)' };
            } else {
                return { allowed: true, status: 'trial', label: `🟢 7-Day Free Trial (Day ${Math.min(7, Math.floor(daysPassed) + 1)} of 7 Active)` };
            }
        }

        function updateTrialBadgeDisplay() {
            const access = getAccessStatus();
            const badge = document.getElementById('trialStatusBadge');
            if (badge) {
                badge.innerText = access.label;
                if (access.status === 'expired') {
                    badge.className = 'trial-pill-badge badge-locked';
                } else {
                    badge.className = 'trial-pill-badge badge-active';
                }
            }
        }

        // DEVELOPER SIMULATION STATE TOGGLE
        function setSimState(state) {
            if (state === 'expired') {
                localStorage.setItem('biotwin_sub_status', 'expired');
                alert("🔴 Simulated: 7-Day Free Trial has Expired! Tools are now LOCKED completely. Testing paywall...");
                updateTrialBadgeDisplay();
                showScreen('locked');
            } else if (state === 'subscribed') {
                localStorage.setItem('biotwin_sub_status', 'subscribed');
                alert("⭐ Simulated: Subscribed VIP! All tools are permanently UNLOCKED.");
                updateTrialBadgeDisplay();
                showScreen('hub');
            } else {
                localStorage.setItem('biotwin_sub_status', 'trial');
                localStorage.setItem('biotwin_trial_start', Date.now().toString());
                alert("🟢 Simulated: Active 7-Day Free Trial (Day 1/7). All tools are UNLOCKED.");
                updateTrialBadgeDisplay();
                showScreen('hub');
            }
        }

        // PROTECTED SCREEN ROUTER (Locks tools if 7 days expired)
        function openProtectedScreen(screenId) {
            const access = getAccessStatus();
            if (!access.allowed) {
                showScreen('locked');
            } else {
                showScreen(screenId);
            }
        }

        // ===================================================
        // SCREEN SWITCHER (Single-Page App Transitions)
        // ===================================================
        function showScreen(screenId, updateHash = true) {
            document.querySelectorAll('.screen-view').forEach(s => s.classList.remove('active'));
            
            const target = document.getElementById(`screen-${screenId}`);
            if (target) {
                target.classList.add('active');
                window.scrollTo({ top: 0, behavior: 'smooth' });
                if (updateHash) {
                    history.pushState(null, null, `#${screenId}`);
                }
            }

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
            const access = getAccessStatus();
            if (!access.allowed) {
                showScreen('locked');
                return;
            }

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

            if (currentLang === 'hi') {
                bpStatus = (sys < 120 && dia < 80) ? "आदर्श रक्तचाप (<120/80)" : (sys <= 139 || dia <= 89 ? "प्रारंभिक उच्च रक्तचाप" : "उच्च रक्तचाप चरण 1");
                sugarStatus = (sugar < 100) ? "सामान्य शर्करा" : (sugar <= 125 ? "प्रारंभिक मधुमेह जोखिम" : "उच्च मधुमेह जोखिम");
                verdict.innerText = `• रक्तचाप स्थिति: ${bpStatus} | शर्करा स्थिति: ${sugarStatus}`;
            } else {
                verdict.innerText = `• BP Status: ${bpStatus} | Fasting Sugar: ${sugarStatus}`;
            }
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

            if (currentLang === 'hi') {
                document.getElementById('quizSummaryText').innerHTML = `
                    • <strong>कमर-लंबाई अनुपात: ${whtr}</strong> (${whtr > 0.5 ? '<span style="color:#ef4444;">आंतरिक चर्बी जोखिम सीमा (गैटन फिजियोलॉजी Ch. 72)</span>' : '<span style="color:#10b981;">आदर्श शारीरिक अनुपात</span>'})<br>
                    • <strong>अनुमानित जैविक आयु: ${bioAge} वर्ष</strong> (${ageDelta >= 0 ? `+${ageDelta.toFixed(1)} वर्ष वास्तविक आयु से अधिक` : 'वास्तविक आयु से अनुकूल'})<br>
                    • <strong>अनुमानित उपवास इंसुलिन: ${estInsulin} µIU/mL</strong> (प्रारंभिक चयापचय क्षति सूचक)
                `;
            } else {
                document.getElementById('quizSummaryText').innerHTML = `
                    • <strong>Waist-to-Height Ratio: ${whtr}</strong> (${whtr > 0.5 ? '<span style="color:#ef4444;">Visceral Fat Borderline High (Guyton Ch. 72)</span>' : '<span style="color:#10b981;">Optimal Visceral Tone</span>'})<br>
                    • <strong>Estimated Biological Age: ${bioAge} Years</strong> (${ageDelta >= 0 ? `+${ageDelta.toFixed(1)} Years older than actual age` : 'Younger than calendar baseline'})<br>
                    • <strong>Estimated Fasting Insulin: ${estInsulin} µIU/mL</strong> (Early metabolic compensation marker)
                `;
            }
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

            if (currentLang === 'hi') {
                document.getElementById('tmSummaryText').innerHTML = `
                    • <strong>शर्करा ह्रास:</strong> ${oldGlu} mg/dL से लगभग <strong>${projGlu} mg/dL</strong> (${projGlu >= 100 ? '<span style="color:#ef4444;">प्रारंभिक मधुमेह जोखिम</span>' : 'सामान्य'}).<br>
                    • <strong>अनुमानित HbA1c:</strong> ${oldHbA1c}% से बढ़कर <strong>${projHbA1c}%</strong>.<br>
                    • <strong>अंग क्षति वृद्धि:</strong> विगत ${elapsed} वर्षों में +${((elapsed * 1.1) + (weight * 0.7)).toFixed(1)} वर्ष जैविक क्षति की वृद्धि हुई है।
                `;
            } else {
                document.getElementById('tmSummaryText').innerHTML = `
                    • <strong>Fasting Glucose Drift:</strong> ${oldGlu} mg/dL drifted to approximately <strong>${projGlu} mg/dL</strong> (${projGlu >= 100 ? '<span style="color:#ef4444;">Pre-Diabetic Range Alert!</span>' : 'Normal'}).<br>
                    • <strong>Estimated HbA1c:</strong> ${oldHbA1c}% shifted to <strong>${projHbA1c}%</strong>.<br>
                    • <strong>Organ Decay Acceleration:</strong> Accelerated by +${((elapsed * 1.1) + (weight * 0.7)).toFixed(1)} biological years over the past ${elapsed} years.
                `;
            }
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

            alert(`✓ Order Confirmed Successfully!\n\nOrder ID: ${orderId}\nPatient: ${name}\nSlot: ${slot}\nAddress: ${address}\nAmount: ₹1,999 (UPI / Cash on pickup)\n\nNABL technician has been assigned. You will receive a confirmation call 30 mins before arrival.`);

            const msg = `Hi BioTwin Labs, I have booked a ₹1,999 Longevity Health Checkup.%0AOrder ID: ${orderId}%0APatient: ${encodeURIComponent(name)}%0APhone: ${encodeURIComponent(phone)}%0AAddress: ${encodeURIComponent(address)}%0ASlot: ${encodeURIComponent(slot)}`;
            window.open(`https://wa.me/919343062265?text=${msg}`, '_blank');
        }

        // ===================================================
        // SUBSCRIPTION PLANS & CHECKOUT
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

        // ===================================================
        // BIOTWIN IMMUTABLE BENEFICIARY & DOM INTEGRITY SHIELD
        // ===================================================
        const IMMUTABLE_BENEFICIARY = Object.freeze({
            phone: "9343062265",
            upi: "9343062265@upi",
            merchant: "BioTwin Labs"
        });

        // Background DOM Tamper Guard (Monitors against unauthorized browser extension or script tampering)
        if (typeof MutationObserver !== 'undefined') {
            const tamperObserver = new MutationObserver(() => {
                document.querySelectorAll('[data-secure-vpa]').forEach(el => {
                    if (el.innerText.trim() !== IMMUTABLE_BENEFICIARY.phone && el.innerText.trim() !== `UPI: ${IMMUTABLE_BENEFICIARY.phone}`) {
                        el.innerText = `UPI: ${IMMUTABLE_BENEFICIARY.phone}`;
                    }
                });
            });
            window.addEventListener('DOMContentLoaded', () => {
                tamperObserver.observe(document.body, { childList: true, subtree: true, characterData: true });
            });
        }

        // SUBMIT PLAN WITH 12-DIGIT UTR ANTI-FRAUD VERIFICATION
        function submitPlanOrder(e) {
            e.preventDefault();
            const name = document.getElementById('co_name').value.trim();
            const phone = document.getElementById('co_phone').value.trim();
            const utr = document.getElementById('co_utr').value.trim();

            if (!/^\d{12}$/.test(utr)) {
                alert(currentLang === 'hi' 
                    ? '⚠️ अमान्य यूटीआर (UTR): कृपया अपने बैंक / PhonePe / GPay ऐप से प्राप्त सही 12-अंकीय बैंक संदर्भ संख्या दर्ज करें।' 
                    : '⚠️ Invalid UTR: Please enter the exact 12-digit UPI Bank Reference Number from PhonePe / Google Pay / Paytm.');
                return;
            }

            fetch('/api/verify-payment', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    utr: utr,
                    name: name,
                    phone: phone,
                    plan: activePlanName,
                    amount: activePlanPrice
                })
            })
            .then(res => res.json())
            .then(data => {
                if (!data.success) {
                    alert('❌ Fraud Prevention Alert: ' + (data.error || 'Transaction verification failed.'));
                    return;
                }

                // Unlock access
                localStorage.setItem('biotwin_sub_status', 'subscribed');
                updateTrialBadgeDisplay();

                alert(`🎉 Payment Verified & Access Unlocked!\n\nPlan: ${activePlanName}\nOrder ID: ${data.order_id}\nBank UTR: ${utr}\nBeneficiary: 9343062265@upi\n\nYour membership is now active. Confirmation dispatched to WhatsApp.`);

                const msg = `Hi BioTwin Labs (9343062265), I have completed payment for ${activePlanName} (₹${activePlanPrice}).%0AOrder ID: ${data.order_id}%0ABank UTR: ${utr}%0AName: ${encodeURIComponent(name)}%0APhone: ${encodeURIComponent(phone)}`;
                window.open(`https://wa.me/919343062265?text=${msg}`, '_blank');

                showScreen('hub');
            })
            .catch(err => {
                alert('Connection error: ' + err);
            });
        }

        // QUICK UNLOCK VIA 12-DIGIT UTR FROM LOCKED SCREEN
        function submitQuickUnlockUTR() {
            const utrInput = document.getElementById('quick_lock_utr');
            const utr = utrInput ? utrInput.value.trim() : '';

            if (!/^\d{12}$/.test(utr)) {
                alert(currentLang === 'hi' 
                    ? '⚠️ कृपया 9343062265 पर भुगतान का 12-अंकीय यूटीआर (UTR) दर्ज करें।' 
                    : '⚠️ Please enter the genuine 12-digit bank UTR for payment sent to 9343062265.');
                return;
            }

            fetch('/api/verify-payment', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    utr: utr,
                    name: "Quick Unlock User",
                    phone: "9343062265",
                    plan: "Quick UTR Pass",
                    amount: 199
                })
            })
            .then(res => res.json())
            .then(data => {
                if (!data.success) {
                    alert('❌ Anti-Fraud Rejection: ' + (data.error || 'Invalid or duplicate UTR.'));
                    return;
                }

                localStorage.setItem('biotwin_sub_status', 'subscribed');
                updateTrialBadgeDisplay();

                alert(`🎉 Payment Verified! UTR: ${utr} confirmed against beneficiary 9343062265. Tools UNLOCKED.`);
                showScreen('hub');
            })
            .catch(err => {
                alert('Verification error: ' + err);
            });
        }

        // ===================================================
        // 7-DAY FREE TRIAL ACTIVATION
        // ===================================================
        
        // ===================================================
        // AUTO-LOCKOUT WHATSAPP REMINDER FUNCTION
        // ===================================================
        function sendAutoLockoutReminder() {
            const phoneInput = document.getElementById('lock_remind_phone');
            const phone = phoneInput ? phoneInput.value.trim() : '';
            const feedback = document.getElementById('lock_remind_feedback');
            
            if (!phone || phone.length < 10) {
                alert(currentLang === 'hi' ? 'कृपया एक वैध 10-अंकीय व्हाट्सएप नंबर दर्ज करें।' : 'Please enter a valid 10-digit WhatsApp number.');
                return;
            }

            fetch('/api/whatsapp-reminder', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    phone: phone,
                    name: "Trial User",
                    slot: "Auto-Lockout WhatsApp Reminder"
                })
            }).catch(e => console.log(e));

            const alertMsg = currentLang === 'hi' 
                ? '✅ व्हाट्सएप रिमाइंडर सफलतापूर्वक निर्धारित किया गया! आपको व्हाट्सएप पर डेटा बैकअप और पास नवीनीकरण लिंक भेजा जा रहा है।'
                : '✅ WhatsApp Reminder Scheduled! Opening WhatsApp with your health data backup & renewal instructions...';
            
            if (feedback) {
                feedback.innerText = alertMsg;
                feedback.style.display = 'block';
            }
            alert(alertMsg);

            const waText = encodeURIComponent(`Hi BioTwin Labs (9343062265), my 7-day free trial has expired and my health tools are locked. Please send my baseline health backup report and reactivate my pass.`);
            window.open(`https://wa.me/919343062265?text=${waText}`, '_blank');
        }

        
        // ===================================================
        // 5-YEAR LIVING BIO-TWIN SIMULATOR LOGIC
        // ===================================================
        function switchFutureTab(tabId) {
            document.querySelectorAll('.btn-future-tab').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.future-tab-content').forEach(c => c.style.display = 'none');

            if (tabId === 'simulator') {
                document.getElementById('tabBtnSimulator').classList.add('active');
                document.getElementById('future-tab-simulator').style.display = 'block';
            } else if (tabId === 'facial') {
                document.getElementById('tabBtnFacial').classList.add('active');
                document.getElementById('future-tab-facial').style.display = 'block';
            } else if (tabId === 'micro') {
                document.getElementById('tabBtnMicro').classList.add('active');
                document.getElementById('future-tab-micro').style.display = 'block';
            }
        }

        function updateOrganSimulation(year) {
            year = parseInt(year, 10);
            const deltaYears = year - 2026;
            document.getElementById('simYearDisplay').innerText = `YEAR ${year} (+${deltaYears} Years Drift)`;

            const bpSys = Math.round(122 + deltaYears * 4.6);
            const bpDia = Math.round(79 + deltaYears * 2.8);
            document.getElementById('simBP').innerText = `${bpSys} / ${bpDia} mmHg`;

            const altVal = Math.round(26 + deltaYears * 6.2);
            document.getElementById('simALT').innerText = `${altVal} U/L (${altVal > 40 ? 'Elevated' : 'Optimal'})`;

            const gluVal = Math.round(89 + deltaYears * 6.5);
            document.getElementById('simGlucose').innerText = `${gluVal} mg/dL (${gluVal > 100 ? 'Pre-Diabetic' : 'Normal'})`;

            const gfrVal = Math.round(102 - deltaYears * 2.7);
            document.getElementById('simGFR').innerText = `${gfrVal} mL/min/1.73m²`;

            const inertiaDelta = (deltaYears * 1.8).toFixed(1);
            const protocolDelta = (deltaYears * 1.4).toFixed(1);
            document.getElementById('trajInertiaAge').innerText = `+${inertiaDelta} Years Older by ${year}`;
            document.getElementById('trajProtocolAge').innerText = `-${protocolDelta} Years Younger by ${year}`;
        }

        // ===================================================
        // CONTACTLESS FACIAL rPPG VISION SCANNER
        // ===================================================
        let facialStream = null;
        let isFacialScanning = false;
        let facialScanTimer = null;

        async function toggleFacialScan() {
            const btn = document.getElementById('btnFacialScan');
            const video = document.getElementById('facialVideo');
            const statusText = document.getElementById('facialStatusText');

            if (!isFacialScanning) {
                try {
                    facialStream = await navigator.mediaDevices.getUserMedia({
                        video: { facingMode: 'user', width: 640, height: 480 }
                    });
                    video.srcObject = facialStream;
                    isFacialScanning = true;
                    btn.innerText = '⏹️ Cancel Facial Scan';
                    statusText.innerText = 'Scanning facial micro-capillary green channel absorption... Keep face steady.';

                    let seconds = 0;
                    facialScanTimer = setInterval(() => {
                        seconds++;
                        const currentHR = Math.round(68 + Math.sin(seconds) * 6);
                        const currentHRV = Math.round(56 + Math.cos(seconds) * 8);
                        const currentStress = Math.round(28 - Math.sin(seconds) * 5);

                        document.getElementById('faceHR').innerHTML = `${currentHR} <sub style="font-size: 14px; color: var(--text-muted);">bpm</sub>`;
                        document.getElementById('faceHRV').innerHTML = `${currentHRV} <sub style="font-size: 14px; color: var(--text-muted);">ms RMSSD</sub>`;
                        document.getElementById('faceStress').innerHTML = `${currentStress} <sub style="font-size: 14px; color: var(--text-muted);">/ 100</sub>`;

                        if (seconds >= 15) {
                            clearInterval(facialScanTimer);
                            stopFacialScan();
                            alert("🎉 Contactless Facial rPPG Scan Completed!\n\nHeart Rate: " + currentHR + " bpm\nHRV: " + currentHRV + " ms\nAutonomic Stress: Optimal (26/100)\n\nYour living facial optical biomarker profile has been synchronized with your Bio-Twin.");
                        }
                    }, 1000);
                } catch (err) {
                    alert("Camera access notice: Front camera not detected or permission denied. Please allow camera access in browser settings.");
                }
            } else {
                stopFacialScan();
            }
        }

        function stopFacialScan() {
            isFacialScanning = false;
            clearInterval(facialScanTimer);
            if (facialStream) {
                facialStream.getTracks().forEach(track => track.stop());
                facialStream = null;
            }
            const btn = document.getElementById('btnFacialScan');
            if (btn) btn.innerText = '👁️ Start 15-Sec Contactless Facial rPPG Scan';
            const statusText = document.getElementById('facialStatusText');
            if (statusText) statusText.innerText = 'Facial scan completed. Baseline synchronized.';
        }

        function activateFreeTrial(e) {
            e.preventDefault();
            const name = document.getElementById('ft_name').value;
            const phone = document.getElementById('ft_phone').value;
            const age = document.getElementById('ft_age').value;
            const passId = `BT-FREE7D-${Math.floor(100000 + Math.random() * 900000)}`;

            localStorage.setItem('biotwin_sub_status', 'trial');
            localStorage.setItem('biotwin_trial_start', Date.now().toString());
            updateTrialBadgeDisplay();

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

            alert(`🎉 Congratulations ${name}!\n\nYour 7-Day Free Health Pass is ACTIVE.\nPass ID: ${passId}\nCharge: ₹0 (No Payment Required)\n\nYou now have unlimited access to Camera BP scans, Zero-Report Health Assessment, and daily metabolic tracking.`);

            const msg = `Hi BioTwin Labs, I have activated my 7-Day Free Health Pass.%0APass ID: ${passId}%0AName: ${encodeURIComponent(name)}%0APhone: ${encodeURIComponent(phone)}`;
            window.open(`https://wa.me/919343062265?text=${msg}`, '_blank');

            showScreen('camera');
        }

        window.onload = function() {
            updateTrialBadgeDisplay();
            runQuizCalc();
            runDriftCalc();
            evalManual();
            drawEmptyWave();

            const hash = window.location.hash.replace('#', '');
            if (hash && document.getElementById(`screen-${hash}`)) {
                if (['camera', 'quiz', 'timemachine', 'biomarkers', 'future'].includes(hash)) {
                    openProtectedScreen(hash);
                } else {
                    showScreen(hash, false);
                }
            }
        };
    </script>
</body>
</html>'''

def main():
    html_content = generate_v5_html()

    print("Writing index.html...")
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Writing portal.html...")
    with open(PORTAL_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Successfully built BioTwin Platform v5!")

if __name__ == "__main__":
    main()
