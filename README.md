# ShipmentDoc Compliance AI
**AI-powered Dangerous Goods & Customs Clearance Compliance System**
*Logistics / Supply Chain · Medium Enterprise · Kinda Faisal · 2026*

---

## 🔗 Live Portals

| Portal | URL | For |
|--------|-----|-----|
| 🚛 Shipper Portal | https://final-project-dg-customs-compliance-3djmsuecztvsuux7jgpyai.streamlit.app/ | Shippers preparing shipment documents |
| 🏢 Freight Forwarder Portal | https://final-project-dg-customs-compliance-mffpsnzkusr6pmhcb6e8xv.streamlit.app/ | Operations teams doing final compliance check |

---

## 📋 Problem Statement

International logistics compliance is one of the most time-consuming tasks in the supply chain. Operations staff spend **70–80% of their working day** manually checking whether dangerous goods and customs documents are complete, correctly formatted, and compliant with international agreements (ADR, IMDG, IATA, EU UCC, CMR).

---

## 💡 Solution

Two AI-powered portals that automate document compliance checking across both dangerous goods regulations and customs clearance requirements.

### Agent 1 — Freight Forwarder Portal (n8n + OpenAI GPT-4o)
- Operations team runs final compliance check before dispatch
- n8n workflow: webhook → regulation selector → GPT-4o → structured checklist
- Checks: ADR/IMDG/IATA + EU customs per route

### Agent 2 — Shipper Portal (Python + OpenAI GPT-4o)
- Shippers check documents before submitting to freight forwarder
- 3-column UI: Shipment Details · Customs Information · Dangerous Goods
- Pre-validation + AI checklist in 0.44 seconds

---

## 📊 Performance

| Metric | Value |
|--------|-------|
| Response time | 0.44 seconds |
| Accuracy (LangSmith) | 90.7% |
| Human confidence rating | 8.7 / 10 |
| Hallucination rate | 1.2% |
| EU AI Act | Limited Risk (Art. 52) |

---

## 📁 Repository Structure
```
final-project-dg-customs-compliance/
├── shipper/
│   ├── shipper_portal.py
│   ├── shipper_agent.py
│   └── requirements.txt
├── compliance/
│   ├── eu_ai_act_compliance.md
│   └── gdpr_documentation.md
├── poc/
│   ├── poc_documentation.md
│   └── poc_workflow.json
├── README.md
├── use_case_definition.md
├── strategic_plan.md
├── roi_risk_assessment.md
├── presentation.pptx
├── final_report.pdf
└── .env.example
```

---

## ⚙️ Setup
```bash
git clone https://github.com/kindafaisal-ui/final-project-dg-customs-compliance.git
cd final-project-dg-customs-compliance
pip install -r shipper/requirements.txt
cp .env.example .env
# Add your OpenAI API key to .env
streamlit run shipper/shipper_portal.py
```

---

## 📜 Regulations Covered

ADR 2023 · IMDG Code · IATA DGR · EU UCC · CMR Convention · EUR.1 / REX · EU AI Act Art. 52 · GDPR Art. 6(1)(b)

---

## 👤 Author

**Kinda Faisal** — 6 years logistics & supply chain operations
GitHub: [kindafaisal-ui](https://github.com/kindafaisal-ui)
