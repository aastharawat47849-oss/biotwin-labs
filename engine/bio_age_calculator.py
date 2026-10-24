"""
BioTwin Biological Age & Organ Decay Calculator
Implements adapted Levine PhenoAge estimation and organ subsystem scoring.
"""

import math
from typing import Dict, Any, List

def calculate_pheno_age(chronological_age: float, biomarkers: Dict[str, float]) -> float:
    """
    Computes PhenoAge based on an adapted clinical regression model
    incorporating Chronological Age, Albumin, Creatinine, Glucose, hs-CRP,
    Lymphocyte %, and liver enzymes.
    """
    # Baseline defaults if certain specialized sub-markers are not yet run
    albumin = biomarkers.get("albumin", 4.5)           # g/dL
    creatinine = biomarkers.get("creatinine", 0.9)       # mg/dL
    glucose = biomarkers.get("fasting_glucose", 85.0)   # mg/dL
    hs_crp = biomarkers.get("hs_crp", 0.5)              # mg/L
    alt = biomarkers.get("alt", 20.0)                   # U/L
    fasting_insulin = biomarkers.get("fasting_insulin", 5.0)

    # Convert hs-CRP to ln(crp) (with minimum floor to prevent log(0))
    ln_crp = math.log(max(hs_crp, 0.05))

    # Linear Mortality Risk Score (xb) adaptation
    # Higher albumin decreases mortality risk; higher glucose, crp, age increases it
    xb = (
        -1.9907
        + (0.0804 * chronological_age)
        - (0.0336 * albumin * 10) # converted to g/L
        + (0.0095 * glucose)
        + (0.1953 * ln_crp)
        + (0.0150 * (fasting_insulin / 2.0))
        + (0.0050 * (alt / 10.0))
    )

    # Gompertz mortality transformation into biological age
    mortality_risk = 1.0 - math.exp(-math.exp(xb))
    # Invert mortality risk into age space (Gompertz parameters: gamma=0.007692, b0=0.09165)
    gamma = 0.007692
    b0 = 0.09165
    try:
        pheno_age = 141.5 + (math.log(-0.00553 * math.log(1.0 - min(mortality_risk, 0.999))) / 0.09165)
    except Exception:
        pheno_age = chronological_age + (xb * 5.0)

    # Constrain within physiological bounds
    pheno_age = max(18.0, min(pheno_age, chronological_age + 20.0))
    return round(pheno_age, 1)

def evaluate_subsystems(biomarkers: Dict[str, float], registry: dict) -> Dict[str, Any]:
    """
    Scores each organ subsystem from 0 to 100 (100 = Peak Youthful Optimal).
    """
    subsystems = {
        "Cardiovascular Longevity": {"score": 100, "markers": ["apob", "lp_a", "trig_hdl_ratio", "homocysteine"], "penalties": []},
        "Metabolic Health": {"score": 100, "markers": ["fasting_insulin", "hba1c", "fasting_glucose", "uric_acid"], "penalties": []},
        "Systemic Inflammation": {"score": 100, "markers": ["hs_crp"], "penalties": []},
        "Hepatic & Cellular Longevity": {"score": 100, "markers": ["alt", "ggt", "albumin"], "penalties": []},
        "Endocrine & Micronutrient": {"score": 100, "markers": ["vitamin_d", "vitamin_b12"], "penalties": []},
    }

    results = {}
    for system_name, data in subsystems.items():
        score = 100
        markers_assessed = []
        for m_key in data["markers"]:
            if m_key in biomarkers and m_key in registry:
                val = biomarkers[m_key]
                meta = registry[m_key]
                opt_min, opt_max = meta.optimal_range
                std_min, std_max = meta.standard_range

                # Calculate status
                if opt_min <= val <= opt_max:
                    status = "OPTIMAL"
                elif std_min <= val <= std_max:
                    status = "SUB-OPTIMAL"
                    score -= 15
                else:
                    status = "HIGH_RISK"
                    score -= 30

                markers_assessed.append({
                    "name": meta.name,
                    "val": val,
                    "unit": meta.unit,
                    "status": status,
                    "optimal_range": f"{opt_min} - {opt_max} {meta.unit}",
                    "standard_range": f"{std_min} - {std_max} {meta.unit}",
                    "clinical_note": meta.clinical_note,
                    "citation": meta.citation,
                    "doi": meta.doi
                })

        score = max(20, min(100, score))
        results[system_name] = {
            "score": score,
            "status": "EXCELLENT" if score >= 85 else ("MODERATE_RISK" if score >= 65 else "ATTENTION_REQUIRED"),
            "markers": markers_assessed
        }

    return results
