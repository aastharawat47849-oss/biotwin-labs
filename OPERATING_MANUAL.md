# BioTwin Labs — Master Founder Operating Manual
## Complete Operational Guide: From Zero to First 50 Users & Revenue

---

### 1. How to Run Your Web Platform (1-Click)

You have a complete full-stack web application running locally on your computer.

#### To Start the Web Server:
Open your PowerShell terminal and run:
```powershell
python "c:\Users\B-WOI\OneDrive\Desktop\BioTwin-Platform\web\app.py"
```
Or double-click **`START_BIOTWIN.bat`** on your desktop.

#### URLs:
- **Client Intake Portal:** [http://127.0.0.1:5050](http://127.0.0.1:5050)
- **Founder Leads & CRM Dashboard:** [http://127.0.0.1:5050/leads](http://127.0.0.1:5050/leads)

---

### 2. How the Client Flow Works

```
1. Client Lands on Portal (http://127.0.0.1:5050)
        │
        ▼
2. Enters Name, Age, Phone & Lab Biomarkers (or clicks Quick Demo)
        │
        ▼
3. Clicks "Generate My Bio-Twin Longevity Report"
        │
        ├──► AI calculates Levine PhenoAge (Biological Age vs Actual Age)
        ├──► Scores 5 Organ Subsystems (Cardio, Metabolic, Inflammation, Liver, Endocrine)
        ├──► Generates Personalized 90-Day Protocol with Lancet/NEJM citations
        ├──► Generates downloadable Vector PDF Report automatically
        └──► Saves lead into Founder CRM (http://127.0.0.1:5050/leads)
```

---

### 3. File & Code Directory Structure

```
BioTwin-Platform/
│
├── START_BIOTWIN.bat             <-- Double-click to launch server
├── sample_executive_report.pdf   <-- Ready demo PDF (Send on WhatsApp)
├── sample_executive_report.html  <-- Interactive HTML demo
├── OPERATING_MANUAL.md           <-- This master guide
│
├── engine/                       <-- Core Clinical & Math Engine
│   ├── clinical_matrix.py        <-- 72-biomarker optimal reference database
│   ├── bio_age_calculator.py     <-- Levine PhenoAge & Organ Scoring algorithm
│   ├── generate_report.py        <-- Standalone HTML report builder
│   └── cli_input.py              <-- Terminal intake script
│
├── web/                          <-- Full-Stack Web Application
│   ├── app.py                    <-- Flask Backend Server (Port 5050)
│   ├── templates/
│   │   ├── index.html            <-- High-converting landing & intake page
│   │   ├── report.html           <-- Interactive client report with PDF download
│   │   └── leads.html            <-- Founder CRM dashboard
│   └── storage/
│       ├── leads.json            <-- Database of all submitted leads
│       └── reports/              <-- Generated HTML & PDF files
│
└── marketing/
    └── viral_launch_kit.md       <-- Copy-paste WhatsApp, LinkedIn & Upsell scripts
```

---

### 4. Step-by-Step 7-Day Launch Plan

- **Day 1 (Today):** Test the portal at `http://127.0.0.1:5050`. Click *"👔 High-Stress Executive"* and generate the report. Open the PDF.
- **Day 2:** Copy the WhatsApp broadcast message from `marketing/viral_launch_kit.md` and send it to 10–15 trusted contacts (friends, family, gym trainers, business uncles).
- **Day 3:** For everyone who sends their blood report, input their numbers into the portal and WhatsApp them their official PDF report.
- **Day 4–5:** Follow up with the conversion script in `viral_launch_kit.md` to offer the ₹1,999 At-Cost Fresh Retest.
- **Day 6–7:** Sign up as a B2B partner with Redcliffe Labs / Thyrocare to fulfill fresh home blood draws.
