# MVP Documentation
## ShipmentDoc Compliance AI — Working Application

**Consultant:** Kinda Faisal — Freelance AI Consultant
**MVP Type:** Python + Streamlit + LangChain + n8n
**Live URL:** https://final-project-dg-customs-compliance-6bqksxcg6fzuf9vvjx2czt.streamlit.app/
**GitHub:** https://github.com/kindafaisal-ui/final-project-dg-customs-compliance
**Date:** March 2026

---

## 1. What is the MVP?

The MVP (Minimum Viable Product) extends the n8n POC into a fully functional web application that operations staff and management can use every day. It demonstrates the complete AI compliance automation system — from document analysis to user interface to automated alerts.

**The MVP includes:**
- **Streamlit compliance portal** — web interface for operations staff
- **LangChain AI agent** — automated DG and customs compliance checking
- **n8n automation workflow** — scheduled and on-demand email alerts
- **LangSmith monitoring** — full AI decision transparency
- **Evaluation system** — LLM-as-judge quality assessment (8.7/10)

---

## 2. Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    USER INTERFACES                       │
│  Streamlit Portal          Gmail (management alerts)    │
│  (operations staff)        (Chleo + managers)           │
└──────────────┬──────────────────────────┬───────────────┘
               │                          │
               ▼                          ▼
┌─────────────────────────┐  ┌────────────────────────┐
│    ORCHESTRATOR          │  │   AUTOMATION LAYER     │
│    main.py               │  │   n8n Cloud Workflow   │
│    - Load dataset         │  │   - Schedule trigger   │
│    - Run AI agent         │  │   - Webhook trigger    │
│    - Save results         │  │   - Manual trigger     │
│    - Trigger n8n          │  │   - AI agent node      │
│    - Generate insights    │  │   - Gmail send         │
└──────────┬──────────────┘  └────────────────────────┘
           │
           ▼
┌─────────────────────────┐
│      AI AGENT LAYER     │
│   langchain_agent.py    │
│   - check_dg_compliance │
│   - check_customs        │
│   - get_document_stats  │
│   LLM: GPT-3.5-Turbo    │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐  ┌────────────────────────┐
│      DATA LAYER         │  │   MONITORING LAYER     │
│   shipments.csv         │  │   LangSmith EU         │
│   (500 test documents)  │  │   - All AI traces      │
│   compliance_results/   │  │   - Confidence scores  │
│   (processed results)   │  │   - Latency metrics    │
└─────────────────────────┘  └────────────────────────┘
```

---

## 3. Component Descriptions

### dashboard_app.py — Streamlit Compliance Portal
The main user interface for operations staff. Reads compliance results from the latest CSV file and displays them with full violation details, customs issues, and plain-language action messages.

**Features:**
- KPI cards (500 docs, 90.7% confidence, 44s processing, 1.2% error rate, €80K savings)
- "Start Analysis" button — triggers full compliance check
- Document results with DG and customs violations separated
- Plain-language action message per document
- Links to LangSmith, Tableau, and n8n
- Business impact panel (83h/day saved, €90K fine risk avoided)

### main.py — System Orchestrator
Connects all components and runs the full pipeline with one command.

**Steps:**
1. Load 500-document dataset from `data/raw/shipments.csv`
2. Run LangChain AI agent on 5 representative documents (3 DG + 2 Customs)
3. Save results to `data/processed/compliance_results_[timestamp].csv`
4. Update LangSmith dataset with new examples
5. Generate 5 business insights from full dataset
6. Trigger n8n webhook — sends email alert

### agent/langchain_agent.py — LangChain Compliance Agent
The core AI component. Uses LangChain with three specialized tools:

| Tool | Function |
|---|---|
| `check_dg_compliance` | Validates DG documents against ADR 2023, IMDG, IATA DGR with specific article references |
| `check_customs_compliance` | Validates customs documents against EU UCC, CMR, EUR.1 with route-specific rules |
| `get_document_stats` | Returns dataset statistics for insight generation |

### evaluation/evaluation.py — LLM-as-Judge
A second GPT-3.5-Turbo instance evaluates the quality of AI-generated insights on 4 criteria:
- Relevance: 9.1/10
- Accuracy: 9.3/10
- Actionability: 8.1/10
- Clarity: 8.9/10
- **Overall: 8.7/10**

---

## 4. Setup and Installation

### Prerequisites
- Python 3.13+
- OpenAI API key (https://platform.openai.com)
- LangSmith API key (https://smith.langchain.com)
- n8n Cloud account (optional — for automation)

### Installation Steps

**Step 1 — Clone the repository:**
```bash
git clone https://github.com/kindafaisal-ui/final-project-dg-customs-compliance.git
cd final-project-dg-customs-compliance
```

**Step 2 — Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
# or: venv\Scripts\activate  # Windows
```

**Step 3 — Install dependencies:**
```bash
pip install -r mvp/requirements.txt
```

**Step 4 — Configure API keys:**
```bash
cp mvp/.env.example mvp/.env
# Edit mvp/.env and add your API keys
```

**Step 5 — Generate dataset:**
```bash
cd mvp
python generate_dataset.py
```

**Step 6 — Run full system:**
```bash
python main.py
```

**Step 7 — Run compliance portal:**
```bash
streamlit run dashboard_app.py
```

Open browser at: http://localhost:8501

---

## 5. How to Run

### Option A — Full Pipeline (Recommended)
```bash
cd mvp
source ../venv/bin/activate
python main.py
```
This runs all 6 components: dataset → AI agent → save results → LangSmith → insights → n8n webhook

### Option B — Portal Only
```bash
cd mvp
streamlit run dashboard_app.py
```
Opens the compliance portal. Click "Start Analysis" to trigger the full pipeline from the UI.

### Option C — Evaluation Only
```bash
cd mvp
python evaluation/evaluation.py
```
Runs LLM-as-judge evaluation on AI-generated insights.

---

## 6. Known Limitations

| Limitation | Impact | Production Resolution |
|---|---|---|
| Synthetic dataset (500 records) | Not real shipment data | Connect to client TMS in Phase 2 |
| No user authentication | Anyone with URL can access | Implement SSO in Phase 3 |
| Regulation rules hardcoded in prompts | Need manual update when rules change | Automated regulation monitoring in Phase 3 |
| No international law expert validation | Accuracy not legally verified | Law expert review in Phase 2 |
| 5 documents analyzed per run | Not full 500 | Scale to full volume in Phase 2 |
| No real-time data | Results from CSV files | Live TMS integration in Phase 3 |
| English only | German operations staff may prefer German UI | German language support in Phase 4 |
| No incident response | System fails gracefully but no alerting | Implement PagerDuty/alerting in Phase 3 |

---

## 7. How the MVP Extends the POC

| Feature | POC (n8n only) | MVP (Full system) |
|---|---|---|
| Trigger | Schedule + webhook | Schedule + webhook + manual + Streamlit button |
| Interface | Email only | Email + Streamlit compliance portal |
| Violation detail | Short summary | Full regulation article + plain-language action |
| Monitoring | Basic n8n logs | Full LangSmith audit trail |
| Quality assurance | None | LLM-as-judge evaluation (8.7/10) |
| Accessibility | Email inbox | Public URL — any device, anywhere |
| Business insights | None | 5 AI-generated business insights per run |
| Deployment | Local only | Live on Streamlit Cloud |

---

## 8. Live Demo

**Public URL:** https://final-project-dg-customs-compliance-6bqksxcg6fzuf9vvjx2czt.streamlit.app/

The live demo shows:
- Real compliance results from the AI agent
- Full violation details per document
- Plain-language action messages
- Business impact metrics
- Links to LangSmith, Tableau, and n8n

**Note:** The live demo uses synthetic data. Real shipment data would be connected via TMS integration in Phase 2.

---

*Document prepared by: Kinda Faisal — Freelance AI Consultant | AI Consulting Bootcamp — Week 9 | 2026*