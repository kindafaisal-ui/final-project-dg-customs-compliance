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

## 📹 Demo Recording

https://github.com/user-attachments/assets/2dc91d9f-5d0f-4e7f-bd06-6c919b123574

---

## 📋 Problem Statement

International logistics compliance is one of the most time-consuming tasks in the supply chain. Operations staff spend **70–80% of their working day** manually checking whether dangerous goods and customs documents are complete, correctly formatted, and compliant with international agreements (ADR, IMDG, IATA, EU UCC, CMR). One mistake means a €50,000 fine or a truck stopped at the border for 2 days.

---

## 💡 Solution — Two AI Agents

### Agent 1 — Freight Forwarder Portal (n8n + OpenAI GPT-4o)

Used by the **operations team** for final compliance checks before dispatch.
```
Shipment Documents (500/day)
        ↓
n8n Schedule Trigger (every night 00:00)
        ↓
Google Sheets — reads all pending shipments
        ↓
AI Compliance Logic Engine (GPT-4o via LangChain)
        ↓
    ┌───────────────────────────────┐
    │  DG Check: ADR · IMDG · IATA │
    │  Customs: UCC · CMR · EUR.1  │
    └───────────────────────────────┘
        ↓
LangSmith — full audit trail logged
        ↓
📧 Gmail Alert — email to management at 00:00
        ↓
Streamlit Portal — operations team reviews flagged docs
        ↓
✅ Human Decision — final approval before dispatch
```

**Key features:**
- Runs automatically every night at midnight
- Checks all 6 regulations simultaneously per shipment
- Sends consolidated email alert to management at 06:00
- Full LangSmith audit trail for every AI decision
- Human makes the final dispatch decision — always

---

### Agent 2 — Shipper Portal (Python + OpenAI GPT-4o)

Used by **shippers** at the start of the process, before submitting documents to their freight forwarder.
```
Shipper fills 3-column form:
┌─────────────────┬──────────────────┬──────────────────┐
│ Shipment Details│Customs Information│ Dangerous Goods  │
│ Route           │ HS Code (8-digit) │ DG Yes/No        │
│ Goods           │ EORI Number       │ DG Class         │
│ Transport Mode  │ Commercial Invoice│ UN Number        │
└─────────────────┴──────────────────┴──────────────────┘
        ↓
Pre-Validation (instant — before AI call)
— HS code must be 8 digits
— EORI must start with DE
— UN number must start with UN
        ↓
shipper_agent.py → OpenAI GPT-4o
        ↓
4-section compliance checklist:
1. Customs Compliance
2. Dangerous Goods Compliance
3. Critical Flags
4. Submission Checklist
        ↓
✅ Shipper prepares documents → sends to Freight Forwarder
```

---

## 🏗️ Full System Architecture
```
┌─────────────────────────────────────────────────────────┐
│                      SHIPPER                            │
│  Uses Agent 2 — Shipper Portal                          │
│  Gets AI checklist → prepares all documents             │
└─────────────────────────┬───────────────────────────────┘
                          │ Documents submitted
                          ▼
┌─────────────────────────────────────────────────────────┐
│              FREIGHT FORWARDER / OPERATIONS             │
│  Uses Agent 1 — Freight Forwarder Portal                │
│  n8n runs overnight → email alert at 00:00              │
│  Reviews flagged documents in Streamlit portal          │
└─────────────────────────┬───────────────────────────────┘
                          │ Human approves ✅
                          ▼
                  SHIPMENT DISPATCHED
```

---

## 📊 Performance

| Metric | Value |
|--------|-------|
| Response time | 0.44 seconds |
| Accuracy (LangSmith) | 90.7% |
| Human confidence rating | 8.7 / 10 before every decision |
| Hallucination rate | 1.2% |
| Test scenarios | 50 |

---

## ⚖️ EU AI Act — Limited Risk (Article 52)

- **Classification:** Limited Risk — not High Risk because the AI never makes autonomous decisions
- **Transparency:** Users are always informed they are interacting with an AI system
- **Human in the Loop:** Every flagged document is reviewed by a human before dispatch. The AI recommends — the human decides. Always.
- **Audit Trail:** Every AI decision logged in LangSmith with full traceability
- **No prohibited practices:** System does not use manipulation, social scoring, or biometric identification

---

## 🌿 Green Tech

- **Serverless deployment** — Streamlit Cloud, no always-on servers
- **Off-peak processing** — n8n workflow runs at midnight on low-demand energy
- **GPT-4o efficiency** — single API call per compliance check, no redundant processing
- **80% fewer customs holds** → less trucks idling at borders → less CO₂ emissions
- **Paper reduction** — AI automation replaces manual document printing and re-checking

---

## 🔒 GDPR Compliance

- **Legal basis:** Article 6(1)(b) — processing necessary for contract performance
- **Data minimisation:** Only shipment data collected (HS codes, EORI, goods description)
- **No personal data stored** beyond the session
- **Third-party transfers:** OpenAI API covered by EU Data Processing Agreement
- **EU servers:** Frankfurt region

---

## 📜 Regulations Covered

| Regulation | Scope | Status |
|-----------|-------|--------|
| ADR 2023 | Road dangerous goods | ✅ |
| IMDG Code | Sea dangerous goods | ✅ |
| IATA DGR | Air dangerous goods | ✅ |
| EU UCC | Customs clearance | ✅ |
| CMR Convention | Road freight documents | ✅ |
| EUR.1 / REX | Preferential tariffs | ✅ |

**Routes:** DE→CH · DE→GB · DE→US · DE→CN · DE→FR · DE→PL · DE→TR

---




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

## 👤 Author

**Kinda Faisal** — 6 years logistics & supply chain operations experience
GitHub: [kindafaisal-ui](https://github.com/kindafaisal-ui)
