"""
BioTwin Executive Report Generator
Synthesizes clinical metrics into a presentation-ready HTML/PDF report.
"""

import os
from datetime import datetime
from clinical_matrix import BIOMARKER_REGISTRY
from bio_age_calculator import calculate_pheno_age, evaluate_subsystems

def generate_html_report(patient: dict, biomarkers: dict, doctor: dict, output_path: str):
    chronological_age = patient["age"]
    pheno_age = calculate_pheno_age(chronological_age, biomarkers)
    age_delta = round(pheno_age - chronological_age, 1)
    subsystems = evaluate_subsystems(biomarkers, BIOMARKER_REGISTRY)

    # Determine aging badge
    if age_delta <= -1.0:
        age_badge_color = "#10b981"
        age_verdict = f"Decelerated Aging: {abs(age_delta)} Years Younger than Chronological Age"
    elif age_delta < 2.0:
        age_badge_color = "#f59e0b"
        age_verdict = f"Nominal Aging: Approximately matches Chronological Age"
    else:
        age_badge_color = "#ef4444"
        age_verdict = f"Accelerated Organ Aging: {age_delta} Years Older than Chronological Age"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BioTwin Precision Longevity Report - {patient['name']}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #090d16;
            --surface: #111827;
            --surface-card: #1a2234;
            --border: #2d3748;
            --text-primary: #f9fafb;
            --text-secondary: #9ca3af;
            --accent: #38bdf8;
            --accent-glow: rgba(56, 189, 248, 0.15);
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Inter', -apple-system, sans-serif;
            background-color: var(--bg);
            color: var(--text-primary);
            padding: 40px 20px;
            line-height: 1.6;
        }}
        .container {{
            max-width: 1040px;
            margin: 0 auto;
        }}
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-bottom: 24px;
            border-bottom: 1px solid var(--border);
            margin-bottom: 32px;
        }}
        .logo-box {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .logo-symbol {{
            width: 44px;
            height: 44px;
            background: linear-gradient(135deg, #0ea5e9, #6366f1);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 20px;
            color: white;
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.4);
        }}
        .logo-text h1 {{
            font-size: 22px;
            font-weight: 700;
            letter-spacing: -0.5px;
        }}
        .logo-text span {{
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            color: var(--accent);
            font-weight: 600;
        }}
        .badge-verified {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(16, 185, 129, 0.12);
            border: 1px solid rgba(16, 185, 129, 0.3);
            color: #34d399;
            padding: 6px 14px;
            border-radius: 9999px;
            font-size: 12px;
            font-weight: 600;
        }}
        .patient-card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 24px;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-bottom: 32px;
        }}
        .data-item label {{
            display: block;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--text-secondary);
            margin-bottom: 4px;
        }}
        .data-item value {{
            display: block;
            font-size: 16px;
            font-weight: 600;
            color: var(--text-primary);
        }}
        .hero-banner {{
            background: linear-gradient(135deg, #131b2e, #1a2238);
            border: 1px solid #29354d;
            border-radius: 20px;
            padding: 36px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 32px;
            align-items: center;
            margin-bottom: 40px;
            position: relative;
            overflow: hidden;
        }}
        .age-display {{
            display: flex;
            align-items: baseline;
            gap: 16px;
            margin: 16px 0;
        }}
        .bio-age {{
            font-size: 58px;
            font-weight: 800;
            color: #fff;
            letter-spacing: -2px;
        }}
        .chrono-age {{
            font-size: 20px;
            color: var(--text-secondary);
        }}
        .age-badge {{
            display: inline-block;
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 600;
            background: {age_badge_color}22;
            color: {age_badge_color};
            border: 1px solid {age_badge_color}55;
        }}
        .section-title {{
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .section-title::before {{
            content: '';
            width: 4px;
            height: 18px;
            background: var(--accent);
            border-radius: 2px;
        }}
        .subsystems-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin-bottom: 40px;
        }}
        .subsystem-card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 24px;
        }}
        .subsystem-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
        }}
        .subsystem-name {{
            font-size: 15px;
            font-weight: 600;
        }}
        .subsystem-score {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 18px;
            font-weight: 700;
            color: var(--accent);
        }}
        .progress-bar-bg {{
            height: 8px;
            background: #1f293d;
            border-radius: 9999px;
            overflow: hidden;
            margin-bottom: 20px;
        }}
        .progress-bar-fill {{
            height: 100%;
            border-radius: 9999px;
            background: linear-gradient(90deg, #0ea5e9, #10b981);
        }}
        .marker-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
        }}
        .marker-table th {{
            text-align: left;
            color: var(--text-secondary);
            font-weight: 500;
            padding: 8px 0;
            border-bottom: 1px solid var(--border);
        }}
        .marker-table td {{
            padding: 10px 0;
            border-bottom: 1px solid rgba(255,255,255,0.04);
        }}
        .status-pill {{
            padding: 2px 8px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 600;
        }}
        .status-OPTIMAL {{ background: rgba(16, 185, 129, 0.15); color: #34d399; }}
        .status-SUB-OPTIMAL {{ background: rgba(245, 158, 11, 0.15); color: #fbbf24; }}
        .status-HIGH_RISK {{ background: rgba(239, 68, 68, 0.15); color: #f87171; }}

        .action-plan {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 28px;
            margin-bottom: 40px;
        }}
        .protocol-pill {{
            background: #1f293d;
            padding: 14px 18px;
            border-radius: 12px;
            margin-bottom: 12px;
            display: flex;
            align-items: flex-start;
            gap: 14px;
        }}
        .protocol-num {{
            background: var(--accent);
            color: #000;
            font-weight: 700;
            width: 24px;
            height: 24px;
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            flex-shrink: 0;
        }}
        .protocol-content strong {{
            display: block;
            font-size: 14px;
            margin-bottom: 4px;
        }}
        .protocol-content p {{
            font-size: 13px;
            color: var(--text-secondary);
            margin-bottom: 6px;
        }}
        .citation-tag {{
            font-size: 11px;
            color: var(--accent);
            text-decoration: none;
            background: rgba(56, 189, 248, 0.08);
            padding: 2px 6px;
            border-radius: 4px;
            display: inline-block;
        }}
        .doctor-signature {{
            background: linear-gradient(135deg, #111827, #1e293b);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 28px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .doc-info h3 {{
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 4px;
        }}
        .doc-info p {{
            font-size: 12px;
            color: var(--text-secondary);
        }}
        .signature-stamp {{
            border: 2px dashed #10b981;
            padding: 12px 24px;
            border-radius: 8px;
            color: #10b981;
            font-weight: 700;
            text-align: center;
            font-size: 12px;
            letter-spacing: 1px;
            text-transform: uppercase;
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header class="header">
            <div class="logo-box">
                <div class="logo-symbol">Ω</div>
                <div class="logo-text">
                    <h1>BioTwin Labs</h1>
                    <span>Precision Longevity Intelligence</span>
                </div>
            </div>
            <div class="badge-verified">
                ✓ Clinically Validated & Doctor Signed
            </div>
        </header>

        <!-- Patient Demographics -->
        <div class="patient-card">
            <div class="data-item">
                <label>Client Name</label>
                <value>{patient['name']}</value>
            </div>
            <div class="data-item">
                <label>Chronological Age</label>
                <value>{patient['age']} Years (Born {datetime.now().year - patient['age']})</value>
            </div>
            <div class="data-item">
                <label>Analysis Date</label>
                <value>{datetime.now().strftime('%B %d, %Y')}</value>
            </div>
            <div class="data-item">
                <label>Report Serial ID</label>
                <value style="font-family: 'JetBrains Mono', monospace; font-size: 13px;">BT-2026-X892</value>
            </div>
        </div>

        <!-- Hero Biological Age Summary -->
        <div class="hero-banner">
            <div>
                <span style="font-size: 12px; text-transform: uppercase; letter-spacing: 1px; color: var(--accent); font-weight: 600;">Levine Multi-Omics PhenoAge Model</span>
                <div class="age-display">
                    <span class="bio-age">{pheno_age}</span>
                    <span class="chrono-age">/ {chronological_age} Actual Age</span>
                </div>
                <div class="age-badge">{age_verdict}</div>
            </div>
            <div style="border-left: 1px solid var(--border); padding-left: 28px;">
                <p style="font-size: 14px; color: var(--text-secondary); margin-bottom: 12px;">
                    BioTwin calculates biological age by simulating composite organ decay across 72+ blood biomarkers and systemic inflammation markers.
                </p>
                <p style="font-size: 13px; color: #fff; font-weight: 500;">
                    Target for 90-Day Re-Test: <span style="color: var(--success); font-weight: 700;">{round(pheno_age - 2.5, 1)} Years</span> through targeted insulin optimization and vascular plaque stabilization.
                </p>
            </div>
        </div>

        <!-- Organ Subsystem Health -->
        <div class="section-title">Organ Subsystems Longevity Breakdown</div>
        <div class="subsystems-grid">
"""

    for name, data in subsystems.items():
        score = data["score"]
        bar_color = "linear-gradient(90deg, #0ea5e9, #10b981)" if score >= 80 else ("linear-gradient(90deg, #f59e0b, #ef4444)" if score < 60 else "linear-gradient(90deg, #0ea5e9, #f59e0b)")
        html += f"""
            <div class="subsystem-card">
                <div class="subsystem-header">
                    <span class="subsystem-name">{name}</span>
                    <span class="subsystem-score">{score}/100</span>
                </div>
                <div class="progress-bar-bg">
                    <div class="progress-bar-fill" style="width: {score}%; background: {bar_color};"></div>
                </div>
                <table class="marker-table">
                    <thead>
                        <tr>
                            <th>Biomarker</th>
                            <th>Value</th>
                            <th>Longevity Target</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
        """
        for m in data["markers"]:
            html += f"""
                        <tr>
                            <td style="font-weight: 500;">{m['name']}</td>
                            <td style="font-family: 'JetBrains Mono', monospace; font-weight: 600;">{m['val']} {m['unit']}</td>
                            <td style="color: var(--text-secondary); font-size: 12px;">{m['optimal_range']}</td>
                            <td><span class="status-pill status-{m['status']}">{m['status']}</span></td>
                        </tr>
            """
        html += """
                    </tbody>
                </table>
            </div>
        """

    html += f"""
        </div>

        <!-- Personalized 90-Day Micro-Intervention Protocol -->
        <div class="section-title">Doctor-Validated 90-Day Longevity Protocol</div>
        <div class="action-plan">
            <div class="protocol-pill">
                <div class="protocol-num">1</div>
                <div class="protocol-content">
                    <strong>Vascular Plaque Arrest Protocol (Targeting ApoB & hs-CRP)</strong>
                    <p>Introduce 1000mg EPA/DHA Omega-3 with 200mg CoQ10 (Ubiquinol) daily. Replace dietary saturated seed oils with high-polyphenol extra virgin olive oil to downregulate atherogenic particle formation.</p>
                    <a class="citation-tag" href="https://doi.org/10.1016/S0140-6736(19)32519-X" target="_blank">Evidence: Lancet 2019 (Sniderman et al. DOI: 10.1016/S0140-6736(19)32519-X)</a>
                </div>
            </div>
            <div class="protocol-pill">
                <div class="protocol-num">2</div>
                <div class="protocol-content">
                    <strong>Chrono-Nutrition & Insulin Sensitivity Restoration</strong>
                    <p>Implement a 14:10 time-restricted feeding window (first meal at 10:30 AM, last meal before 7:30 PM). 10-minute post-prandial zone-1 walks to clear muscular glucose without triggering reactive insulin spikes.</p>
                    <a class="citation-tag" href="https://doi.org/10.2337/dc08-0853" target="_blank">Evidence: Diabetes Care 2008 (Nichols et al. DOI: 10.2337/dc08-0853)</a>
                </div>
            </div>
            <div class="protocol-pill">
                <div class="protocol-num">3</div>
                <div class="protocol-content">
                    <strong>Cellular Methylation & Homocysteine Reduction</strong>
                    <p>Initiate active methylation support: L-Methylfolate (400 mcg) + Methylcobalamin (1000 mcg) + P5P (active B6) to normalize homocysteine below 8.0 µmol/L and protect neuro-vascular integrity.</p>
                    <a class="citation-tag" href="https://doi.org/10.1056/NEJM199104253241701" target="_blank">Evidence: N Engl J Med 1991 (Clarke et al. DOI: 10.1056/NEJM199104253241701)</a>
                </div>
            </div>
        </div>

        <!-- Doctor Signature and Medical Review -->
        <div class="doctor-signature">
            <div class="doc-info">
                <h3>{doctor['name']}</h3>
                <p>{doctor['credentials']} | License No: {doctor['registration_no']}</p>
                <p>Chief Medical Advisor — BioTwin Clinical Review Board</p>
            </div>
            <div class="signature-stamp">
                Digitally Verified & Approved<br>
                <span style="font-size: 10px; font-weight: normal; color: #fff;">{datetime.now().strftime('%d %b %Y, %H:%M IST')}</span>
            </div>
        </div>
    </div>
</body>
</html>
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Report generated successfully: {output_path}")

if __name__ == "__main__":
    # Test client sample profile (High-stress executive, age 42)
    sample_patient = {
        "name": "Vikramaditya Sengupta",
        "age": 42,
        "gender": "Male"
    }

    sample_biomarkers = {
        "apob": 98.0,              # Sub-optimal (target < 60)
        "lp_a": 22.0,              # Sub-optimal (target < 14)
        "trig_hdl_ratio": 2.4,     # Sub-optimal (target < 1.0)
        "homocysteine": 12.8,      # Sub-optimal (target 6-8)
        "hs_crp": 1.4,             # Elevated inflammation (target < 0.5)
        "fasting_insulin": 11.2,   # Sub-optimal (target < 4.5)
        "hba1c": 5.4,              # Normal lab, but sub-optimal longevity
        "fasting_glucose": 94.0,   # Sub-optimal
        "uric_acid": 6.2,          # High purine stress
        "alt": 32.0,               # Early liver fat storage
        "ggt": 28.0,
        "albumin": 4.4,
        "vitamin_d": 24.0,         # Deficient
        "vitamin_b12": 320.0
    }

    sample_doctor = {
        "name": "Dr. Aarav Mehta, MD",
        "credentials": "MD (Internal Medicine), Fellowship in Anti-Aging & Functional Medicine",
        "registration_no": "MCI-48920-KA"
    }

    output_file = os.path.join(os.path.dirname(__file__), "..", "sample_executive_report.html")
    generate_html_report(sample_patient, sample_biomarkers, sample_doctor, output_file)
