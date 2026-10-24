# -*- coding: utf-8 -*-
import os

BASE_DIR = r"c:\Users\B-WOI\OneDrive\Desktop\BioTwin-Platform"
CRM_PATH = os.path.join(BASE_DIR, "web", "templates", "founder_crm.html")

with open(CRM_PATH, "r", encoding="utf-8") as f:
    crm_content = f.read()

# Replace button in CRM to include Expiry Reminder
old_action = """                        <a href="https://wa.me/{{ lead.phone }}?text=Hi+{{ lead.name }},+BioTwin+phlebotomist+sample+collection+confirmed" target="_blank" class="btn-wa-call">
                            💬 Chat on WhatsApp
                        </a>"""

new_action = """                        <div style="display: flex; gap: 6px; flex-wrap: wrap;">
                            <a href="https://wa.me/{{ lead.phone }}?text=Hi+{{ lead.name }},+BioTwin+order+confirmed.+Contacting+from+9343062265" target="_blank" class="btn-wa-call">
                                💬 WhatsApp
                            </a>
                            <a href="https://wa.me/{{ lead.phone }}?text=Hello+{{ lead.name }},+your+7-Day+Free+Trial+on+BioTwin+Labs+has+concluded+and+tools+are+locked.+Reactivate+today+for+just+Rs+199/week+or+Rs+2499/month+to+continue+tracking+your+biological+age.+Pay+via+UPI+to+9343062265+or+reply+here+to+unlock." target="_blank" class="btn-wa-call" style="background: #f59e0b; color: #000;">
                                🔔 Send Expiry Reminder
                            </a>
                        </div>"""

if old_action in crm_content:
    crm_content = crm_content.replace(old_action, new_action)
    with open(CRM_PATH, "w", encoding="utf-8") as f:
        f.write(crm_content)
    print("founder_crm.html updated successfully with WhatsApp Expiry Reminder button!")
else:
    # Try normalizing newlines
    crm_normalized = crm_content.replace("\r\n", "\n")
    old_normalized = old_action.replace("\r\n", "\n")
    if old_normalized in crm_normalized:
        crm_normalized = crm_normalized.replace(old_normalized, new_action)
        with open(CRM_PATH, "w", encoding="utf-8") as f:
            f.write(crm_normalized)
        print("founder_crm.html updated successfully with normalized newlines!")
    else:
        print("Could not find old_action in founder_crm.html")
