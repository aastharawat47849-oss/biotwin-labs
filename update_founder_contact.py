# -*- coding: utf-8 -*-
"""
Script to inject founder's real contact number and UPI details: 9343062265
"""

import os
import re

BASE_DIR = r"c:\Users\B-WOI\OneDrive\Desktop\BioTwin-Platform"
UNIFIED_SCRIPT = os.path.join(BASE_DIR, "build_unified_app.py")

with open(UNIFIED_SCRIPT, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace all WhatsApp URLs with 919343062265
content = content.replace("wa.me/919876543210", "wa.me/919343062265")

# 2. Replace all UPI IDs with 9343062265@upi
content = content.replace("pa=founder@oksbi", "pa=9343062265@upi")

# 3. Replace navbar helpline label to show the real number
content = content.replace(
    '<span>Helpline</span>',
    '<span>WhatsApp: 9343062265</span>'
)
content = content.replace(
    '<span>Patient Support</span>',
    '<span>WhatsApp: 9343062265</span>'
)

# 4. Enhance the QR code box in Screen 5 (Booking) with prominent UPI number badge
OLD_QR_CARD = '''                    <div class="qr-card">
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
                            <img src="https://api.qrserver.com/v1/create-qr-code/?size=170x170&data=upi://pay?pa=founder@oksbi&pn=BioTwin%20Labs&am=1999&cu=INR&tn=72-Biomarker-Home-Draw" alt="UPI QR Code">
                        </div>

                        <p style="font-size: 11px; color: var(--text-muted); margin-bottom: 6px;">
                            Scan to pay via <strong>PhonePe, GPay, Paytm, or Cash on Pickup</strong>
                        </p>

                        <a href="#" class="btn-wa" onclick="directWhatsApp(event)">
                            <span>💬</span>
                            <span data-i18n="btn_wa_chat">Book on WhatsApp</span>
                        </a>
                    </div>'''

NEW_QR_CARD = '''                    <div class="qr-card">
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
                    </div>'''

if OLD_QR_CARD in content:
    content = content.replace(OLD_QR_CARD, NEW_QR_CARD)
else:
    # If already modified or slight mismatch, do regex/substring replace
    content = content.replace("pa=founder@oksbi", "pa=9343062265@upi")

# 5. In the checkout box for subscriptions, show 9343062265 badge as well
OLD_CO_BOX = '''                        <div style="text-align: center; background: #000; padding: 14px; border-radius: 12px; border: 1px solid var(--border);">
                            <div style="width: 140px; height: 140px; background: #fff; padding: 6px; border-radius: 10px; margin: 0 auto 8px;">
                                <img id="coQrImg" src="https://api.qrserver.com/v1/create-qr-code/?size=140x140&data=upi://pay?pa=founder@oksbi&pn=BioTwin%20Labs&am=2499&cu=INR&tn=Longevity-Subscription" style="width: 100%; height: 100%; object-fit: contain;">
                            </div>
                            <span style="font-size: 10px; color: var(--text-dim);">Scan via PhonePe/GPay/Paytm</span>
                        </div>'''

NEW_CO_BOX = '''                        <div style="text-align: center; background: #000; padding: 14px; border-radius: 12px; border: 1px solid var(--border);">
                            <div style="width: 140px; height: 140px; background: #fff; padding: 6px; border-radius: 10px; margin: 0 auto 8px;">
                                <img id="coQrImg" src="https://api.qrserver.com/v1/create-qr-code/?size=140x140&data=upi://pay?pa=9343062265@upi&pn=BioTwin%20Labs&am=2499&cu=INR&tn=Longevity-Subscription" style="width: 100%; height: 100%; object-fit: contain;">
                            </div>
                            <span style="font-size: 11px; color: #34d399; font-family: 'JetBrains Mono', monospace; font-weight: 700; display: block;">UPI: 9343062265</span>
                            <span style="font-size: 10px; color: var(--text-dim);">Scan QR or Pay on 9343062265</span>
                        </div>'''

if OLD_CO_BOX in content:
    content = content.replace(OLD_CO_BOX, NEW_CO_BOX)
else:
    content = content.replace("pa=founder@oksbi", "pa=9343062265@upi")

# 6. In JS selectPlan function, update the QR generator URL
content = content.replace("pa=founder@oksbi", "pa=9343062265@upi")

# 7. Update any remaining 9876543210 in JS WhatsApp redirects
content = content.replace("wa.me/919876543210", "wa.me/919343062265")

with open(UNIFIED_SCRIPT, "w", encoding="utf-8") as f:
    f.write(content)

print("build_unified_app.py updated with 9343062265 successfully!")
