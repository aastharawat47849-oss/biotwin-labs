# -*- coding: utf-8 -*-
"""
Script to add '7 Din Free' (7-Day Free Health & Longevity Trial) to BioTwin Labs.
Adds:
1. Navbar Highlight Pill: '🎁 7 Days Free Pass'
2. Hero Section 7-Day Free Trial Spotlight Banner
3. Dedicated Screen 'screen-freetrial' with 7-Day Health Tracking Timeline & 1-Click ₹0 Activation
4. Translation entries in English, Hindi, and Hinglish
"""

import os
import re

FILE_PATH = r"c:\Users\B-WOI\OneDrive\Desktop\BioTwin-Platform\build_unified_app.py"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Add CSS for Trial Banner & 7-Day Timeline
CSS_INJECTION = '''
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
'''

# Insert CSS right before @media
code = code.replace("@media (max-width: 900px) {", CSS_INJECTION + "\n        @media (max-width: 900px) {")

# 2. Add '7 Days Free Pass' button to Navbar
NAV_BTN = '''
            <button class="btn-nav" onclick="showScreen('freetrial')" style="background: rgba(16, 185, 129, 0.12); border-color: rgba(16, 185, 129, 0.35); color: #34d399;">
                <span>🎁</span>
                <span data-i18n="nav_free_trial">7 Days Free Trial</span>
            </button>
'''
code = code.replace('<button class="btn-nav" onclick="showScreen(\'hub\')">', NAV_BTN + '\n            <button class="btn-nav" onclick="showScreen(\'hub\')">')

# 3. Add 7-Day Free Banner inside catalog-container (Screen 0)
TRIAL_BANNER_HTML = '''
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
'''
code = code.replace('<div class="catalog-grid" id="catalogGrid">', TRIAL_BANNER_HTML + '\n            <div class="catalog-grid" id="catalogGrid">')

# 4. Add Dedicated Screen: 'screen-freetrial'
FREE_TRIAL_SCREEN_HTML = '''
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
                            <input type="tel" id="ft_phone" class="input-control" placeholder="e.g. 9876543210" required>
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
'''

code = code.replace('<!-- SCREEN 5: DEDICATED AT-HOME BLOOD TEST BOOKING', FREE_TRIAL_SCREEN_HTML + '\n    <!-- SCREEN 5: DEDICATED AT-HOME BLOOD TEST BOOKING')

# 5. Add activateFreeTrial JS function
JS_FREE_TRIAL = '''
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

            alert(`🎉 Congratulations ${name}!\n\nYour 7-Day Free Health Pass is ACTIVE.\nPass ID: ${passId}\nCharge: ₹0 (No Payment Required)\n\nYou now have unlimited access to Camera BP scans, Zero-Report Health Assessment, and daily metabolic tracking.`);

            const msg = `Hi BioTwin Labs, I have activated my 7-Day Free Health Pass.%0APass ID: ${passId}%0AName: ${encodeURIComponent(name)}%0APhone: ${encodeURIComponent(phone)}`;
            window.open(`https://wa.me/919876543210?text=${msg}`, '_blank');

            // Open camera scanner to let user do Day 1 checkup immediately!
            showScreen('camera');
        }
'''

code = code.replace('function submitHomeBooking(e) {', JS_FREE_TRIAL + '\n        function submitHomeBooking(e) {')

# 6. Update Translation Dictionary
DICT_EN = '''
                nav_free_trial: "7 Days Free Trial",
                tb_badge: "🎁 SPECIAL LAUNCH OFFER • 7 DAYS FREE",
                tb_title: "Start Your 7-Day Free Health & Longevity Trial",
                tb_desc: "No payment or credit card required. Check your BP daily using your phone camera, calculate biological age, and monitor health for 7 days at ₹0!",
                btn_start_trial: "Start 7-Day Free Trial (₹0) →",
                ft_badge: "100% Free Health Monitoring",
                ft_title: "Activate Your 7-Day Free Longevity Pass",
                ft_desc: "You don't pay a single rupee for the first 7 days. Track your camera BP, post-meal glucose stability, and biological age. Here is your 7-Day Roadmap:",
'''

DICT_HI = '''
                nav_free_trial: "7 दिन बिल्कुल फ्री",
                tb_badge: "🎁 खास ऑफर • 7 दिन बिल्कुल फ्री",
                tb_title: "7 दिन का बिल्कुल फ्री हेल्थ व लंबी उम्र ट्रायल",
                tb_desc: "बिना किसी पेमेंट या कार्ड के — पहले 7 दिन रोजाना फोन कैमरे से बीपी जांचें, अपनी बायोलॉजिकल उम्र देखें और स्वास्थ्य ट्रैक करें बिल्कुल ₹0 में!",
                btn_start_trial: "7 दिन का फ्री ट्रायल शुरू करें (₹0) →",
                ft_badge: "100% फ्री स्वास्थ्य जांच",
                ft_title: "अपना 7 दिन का फ्री हेल्थ पास एक्टिवेट करें",
                ft_desc: "पहले 7 दिन आपको एक भी रुपया नहीं देना है। कैमरे से रोज बीपी मापें, खाने के बाद शुगर क्रैश और अंदरूनी उम्र ट्रैक करें। यह रहा आपका 7-दिन का प्लान:",
'''

DICT_HINGLISH = '''
                nav_free_trial: "7 Days Free Trial",
                tb_badge: "🎁 SPECIAL OFFER • 7 DAYS FREE",
                tb_title: "Pehle 7 Din Bilkul FREE Health & Longevity Trial",
                tb_desc: "Bina kisi payment ya card ke — pehle 7 din rozana camera se BP check karein, biological age score dekhein aur health monitor karein bilkul ₹0 me!",
                btn_start_trial: "Start 7-Day Free Trial (₹0) →",
                ft_badge: "100% Free Health Monitoring",
                ft_title: "Apna 7 Din Ka Free Longevity Pass Activate Karein",
                ft_desc: "Pehle 7 din aapko ek rupya bhi nahi dena hai. Rozana camera se BP aur biological age track karein. Yeh raha aapka 7-Day Plan:",
'''

code = code.replace('brand_title: "BioTwin Labs",\n                brand_sub:', 'brand_title: "BioTwin Labs",\n' + DICT_EN + '                brand_sub:')
code = code.replace('brand_title: "बायोट्विन लैब्स (BioTwin Labs)",\n                brand_sub:', 'brand_title: "बायोट्विन लैब्स (BioTwin Labs)",\n' + DICT_HI + '                brand_sub:')
code = code.replace('brand_title: "BioTwin Labs",\n                brand_sub: "Precision Longevity & Full Body Checkup Platform",', 'brand_title: "BioTwin Labs",\n' + DICT_HINGLISH + '                brand_sub: "Precision Longevity & Full Body Checkup Platform",')

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(code)

print("build_unified_app.py updated with 7-Day Free Trial!")
