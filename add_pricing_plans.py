# -*- coding: utf-8 -*-
"""
Add Normal Affordable Charges (₹199, ₹299) and 1-Month Subscriptions (₹2,499, ₹3,499) to BioTwin Labs.
Aligned exactly with user specifications:
- 7 Days Free Trial: ₹0
- Post 7-Day Normal Checkup Charges: ₹199 (Weekly Pass) / ₹299 (Deep Report Pass)
- 1-Month Subscriptions: ₹2,499 (Standard Monthly) / ₹3,499 (VIP Monthly with At-Home Blood Draw & Doctor Review)
"""

import os

FILE_PATH = r"c:\Users\B-WOI\OneDrive\Desktop\BioTwin-Platform\build_unified_app.py"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Add CSS for Pricing & Subscription Grid
CSS_PRICING = '''
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
'''

# Insert CSS before @media
code = code.replace("@media (max-width: 900px) {", CSS_PRICING + "\n        @media (max-width: 900px) {")

# 2. Add 'Subscriptions' button to Navbar
NAV_SUB_BTN = '''
            <button class="btn-nav" onclick="showScreen('plans')">
                <span>💎</span>
                <span data-i18n="nav_plans">Plans (₹199 - ₹3,499)</span>
            </button>
'''
code = code.replace('<button class="btn-nav" onclick="showScreen(\'hub\')">', NAV_SUB_BTN + '\n            <button class="btn-nav" onclick="showScreen(\'hub\')">')

# 3. Add Pricing Section to Screen 0 (Main Catalog Hub)
PLANS_SECTION_HTML = '''
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
'''

code = code.replace('</div>\n    </div>\n\n    <!-- ================================================= -->\n    <!-- SCREEN 1: DEDICATED CAMERA BP', '</div>\n    </div>\n\n' + PLANS_SECTION_HTML + '\n\n    <!-- ================================================= -->\n    <!-- SCREEN 1: DEDICATED CAMERA BP')

# 4. Add Dedicated Screen: 'screen-plans'
SCREEN_PLANS_HTML = '''
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
                                <input type="tel" id="co_phone" class="input-control" placeholder="e.g. 9876543210" required>
                            </div>
                            <button type="submit" class="btn-action-main" style="margin-top: 14px;">
                                <span>⚡</span>
                                <span>Confirm & Activate Subscription</span>
                            </button>
                        </form>

                        <div style="text-align: center; background: #000; padding: 14px; border-radius: 12px; border: 1px solid var(--border);">
                            <div style="width: 140px; height: 140px; background: #fff; padding: 6px; border-radius: 10px; margin: 0 auto 8px;">
                                <img id="coQrImg" src="https://api.qrserver.com/v1/create-qr-code/?size=140x140&data=upi://pay?pa=founder@oksbi&pn=BioTwin%20Labs&am=2499&cu=INR&tn=Longevity-Subscription" style="width: 100%; height: 100%; object-fit: contain;">
                            </div>
                            <span style="font-size: 10px; color: var(--text-dim);">Scan via PhonePe/GPay/Paytm</span>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>
'''

code = code.replace('<!-- SCREEN: DEDICATED 7-DAY FREE TRIAL SCREEN', SCREEN_PLANS_HTML + '\n    <!-- SCREEN: DEDICATED 7-DAY FREE TRIAL SCREEN')

# 5. Add selectPlan and submitPlanOrder JS Functions
JS_PLAN_FUNCTIONS = '''
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
            
            const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=140x140&data=upi://pay?pa=founder@oksbi&pn=BioTwin%20Labs&am=${price}&cu=INR&tn=${encodeURIComponent(planName)}`;
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

            alert(`🎉 Subscription Activated Successfully!\n\nPlan: ${activePlanName}\nOrder ID: ${orderId}\nPrice: ₹${activePlanPrice}\nPatient: ${name}\n\nYour membership access has been unlocked. Details sent to WhatsApp.`);

            const msg = `Hi BioTwin Labs, I have subscribed to ${activePlanName} (₹${activePlanPrice}).%0AOrder ID: ${orderId}%0AName: ${encodeURIComponent(name)}%0APhone: ${encodeURIComponent(phone)}`;
            window.open(`https://wa.me/919876543210?text=${msg}`, '_blank');
        }
'''

code = code.replace('function activateFreeTrial(e) {', JS_PLAN_FUNCTIONS + '\n        function activateFreeTrial(e) {')

# 6. Add Translation Strings
DICT_PLANS_EN = '''
                nav_plans: "Plans (₹199 - ₹3,499)",
                sec_plans_title: "Affordable Normal Passes & 1-Month Subscriptions",
                sec_plans_sub: "First 7 days are 100% FREE. After that, keep monitoring with normal weekly passes (₹199, ₹299) or monthly memberships (₹2,499, ₹3,499):",
                p_screen_title: "Choose Your Health Monitoring Pass",
                p_screen_desc: "First 7 days free trial. After that, pick from normal affordable passes or full-body monthly subscriptions:",
'''

DICT_PLANS_HI = '''
                nav_plans: "प्लान्स (₹199 - ₹3,499)",
                sec_plans_title: "7 दिन के बाद सामान्य शुल्क एवं 1 महीने के सब्सक्रिप्शन",
                sec_plans_sub: "पहले 7 दिन बिल्कुल फ्री हैं। उसके बाद कोई महंगा खर्च नहीं — केवल सामान्य ₹199/₹299 के पास या ₹2,499/₹3,499 के मासिक सब्सक्रिप्शन में से चुनें:",
                p_screen_title: "अपना हेल्थ मॉनिटरिंग पास चुनें",
                p_screen_desc: "पहले 7 दिन बिल्कुल फ्री। उसके बाद सामान्य साप्ताहिक पास या पूरे 1 महीने के सब्सक्रिप्शन में से चुनें:",
'''

DICT_PLANS_HINGLISH = '''
                nav_plans: "Plans (₹199 - ₹3,499)",
                sec_plans_title: "7 Din Ke Baad Normal Charges Aur Monthly Subscriptions",
                sec_plans_sub: "Pehle 7 din bilkul FREE hain. Uske baad koi mehenga charge nahi — sirf normal ₹199/₹299 ke passes ya poor mahine ke subscription me se chunein:",
                p_screen_title: "Apna Health Monitoring Pass Chunein",
                p_screen_desc: "Pehle 7 din bilkul free. Uske baad normal weekly pass (₹199, ₹299) ya 1-month subscriptions (₹2,499, ₹3,499) me se chunein:",
'''

code = code.replace('nav_free_trial: "7 Days Free Trial",\n', 'nav_free_trial: "7 Days Free Trial",\n' + DICT_PLANS_EN)
code = code.replace('nav_free_trial: "7 दिन बिल्कुल फ्री",\n', 'nav_free_trial: "7 दिन बिल्कुल फ्री",\n' + DICT_PLANS_HI)
code = code.replace('nav_free_trial: "7 Days Free Trial",\n                tb_badge:', 'nav_free_trial: "7 Days Free Trial",\n' + DICT_PLANS_HINGLISH + '                tb_badge:')

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(code)

print("Pricing plans successfully injected into build_unified_app.py!")
