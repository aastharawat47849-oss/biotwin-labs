"""
BioTwin Interactive Patient Intake & Report Generator
Allows entering any patient's blood test results and instantly generates their BioTwin report.
"""

import os
import json
from generate_report import generate_html_report

def run_intake():
    print("=" * 60)
    print("   BIOTWIN LABS - NEW CLIENT INTAKE & REPORT GENERATOR   ")
    print("=" * 60)

    # 1. Demographics
    name = input("Client Name: ").strip() or "Client Demo"
    age_str = input("Age (Years): ").strip() or "40"
    age = float(age_str)
    gender = input("Gender (Male/Female): ").strip() or "Male"

    patient = {
        "name": name,
        "age": int(age),
        "gender": gender
    }

    # 2. Key Biomarkers Intake (with default fallbacks)
    print("\nEnter Biomarker Values (Press Enter to use standard average default):")
    def get_val(prompt, default_val):
        val = input(f"{prompt} [Default: {default_val}]: ").strip()
        try:
            return float(val) if val else default_val
        except ValueError:
            return default_val

    biomarkers = {
        "apob": get_val("Apolipoprotein B (ApoB) [mg/dL]", 85.0),
        "lp_a": get_val("Lipoprotein(a) [Lp(a)] [mg/dL]", 15.0),
        "trig_hdl_ratio": get_val("Triglyceride/HDL Ratio", 1.8),
        "homocysteine": get_val("Homocysteine [umol/L]", 10.5),
        "hs_crp": get_val("hs-CRP (Inflammation) [mg/L]", 1.1),
        "fasting_insulin": get_val("Fasting Insulin [uIU/mL]", 8.5),
        "hba1c": get_val("HbA1c [%]", 5.3),
        "fasting_glucose": get_val("Fasting Glucose [mg/dL]", 89.0),
        "uric_acid": get_val("Serum Uric Acid [mg/dL]", 5.5),
        "alt": get_val("ALT (Liver) [U/L]", 26.0),
        "ggt": get_val("GGT (Oxidative stress) [U/L]", 22.0),
        "albumin": get_val("Albumin [g/dL]", 4.5),
        "vitamin_d": get_val("Vitamin D3 [ng/mL]", 28.0),
        "vitamin_b12": get_val("Vitamin B12 [pg/mL]", 380.0),
    }

    doctor = {
        "name": "Dr. Aarav Mehta, MD",
        "credentials": "MD (Internal Medicine), Fellowship in Anti-Aging & Functional Medicine",
        "registration_no": "MCI-48920-KA"
    }

    safe_filename = name.lower().replace(" ", "_")
    output_html = os.path.join(os.path.dirname(__file__), "..", f"{safe_filename}_report.html")
    generate_html_report(patient, biomarkers, doctor, output_html)

    print(f"\n[SUCCESS] New Report Generated: {output_html}")
    print("Opening report in your browser...")
    os.system(f'start "" "{output_html}"')

if __name__ == "__main__":
    run_intake()
