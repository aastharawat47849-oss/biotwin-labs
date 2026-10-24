"""
BioTwin Intelligence Platform - Clinical Longevity Matrix
Defines standard vs optimal longevity boundaries, categories, and scientific evidence.
"""

from dataclasses import dataclass
from typing import Tuple, Optional

@dataclass
class BiomarkerDefinition:
    key: str
    name: str
    category: str
    unit: str
    standard_range: Tuple[float, float]
    optimal_range: Tuple[float, float]
    lower_is_better: bool
    citation: str
    doi: str
    clinical_note: str

BIOMARKER_REGISTRY = {
    # 1. Advanced Cardiovascular
    "apob": BiomarkerDefinition(
        key="apob",
        name="Apolipoprotein B (ApoB)",
        category="Cardiovascular Longevity",
        unit="mg/dL",
        standard_range=(40.0, 125.0),
        optimal_range=(40.0, 60.0),
        lower_is_better=True,
        citation="Sniderman AD et al. Lancet 2019; 394: 1845-56",
        doi="10.1016/S0140-6736(19)32519-X",
        clinical_note="ApoB reflects total atherogenic particle concentration; target < 60 mg/dL halts arterial plaque progression."
    ),
    "lp_a": BiomarkerDefinition(
        key="lp_a",
        name="Lipoprotein(a) [Lp(a)]",
        category="Cardiovascular Longevity",
        unit="mg/dL",
        standard_range=(0.0, 30.0),
        optimal_range=(0.0, 14.0),
        lower_is_better=True,
        citation="Tsimikas S. J Am Coll Cardiol 2017; 69(6): 692-711",
        doi="10.1016/j.jacc.2016.11.054",
        clinical_note="Genetically determined cardiovascular risk factor; non-modifiable by diet, requires targeted risk mitigation."
    ),
    "trig_hdl_ratio": BiomarkerDefinition(
        key="trig_hdl_ratio",
        name="Triglyceride to HDL Ratio",
        category="Cardiovascular Longevity",
        unit="ratio",
        standard_range=(0.0, 3.0),
        optimal_range=(0.0, 1.0),
        lower_is_better=True,
        citation="McLaughlin T et al. Ann Intern Med 2003; 139(10): 802-9",
        doi="10.7326/0003-4819-139-10-200311180-00008",
        clinical_note="Surpassing indicator of atherogenic small dense LDL particles and hepatic insulin resistance."
    ),
    "homocysteine": BiomarkerDefinition(
        key="homocysteine",
        name="Homocysteine",
        category="Cardiovascular Longevity",
        unit="umol/L",
        standard_range=(5.0, 15.0),
        optimal_range=(6.0, 8.0),
        lower_is_better=True,
        citation="Clarke R et al. N Engl J Med 1991; 324(17): 1149-55",
        doi="10.1056/NEJM199104253241701",
        clinical_note="Elevated homocysteine induces vascular endothelial toxicity and methylation impairment."
    ),
    "hs_crp": BiomarkerDefinition(
        key="hs_crp",
        name="High-Sensitivity C-Reactive Protein (hs-CRP)",
        category="Systemic Inflammation",
        unit="mg/L",
        standard_range=(0.0, 3.0),
        optimal_range=(0.0, 0.5),
        lower_is_better=True,
        citation="Ridker PM. Circulation 2003; 107(3): 363-9",
        doi="10.1161/01.CIR.0000053730.47739.3C",
        clinical_note="Indicates low-grade subclinical vascular inflammation; levels > 0.5 mg/L indicate accelerated vascular aging."
    ),

    # 2. Metabolic & Glycemic
    "fasting_insulin": BiomarkerDefinition(
        key="fasting_insulin",
        name="Fasting Insulin",
        category="Metabolic Health",
        unit="uIU/mL",
        standard_range=(2.6, 24.9),
        optimal_range=(1.5, 4.5),
        lower_is_better=True,
        citation="Kraft JR. Detection of Diabetes Mellitus In Situ (1975) / Crofts C et al. 2016",
        doi="10.3389/fendo.2016.00135",
        clinical_note="Early biomarker of hyperinsulinemia and cellular insulin resistance, preceding glucose spikes by 10 years."
    ),
    "hba1c": BiomarkerDefinition(
        key="hba1c",
        name="Glycated Hemoglobin (HbA1c)",
        category="Metabolic Health",
        unit="%",
        standard_range=(4.0, 5.6),
        optimal_range=(4.8, 5.2),
        lower_is_better=True,
        citation="Selvin E et al. N Engl J Med 2010; 362(9): 800-11",
        doi="10.1056/NEJMoa0908359",
        clinical_note="Average 90-day glycemic control; values above 5.3% indicate microvascular protein glycation."
    ),
    "fasting_glucose": BiomarkerDefinition(
        key="fasting_glucose",
        name="Fasting Blood Glucose",
        category="Metabolic Health",
        unit="mg/dL",
        standard_range=(70.0, 99.0),
        optimal_range=(74.0, 85.0),
        lower_is_better=True,
        citation="Nichols GA et al. Diabetes Care 2008; 31(10): 2001-4",
        doi="10.2337/dc08-0853",
        clinical_note="Optimal fasting range prevents hepatic gluconeogenesis overshoot and glycation spikes."
    ),
    "uric_acid": BiomarkerDefinition(
        key="uric_acid",
        name="Serum Uric Acid",
        category="Metabolic Health",
        unit="mg/dL",
        standard_range=(3.5, 7.2),
        optimal_range=(4.0, 5.0),
        lower_is_better=True,
        citation="Johnson RJ et al. Nat Rev Rheumatol 2013; 9(10): 630-40",
        doi="10.1038/nrrheum.2013.113",
        clinical_note="Values > 5.5 mg/dL suppress endothelial nitric oxide and signal fructose/purine metabolic stress."
    ),

    # 3. Hepatic & Cellular
    "alt": BiomarkerDefinition(
        key="alt",
        name="Alanine Aminotransferase (ALT)",
        category="Hepatic & Cellular Longevity",
        unit="U/L",
        standard_range=(7.0, 56.0),
        optimal_range=(10.0, 22.0),
        lower_is_better=True,
        citation="Kim HC et al. BMJ 2004; 328(7446): 983",
        doi="10.1136/bmj.38050.593634.63",
        clinical_note="Levels above 25 U/L strongly correlate with occult non-alcoholic fatty liver disease (NAFLD)."
    ),
    "ggt": BiomarkerDefinition(
        key="ggt",
        name="Gamma-Glutamyl Transferase (GGT)",
        category="Hepatic & Cellular Longevity",
        unit="U/L",
        standard_range=(9.0, 48.0),
        optimal_range=(10.0, 18.0),
        lower_is_better=True,
        citation="Lee DH et al. Clin Chem 2004; 50(10): 1874-6",
        doi="10.1373/clinchem.2004.037192",
        clinical_note="Ultra-sensitive marker for hepatic oxidative stress and systemic glutathione depletion."
    ),
    "albumin": BiomarkerDefinition(
        key="albumin",
        name="Serum Albumin",
        category="Hepatic & Cellular Longevity",
        unit="g/dL",
        standard_range=(3.5, 5.2),
        optimal_range=(4.5, 5.0),
        lower_is_better=False,
        citation="Levine ME. J Gerontol A Biol Sci Med Sci 2013; 68(6): 667-74",
        doi="10.1093/gerona/gls233",
        clinical_note="Crucial biomarker in Levine PhenoAge; higher levels indicate plasma oncotic and antioxidant capacity."
    ),

    # 4. Micronutrients & Endocrine
    "vitamin_d": BiomarkerDefinition(
        key="vitamin_d",
        name="25-Hydroxy Vitamin D3",
        category="Endocrine & Micronutrient",
        unit="ng/mL",
        standard_range=(30.0, 100.0),
        optimal_range=(55.0, 75.0),
        lower_is_better=False,
        citation="Holick MF. N Engl J Med 2007; 357(3): 266-81",
        doi="10.1056/NEJMra070553",
        clinical_note="Nuclear receptor ligand regulating expression of > 2,000 genes in innate immunity and longevity."
    ),
    "vitamin_b12": BiomarkerDefinition(
        key="vitamin_b12",
        name="Vitamin B12 (Active Cobalamin)",
        category="Endocrine & Micronutrient",
        unit="pg/mL",
        standard_range=(200.0, 900.0),
        optimal_range=(600.0, 900.0),
        lower_is_better=False,
        citation="Stabler SP. N Engl J Med 2013; 368(2): 149-60",
        doi="10.1056/NEJMcp1113996",
        clinical_note="Essential co-factor for remethylation of homocysteine and neuro-protective myelin maintenance."
    ),
}
