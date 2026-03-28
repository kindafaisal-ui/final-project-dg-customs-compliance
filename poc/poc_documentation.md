# POC Documentation
## ShipmentDoc Compliance AI — No-Code / Low-Code Proof of Concept

**Consultant:** Kinda Faisal — Freelance AI Consultant
**POC Tool:** n8n Cloud
**Date:** March 2026

---

## 1. Overview

This document describes the No-Code / Low-Code Proof of Concept (POC) built to demonstrate that AI-powered DG and Customs compliance checking is technically feasible and practically useful for a medium-sized German freight forwarder.

The POC uses **n8n** as the primary automation tool, connected to an OpenAI language model, Google Sheets as a data source, and Gmail for alert delivery. It demonstrates the complete workflow from document data input to compliance decision to human notification — without requiring any manual intervention.

---

## 2. Tools Used and Why

| Tool | Purpose | Why chosen |
|---|---|---|
| **n8n Cloud** | Workflow automation — connects all components | No-code, visual, supports AI agents, webhook triggers, free trial available |
| **OpenAI GPT-3.5-Turbo** | AI compliance checking and plain-language explanations | Reliable, cost-effective, good at structured text analysis |
| **Google Sheets** | Shipment document data source | Simple, accessible, no database setup required for POC |
| **Gmail** | Daily compliance email alert | Free, widely used, easy to configure in n8n |
| **LangSmith** | AI decision tracing and transparency | Addresses client's concern about AI being a black box |

---

## 3. POC Workflow — Step by Step

### Trigger Options
The workflow supports three trigger methods:

**Trigger 1 — Schedule (midnight automatic)**
Runs automatically every night at 00:00. Operations team receives the compliance report when they arrive in the morning.

**Trigger 2 — Webhook (from Python pipeline)**
Triggered by `python main.py` — allows on-demand compliance checking during the day.

**Trigger 3 — Manual (Execute workflow button)**
Used for testing and demonstrations — click the button in n8n to run the full workflow immediately.

### Workflow Steps

**Step 1 — Get row(s) in sheet**
The workflow reads shipment document data from Google Sheets. Each row contains: doc_id, doc_type, route, UN number, DG class, compliance status, error details.

**Step 2 — Compliance Logic Engine (AI Agent)**
The OpenAI GPT-3.5-Turbo model receives the shipment data and a structured system prompt. It checks the document against applicable regulations and produces a compliance assessment with:
- DG compliance status (COMPLIANT / NON-COMPLIANT)
- Customs compliance status (COMPLIANT / REVIEW REQUIRED)
- Specific violation details in plain language
- One clear action sentence for the operations team

**Step 3 — Automated Emergency Alert (Gmail)**
If compliance issues are found, Gmail sends a consolidated daily report to the operations team and management. The email contains all flagged shipments in one message — not one email per document.

**Step 4 — Update row in sheet**
The compliance result is written back to Google Sheets, creating a running log of all compliance checks performed.

### Email Format
```
⚠️ Daily Compliance Report — [Date]

[X] shipments require attention today:

🚨 DOC-5000 — DE→CH — DG Declaration (IATA)
   Issue: Packing instruction not verified for UN2891
   Action: Contact carrier to complete IATA declaration before booking flight

⚠️ DOC-5001 — DE→CN — Customs Export Declaration
   Issue: HS code must be 8-digit, EORI format incorrect
   Action: Correct export declaration before customs submission

✅ DOC-5002 — DE→FR — Compliant. No action required.

---
ShipmentDoc AI · Kinda Faisal AI Consulting
```

---

## 4. AI Capability Demonstrated

The POC demonstrates the following AI capabilities:

**1. Structured compliance reasoning**
The AI applies rule-based logic to check documents against specific regulation articles (ADR 2023, IMDG Code, IATA DGR, EU UCC) — going beyond simple keyword matching.

**2. Route-specific intelligence**
The AI understands that different routes require different documents — DE→TR requires EUR.1, DE→GB requires post-Brexit declarations, DE→CH requires alpine tunnel codes.

**3. Plain-language generation**
The AI translates technical regulation violations into simple, actionable messages that non-technical operations staff can understand and act on immediately.

**4. Transparency via LangSmith**
Every AI decision is automatically traced in LangSmith — input, output, reasoning, latency, and confidence. This addresses the client's core concern about AI transparency.

---

## 5. Demo Recording

A 2–5 minute screen recording demonstrating the full POC workflow is available at:

**[Link to demo recording — to be added after recording]**

The recording shows:
1. The Streamlit compliance portal — clicking "Start Analysis"
2. n8n workflow executing — all nodes turning green
3. Gmail inbox — consolidated compliance email arriving
4. LangSmith traces — full audit trail of AI decisions
5. Tableau dashboard — KPI overview

---

## 6. Known Limitations of the POC vs. Production System

| Limitation | POC | Production |
|---|---|---|
| Data source | Google Sheets (manual entry) | Live TMS / ERP integration |
| Document types | 7 synthetic document types | All document types per client |
| Regulation updates | Manual prompt updates | Scheduled regulation monitoring |
| Scale | 5 documents per run | 300+ documents per day |
| Authentication | No user login | SSO / role-based access |
| Error handling | Basic try/except | Full error recovery and alerting |
| Expert validation | Not validated by legal expert | International law expert review required |
| Uptime | No SLA | 99.9% uptime SLA |
| Data privacy | Synthetic data only | Full GDPR compliance required |

---

## 7. How to Reproduce / Run the POC

### Prerequisites
- n8n Cloud account (https://app.n8n.cloud)
- OpenAI API key
- Google Sheets with shipment data
- Gmail account connected to n8n

### Steps
1. Import `poc_workflow.json` into n8n (Menu → Import workflow)
2. Connect credentials: OpenAI API key, Google Sheets OAuth, Gmail OAuth
3. Update the Google Sheets node with your sheet ID
4. Click "Execute workflow" to run manually
5. Check Gmail for the compliance report

### Python Pipeline (MVP)
For the full system with Streamlit portal:
```bash
cd mvp/
pip install -r requirements.txt
cp .env.example .env  # Add your API keys
python generate_dataset.py
streamlit run dashboard_app.py
```

---

*Document prepared by: Kinda Faisal — Freelance AI Consultant | AI Consulting Bootcamp — Week 9 | 2026*
