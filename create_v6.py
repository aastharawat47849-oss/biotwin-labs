# -*- coding: utf-8 -*-
import os
import sys

BASE_DIR = r"c:\Users\B-WOI\OneDrive\Desktop\BioTwin-Platform"
SRC_PATH = os.path.join(BASE_DIR, "build_complete_platform_v5.py")
INDEX_PATH = os.path.join(BASE_DIR, "web", "templates", "index.html")
PORTAL_PATH = os.path.join(BASE_DIR, "portal.html")

with open(SRC_PATH, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Add CSS styling for lockout-wa-reminder-box and legal-disclaimer-box
css_additions = """
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
"""
code = code.replace("/* Catalog Grid */", css_additions + "\n        /* Catalog Grid */")

# 2. Add WhatsApp Reminder Box inside #screen-locked
locked_target = """                <div style="max-width: 480px; margin: 0 auto; background: var(--surface-card); border: 1px dashed var(--accent); border-radius: 16px; padding: 20px;">
                    <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 8px;">Scan UPI QR to Instantly Unlock:</div>
                    <div style="width: 140px; height: 140px; background: #fff; padding: 6px; border-radius: 10px; margin: 0 auto 10px;">
                        <img src="https://api.qrserver.com/v1/create-qr-code/?size=140x140&data=upi://pay?pa=9343062265@upi&pn=BioTwin%20Labs&am=199&cu=INR&tn=Reactivate-Access" style="width: 100%; height: 100%; object-fit: contain;">
                    </div>
                    <div style="font-size: 11px; color: #34d399; font-family: 'JetBrains Mono', monospace; font-weight: 700;">UPI / GPay / PhonePe: 9343062265</div>
                    <a href="https://wa.me/919343062265?text=Hi+BioTwin+Labs,+my+7-day+trial+expired.+Please+reactivate+my+access." target="_blank" class="btn-wa" style="margin-top: 14px;">
                        <span>💬</span>
                        <span data-i18n="lock_btn_wa">WhatsApp to Reactivate (9343062265)</span>
                    </a>
                </div>"""

locked_replacement = """                <div style="max-width: 520px; margin: 0 auto; background: var(--surface-card); border: 1px dashed var(--accent); border-radius: 16px; padding: 20px;">
                    <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 8px;">Scan UPI QR to Instantly Unlock (₹199 / ₹299 / ₹2,499 / ₹3,499):</div>
                    <div style="width: 140px; height: 140px; background: #fff; padding: 6px; border-radius: 10px; margin: 0 auto 10px;">
                        <img src="https://api.qrserver.com/v1/create-qr-code/?size=140x140&data=upi://pay?pa=9343062265@upi&pn=BioTwin%20Labs&am=199&cu=INR&tn=Reactivate-Access" style="width: 100%; height: 100%; object-fit: contain;">
                    </div>
                    <div style="font-size: 12px; color: #34d399; font-family: 'JetBrains Mono', monospace; font-weight: 700;">UPI / GPay / PhonePe: 9343062265</div>
                    <a href="https://wa.me/919343062265?text=Hi+BioTwin+Labs,+my+7-day+trial+expired.+Please+reactivate+my+access." target="_blank" class="btn-wa" style="margin-top: 14px;">
                        <span>💬</span>
                        <span data-i18n="lock_btn_wa">WhatsApp to Reactivate (9343062265)</span>
                    </a>
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
                </div>"""

if locked_target in code:
    code = code.replace(locked_target, locked_replacement)
    print("Replaced locked screen content successfully!")
else:
    print("Failed to find locked_target in code!")

# 3. Add Screen Disclaimers: Camera
cam_target = """                        <button class="btn-action-main" id="btnToggleScan" onclick="toggleScan()">
                            <span>⚡</span>
                            <span data-i18n="btn_start_scan">Start 15-Second Optical Camera Scan</span>
                        </button>
                    </div>
                </div>"""

cam_replacement = """                        <button class="btn-action-main" id="btnToggleScan" onclick="toggleScan()">
                            <span>⚡</span>
                            <span data-i18n="btn_start_scan">Start 15-Second Optical Camera Scan</span>
                        </button>
                    </div>
                </div>

                <!-- Camera Clinical Disclaimer Banner -->
                <div style="margin-top: 20px; background: rgba(56, 189, 248, 0.08); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 12px; padding: 14px 18px; font-size: 12px; color: #94a3b8; display: flex; align-items: flex-start; gap: 10px;">
                    <span style="font-size: 18px;">⚖️</span>
                    <span data-i18n="cam_disclaimer">Clinical Screening Notice: Fingertip optical photoplethysmography is designed for preventive wellness screening and arterial elasticity trend monitoring. It is not an invasive ICU-grade arterial line monitor. Always verify persistent clinical abnormalities with a licensed physician.</span>
                </div>"""

if cam_target in code:
    code = code.replace(cam_target, cam_replacement)
    print("Replaced camera screen disclaimer successfully!")
else:
    print("Failed to find cam_target in code!")

# Screen Disclaimers: Zero-Report Quiz
quiz_target = """                    <button class="btn-action-main" onclick="showScreen('booking')">
                        <span>🩸</span>
                        <span data-i18n="btn_confirm_blood_draw">Confirm with ₹1,999 At-Home Blood Test</span>
                    </button>
                </div>
            </div>
        </div>
    </div>"""

quiz_replacement = """                    <button class="btn-action-main" onclick="showScreen('booking')">
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
    </div>"""

if quiz_target in code:
    code = code.replace(quiz_target, quiz_replacement)
    print("Replaced quiz screen disclaimer successfully!")
else:
    print("Failed to find quiz_target in code!")

# Screen Disclaimers: Time Machine
tm_target = """                    <button class="btn-action-main" onclick="showScreen('booking')">
                        <span>🏠</span>
                        <span data-i18n="btn_stop_drift">Schedule Clinical Phlebotomy (₹1,999)</span>
                    </button>
                </div>
            </div>
        </div>
    </div>"""

tm_replacement = """                    <button class="btn-action-main" onclick="showScreen('booking')">
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
    </div>"""

if tm_target in code:
    code = code.replace(tm_target, tm_replacement)
    print("Replaced time machine screen disclaimer successfully!")
else:
    print("Failed to find tm_target in code!")

# 4. Replace one-line Footer with Complete Legal Medical Disclaimer
footer_target = """    <!-- FOOTER -->
    <footer class="footer">
        © 2026 BioTwin Labs. Aligned with Harrison's Principles of Internal Medicine & Guyton Physiology. Contact: +91 9343062265.
    </footer>"""

footer_replacement = """    <!-- GLOBAL COMPREHENSIVE LEGAL MEDICAL DISCLAIMER & FOOTER -->
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
    </footer>"""

if footer_target in code:
    code = code.replace(footer_target, footer_replacement)
    print("Replaced footer with full Legal Disclaimer successfully!")
else:
    print("Failed to find footer_target in code!")

# 5. Add translations to DICT (en, hi, hinglish)
en_dict_additions = """                lock_reminder_title: "Auto-Lockout WhatsApp Reminder & Backup Service",
                lock_reminder_desc: "Your 7-day health tracking and biological age simulations are currently paused. Enter your WhatsApp number below to receive an automated encrypted backup of your baseline readings and an instant 1-tap reactivation pass link.",
                lock_reminder_btn: "Send WhatsApp Reminder Alert",
                cam_disclaimer: "Clinical Screening Notice: Fingertip optical photoplethysmography is designed for preventive wellness screening and arterial elasticity trend monitoring. It is not an invasive ICU-grade arterial line monitor. Always verify persistent clinical abnormalities with a licensed physician.",
                quiz_disclaimer: "Algorithmic Assessment Notice: Calculated phenotypic biological age reflects statistical metabolic variance and Guyton physiological markers. It does not replace clinical laboratory diagnostic tests, coronary calcium scoring, or physician consultation.",
                tm_disclaimer: "Projection Notice: Metabolic drift calculations represent a mathematical projection based on Harrison's beta-cell exhaustion models. A fresh blood draw is recommended to verify actual cellular biomarkers.",
                disclaimer_title: "Statutory Medical Disclaimer & Regulatory Telemedicine Compliance",
                disclaimer_body: "Bio-Twin Labs is an investigational artificial intelligence platform providing algorithmic physiological simulations, biological age analytics, and preventive wellness tracking (aligned with Guyton & Hall Textbook of Medical Physiology and Levine PhenoAge clinical methodologies). Bio-Twin Labs does NOT constitute or offer clinical medical diagnosis, medical treatment, prescription of pharmaceutical drugs, or emergency healthcare services. This platform is not an alternative to professional clinical evaluation by a Registered Medical Practitioner (MBBS/MD). If you or a family member are experiencing acute symptoms, chest pressure, severe shortness of breath, acute palpitations, sudden neurological numbness, or any life-threatening symptoms, immediately contact emergency services (dial 112 or 108 in India) or report to the nearest hospital casualty emergency room. Diagnostic blood tests and home phlebotomy sample collections are executed independently by accredited NABL / ICMR certified laboratory partners.",
"""

code = code.replace('lock_btn_wa: "WhatsApp to Reactivate (9343062265)"\n            },', 'lock_btn_wa: "WhatsApp to Reactivate (9343062265)",\n' + en_dict_additions + '            },')

hi_dict_additions = """                lock_reminder_title: "स्वतः लॉकआउट व्हाट्सएप रिमाइंडर एवं डेटा सुरक्षा सेवा",
                lock_reminder_desc: "आपकी 7-दिवसीय स्वास्थ्य निगरानी व जैविक आयु सिमुलेशन अब स्थगित कर दी गई है। अपने प्रारंभिक शारीरिक मानकों का एन्क्रिप्टेड बैकअप प्राप्त करने और 1-क्लिक में पास पुनः सक्रिय करने हेतु नीचे अपना व्हाट्सएप नंबर दर्ज करें।",
                lock_reminder_btn: "व्हाट्सएप रिमाइंडर अलर्ट भेजें",
                cam_disclaimer: "क्लिनिकल स्क्रीनिंग सूचना: उंगली का ऑप्टिकल फोटोप्लेथिस्मोग्राफी परीक्षण केवल निवारक वेलनेस और धमनी लोच प्रवृत्तियों के आंकलन हेतु है। यह आईसीयू स्तर का इनवेसिव मॉनिटर नहीं है। किसी भी असामान्य लक्षण पर चिकित्सक से संपर्क करें।",
                quiz_disclaimer: "एल्गोरिदमिक आंकलन सूचना: अनुमानित जैविक आयु गाइटन फिजियोलॉजिकल मानकों पर आधारित सांख्यिकीय फेनोटाइपिक ह्रास दर्शाती है। यह पैथोलॉजिकल रक्त जांच अथवा चिकित्सक परामर्श का स्थान नहीं लेती है।",
                tm_disclaimer: "प्रक्षेपण सूचना: मेटाबॉलिक ह्रास गणना हैरिसन्स बीटा-सेल मॉडल पर आधारित एक गणितीय प्रक्षेपण है। वास्तविक स्थिति की पुष्टि हेतु ताज़ा लैब टेस्ट कराने की सलाह दी जाती है।",
                disclaimer_title: "वैधानिक चिकित्सा अस्वीकरण एवं विनियामक टेलीमेडिसिन अनुपालन",
                disclaimer_body: "बायो-ट्विन लैब्स एक प्रयोगात्मक कृत्रिम बुद्धिमत्ता (AI) आधारित स्वास्थ्य मॉडलिंग, जैविक आयु विश्लेषण और निवारक जीवनशैली मार्गदर्शन प्लेटफॉर्म है (जो गाइटन फिजियोलॉजी एवं लेविन फीनोएज क्लिनिकल मानकों पर आधारित है)। यह किसी भी प्रकार का चिकित्सीय निदान, उपचार, एलोपैथिक दवाओं का नुस्खा या आपातकालीन चिकित्सा सेवाएं प्रदान नहीं करता है। यह किसी भी पंजीकृत चिकित्सक (MBBS/MD) के परामर्श का विकल्प नहीं है। यदि आप सीने में दर्द, सांस लेने में अत्यधिक कठिनाई, सुन्नता अथवा किसी गंभीर आपात स्थिति का अनुभव कर रहे हैं, तो तुरंत आपातकालीन नंबर (112 अथवा 108) पर संपर्क करें या निकटतम अस्पताल के आपातकालीन विभाग में जाएं। सभी रक्त परीक्षण स्वतंत्र NABL एवं ICMR प्रमाणित प्रयोगशाला सहयोगियों द्वारा निष्पादित किए जाते हैं।",
"""

code = code.replace('lock_btn_wa: "पुनः सक्रिय करने हेतु व्हाट्सएप करें (9343062265)"\n            },', 'lock_btn_wa: "पुनः सक्रिय करने हेतु व्हाट्सएप करें (9343062265)",\n' + hi_dict_additions + '            },')

hinglish_dict_additions = """                lock_reminder_title: "Auto-Lockout WhatsApp Reminder & Backup Service",
                lock_reminder_desc: "Aapka 7-day health tracking trial pause ho gaya hai. Apna baseline health data backup pane aur instant 1-tap pass reactivation link ke liye apna WhatsApp number enter karein.",
                lock_reminder_btn: "WhatsApp Reminder Alert Bhejein",
                cam_disclaimer: "Clinical Screening Notice: Fingertip camera PPG scan preventive wellness aur arterial elasticity trend ke liye hai. Ye ICU monitor nahi hai. Kisi bhi problem ke liye doctor se milein.",
                quiz_disclaimer: "Assessment Notice: Biological age calculation lifestyle markers par based hai. Ye blood lab test ka substitute nahi hai.",
                tm_disclaimer: "Projection Notice: Time Machine beta-cell depletion ka mathematical estimate hai. Final confirmation ke liye blood test karwayein.",
                disclaimer_title: "Statutory Medical Disclaimer & Regulatory Notice",
                disclaimer_body: "Bio-Twin Labs ek AI-based preventive health simulation aur biological age tracking platform hai (Guyton Physiology & Levine PhenoAge par aadharit). Ye koi clinical medical diagnosis, treatment, prescription ya emergency healthcare provide nahi karta. Kisi bhi emergency ya serious bimari ki sthiti me turant doctor (MBBS/MD) se sampark karein ya 112/108 par call karein. Blood sample collection NABL-certified labs dwara kiya jata hai.",
"""

code = code.replace('lock_btn_wa: "WhatsApp Par Reactivate Karein (9343062265)"\n            }', 'lock_btn_wa: "WhatsApp Par Reactivate Karein (9343062265)",\n' + hinglish_dict_additions + '            }')

# 6. Add sendAutoLockoutReminder JS function
js_function = """
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
"""

code = code.replace("function activateFreeTrial(e) {", js_function + "\n        function activateFreeTrial(e) {")

# Save as build_complete_platform_v6.py
dest_script = os.path.join(BASE_DIR, "build_complete_platform_v6.py")
with open(dest_script, "w", encoding="utf-8") as f:
    f.write(code)

print("build_complete_platform_v6.py created successfully!")
