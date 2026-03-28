# ShipmentDoc Compliance AI
### Dangerous Goods & Customs Clearance Automation

**Consultant:** Kinda Faisal — Freelance AI Consultant  
**Client:** Medium German Freight Forwarder (50–200 employees)  
**Live Demo:** [Open Portal](https://final-project-dg-customs-compliance-6bqksxcg6fzuf9vvjx2czt.streamlit.app/)  
**Built in:** 2 days as a Proof of Concept  
**Bootcamp:** AI Consulting Bootcamp — Final Project — Week 9

---

## The Story

I met Chleo at a dinner. She runs a medium-sized freight forwarding company in Germany and her team spends 9–12 minutes manually checking every shipment document for compliance with international Dangerous Goods and Customs regulations.

She told me: *"I am scared of AI — I don't trust it."*

Two days later I came back with this.

---

## What Problem Does This Solve?

Every international shipment must comply with strict regulations before goods can cross borders:

- **ADR 2023** — Dangerous Goods by road
- **IMDG Code** — Dangerous Goods by sea  
- **IATA DGR** — Dangerous Goods by air
- **EU Customs Code (UCC)** — Export declarations, HS codes, EORI numbers

Missing a tunnel restriction code, using a 6-digit instead of 8-digit HS code, or having the wrong EORI format can cause fines up to **€50,000 per violation** and customs holds of **1–2 days at the border**.

The current process: **9–12 minutes per document, manually, with a 5–10% error rate.**

---

## What Does This System Do?

The AI reads shipment document data, checks it against international compliance rules, and tells the operations team exactly what is wrong and what to do — in plain language, in 44 seconds.

**The final decision always stays with the human.** The AI flags issues. The human approves or acts.

---

## Results

| Metric | Before | After | Improvement |
|---|---|---|---|
| Processing time | 603 seconds | 44 seconds | 93% faster |
| Error rate | 5–10% | 1.2% | 94% reduction |
| AI confidence | — | 90.7% | — |
| Annual savings | — | €80,000+ | ROI: 1,589% |
| AI quality score | — | 8.7/10 | LLM-as-judge |

---

## System Components

| Component | Technology | Purpose |
|---|---|---|
| AI Agent | LangChain + GPT-3.5-Turbo | DG and customs compliance checking |
| Compliance Portal | Streamlit | Operations staff daily workspace |
| Automation | n8n Cloud | Scheduled email alerts + webhook |
| Monitoring | LangSmith EU | Full AI decision transparency |
| Evaluation | LLM-as-Judge | Quality assurance — 8.7/10 |
| Dataset | 500 synthetic documents | 7 document types × 10 routes |

---

## Repository Structure

```
final-project-kinda-faisal/
├── use_case_definition.md + .pdf
├── poc/
│   ├── poc_workflow.json
│   └── poc_documentation.md + .pdf
├── roi_risk_assessment.md + .pdf
├── compliance/
│   ├── eu_ai_act_compliance.md + .pdf
│   └── gdpr_documentation.md + .pdf
├── strategic_plan.md + .pdf
├── presentation.pptx
├── mvp/
│   ├── dashboard_app.py
│   ├── main.py
│   ├── generate_dataset.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── agent/langchain_agent.py
│   ├── data/raw/shipments.csv
│   └── mvp_documentation.md + .pdf
└── README.md
```

---

## EU AI Act Classification

**LIMITED RISK** — The system is a decision-support tool, not an autonomous decision-maker.

- Used by a **private company** — not by customs authorities or border control
- **Human-in-the-loop** — every flagged document reviewed before dispatch
- Based on **internationally defined rules** — not discretionary AI judgement
- Full **LangSmith audit trail** — every AI decision is traceable

---

## GDPR Compliance

Personal data processed: shipper name/address, consignee name/address, driver name, emergency contact, EORI number.

- **Legal basis:** Contract performance + legal obligation (EU UCC, ADR 2023)
- **Data location:** EU servers only — LangSmith Frankfurt endpoint
- **Retention:** 90 days for results, 30 days for AI traces
- **POC data:** Synthetic only — no real personal data used

---

## Green Technology

- GPT-3.5-Turbo not GPT-4 — **10× less energy** per API call
- EU servers — **higher renewable energy** mix
- Off-peak processing — n8n runs at midnight
- 80% fewer customs holds — **less trucks idling = less CO₂**

---

## How to Run

```bash
git clone https://github.com/kindafaisal-ui/final-project-dg-customs-compliance.git
cd final-project-dg-customs-compliance/mvp
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # Add your API keys
python generate_dataset.py
python main.py
streamlit run dashboard_app.py
```

Open browser at: **http://localhost:8501**

---

## Live Systems

| System | Purpose |
|---|---|
| [Compliance Portal](https://final-project-dg-customs-compliance-6bqksxcg6fzuf9vvjx2czt.streamlit.app/) | Operations staff daily workspace |
| [LangSmith](https://eu.smith.langchain.com) | AI decision audit trail |
| [n8n](https://kinda5.app.n8n.cloud) | Automation workflow |
| [Tableau](https://dub01.online.tableau.com) | KPI dashboard |

---

## About the Consultant

**Kinda Faisal** is a freelance AI consultant with 6 years of hands-on experience in international logistics. After completing an AI Consulting Bootcamp, she combines deep domain expertise with practical AI implementation skills — building solutions that are transparent, affordable, and specifically designed for the freight industry.

*"I don't just use AI. I build AI that logistics professionals can actually trust."*

---

*Final Project — AI Consulting Bootcamp — Week 9 — 2026*