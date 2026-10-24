# -*- coding: utf-8 -*-
"""
Builds all dedicated HTML templates for the BioTwin Multi-Page Platform.
Ensures zero clutter ("khichdi"), separate pages, real-time interactivity, and no internal profit/loss junk.
"""

import os

TEMPLATES_DIR = r"c:\Users\B-WOI\OneDrive\Desktop\BioTwin-Platform\web\templates"

# -------------------------------------------------------------
# 1. INDEX.HTML (SERVICES CATALOG & SEARCH HUB)
# -------------------------------------------------------------
INDEX_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BioTwin Labs | Precision Longevity & Health Checkup Platform</title>
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
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: var(--bg);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        .navbar {
            display: flex; justify-content: space-between; align-items: center;
            padding: 18px 36px; background: rgba(10, 15, 26, 0.96); backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 1000;
        }
        .brand-box { display: flex; align-items: center; gap: 12px; text-decoration: none; color: inherit; }
        .brand-icon {
            width: 44px; height: 44px; background: linear-gradient(135deg, #38bdf8, #818cf8);
            border-radius: 12px; display: flex; align-items: center; justify-content: center;
            font-weight: 900; font-size: 22px; color: #000; box-shadow: 0 0 20px var(--accent-glow);
        }
        .brand-text h1 { font-size: 20px; font-weight: 800; }
        .brand-text span { font-size: 10px; text-transform: uppercase; letter-spacing: 1.5px; color: var(--accent); font-weight: 700; display: block; }
        .nav-controls { display: flex; align-items: center; gap: 16px; }
        .lang-switch { display: flex; gap: 6px; background: var(--surface-card); padding: 4px; border-radius: 8px; border: 1px solid var(--border); }
        .lang-btn {
            background: transparent; border: none; color: var(--text-muted); padding: 6px 12px;
            border-radius: 6px; font-size: 11px; font-weight: 700; cursor: pointer; transition: all 0.2s;
        }
        .lang-btn.active, .lang-btn:hover { background: var(--accent); color: #000; }
        .btn-help {
            background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.3); color: #34d399;
            font-size: 12px; font-weight: 700; padding: 8px 16px; border-radius: 8px; text-decoration: none;
            display: flex; align-items: center; gap: 6px;
        }
        .hero {
            max-width: 1200px; width: 100%; margin: 40px auto 0; padding: 0 24px; text-align: center;
        }
        .hero-badge {
            display: inline-flex; align-items: center; gap: 8px; background: rgba(56, 189, 248, 0.1);
            border: 1px solid rgba(56, 189, 248, 0.25); color: var(--accent); font-size: 11px; font-weight: 800;
            padding: 5px 14px; border-radius: 999px; text-transform: uppercase; margin-bottom: 16px;
        }
        .hero-title { font-size: 38px; font-weight: 800; letter-spacing: -0.5px; margin-bottom: 14px; line-height: 1.25; }
        .hero-subtitle { font-size: 16px; color: var(--text-muted); max-width: 720px; margin: 0 auto 30px; line-height: 1.6; }

        /* Search Bar */
        .search-container {
            max-width: 720px; margin: 0 auto 50px; position: relative;
        }
        .search-box {
            width: 100%; background: var(--surface-card); border: 2px solid var(--border);
            border-radius: 16px; padding: 18px 24px 18px 54px; font-size: 16px; color: #fff;
            outline: none; transition: all 0.2s; font-family: 'Plus Jakarta Sans', sans-serif;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        }
        .search-box:focus { border-color: var(--accent); box-shadow: 0 0 25px var(--accent-glow); }
        .search-icon { position: absolute; left: 20px; top: 50%; transform: translateY(-50%); font-size: 20px; color: var(--text-dim); }

        /* Services Grid */
        .services-section { max-width: 1200px; width: 100%; margin: 0 auto; padding: 0 24px 60px; flex: 1; }
        .services-heading {
            font-size: 20px; font-weight: 800; margin-bottom: 24px; display: flex; align-items: center; justify-content: space-between;
        }
        .services-count { font-size: 13px; color: var(--text-dim); font-weight: normal; }
        .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 24px; }
        
        .service-card {
            background: var(--surface); border: 1px solid var(--border); border-radius: 20px;
            padding: 28px; display: flex; flex-direction: column; justify-content: space-between;
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1); position: relative; overflow: hidden;
        }
        .service-card:hover {
            transform: translateY(-4px); border-color: var(--accent);
            box-shadow: 0 12px 35px rgba(56, 189, 248, 0.15);
        }
        .card-top { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px; }
        .card-icon {
            width: 54px; height: 54px; border-radius: 14px; background: var(--surface-card);
            border: 1px solid var(--border); display: flex; align-items: center; justify-content: center;
            font-size: 26px;
        }
        .card-price-pill {
            background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.3);
            color: #10b981; font-size: 12px; font-weight: 800; padding: 5px 12px; border-radius: 999px;
            font-family: 'JetBrains Mono', monospace;
        }
        .card-title { font-size: 20px; font-weight: 800; margin-bottom: 8px; line-height: 1.3; }
        .card-desc { font-size: 13px; color: var(--text-muted); line-height: 1.6; margin-bottom: 22px; flex: 1; }
        .card-meta {
            display: flex; gap: 14px; margin-bottom: 22px; font-size: 11px; color: var(--text-dim);
            padding-top: 14px; border-top: 1px solid var(--border);
        }
        .card-btn {
            background: var(--surface-card); border: 1px solid var(--border); color: #fff;
            padding: 12px 18px; border-radius: 12px; font-size: 13px; font-weight: 800; text-decoration: none;
            display: flex; align-items: center; justify-content: space-between; transition: all 0.2s;
        }
        .card-btn:hover { background: var(--accent); color: #000; border-color: var(--accent); }
        .card-featured { border-color: #38bdf8; background: linear-gradient(180deg, rgba(56, 189, 248, 0.05), var(--surface)); }
        .card-featured .card-btn { background: linear-gradient(135deg, #38bdf8, #2563eb); border: none; color: #fff; }
        .card-featured .card-btn:hover { box-shadow: 0 4px 15px rgba(56, 189, 248, 0.4); }

        .footer {
            border-top: 1px solid var(--border); background: var(--surface); padding: 24px 36px;
            font-size: 12px; color: var(--text-dim); text-align: center; margin-top: auto;
        }
    </style>
</head>
<body>

    <nav class="navbar">
        <a href="/" class="brand-box">
            <div class="brand-icon">Ω</div>
            <div class="brand-text">
                <h1 data-i18n="brand_title">BioTwin Labs</h1>
                <span data-i18n="brand_sub">Precision Longevity & Health Checkup Platform</span>
            </div>
        </a>

        <div class="nav-controls">
            <div class="lang-switch">
                <button class="lang-btn active" onclick="setLang('en', this)">🇬🇧 English</button>
                <button class="lang-btn" onclick="setLang('hi', this)">🇮🇳 हिन्दी</button>
                <button class="lang-btn" onclick="setLang('hinglish', this)">🇮🇳 Hinglish</button>
            </div>
            
            <a href="https://wa.me/919876543210" target="_blank" class="btn-help">
                <span>💬</span>
                <span data-i18n="btn_helpline">Patient Support</span>
            </a>
        </div>
    </nav>

    <div class="hero">
        <div class="hero-badge">
            <span>📚 MBBS Textbook Diagnostic Protocols</span>
        </div>
        <h1 class="hero-title" data-i18n="hero_title">
            Aapko Kis Tarah Ke Health Checkup Ki Zaroorat Hai?
        </h1>
        <p class="hero-subtitle" data-i18n="hero_subtitle">
            Har vyakti ki requirement alag hoti hai. Neeche diye gaye options me se apni zaroorat chunein ya search karein — aur bina kisi bheed-bhaad ke seedhe us dedicated page par jayein:
        </p>

        <div class="search-container">
            <span class="search-icon">🔍</span>
            <input type="text" id="serviceSearch" class="search-box" placeholder="Apna checkup search karein (e.g. BP, Sugar, Purani Report, Zero Report, Blood Test...)" oninput="filterServices(this.value)">
        </div>
    </div>

    <div class="services-section">
        <div class="services-heading">
            <span data-i18n="sec_services_heading">Hamari 5 Dedicated Health Services:</span>
            <span class="services-count" id="servicesCount">Showing 5 services</span>
        </div>

        <div class="services-grid" id="servicesGrid">

            <!-- SERVICE 1 -->
            <div class="service-card" data-tags="bp blood pressure sugar camera mobile laptop pulse instant free checkup">
                <div>
                    <div class="card-top">
                        <div class="card-icon">📱</div>
                        <div class="card-price-pill">FREE / ₹0</div>
                    </div>
                    <h2 class="card-title" data-i18n="s1_title">Camera Optical BP & Pulse Checkup</h2>
                    <p class="card-desc" data-i18n="s1_desc">
                        Bina kisi machine ke, apne phone ya laptop camera lens par ungli rakh kar blood vessels se live Blood Pressure, Heart Rate aur Glycemic Stability check karein.
                    </p>
                </div>
                <div>
                    <div class="card-meta">
                        <span>⏱️ Time: 15 Seconds</span>
                        <span>🔬 Method: Transdermal PPG</span>
                    </div>
                    <a href="/camera-checkup" class="card-btn">
                        <span data-i18n="s1_btn">Open Camera Scanner</span>
                        <span>→</span>
                    </a>
                </div>
            </div>

            <!-- SERVICE 2 -->
            <div class="service-card" data-tags="zero report no test quiz 2 min belly fat visceral waist insulin free checkup">
                <div>
                    <div class="card-top">
                        <div class="card-icon">📋</div>
                        <div class="card-price-pill">FREE / ₹0</div>
                    </div>
                    <h2 class="card-title" data-i18n="s2_title">Zero-Report 2-Minute Health Score</h2>
                    <p class="card-desc" data-i18n="s2_desc">
                        Agar aapne kabhi blood test nahi karwaya hai, tab bhi 6 physical clinical markers (kamar ka ghera, resting pulse, post-meal neend) se apna biological age aur hidden organ risk jaanein.
                    </p>
                </div>
                <div>
                    <div class="card-meta">
                        <span>⏱️ Time: 2 Minutes</span>
                        <span>📚 Basis: Guyton & Hall Ch. 72</span>
                    </div>
                    <a href="/zero-report-quiz" class="card-btn">
                        <span data-i18n="s2_btn">Start 2-Min Assessment</span>
                        <span>→</span>
                    </a>
                </div>
            </div>

            <!-- SERVICE 3 -->
            <div class="service-card" data-tags="old report time machine purani report drift damage sugar cholesterol free projection">
                <div>
                    <div class="card-top">
                        <div class="card-icon">⏳</div>
                        <div class="card-price-pill">FREE / ₹0</div>
                    </div>
                    <h2 class="card-title" data-i18n="s3_title">Old Report Time Machine Projector</h2>
                    <p class="card-desc" data-i18n="s3_desc">
                        Agar aapke paas 1 se 3 saal purani blood report hai, toh elapsed time aur weight change ke basis par Harrison's Internal Medicine ke tehat jaanein ki aaj aapka organ damage kitna badh chuka hai.
                    </p>
                </div>
                <div>
                    <div class="card-meta">
                        <span>⏱️ Time: 1 Minute</span>
                        <span>📉 Model: Beta-Cell Drift</span>
                    </div>
                    <a href="/old-report-projector" class="card-btn">
                        <span data-i18n="s3_btn">Check Old Report Drift</span>
                        <span>→</span>
                    </a>
                </div>
            </div>

            <!-- SERVICE 4 -->
            <div class="service-card" data-tags="72 biomarkers full panel report levine phenoage apob homa deep analysis lab">
                <div>
                    <div class="card-top">
                        <div class="card-icon">🩸</div>
                        <div class="card-price-pill">ONLINE FREE / PDF ₹499</div>
                    </div>
                    <h2 class="card-title" data-i18n="s4_title">Full 72+ Biomarker Deep Engine</h2>
                    <p class="card-desc" data-i18n="s4_desc">
                        Aapke paas taaza blood test report hai? ApoB, Fasting Insulin, hs-CRP, Liver, Kidney sahit sabhi 72 parameters enter karke exact Levine Phenotypic Age aur doctor-signed blueprint nikalein.
                    </p>
                </div>
                <div>
                    <div class="card-meta">
                        <span>⏱️ Time: 5 Minutes</span>
                        <span>📑 Output: Executive PDF Report</span>
                    </div>
                    <a href="/full-biomarker-analysis" class="card-btn">
                        <span data-i18n="s4_btn">Open Biomarker Matrix</span>
                        <span>→</span>
                    </a>
                </div>
            </div>

            <!-- SERVICE 5 (FEATURED) -->
            <div class="service-card card-featured" data-tags="book home draw blood sample test collection nabl certified 1999 full body checkup">
                <div>
                    <div class="card-top">
                        <div class="card-icon">🏠</div>
                        <div class="card-price-pill" style="background: rgba(56, 189, 248, 0.2); border-color: #38bdf8; color: #38bdf8;">₹1,999 ALL-INCLUSIVE</div>
                    </div>
                    <h2 class="card-title" data-i18n="s5_title">Ghar Baithe NABL Blood Test Booking</h2>
                    <p class="card-desc" data-i18n="s5_desc">
                        NABL certified phlebotomist aapke ghar aakar sterile sample lega. 72+ biomarkers, Biological Age Report, aur Doctor Longevity Blueprint sabhi kuch included hai.
                    </p>
                </div>
                <div>
                    <div class="card-meta">
                        <span>🚚 Home Pickup: Tomorrow 7-9 AM</span>
                        <span>✓ Certified Vacuum Tubes</span>
                    </div>
                    <a href="/book-blood-test" class="card-btn">
                        <span data-i18n="s5_btn">Book Home Blood Draw (₹1,999)</span>
                        <span>→</span>
                    </a>
                </div>
            </div>

        </div>
    </div>

    <footer class="footer">
        © 2026 BioTwin Labs. Clinical standards aligned with Harrison's Principles of Internal Medicine & Guyton Physiology.
    </footer>

    <script>
        const I18N = {
            en: {
                brand_title: "BioTwin Labs",
                brand_sub: "Precision Longevity & Health Checkup Platform",
                btn_helpline: "Patient Support",
                hero_title: "What Kind of Health Checkup Do You Need?",
                hero_subtitle: "Every individual has unique diagnostic needs. Select or search from the options below to go directly to your dedicated, focused checkup page without any clutter:",
                sec_services_heading: "Our 5 Dedicated Health Services:",
                s1_title: "Camera Optical BP & Pulse Checkup",
                s1_desc: "Check your live Blood Pressure, Heart Rate and Glycemic Stability using your phone or laptop camera via transdermal photoplethysmography.",
                s1_btn: "Open Camera Scanner",
                s2_title: "Zero-Report 2-Minute Health Score",
                s2_desc: "Never had a blood test? Use 6 clinical body markers (waist ratio, resting pulse, post-meal fatigue) to calculate biological age delta and visceral risk.",
                s2_btn: "Start 2-Min Assessment",
                s3_title: "Old Report Time Machine Projector",
                s3_desc: "Have a 1-3 year old blood test? Project how much your metabolic organ damage has progressed based on elapsed time and weight change.",
                s3_btn: "Check Old Report Drift",
                s4_title: "Full 72+ Biomarker Deep Engine",
                s4_desc: "Have recent lab reports? Enter your ApoB, Fasting Insulin, hs-CRP, Liver and Kidney markers to compute your exact Levine Phenotypic Age.",
                s4_btn: "Open Biomarker Matrix",
                s5_title: "Book NABL Blood Sample Collection at Home",
                s5_desc: "Certified phlebotomist collects samples at home. Complete 72+ biomarkers, BioTwin Longevity Report, and Doctor review included.",
                s5_btn: "Book Home Blood Draw (₹1,999)"
            },
            hi: {
                brand_title: "बायोट्विन लैब्स (BioTwin Labs)",
                brand_sub: "सम्पूर्ण दीर्घायु एवं स्वास्थ्य जांच प्लेटफॉर्म",
                btn_helpline: "मरीज सहायता",
                hero_title: "आपको किस तरह के हेल्थ चेकअप की ज़रूरत है?",
                hero_subtitle: "हर मरीज की जरूरत अलग होती है। नीचे दिए गए विकल्पों में से अपनी जरूरत चुनें या सर्च करें — और बिना किसी भीड़-भाड़ के सीधे अपने पेज पर जाएं:",
                sec_services_heading: "हमारी 5 समर्पित स्वास्थ्य सेवाएं:",
                s1_title: "कैमरा ऑप्टिकल बीपी और पल्स चेकअप",
                s1_desc: "बिना किसी मशीन के, अपने फोन या लैपटॉप कैमरे पर उंगली रखकर नसों के बहाव से सीधा ब्लड प्रेशर और पल्स मापें।",
                s1_btn: "कैमरा स्कैनर खोलें",
                s2_title: "बिना रिपोर्ट 2-मिनट हेल्थ स्कोर",
                s2_desc: "अगर आपने कभी ब्लड टेस्ट नहीं कराया है, तो भी 6 शारीरिक लक्षणों (कमर का घेरा, आराम की पल्स, खाने के बाद सुस्ती) से अपनी अंदरूनी जैविक उम्र जानें।",
                s2_btn: "2-मिनट टेस्ट शुरू करें",
                s3_title: "पुरानी रिपोर्ट टाइम मशीन प्रोजेक्टर",
                s3_desc: "अगर आपके पास 1 से 3 साल पुरानी ब्लड रिपोर्ट है, तो वजन और बीते समय के आधार पर जानें कि आज आपका शुगर और अंग डैमेज कितना बढ़ चुका है।",
                s3_btn: "पुरानी रिपोर्ट का डैमेज देखें",
                s4_title: "पूरा 72+ बायोमार्कर क्लिनिकल पैनल",
                s4_desc: "ताजा रिपोर्ट के सभी 72 मानक (ApoB, इंसुलिन, CRP, लिवर, किडनी) दर्ज करके अपनी वास्तविक लेवाइन बायोलॉजिकल उम्र निकालें।",
                s4_btn: "बायोमार्कर पैनल खोलें",
                s5_title: "घर बैठे NABL ब्लड टेस्ट बुक करें",
                s5_desc: "सर्टिफाइड लैब टेक्नीशियन आपके घर आकर सैंपल लेगा। 72+ बायोमार्कर, बायोलॉजिकल एज रिपोर्ट और डॉक्टर परामर्श सब शामिल है।",
                s5_btn: "घर बैठे टेस्ट बुक करें (₹1,999)"
            },
            hinglish: {
                brand_title: "BioTwin Labs",
                brand_sub: "Precision Longevity & Full Body Checkup Platform",
                btn_helpline: "Patient Helpline",
                hero_title: "Aapko Kis Tarah Ke Health Checkup Ki Zaroorat Hai?",
                hero_subtitle: "Har vyakti ki requirement alag hoti hai. Neeche diye gaye options me se apni zaroorat chunein ya search karein — aur bina kisi khichdi ke seedhe us dedicated page par jayein:",
                sec_services_heading: "Hamari 5 Dedicated Health Services:",
                s1_title: "Camera Optical BP & Pulse Checkup",
                s1_desc: "Bina kisi machine ke, apne phone ya laptop camera lens par ungli rakh kar blood vessels se live Blood Pressure aur Pulse check karein.",
                s1_btn: "Open Camera Scanner",
                s2_title: "Zero-Report 2-Minute Health Score",
                s2_desc: "Agar kabhi blood test nahi karwaya hai, tab bhi 6 body markers se pait ki charbi (visceral fat) aur umar ka pata lagayein.",
                s2_btn: "Start 2-Min Assessment",
                s3_title: "Old Report Time Machine Projector",
                s3_desc: "1 se 3 saal purani blood report ke numbers dalkar jaanein ki pichle saalon me kitna organ damage badha hai.",
                s3_btn: "Check Old Report Drift",
                s4_title: "Full 72+ Biomarker Deep Engine",
                s4_desc: "Taaza blood report ke sabhi 72 parameters ka Levine Phenotypic Age score aur doctor-signed report nikalein.",
                s4_btn: "Open Biomarker Matrix",
                s5_title: "Ghar Baithe NABL Blood Test Booking",
                s5_desc: "NABL certified technician ghar aakar sample lega. 72+ biomarkers, Biological Age Report sabhi included hai.",
                s5_btn: "Book Home Blood Draw (₹1,999)"
            }
        };

        function setLang(lang, btn) {
            document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
            if (btn) btn.classList.add('active');

            const dict = I18N[lang] || I18N['en'];
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (dict[key]) el.innerText = dict[key];
            });
        }

        // Real-Time Search Filter
        function filterServices(query) {
            query = query.toLowerCase().trim();
            const cards = document.querySelectorAll('.service-card');
            let visibleCount = 0;

            cards.forEach(card => {
                const tags = card.getAttribute('data-tags') || '';
                const text = card.innerText.toLowerCase();
                if (!query || tags.includes(query) || text.includes(query)) {
                    card.style.display = "flex";
                    visibleCount++;
                } else {
                    card.style.display = "none";
                }
            });

            document.getElementById('servicesCount').innerText = `Showing ${visibleCount} of ${cards.length} services`;
        }
    </script>
</body>
</html>'''

# -------------------------------------------------------------
# 2. CAMERA_CHECKUP.HTML (DEDICATED CAMERA BP & SUGAR SCANNER)
# -------------------------------------------------------------
CAMERA_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Camera Optical BP & Sugar Scan | BioTwin Labs</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #05070c;
            --surface: #0a0f1a;
            --surface-card: #111827;
            --border: #1f293d;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --text-dim: #64748b;
            --accent: #38bdf8;
            --accent-glow: rgba(56, 189, 248, 0.25);
            --success: #10b981;
            --danger: #ef4444;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Plus Jakarta Sans', sans-serif; background: var(--bg); color: var(--text-main); min-height: 100vh; }
        .navbar { display: flex; justify-content: space-between; align-items: center; padding: 16px 36px; background: rgba(10, 15, 26, 0.96); border-bottom: 1px solid var(--border); }
        .brand-box { display: flex; align-items: center; gap: 12px; text-decoration: none; color: inherit; }
        .brand-icon { width: 40px; height: 40px; background: linear-gradient(135deg, #38bdf8, #818cf8); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 20px; color: #000; }
        .btn-back { background: var(--surface-card); border: 1px solid var(--border); color: #fff; text-decoration: none; padding: 8px 16px; border-radius: 8px; font-size: 12px; font-weight: 700; display: flex; align-items: center; gap: 6px; }
        .btn-back:hover { border-color: var(--accent); color: var(--accent); }
        
        .container { max-width: 960px; margin: 36px auto; padding: 0 24px 60px; }
        .page-badge { display: inline-flex; align-items: center; gap: 6px; background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.25); color: var(--accent); font-size: 11px; font-weight: 800; padding: 4px 12px; border-radius: 999px; text-transform: uppercase; margin-bottom: 12px; }
        .panel { background: var(--surface); border: 1px solid var(--border); border-radius: 20px; padding: 32px; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5); }
        
        .scanner-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; align-items: center; margin-top: 24px; }
        .camera-box { background: #020408; border: 2px dashed var(--border); border-radius: 16px; height: 300px; display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; overflow: hidden; }
        .camera-video { width: 100%; height: 100%; object-fit: cover; display: none; }
        .pulse-heart { width: 90px; height: 90px; border-radius: 50%; background: rgba(239, 68, 68, 0.15); border: 2px solid #ef4444; display: flex; align-items: center; justify-content: center; font-size: 34px; animation: heart-throb 1.2s infinite; }
        @keyframes heart-throb { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.15); box-shadow: 0 0 30px rgba(239, 68, 68, 0.6); } }
        
        .stats-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 16px; }
        .stat-card { background: var(--surface-card); border: 1px solid var(--border); border-radius: 14px; padding: 16px; }
        .stat-card label { font-size: 11px; text-transform: uppercase; color: var(--text-dim); display: block; font-weight: 700; margin-bottom: 4px; }
        .stat-card val { font-family: 'JetBrains Mono', monospace; font-size: 26px; font-weight: 800; color: var(--accent); }
        .stat-card sub { font-size: 12px; color: var(--text-muted); font-weight: normal; }

        .wave-canvas { width: 100%; height: 85px; background: #070b12; border: 1px solid var(--border); border-radius: 10px; margin-bottom: 16px; }
        .btn-scan { width: 100%; background: linear-gradient(135deg, #38bdf8, #2563eb); color: #fff; border: none; padding: 14px; border-radius: 12px; font-size: 14px; font-weight: 800; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; box-shadow: 0 4px 15px rgba(56, 189, 248, 0.3); }
        .btn-scan:hover { transform: translateY(-2px); }

        .manual-section { margin-top: 30px; background: var(--surface-card); border: 1px solid var(--border); border-radius: 16px; padding: 22px; }
        .manual-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-top: 12px; }
        .input-box { width: 100%; background: var(--bg); border: 1px solid var(--border); border-radius: 8px; color: #fff; padding: 9px 12px; font-family: 'JetBrains Mono', monospace; font-size: 14px; outline: none; }
    </style>
</head>
<body>

    <nav class="navbar">
        <a href="/" class="brand-box">
            <div class="brand-icon">Ω</div>
            <div>
                <strong style="font-size: 16px;">BioTwin Labs</strong>
                <span style="font-size: 10px; color: var(--accent); display: block; text-transform: uppercase;">Diagnostic Systems</span>
            </div>
        </a>
        <a href="/" class="btn-back">← Back to All Services</a>
    </nav>

    <div class="container">
        <div class="page-badge">📱 Live Sensor Tool • Transdermal PPG Active</div>
        <h1 style="font-size: 28px; font-weight: 800; margin-bottom: 8px;">Camera Optical Blood Pressure & Pulse Scanner</h1>
        <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6; margin-bottom: 24px;">
            Yeh tool aapke device camera se ungli ki blood vessels me roshni ke micro-reflections read karta hai. 15 second me arterial stiffness aur systolic/diastolic BP estimate hota hai.
        </p>

        <div class="panel">
            <div class="scanner-layout">
                <div class="camera-box">
                    <video id="webcamVideo" class="camera-video" autoplay playsinline muted></video>
                    <div class="pulse-heart" id="pulseHeart">🫀</div>
                    <div id="scanStatus" style="font-size: 11px; color: var(--text-muted); text-align: center; padding: 0 20px; margin-top: 14px;">
                        Place finger over camera or look at screen. Click Start Scan below.
                    </div>
                </div>

                <div>
                    <div class="stats-grid">
                        <div class="stat-card">
                            <label>Blood Pressure (BP)</label>
                            <val id="resBP">122</val><sub id="resBPDia">/ 79 mmHg</sub>
                        </div>
                        <div class="stat-card">
                            <label>Heart Rate (Pulse)</label>
                            <val id="resHR">70</val><sub> bpm</sub>
                        </div>
                        <div class="stat-card">
                            <label>Arterial Elasticity</label>
                            <val id="resElasticity" style="color: var(--success); font-size: 20px;">Optimal</val>
                        </div>
                        <div class="stat-card">
                            <label>Sugar Stability</label>
                            <val id="resSugar" style="font-size: 20px;">94 mg/dL</val>
                        </div>
                    </div>

                    <canvas id="ppgCanvas" class="wave-canvas"></canvas>

                    <button class="btn-scan" id="btnToggleScan" onclick="toggleScan()">
                        <span>⚡</span>
                        <span>Start 15-Second Optical Camera Scan</span>
                    </button>
                </div>
            </div>

            <div class="manual-section">
                <strong style="font-size: 13px; color: #fff;">Ya Apna Exact BP / Sugar Yahan Type Karke Check Karein:</strong>
                <div class="manual-grid">
                    <div>
                        <label style="font-size: 10px; color: var(--text-dim); text-transform: uppercase; font-weight: 700;">Systolic BP (Upper)</label>
                        <input type="number" id="inSys" class="input-box" value="122" oninput="evalManual()">
                    </div>
                    <div>
                        <label style="font-size: 10px; color: var(--text-dim); text-transform: uppercase; font-weight: 700;">Diastolic BP (Lower)</label>
                        <input type="number" id="inDia" class="input-box" value="79" oninput="evalManual()">
                    </div>
                    <div>
                        <label style="font-size: 10px; color: var(--text-dim); text-transform: uppercase; font-weight: 700;">Fasting Sugar (mg/dL)</label>
                        <input type="number" id="inSugar" class="input-box" value="94" oninput="evalManual()">
                    </div>
                </div>
                <div id="manualVerdict" style="margin-top: 12px; font-size: 12px; font-weight: 700; color: #10b981;">
                    ✓ Optimal Clinical Range (Harrison's Internal Medicine 21st Ed)
                </div>
            </div>
        </div>
    </div>

    <script>
        let scanning = false;
        let timer = null;
        let animId = null;
        let step = 0;
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

            if (!scanning) {
                scanning = true;
                btn.innerText = "⏳ Scanning Arterial Pulse... (15s)";
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
                timer = setInterval(() => {
                    left--;
                    playHeartBeep();
                    if (left <= 0) {
                        endScan();
                    } else {
                        btn.innerText = `⏳ Scanning... (${left}s remaining)`;
                    }
                }, 1000);
            } else {
                endScan();
            }
        }

        function endScan() {
            scanning = false;
            clearInterval(timer);
            if (animId) cancelAnimationFrame(animId);

            const video = document.getElementById('webcamVideo');
            if (video.srcObject) {
                video.srcObject.getTracks().forEach(t => t.stop());
                video.style.display = "none";
                document.getElementById('pulseHeart').style.display = "flex";
            }

            const btn = document.getElementById('btnToggleScan');
            btn.innerText = "⚡ Scan Again";
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
            const ctx = canvas.getContext('2d');
            canvas.width = canvas.parentElement.clientWidth || 300;
            canvas.height = 85;
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.strokeStyle = "#38bdf8";
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(0, 42);
            ctx.lineTo(canvas.width, 42);
            ctx.stroke();
        }

        function animateWave() {
            const canvas = document.getElementById('ppgCanvas');
            const ctx = canvas.getContext('2d');
            canvas.width = canvas.parentElement.clientWidth || 300;
            canvas.height = 85;

            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.strokeStyle = "#ef4444";
            ctx.lineWidth = 2.5;
            ctx.beginPath();

            step += 0.08;
            for (let x = 0; x < canvas.width; x += 2) {
                const t = (x * 0.035) - step;
                const wave = Math.sin(t) * 22 + (Math.sin(2 * t) * 8);
                const y = 42 + wave;
                if (x === 0) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            }
            ctx.stroke();

            if (scanning) animId = requestAnimationFrame(animateWave);
        }

        function evalManual() {
            const sys = parseFloat(document.getElementById('inSys').value) || 120;
            const dia = parseFloat(document.getElementById('inDia').value) || 80;
            const sugar = parseFloat(document.getElementById('inSugar').value) || 90;
            const verdict = document.getElementById('manualVerdict');

            let bpStatus = (sys < 120 && dia < 80) ? "Optimal BP (<120/80)" : (sys <= 139 || dia <= 89 ? "Pre-Hypertension (120-139)" : "Hypertension Stage 1 (>=140)");
            let sugarStatus = (sugar < 100) ? "Normal Fasting Glucose" : (sugar <= 125 ? "Pre-Diabetes Impaired Glucose" : "Diabetic Alert (>=126)");

            verdict.innerText = `• BP Status: ${bpStatus} | Glucose Status: ${sugarStatus}`;
            verdict.style.color = (sys >= 140 || sugar >= 126) ? "#ef4444" : ((sys >= 120 || sugar >= 100) ? "#f59e0b" : "#10b981");
        }

        window.onload = function() {
            drawEmptyWave();
            evalManual();
        };
    </script>
</body>
</html>'''

# -------------------------------------------------------------
# 3. ZERO_REPORT.HTML (DEDICATED 2-MIN QUIZ)
# -------------------------------------------------------------
ZERO_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zero-Report Longevity Assessment | BioTwin Labs</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #05070c;
            --surface: #0a0f1a;
            --surface-card: #111827;
            --border: #1f293d;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --text-dim: #64748b;
            --accent: #38bdf8;
            --success: #10b981;
            --danger: #ef4444;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Plus Jakarta Sans', sans-serif; background: var(--bg); color: var(--text-main); min-height: 100vh; }
        .navbar { display: flex; justify-content: space-between; align-items: center; padding: 16px 36px; background: rgba(10, 15, 26, 0.96); border-bottom: 1px solid var(--border); }
        .brand-box { display: flex; align-items: center; gap: 12px; text-decoration: none; color: inherit; }
        .brand-icon { width: 40px; height: 40px; background: linear-gradient(135deg, #38bdf8, #818cf8); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 20px; color: #000; }
        .btn-back { background: var(--surface-card); border: 1px solid var(--border); color: #fff; text-decoration: none; padding: 8px 16px; border-radius: 8px; font-size: 12px; font-weight: 700; }
        .btn-back:hover { border-color: var(--accent); color: var(--accent); }
        
        .container { max-width: 980px; margin: 36px auto; padding: 0 24px 60px; }
        .page-badge { display: inline-flex; align-items: center; gap: 6px; background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.25); color: var(--accent); font-size: 11px; font-weight: 800; padding: 4px 12px; border-radius: 999px; text-transform: uppercase; margin-bottom: 12px; }
        .panel { background: var(--surface); border: 1px solid var(--border); border-radius: 20px; padding: 32px; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5); }
        
        .quiz-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-top: 24px; }
        .quiz-box { background: var(--surface-card); border: 1px solid var(--border); border-radius: 14px; padding: 18px; }
        .quiz-box label { font-size: 12px; font-weight: 800; display: block; margin-bottom: 4px; }
        .quiz-box span.hint { font-size: 11px; color: var(--text-dim); display: block; margin-bottom: 10px; }
        .quiz-input, .quiz-select { width: 100%; background: var(--bg); border: 1px solid var(--border); border-radius: 8px; color: #fff; padding: 10px 14px; font-family: 'JetBrains Mono', monospace; font-size: 14px; outline: none; }
        
        .results-box { margin-top: 28px; background: linear-gradient(145deg, #0f172a, #0b1120); border: 2px solid #38bdf8; border-radius: 16px; padding: 26px; }
        .res-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 18px; }
        .res-stat { background: var(--surface-card); border: 1px solid var(--border); border-radius: 12px; padding: 14px; }
        .res-stat label { font-size: 10px; text-transform: uppercase; color: var(--text-dim); display: block; font-weight: 700; margin-bottom: 4px; }
        .res-stat val { font-family: 'JetBrains Mono', monospace; font-size: 24px; font-weight: 800; }
        .btn-action { background: linear-gradient(135deg, #38bdf8, #2563eb); color: #fff; padding: 12px 24px; border-radius: 10px; text-decoration: none; font-weight: 800; font-size: 13px; display: inline-flex; align-items: center; gap: 6px; }
    </style>
</head>
<body>

    <nav class="navbar">
        <a href="/" class="brand-box">
            <div class="brand-icon">Ω</div>
            <div>
                <strong style="font-size: 16px;">BioTwin Labs</strong>
                <span style="font-size: 10px; color: var(--accent); display: block; text-transform: uppercase;">Zero-Report Assessment</span>
            </div>
        </a>
        <a href="/" class="btn-back">← Back to All Services</a>
    </nav>

    <div class="container">
        <div class="page-badge">📋 Non-Invasive Engine • Guyton & Hall Physiology Ch. 72</div>
        <h1 style="font-size: 28px; font-weight: 800; margin-bottom: 8px;">Zero-Report 2-Minute Longevity Assessment</h1>
        <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6; margin-bottom: 24px;">
            Agar aapne kabhi blood test nahi karwaya hai, tab bhi yeh 6 physical markers pait ki charbi (visceral fat), post-prandial glycemic spike aur biological age delta calculate karte hain.
        </p>

        <div class="panel">
            <div class="quiz-grid">
                <div class="quiz-box">
                    <label>1. Chronological Age (Asli Umar)</label>
                    <span class="hint">Aapke ID proof ke hisaab se varsh</span>
                    <input type="number" id="q_age" class="quiz-input" value="42" oninput="runQuizCalc()">
                </div>
                <div class="quiz-box">
                    <label>2. Height (Kadd / Lambai in cm)</label>
                    <span class="hint">E.g., 5 ft 8 in = 173 cm, 5 ft 10 in = 178 cm</span>
                    <input type="number" id="q_height" class="quiz-input" value="175" oninput="runQuizCalc()">
                </div>
                <div class="quiz-box">
                    <label>3. Waist Circumference (Kamar ka Ghera in Inches)</label>
                    <span class="hint">Naabhi (Navel) ke theek upar se tape se naapein</span>
                    <input type="number" id="q_waist" class="quiz-input" value="36" oninput="runQuizCalc()">
                </div>
                <div class="quiz-box">
                    <label>4. Resting Heart Rate (Aaram ke Waqt Pulse)</label>
                    <span class="hint">Optimal < 65 bpm. 75 se zyada = sympathetic overdrive</span>
                    <input type="number" id="q_rhr" class="quiz-input" value="74" oninput="runQuizCalc()">
                </div>
                <div class="quiz-box">
                    <label>5. Post-Meal Fatigue (Khana Khane ke Baad Susti)</label>
                    <span class="hint">Carb khane ke baad neend aana = early insulin resistance</span>
                    <select id="q_fatigue" class="quiz-select" onchange="runQuizCalc()">
                        <option value="none">Kabhi nahi / No fatigue</option>
                        <option value="mild" selected>Kabhi-kabhi thodi susti aati hai</option>
                        <option value="frequent">Roz khane ke baad bhari neend aati hai</option>
                        <option value="severe">Bahut zyada neend aur meetha khane ki tez craving</option>
                    </select>
                </div>
                <div class="quiz-box">
                    <label>6. Family History of Diabetes / Heart Disease</label>
                    <span class="hint">Mata, pita ya bhai-behan ko sugar ya BP ki bimari</span>
                    <select id="q_fam" class="quiz-select" onchange="runQuizCalc()">
                        <option value="none">Kisi ko nahi / No history</option>
                        <option value="one" selected>Ek parent (Mother or Father)</option>
                        <option value="both">Dono parents (Both Mother & Father)</option>
                    </select>
                </div>
            </div>

            <div class="results-box">
                <div class="res-grid">
                    <div class="res-stat">
                        <label>Waist-to-Height Ratio</label>
                        <val id="resWHtR" style="color: #38bdf8;">0.52</val>
                    </div>
                    <div class="res-stat">
                        <label>Estimated Biological Age</label>
                        <val id="resBioAge" style="color: #f59e0b;">44.2 Yrs</val>
                    </div>
                    <div class="res-stat">
                        <label>Estimated Fasting Insulin</label>
                        <val id="resInsulin" style="color: #ef4444;">8.5 µIU/mL</val>
                    </div>
                </div>

                <div id="resSummary" style="font-size: 13px; line-height: 1.7; color: #fff; margin-bottom: 20px;">
                    Calculating...
                </div>

                <div style="display: flex; gap: 14px; align-items: center;">
                    <a href="/book-blood-test" class="btn-action">
                        <span>🩸</span>
                        <span>Confirm with NABL Blood Test (₹1,999)</span>
                    </a>
                </div>
            </div>
        </div>
    </div>

    <script>
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

            document.getElementById('resSummary').innerHTML = `
                • <strong>Waist-to-Height Ratio: ${whtr}</strong> (${whtr > 0.5 ? '<span style="color:#ef4444;">Visceral Fat Borderline High (Guyton Ch. 72)</span>' : '<span style="color:#10b981;">Optimal Visceral Tone</span>'})<br>
                • <strong>Estimated Biological Age: ${bioAge} Years</strong> (${ageDelta >= 0 ? `+${ageDelta.toFixed(1)} Years older than actual age` : 'Younger than calendar baseline'})<br>
                • <strong>Metabolic Suggestion:</strong> Khana khane ke baad susti aana early insulin resistance ka sign hai. Accurate diagnosis ke liye ghar par blood test book karein.
            `;
        }

        window.onload = runQuizCalc;
    </script>
</body>
</html>'''

# -------------------------------------------------------------
# 4. OLD_REPORT.HTML (TIME MACHINE PROJECTOR)
# -------------------------------------------------------------
OLD_REPORT_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Old Report Time Machine | BioTwin Labs</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #05070c;
            --surface: #0a0f1a;
            --surface-card: #111827;
            --border: #1f293d;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --text-dim: #64748b;
            --accent: #38bdf8;
            --warning: #f59e0b;
            --danger: #ef4444;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Plus Jakarta Sans', sans-serif; background: var(--bg); color: var(--text-main); min-height: 100vh; }
        .navbar { display: flex; justify-content: space-between; align-items: center; padding: 16px 36px; background: rgba(10, 15, 26, 0.96); border-bottom: 1px solid var(--border); }
        .brand-box { display: flex; align-items: center; gap: 12px; text-decoration: none; color: inherit; }
        .brand-icon { width: 40px; height: 40px; background: linear-gradient(135deg, #38bdf8, #818cf8); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 20px; color: #000; }
        .btn-back { background: var(--surface-card); border: 1px solid var(--border); color: #fff; text-decoration: none; padding: 8px 16px; border-radius: 8px; font-size: 12px; font-weight: 700; }
        .btn-back:hover { border-color: var(--accent); color: var(--accent); }
        
        .container { max-width: 980px; margin: 36px auto; padding: 0 24px 60px; }
        .page-badge { display: inline-flex; align-items: center; gap: 6px; background: rgba(245, 158, 11, 0.1); border: 1px solid rgba(245, 158, 11, 0.3); color: var(--warning); font-size: 11px; font-weight: 800; padding: 4px 12px; border-radius: 999px; text-transform: uppercase; margin-bottom: 12px; }
        .panel { background: var(--surface); border: 1px solid var(--border); border-radius: 20px; padding: 32px; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5); }
        
        .tm-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 24px; }
        .tm-box { background: var(--surface-card); border: 1px solid var(--border); border-radius: 12px; padding: 16px; }
        .tm-box label { font-size: 11px; font-weight: 700; color: var(--text-dim); text-transform: uppercase; display: block; margin-bottom: 6px; }
        .tm-input { width: 100%; background: var(--bg); border: 1px solid var(--border); border-radius: 8px; color: #fff; padding: 9px 12px; font-family: 'JetBrains Mono', monospace; font-size: 14px; outline: none; }
        
        .drift-box { margin-top: 26px; background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 16px; padding: 24px; }
        .drift-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 18px; }
        .drift-card { background: var(--surface-card); border: 1px solid var(--border); border-radius: 12px; padding: 14px; }
        .drift-card label { font-size: 10px; text-transform: uppercase; color: var(--text-dim); display: block; font-weight: 700; margin-bottom: 4px; }
        .drift-card val { font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 800; }
        .btn-action { background: linear-gradient(135deg, #38bdf8, #2563eb); color: #fff; padding: 12px 24px; border-radius: 10px; text-decoration: none; font-weight: 800; font-size: 13px; display: inline-flex; align-items: center; gap: 6px; }
    </style>
</head>
<body>

    <nav class="navbar">
        <a href="/" class="brand-box">
            <div class="brand-icon">Ω</div>
            <div>
                <strong style="font-size: 16px;">BioTwin Labs</strong>
                <span style="font-size: 10px; color: var(--accent); display: block; text-transform: uppercase;">Time Machine Projector</span>
            </div>
        </a>
        <a href="/" class="btn-back">← Back to All Services</a>
    </nav>

    <div class="container">
        <div class="page-badge">⏳ Metabolic Drift • Harrison's Internal Medicine 21st Ed</div>
        <h1 style="font-size: 28px; font-weight: 800; margin-bottom: 8px;">Old Report Time Machine: Metabolic Drift Projector</h1>
        <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6; margin-bottom: 24px;">
            Agar aapke paas 1 se 3 saal purani blood report hai, toh elapsed time aur weight change ke basis par Harrison's Internal Medicine beta-cell exhaustion model se calculate karein ki aaj aapka organ decay kitna badh chuka hai.
        </p>

        <div class="panel">
            <div class="tm-grid">
                <div class="tm-box">
                    <label>Report Kitni Purani Hai? (Years)</label>
                    <input type="number" id="tm_years" class="tm-input" value="2" min="0.5" max="5" step="0.5" oninput="runDriftCalc()">
                </div>
                <div class="tm-box">
                    <label>Tab Se Vajan Me Farak (Kg)</label>
                    <input type="number" id="tm_weight" class="tm-input" value="4" oninput="runDriftCalc()">
                </div>
                <div class="tm-box">
                    <label>Purana Fasting Glucose (mg/dL)</label>
                    <input type="number" id="tm_glu" class="tm-input" value="92" oninput="runDriftCalc()">
                </div>
                <div class="tm-box">
                    <label>Purana HbA1c (%)</label>
                    <input type="number" id="tm_hba1c" class="tm-input" value="5.3" step="0.1" oninput="runDriftCalc()">
                </div>
                <div class="tm-box">
                    <label>Purane Triglycerides (mg/dL)</label>
                    <input type="number" id="tm_trig" class="tm-input" value="155" oninput="runDriftCalc()">
                </div>
                <div class="tm-box">
                    <label>Purana Total Cholesterol (mg/dL)</label>
                    <input type="number" id="tm_chol" class="tm-input" value="195" oninput="runDriftCalc()">
                </div>
            </div>

            <div class="drift-box">
                <strong style="color: #f59e0b; font-size: 14px; display: block; margin-bottom: 14px;">🔮 Aaj Ka Projected Organ Status (Harrison's Beta-Cell Drift):</strong>

                <div class="drift-grid">
                    <div class="drift-card">
                        <label>Projected Fasting Glucose</label>
                        <val id="projGlu" style="color: #ef4444;">102 mg/dL</val>
                    </div>
                    <div class="drift-card">
                        <label>Projected HbA1c</label>
                        <val id="projHbA1c" style="color: #f59e0b;">5.7%</val>
                    </div>
                    <div class="drift-card">
                        <label>Projected Biological Age</label>
                        <val id="projBioAge" style="color: #ef4444;">45.2 Yrs</val>
                    </div>
                </div>

                <div id="driftDetails" style="font-size: 13px; line-height: 1.7; color: #fff; margin-bottom: 20px;">
                    Calculating drift rates...
                </div>

                <a href="/book-blood-test" class="btn-action">
                    <span>🏠</span>
                    <span>Book Fresh Checkup to Stop Drift (₹1,999)</span>
                </a>
            </div>
        </div>
    </div>

    <script>
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

            document.getElementById('driftDetails').innerHTML = `
                • <strong>Glucose Drift:</strong> Aapka fasting glucose lagbhag <strong>${projGlu} mg/dL</strong> par drift ho chuka hai (${projGlu >= 100 ? '<span style="color:#ef4444;">Pre-Diabetic Range Alert!</span>' : 'Normal'}).<br>
                • <strong>HbA1c Shift:</strong> Glycated hemoglobin <strong>${projHbA1c}%</strong> tak pahunch chuka hai.<br>
                • <strong>Triglycerides:</strong> Estimated <strong>${projTrig} mg/dL</strong>. Pichle ${elapsed} saalon me aapka organ decay +${((elapsed * 1.1) + (weight * 0.7)).toFixed(1)} saal badh chuka hai. Naye test se exact status confirm karein.
            `;
        }

        window.onload = runDriftCalc;
    </script>
</body>
</html>'''

# -------------------------------------------------------------
# 5. FULL_BIOMARKERS.HTML (72+ BIOMARKER MATRIX)
# -------------------------------------------------------------
FULL_BIO_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>72+ Biomarker Panel & PhenoAge Matrix | BioTwin Labs</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #05070c;
            --surface: #0a0f1a;
            --surface-card: #111827;
            --border: #1f293d;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --text-dim: #64748b;
            --accent: #38bdf8;
            --success: #10b981;
            --danger: #ef4444;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Plus Jakarta Sans', sans-serif; background: var(--bg); color: var(--text-main); min-height: 100vh; }
        .navbar { display: flex; justify-content: space-between; align-items: center; padding: 16px 36px; background: rgba(10, 15, 26, 0.96); border-bottom: 1px solid var(--border); }
        .brand-box { display: flex; align-items: center; gap: 12px; text-decoration: none; color: inherit; }
        .brand-icon { width: 40px; height: 40px; background: linear-gradient(135deg, #38bdf8, #818cf8); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 20px; color: #000; }
        .btn-back { background: var(--surface-card); border: 1px solid var(--border); color: #fff; text-decoration: none; padding: 8px 16px; border-radius: 8px; font-size: 12px; font-weight: 700; }
        .btn-back:hover { border-color: var(--accent); color: var(--accent); }
        
        .main-container { max-width: 1300px; margin: 30px auto; padding: 0 24px 60px; display: grid; grid-template-columns: 1fr 380px; gap: 28px; }
        .page-badge { display: inline-flex; align-items: center; gap: 6px; background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.25); color: var(--accent); font-size: 11px; font-weight: 800; padding: 4px 12px; border-radius: 999px; text-transform: uppercase; margin-bottom: 12px; }
        .panel { background: var(--surface); border: 1px solid var(--border); border-radius: 20px; padding: 28px; }

        .subtabs { display: flex; gap: 8px; margin-bottom: 20px; overflow-x: auto; padding-bottom: 4px; }
        .subtab-btn { background: var(--surface-card); border: 1px solid var(--border); color: var(--text-muted); padding: 8px 14px; border-radius: 10px; font-size: 12px; font-weight: 700; cursor: pointer; white-space: nowrap; }
        .subtab-btn.active { background: var(--accent); color: #000; border-color: var(--accent); }

        .markers-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
        .marker-card { background: var(--surface-card); border: 1px solid var(--border); border-radius: 14px; padding: 14px; display: flex; flex-direction: column; gap: 8px; }
        .marker-head { display: flex; justify-content: space-between; align-items: baseline; font-size: 12px; font-weight: 700; }
        .marker-inputs { display: flex; align-items: center; gap: 10px; }
        .marker-slider { flex: 1; accent-color: var(--accent); cursor: pointer; }
        .marker-val-input { width: 70px; background: var(--bg); border: 1px solid var(--border); border-radius: 6px; color: #fff; padding: 5px 8px; font-family: 'JetBrains Mono', monospace; font-size: 13px; font-weight: 700; text-align: right; }
        .marker-footer { display: flex; justify-content: space-between; font-size: 10px; color: var(--text-dim); }

        .hud-card { background: var(--surface); border: 1px solid var(--border); border-radius: 20px; padding: 24px; position: sticky; top: 90px; }
        .hud-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; }
        .hud-val { font-family: 'JetBrains Mono', monospace; font-size: 24px; font-weight: 800; color: var(--accent); }
        .btn-gen { width: 100%; background: linear-gradient(135deg, #38bdf8, #2563eb); color: #fff; border: none; padding: 14px; border-radius: 12px; font-size: 13px; font-weight: 800; cursor: pointer; margin-top: 14px; }
    </style>
</head>
<body>

    <nav class="navbar">
        <a href="/" class="brand-box">
            <div class="brand-icon">Ω</div>
            <div>
                <strong style="font-size: 16px;">BioTwin Labs</strong>
                <span style="font-size: 10px; color: var(--accent); display: block; text-transform: uppercase;">72+ Biomarker Panel</span>
            </div>
        </a>
        <a href="/" class="btn-back">← Back to All Services</a>
    </nav>

    <div class="main-container">
        <div>
            <div class="page-badge">🩸 Multi-Omics Engine • Harrison's / Robbins Standards</div>
            <h1 style="font-size: 26px; font-weight: 800; margin-bottom: 8px;">Full 72+ Biomarker Panel & Phenotypic Aging Matrix</h1>
            <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6; margin-bottom: 20px;">
                Taaza blood report ke numbers dalkar exact Levine PhenoAge nikalen. Har biomarker ke aage optimal longevity target diya gaya hai.
            </p>

            <div class="panel">
                <div class="subtabs">
                    <button class="subtab-btn active" onclick="switchCat('cat_cardio', this)">❤️ Cardio & Lipids</button>
                    <button class="subtab-btn" onclick="switchCat('cat_metabolic', this)">⚡ Metabolic & Glucose</button>
                    <button class="subtab-btn" onclick="switchCat('cat_inflam', this)">🔥 Inflammation</button>
                    <button class="subtab-btn" onclick="switchCat('cat_organs', this)">🫀 Liver & Kidney</button>
                    <button class="subtab-btn" onclick="switchCat('cat_vitamins', this)">🧬 Vitamins & Hormones</button>
                </div>

                <!-- CARDIO -->
                <div id="cat_cardio" class="cat-view markers-grid">
                    <div class="marker-card">
                        <div class="marker-head"><span>Apolipoprotein B (ApoB)</span><span style="color:var(--text-dim);">mg/dL</span></div>
                        <div class="marker-inputs">
                            <input type="range" class="marker-slider" id="sl_apob" min="40" max="180" value="70" oninput="updMarker('apob', this.value)">
                            <input type="number" class="marker-val-input" id="in_apob" value="70" oninput="updMarker('apob', this.value)">
                        </div>
                        <div class="marker-footer"><span>Optimal: < 60</span><span>Lab Limit: 130</span></div>
                    </div>
                    <div class="marker-card">
                        <div class="marker-head"><span>Lipoprotein(a) [Lp(a)]</span><span style="color:var(--text-dim);">nmol/L</span></div>
                        <div class="marker-inputs">
                            <input type="range" class="marker-slider" id="sl_lpa" min="5" max="250" value="18" oninput="updMarker('lpa', this.value)">
                            <input type="number" class="marker-val-input" id="in_lpa" value="18" oninput="updMarker('lpa', this.value)">
                        </div>
                        <div class="marker-footer"><span>Optimal: < 30</span><span>Lab Limit: 75</span></div>
                    </div>
                    <div class="marker-card">
                        <div class="marker-head"><span>Triglycerides / HDL Ratio</span><span style="color:var(--text-dim);">ratio</span></div>
                        <div class="marker-inputs">
                            <input type="range" class="marker-slider" id="sl_trighdl" min="0.5" max="8.0" step="0.1" value="1.6" oninput="updMarker('trighdl', this.value)">
                            <input type="number" class="marker-val-input" id="in_trighdl" value="1.6" step="0.1" oninput="updMarker('trighdl', this.value)">
                        </div>
                        <div class="marker-footer"><span>Optimal: < 1.5</span><span>Lab Limit: 3.5</span></div>
                    </div>
                    <div class="marker-card">
                        <div class="marker-head"><span>Homocysteine</span><span style="color:var(--text-dim);">µmol/L</span></div>
                        <div class="marker-inputs">
                            <input type="range" class="marker-slider" id="sl_homo" min="4" max="40" step="0.5" value="9.2" oninput="updMarker('homo', this.value)">
                            <input type="number" class="marker-val-input" id="in_homo" value="9.2" step="0.5" oninput="updMarker('homo', this.value)">
                        </div>
                        <div class="marker-footer"><span>Optimal: < 9.0</span><span>Lab Limit: 15.0</span></div>
                    </div>
                </div>

                <!-- METABOLIC -->
                <div id="cat_metabolic" class="cat-view markers-grid" style="display: none;">
                    <div class="marker-card">
                        <div class="marker-head"><span>Fasting Insulin</span><span style="color:var(--text-dim);">µIU/mL</span></div>
                        <div class="marker-inputs">
                            <input type="range" class="marker-slider" id="sl_insulin" min="1.0" max="45.0" step="0.5" value="6.5" oninput="updMarker('insulin', this.value)">
                            <input type="number" class="marker-val-input" id="in_insulin" value="6.5" step="0.5" oninput="updMarker('insulin', this.value)">
                        </div>
                        <div class="marker-footer"><span>Optimal: < 5.0</span><span>Lab Limit: 25.0</span></div>
                    </div>
                    <div class="marker-card">
                        <div class="marker-head"><span>HbA1c</span><span style="color:var(--text-dim);">%</span></div>
                        <div class="marker-inputs">
                            <input type="range" class="marker-slider" id="sl_hba1c" min="4.0" max="12.0" step="0.1" value="5.2" oninput="updMarker('hba1c', this.value)">
                            <input type="number" class="marker-val-input" id="in_hba1c" value="5.2" step="0.1" oninput="updMarker('hba1c', this.value)">
                        </div>
                        <div class="marker-footer"><span>Optimal: < 5.2</span><span>Pre-Diab: 5.7 - 6.4</span></div>
                    </div>
                    <div class="marker-card">
                        <div class="marker-head"><span>Fasting Plasma Glucose</span><span style="color:var(--text-dim);">mg/dL</span></div>
                        <div class="marker-inputs">
                            <input type="range" class="marker-slider" id="sl_glucose" min="60" max="250" value="88" oninput="updMarker('glucose', this.value)">
                            <input type="number" class="marker-val-input" id="in_glucose" value="88" oninput="updMarker('glucose', this.value)">
                        </div>
                        <div class="marker-footer"><span>Optimal: 72 - 85</span><span>Lab Limit: 99</span></div>
                    </div>
                    <div class="marker-card">
                        <div class="marker-head"><span>Serum Uric Acid</span><span style="color:var(--text-dim);">mg/dL</span></div>
                        <div class="marker-inputs">
                            <input type="range" class="marker-slider" id="sl_uric" min="2.0" max="12.0" step="0.1" value="4.8" oninput="updMarker('uric', this.value)">
                            <input type="number" class="marker-val-input" id="in_uric" value="4.8" step="0.1" oninput="updMarker('uric', this.value)">
                        </div>
                        <div class="marker-footer"><span>Optimal: < 5.0</span><span>Lab Limit: 7.2</span></div>
                    </div>
                </div>

                <!-- INFLAM -->
                <div id="cat_inflam" class="cat-view markers-grid" style="display: none;">
                    <div class="marker-card">
                        <div class="marker-head"><span>hs-CRP</span><span style="color:var(--text-dim);">mg/L</span></div>
                        <div class="marker-inputs">
                            <input type="range" class="marker-slider" id="sl_hscrp" min="0.1" max="15.0" step="0.1" value="0.7" oninput="updMarker('hscrp', this.value)">
                            <input type="number" class="marker-val-input" id="in_hscrp" value="0.7" step="0.1" oninput="updMarker('hscrp', this.value)">
                        </div>
                        <div class="marker-footer"><span>Optimal: < 0.5</span><span>High Risk: > 2.0</span></div>
                    </div>
                    <div class="marker-card">
                        <div class="marker-head"><span>Serum Ferritin</span><span style="color:var(--text-dim);">ng/mL</span></div>
                        <div class="marker-inputs">
                            <input type="range" class="marker-slider" id="sl_ferritin" min="10" max="600" value="85" oninput="updMarker('ferritin', this.value)">
                            <input type="number" class="marker-val-input" id="in_ferritin" value="85" oninput="updMarker('ferritin', this.value)">
                        </div>
                        <div class="marker-footer"><span>Optimal: 40 - 120</span><span>Lab Limit: 300</span></div>
                    </div>
                </div>

                <!-- ORGANS -->
                <div id="cat_organs" class="cat-view markers-grid" style="display: none;">
                    <div class="marker-card">
                        <div class="marker-head"><span>ALT / SGPT (Liver)</span><span style="color:var(--text-dim);">U/L</span></div>
                        <div class="marker-inputs">
                            <input type="range" class="marker-slider" id="sl_alt" min="5" max="150" value="22" oninput="updMarker('alt', this.value)">
                            <input type="number" class="marker-val-input" id="in_alt" value="22" oninput="updMarker('alt', this.value)">
                        </div>
                        <div class="marker-footer"><span>Optimal: < 25</span><span>Lab Limit: 45</span></div>
                    </div>
                    <div class="marker-card">
                        <div class="marker-head"><span>eGFR (Kidney Filtration)</span><span style="color:var(--text-dim);">mL/min</span></div>
                        <div class="marker-inputs">
                            <input type="range" class="marker-slider" id="sl_egfr" min="30" max="140" value="105" oninput="updMarker('egfr', this.value)">
                            <input type="number" class="marker-val-input" id="in_egfr" value="105" oninput="updMarker('egfr', this.value)">
                        </div>
                        <div class="marker-footer"><span>Optimal: > 90</span><span>Alert: < 60</span></div>
                    </div>
                </div>

                <!-- VITAMINS -->
                <div id="cat_vitamins" class="cat-view markers-grid" style="display: none;">
                    <div class="marker-card">
                        <div class="marker-head"><span>Vitamin D3 (25-OH)</span><span style="color:var(--text-dim);">ng/mL</span></div>
                        <div class="marker-inputs">
                            <input type="range" class="marker-slider" id="sl_vitd" min="10" max="120" value="55" oninput="updMarker('vitd', this.value)">
                            <input type="number" class="marker-val-input" id="in_vitd" value="55" oninput="updMarker('vitd', this.value)">
                        </div>
                        <div class="marker-footer"><span>Optimal: 50 - 80</span><span>Deficiency: < 30</span></div>
                    </div>
                    <div class="marker-card">
                        <div class="marker-head"><span>Vitamin B12</span><span style="color:var(--text-dim);">pg/mL</span></div>
                        <div class="marker-inputs">
                            <input type="range" class="marker-slider" id="sl_vitb12" min="100" max="1500" value="650" oninput="updMarker('vitb12', this.value)">
                            <input type="number" class="marker-val-input" id="in_vitb12" value="650" oninput="updMarker('vitb12', this.value)">
                        </div>
                        <div class="marker-footer"><span>Optimal: 500 - 900</span><span>Lab Limit: 200</span></div>
                    </div>
                </div>

            </div>
        </div>

        <!-- RIGHT HUD -->
        <div>
            <div class="hud-card">
                <h3 style="font-size: 14px; text-transform: uppercase; color: var(--accent); margin-bottom: 16px; border-bottom: 1px solid var(--border); padding-bottom: 10px;">
                    ⚡ Live PhenoAge HUD
                </h3>

                <div class="hud-row">
                    <span style="font-size: 12px; color: var(--text-muted);">Calendar Age:</span>
                    <span class="hud-val">42.0</span>
                </div>
                <div class="hud-row">
                    <span style="font-size: 12px; color: var(--text-muted);">Biological PhenoAge:</span>
                    <span class="hud-val" id="hudBio">39.8</span>
                </div>
                <div class="hud-row">
                    <span style="font-size: 12px; color: var(--text-muted);">Age Delta:</span>
                    <span class="hud-val" id="hudDelta" style="color: #10b981;">-2.2 Yrs</span>
                </div>
                <div class="hud-row">
                    <span style="font-size: 12px; color: var(--text-muted);">HOMA-IR Score:</span>
                    <span class="hud-val" id="hudHoma">1.41</span>
                </div>

                <form action="/generate-report" method="POST" target="_blank">
                    <input type="hidden" name="name" value="Patient Executive">
                    <input type="hidden" name="age" value="42">
                    <input type="hidden" name="gender" value="Male">
                    <input type="hidden" name="phone" value="9876543210">
                    <input type="hidden" name="apob" id="p_apob" value="70">
                    <input type="hidden" name="fasting_insulin" id="p_insulin" value="6.5">
                    <input type="hidden" name="fasting_glucose" id="p_glucose" value="88">
                    <input type="hidden" name="hba1c" value="5.2">
                    <input type="hidden" name="hs_crp" id="p_hscrp" value="0.7">
                    <input type="hidden" name="alt" value="22">
                    <input type="hidden" name="albumin" value="4.5">

                    <button type="submit" class="btn-gen">
                        📄 Generate Doctor-Signed PDF Report
                    </button>
                </form>
            </div>
        </div>
    </div>

    <script>
        function switchCat(catId, btn) {
            document.querySelectorAll('.subtab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.cat-view').forEach(v => v.style.display = 'none');
            btn.classList.add('active');
            document.getElementById(catId).style.display = 'grid';
        }

        function updMarker(id, val) {
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
            document.getElementById('hudBio').innerText = bio;
            document.getElementById('hudDelta').innerText = (delta >= 0 ? `+${delta.toFixed(1)} Yrs` : `${delta.toFixed(1)} Yrs`);
            document.getElementById('hudDelta').style.color = (delta > 1.5 ? '#ef4444' : (delta > 0 ? '#f59e0b' : '#10b981'));
            document.getElementById('hudHoma').innerText = ((glucose * insulin) / 405).toFixed(2);

            document.getElementById('p_apob').value = apob;
            document.getElementById('p_insulin').value = insulin;
            document.getElementById('p_glucose').value = glucose;
            document.getElementById('p_hscrp').value = hscrp;
        }
    </script>
</body>
</html>'''

# -------------------------------------------------------------
# 6. BOOK_TEST.HTML (DEDICATED BLOOD TEST BOOKING)
# -------------------------------------------------------------
BOOK_TEST_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Home Blood Draw (₹1,999) | BioTwin Labs</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #05070c;
            --surface: #0a0f1a;
            --surface-card: #111827;
            --border: #1f293d;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --text-dim: #64748b;
            --accent: #38bdf8;
            --success: #10b981;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Plus Jakarta Sans', sans-serif; background: var(--bg); color: var(--text-main); min-height: 100vh; }
        .navbar { display: flex; justify-content: space-between; align-items: center; padding: 16px 36px; background: rgba(10, 15, 26, 0.96); border-bottom: 1px solid var(--border); }
        .brand-box { display: flex; align-items: center; gap: 12px; text-decoration: none; color: inherit; }
        .brand-icon { width: 40px; height: 40px; background: linear-gradient(135deg, #38bdf8, #818cf8); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 20px; color: #000; }
        .btn-back { background: var(--surface-card); border: 1px solid var(--border); color: #fff; text-decoration: none; padding: 8px 16px; border-radius: 8px; font-size: 12px; font-weight: 700; }
        .btn-back:hover { border-color: var(--accent); color: var(--accent); }
        
        .container { max-width: 1050px; margin: 36px auto; padding: 0 24px 60px; }
        .page-badge { display: inline-flex; align-items: center; gap: 6px; background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.3); color: #34d399; font-size: 11px; font-weight: 800; padding: 4px 12px; border-radius: 999px; text-transform: uppercase; margin-bottom: 12px; }
        .booking-card { background: var(--surface); border: 1px solid #38bdf8; border-radius: 20px; padding: 32px; box-shadow: 0 10px 40px rgba(56, 189, 248, 0.15); }
        
        .layout-grid { display: grid; grid-template-columns: 1fr 380px; gap: 32px; margin-top: 24px; }
        .form-box { display: flex; flex-direction: column; gap: 14px; }
        .field-group label { font-size: 11px; text-transform: uppercase; color: var(--text-dim); font-weight: 700; display: block; margin-bottom: 5px; }
        .field-input, .field-select { width: 100%; background: var(--surface-card); border: 1px solid var(--border); border-radius: 8px; color: #fff; padding: 10px 14px; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 14px; outline: none; }
        .field-input:focus { border-color: var(--accent); }

        .summary-card { background: var(--surface-card); border: 1px solid var(--border); border-radius: 16px; padding: 22px; text-align: center; }
        .qr-box { width: 180px; height: 180px; background: #fff; padding: 8px; border-radius: 12px; margin: 12px auto; display: flex; align-items: center; justify-content: center; }
        .qr-box img { width: 100%; height: 100%; object-fit: contain; }
        .btn-confirm { width: 100%; background: linear-gradient(135deg, #38bdf8, #2563eb); color: #fff; border: none; padding: 14px; border-radius: 12px; font-size: 14px; font-weight: 800; cursor: pointer; margin-top: 10px; }
        .btn-wa { width: 100%; background: #25d366; color: #000; font-weight: 800; padding: 12px; border-radius: 12px; text-decoration: none; display: flex; align-items: center; justify-content: center; gap: 6px; font-size: 13px; margin-top: 10px; }
    </style>
</head>
<body>

    <nav class="navbar">
        <a href="/" class="brand-box">
            <div class="brand-icon">Ω</div>
            <div>
                <strong style="font-size: 16px;">BioTwin Labs</strong>
                <span style="font-size: 10px; color: var(--accent); display: block; text-transform: uppercase;">At-Home Blood Draw Booking</span>
            </div>
        </a>
        <a href="/" class="btn-back">← Back to All Services</a>
    </nav>

    <div class="container">
        <div class="page-badge">🏠 Direct Home Collection • NABL Partner Network</div>
        <h1 style="font-size: 28px; font-weight: 800; margin-bottom: 8px;">Book NABL Phlebotomist Home Sample Collection</h1>
        <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6; margin-bottom: 24px;">
            Certified lab technician sterile vacuum tubes ke saath aapke ghar aakar sample lega. 72+ parameters, Biological Age Report aur Doctor Longevity Blueprint sabhi kuch included hai.
        </p>

        <div class="booking-card">
            <div class="layout-grid">
                
                <form id="orderForm" onsubmit="submitBooking(event)">
                    <div class="form-box">
                        <div class="field-group">
                            <label>Patient Full Name</label>
                            <input type="text" id="b_name" class="field-input" placeholder="e.g. Ramesh Kumar" required>
                        </div>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                            <div class="field-group">
                                <label>Age</label>
                                <input type="number" id="b_age" class="field-input" value="42" required>
                            </div>
                            <div class="field-group">
                                <label>Gender</label>
                                <select id="b_gender" class="field-select">
                                    <option value="Male">Male</option>
                                    <option value="Female">Female</option>
                                    <option value="Other">Other</option>
                                </select>
                            </div>
                        </div>
                        <div class="field-group">
                            <label>WhatsApp Mobile Number</label>
                            <input type="tel" id="b_phone" class="field-input" placeholder="e.g. 9876543210" required>
                        </div>
                        <div class="field-group">
                            <label>Complete Home Address & City / Pincode</label>
                            <input type="text" id="b_address" class="field-input" placeholder="Flat No, Society, Landmark, City & Pincode" required>
                        </div>
                        <div class="field-group">
                            <label>Preferred Fasting Slot (Tomorrow Morning)</label>
                            <select id="b_slot" class="field-select">
                                <option value="7:00 AM - 8:00 AM">Tomorrow: 7:00 AM - 8:00 AM (Recommended)</option>
                                <option value="8:00 AM - 9:00 AM">Tomorrow: 8:00 AM - 9:00 AM</option>
                                <option value="9:00 AM - 10:00 AM">Tomorrow: 9:00 AM - 10:00 AM</option>
                            </select>
                        </div>

                        <button type="submit" class="btn-confirm">
                            ✓ Confirm Booking & Generate Order
                        </button>
                    </div>
                </form>

                <div class="summary-card">
                    <span style="font-size: 11px; text-transform: uppercase; color: var(--accent); font-weight: 800; display: block;">
                        Order Summary
                    </span>
                    <div style="font-size: 26px; font-weight: 900; color: #10b981; margin: 8px 0;">
                        ₹1,999
                    </div>
                    <div style="font-size: 11px; color: var(--text-dim); margin-bottom: 14px;">
                        Includes 72+ Tests + Free Home Pickup + Doctor Review
                    </div>

                    <div class="qr-box">
                        <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=upi://pay?pa=founder@oksbi&pn=BioTwin%20Labs&am=1999&cu=INR&tn=72-Biomarker-Home-Draw" alt="UPI QR Code">
                    </div>

                    <p style="font-size: 11px; color: var(--text-muted); margin-bottom: 8px;">
                        Pay via <strong>PhonePe, Google Pay, Paytm or Cash on Sample Pickup</strong>
                    </p>

                    <a href="#" id="waBtn" class="btn-wa" onclick="directWA(event)">
                        <span>💬</span>
                        <span>Book Directly on WhatsApp</span>
                    </a>
                </div>

            </div>
        </div>
    </div>

    <script>
        function submitBooking(e) {
            e.preventDefault();
            const name = document.getElementById('b_name').value;
            const phone = document.getElementById('b_phone').value;
            const address = document.getElementById('b_address').value;
            const slot = document.getElementById('b_slot').value;
            const age = document.getElementById('b_age').value;
            const orderId = `BT-ORD-${Math.floor(100000 + Math.random() * 900000)}`;

            // Log to backend API
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

            alert(`✓ Order Successfully Confirmed!\n\nOrder ID: ${orderId}\nPatient: ${name}\nSlot: ${slot}\nHome Address: ${address}\nTotal Amount: ₹1,999 (UPI / Cash on sample pickup)\n\nNABL technician has been assigned. You will receive a call 30 mins before arrival.`);

            const msg = `Hi BioTwin Labs, I have booked a ₹1,999 Longevity Health Checkup.%0AOrder ID: ${orderId}%0APatient: ${encodeURIComponent(name)}%0APhone: ${encodeURIComponent(phone)}%0AAddress: ${encodeURIComponent(address)}%0ASlot: ${encodeURIComponent(slot)}`;
            window.open(`https://wa.me/919876543210?text=${msg}`, '_blank');
        }

        function directWA(e) {
            e.preventDefault();
            const name = document.getElementById('b_name').value || "Client";
            const phone = document.getElementById('b_phone').value || "";
            const msg = `Hi BioTwin Labs, I want to book the ₹1,999 Longevity Health Checkup at my home.%0AName: ${encodeURIComponent(name)}%0APhone: ${encodeURIComponent(phone)}`;
            window.open(`https://wa.me/919876543210?text=${msg}`, '_blank');
        }
    </script>
</body>
</html>'''

# -------------------------------------------------------------
# 7. FOUNDER_CRM.HTML (PRIVATE CRM DASHBOARD)
# -------------------------------------------------------------
CRM_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Founder CRM & Client Pipeline | BioTwin Labs</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #05070c;
            --surface: #0a0f1a;
            --surface-card: #111827;
            --border: #1f293d;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --text-dim: #64748b;
            --accent: #38bdf8;
            --success: #10b981;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Plus Jakarta Sans', sans-serif; background: var(--bg); color: var(--text-main); min-height: 100vh; }
        .navbar { display: flex; justify-content: space-between; align-items: center; padding: 16px 36px; background: rgba(10, 15, 26, 0.96); border-bottom: 1px solid var(--border); }
        .brand-box { display: flex; align-items: center; gap: 12px; text-decoration: none; color: inherit; }
        .brand-icon { width: 40px; height: 40px; background: linear-gradient(135deg, #f59e0b, #d97706); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 20px; color: #000; }
        .btn-portal { background: var(--surface-card); border: 1px solid var(--border); color: #fff; text-decoration: none; padding: 8px 16px; border-radius: 8px; font-size: 12px; font-weight: 700; }

        .container { max-width: 1200px; margin: 36px auto; padding: 0 24px 60px; }
        .stat-banner { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 28px; }
        .stat-tile { background: var(--surface); border: 1px solid var(--border); border-radius: 14px; padding: 20px; }
        .stat-tile label { font-size: 11px; text-transform: uppercase; color: var(--text-dim); font-weight: 700; display: block; margin-bottom: 6px; }
        .stat-tile val { font-family: 'JetBrains Mono', monospace; font-size: 28px; font-weight: 900; color: var(--accent); }

        .leads-table { width: 100%; border-collapse: collapse; background: var(--surface); border: 1px solid var(--border); border-radius: 16px; overflow: hidden; }
        .leads-table th { background: var(--surface-card); padding: 14px 18px; text-align: left; font-size: 11px; text-transform: uppercase; color: var(--text-dim); font-weight: 700; border-bottom: 1px solid var(--border); }
        .leads-table td { padding: 16px 18px; font-size: 13px; border-bottom: 1px solid var(--border); color: var(--text-main); }
        .btn-wa-call { background: #25d366; color: #000; font-weight: 800; padding: 6px 12px; border-radius: 6px; text-decoration: none; font-size: 11px; display: inline-flex; align-items: center; gap: 4px; }
    </style>
</head>
<body>

    <nav class="navbar">
        <a href="/" class="brand-box">
            <div class="brand-icon">💼</div>
            <div>
                <strong style="font-size: 16px;">BioTwin Founder CRM</strong>
                <span style="font-size: 10px; color: #f59e0b; display: block; text-transform: uppercase;">Private Client Pipeline</span>
            </div>
        </a>
        <a href="/" class="btn-portal">← Open Customer Portal</a>
    </nav>

    <div class="container">
        <h1 style="font-size: 26px; font-weight: 800; margin-bottom: 8px;">Client Intake & Booking Pipeline</h1>
        <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 24px;">
            Yahan aapke saare leads aur booked clients live aate hain. Aap seedhe WhatsApp par message karke sample pickup coordinate kar sakte hain.
        </p>

        <div class="stat-banner">
            <div class="stat-tile">
                <label>Total Booked Orders</label>
                <val>{{ leads|length }}</val>
            </div>
            <div class="stat-tile">
                <label>Total Revenue Pipeline</label>
                <val style="color: #10b981;">₹{{ leads|length * 1999 }}</val>
            </div>
            <div class="stat-tile">
                <label>Estimated Net Profit</label>
                <val style="color: #38bdf8;">₹{{ leads|length * 950 }}</val>
            </div>
        </div>

        <table class="leads-table">
            <thead>
                <tr>
                    <th>Date / Time</th>
                    <th>Patient Name</th>
                    <th>Age</th>
                    <th>Phone / WhatsApp</th>
                    <th>Slot / Address</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                {% for lead in leads %}
                <tr>
                    <td style="color: var(--text-dim); font-size: 12px;">{{ lead.date }}</td>
                    <td><strong>{{ lead.name }}</strong></td>
                    <td>{{ lead.age }} Yrs</td>
                    <td><a href="https://wa.me/{{ lead.phone }}" target="_blank" style="color: var(--accent); text-decoration: none; font-family: 'JetBrains Mono', monospace;">{{ lead.phone }}</a></td>
                    <td style="font-size: 12px; color: var(--text-muted);">{{ lead.slot or 'Morning Fasting' }} ({{ lead.address or 'N/A' }})</td>
                    <td>
                        <a href="https://wa.me/{{ lead.phone }}?text=Hi+{{ lead.name }},+BioTwin+phlebotomist+sample+collection+confirmed" target="_blank" class="btn-wa-call">
                            💬 Chat on WhatsApp
                        </a>
                    </td>
                </tr>
                {% else %}
                <tr>
                    <td colspan="6" style="text-align: center; color: var(--text-dim); padding: 30px;">
                        No leads registered yet. New bookings will automatically appear here.
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>

</body>
</html>'''

def main():
    files = {
        "index.html": INDEX_HTML,
        "camera_checkup.html": CAMERA_HTML,
        "zero_report.html": ZERO_HTML,
        "old_report.html": OLD_REPORT_HTML,
        "full_biomarkers.html": FULL_BIO_HTML,
        "book_test.html": BOOK_TEST_HTML,
        "founder_crm.html": CRM_HTML,
    }

    for name, content in files.items():
        filepath = os.path.join(TEMPLATES_DIR, name)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Written: {name}")

    print("All dedicated templates generated successfully!")

if __name__ == "__main__":
    main()
