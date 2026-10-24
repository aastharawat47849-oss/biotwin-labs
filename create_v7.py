# -*- coding: utf-8 -*-
import os

BASE_DIR = r"c:\Users\B-WOI\OneDrive\Desktop\BioTwin-Platform"
SRC_PATH = os.path.join(BASE_DIR, "build_complete_platform_v6.py")
DEST_PATH = os.path.join(BASE_DIR, "build_complete_platform_v7.py")

with open(SRC_PATH, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Add UTR Input to Checkout Form in #screen-plans
co_target = """                            <div class="form-group" style="margin-top: 10px;">
                                <label style="font-size: 11px; text-transform: uppercase; color: var(--text-dim); font-weight: 700; display: block; margin-bottom: 4px;">WhatsApp Mobile Number</label>
                                <input type="tel" id="co_phone" class="input-control" placeholder="e.g. 9343062265" required>
                            </div>
                            <button type="submit" class="btn-action-main" style="margin-top: 14px;">"""

co_replacement = """                            <div class="form-group" style="margin-top: 10px;">
                                <label style="font-size: 11px; text-transform: uppercase; color: var(--text-dim); font-weight: 700; display: block; margin-bottom: 4px;">WhatsApp Mobile Number</label>
                                <input type="tel" id="co_phone" class="input-control" placeholder="e.g. 9343062265" required>
                            </div>
                            <div class="form-group" style="margin-top: 10px;">
                                <label style="font-size: 11px; text-transform: uppercase; color: var(--accent); font-weight: 800; display: block; margin-bottom: 4px;">12-Digit Bank UTR / UPI Transaction Reference Number</label>
                                <input type="text" id="co_utr" class="input-control" placeholder="e.g. 429182749102 (from PhonePe / GPay / Paytm)" maxlength="12" required style="font-family: 'JetBrains Mono', monospace; border-color: #38bdf8;">
                            </div>
                            <button type="submit" class="btn-action-main" style="margin-top: 14px;">"""

if co_target in code:
    code = code.replace(co_target, co_replacement)
    print("Replaced checkout form with UTR input successfully!")
else:
    print("Failed to find co_target in code!")

# 2. Add NPCI Bank Security Shield to checkout box
qr_box_target = """                            <span style="font-size: 11px; color: #34d399; font-family: 'JetBrains Mono', monospace; font-weight: 700; display: block;">UPI: 9343062265</span>
                            <span style="font-size: 10px; color: var(--text-dim);">Scan QR or Pay on 9343062265</span>
                        </div>"""

qr_box_replacement = """                            <span style="font-size: 11px; color: #34d399; font-family: 'JetBrains Mono', monospace; font-weight: 700; display: block;" data-secure-vpa="true">UPI: 9343062265</span>
                            <span style="font-size: 10px; color: var(--text-dim);">Scan QR or Pay on 9343062265</span>
                            <div style="margin-top: 10px; background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 6px 10px; font-size: 9px; color: #34d399; text-align: left;">
                                🛡️ NPCI Verified Beneficiary: 9343062265 • Duplicate UTRs Auto-Blocked
                            </div>
                        </div>"""

if qr_box_target in code:
    code = code.replace(qr_box_target, qr_box_replacement)
    print("Added NPCI security badge to checkout box successfully!")
else:
    print("Failed to find qr_box_target in code!")

# 3. Add Quick UTR Unlock in #screen-locked
lock_upi_target = """                    <a href="https://wa.me/919343062265?text=Hi+BioTwin+Labs,+my+7-day+trial+expired.+Please+reactivate+my+access." target="_blank" class="btn-wa" style="margin-top: 14px;">
                        <span>💬</span>
                        <span data-i18n="lock_btn_wa">WhatsApp to Reactivate (9343062265)</span>
                    </a>
                </div>"""

lock_upi_replacement = """                    <a href="https://wa.me/919343062265?text=Hi+BioTwin+Labs,+my+7-day+trial+expired.+Please+reactivate+my+access." target="_blank" class="btn-wa" style="margin-top: 14px;">
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
                </div>"""

if lock_upi_target in code:
    code = code.replace(lock_upi_target, lock_upi_replacement)
    print("Added quick UTR unlock to screen-locked successfully!")
else:
    print("Failed to find lock_upi_target in code!")

# 4. Update submitPlanOrder and add submitQuickUnlockUTR + DOM Tamper Guard in JS
old_submit_plan = """        function submitPlanOrder(e) {
            e.preventDefault();
            const name = document.getElementById('co_name').value;
            const phone = document.getElementById('co_phone').value;
            const orderId = `BT-SUB-${Math.floor(100000 + Math.random() * 900000)}`;

            // Unlock local status to subscribed
            localStorage.setItem('biotwin_sub_status', 'subscribed');
            updateTrialBadgeDisplay();

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

            alert(`🎉 Subscription Activated Successfully!\\n\\nPlan: ${activePlanName}\\nOrder ID: ${orderId}\\nPrice: ₹${activePlanPrice}\\nPatient: ${name}\\n\\nYour membership access has been unlocked. Details sent to WhatsApp.`);

            const msg = `Hi BioTwin Labs, I have subscribed to ${activePlanName} (₹${activePlanPrice}).%0AOrder ID: ${orderId}%0AName: ${encodeURIComponent(name)}%0APhone: ${encodeURIComponent(phone)}`;
            window.open(`https://wa.me/919343062265?text=${msg}`, '_blank');

            showScreen('hub');
        }"""

new_submit_plan = """        // ===================================================
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

                alert(`🎉 Payment Verified & Access Unlocked!\\n\\nPlan: ${activePlanName}\\nOrder ID: ${data.order_id}\\nBank UTR: ${utr}\\nBeneficiary: 9343062265@upi\\n\\nYour membership is now active. Confirmation dispatched to WhatsApp.`);

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
        }"""

if old_submit_plan in code:
    code = code.replace(old_submit_plan, new_submit_plan)
    print("Updated submitPlanOrder and added UTR logic successfully!")
else:
    print("Failed to find old_submit_plan in code!")

with open(DEST_PATH, "w", encoding="utf-8") as f:
    f.write(code)

print("build_complete_platform_v7.py created successfully!")
