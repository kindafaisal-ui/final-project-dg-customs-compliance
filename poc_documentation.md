# POC Documentation — ShipmentDoc Compliance AI

**Project:** ShipmentDoc Compliance AI — Dangerous Goods & Customs Clearance  
**Author:** Kinda Faisal  
**Date:** April 2026  
**Status:** POC Complete · Deployed

---

## 1. POC Overview

Demonstrates that AI can automate compliance checking for international shipments covering both dangerous goods and customs documentation. Two AI agents serve two user groups in the logistics workflow.

**Objective:** Reduce time operations staff spend on manual document checking from 70–80% of their working day to under 5 minutes per shipment.

---

## Demo Recording

**Video:** https://YOUR-VIDEO-LINK-HERE

## 2. Live Portals

| Portal | URL |
|--------|-----|
| Shipper Portal (Agent 2) | https://final-project-dg-customs-compliance-3djmsuecztvsuux7jgpyai.streamlit.app/ |
| Freight Forwarder Portal (Agent 1) | https://final-project-dg-customs-compliance-mffpsnzkusr6pmhcb6e8xv.streamlit.app/ |

---

## 3. Agent Architecture

### Agent 1 — Freight Forwarder Portal
**Tech:** n8n + OpenAI GPT-4o + Streamlit

**Pipeline:**
1. Webhook trigger receives form submission
2. Input parser extracts route, goods, transport mode, DG class, HS code, EORI
3. Regulation selector determines applicable rules (ADR/IMDG/IATA + customs per route)
4. OpenAI GPT-4o call generates structured compliance checklist
5. Pre-validation runs before AI call for instant error feedback
6. Response formatted and returned to Streamlit UI

### Agent 2 — Shipper Portal
**Tech:** Python (shipper_agent.py) + OpenAI GPT-4o + Streamlit

**Pipeline:**
1. Streamlit 3-column UI collects: shipment details | customs info | dangerous goods
2. Input validator checks HS code length, EORI format, UN number format
3. shipper_agent.py builds structured prompt with all inputs
4. OpenAI GPT-4o returns 4-section checklist
5. UI renders: validation errors, required customs docs, route notes, full checklist

---

## 4. Regulations Covered

| Regulation | Scope |
|-----------|-------|
| ADR 2023 | Road dangerous goods transport |
| IMDG Code | Sea dangerous goods transport |
| IATA DGR | Air dangerous goods transport |
| EU UCC | Customs clearance, HS codes, EORI |
| CMR Convention | Road freight documentation |
| EUR.1 / REX | Preferential tariff certificates |

**Routes supported:** DE→CH, DE→GB, DE→US, DE→CN, DE→FR, DE→PL, DE→TR

---

## 5. Performance Results (LangSmith)

| Metric | Result |
|--------|--------|
| Accuracy | 90.7% |
| Average response time | 0.44 seconds |
| Human confidence rating | 8.7 / 10 |
| Hallucination rate | 1.2% |
| Test scenarios | 50 |

---

## 6. Pre-Validation System

Both portals include instant pre-validation before the AI call:
- HS code must be exactly 8 digits (EU standard)
- EORI number must start with DE (German exporters)
- UN number must follow UNxxxx format
- Goods description must not be empty

---

## 7. EU AI Act & GDPR

- **EU AI Act:** Limited Risk (Article 52) — transparency obligation met, human in the loop
- **GDPR:** Article 6(1)(b) — contract performance. No personal data stored beyond session.

---

## 8. Repository

https://github.com/kindafaisal-ui/final-project-dg-customs-compliance

**Structure:**
```
├── shipper/
│   ├── shipper_portal.py
│   ├── shipper_agent.py
│   └── requirements.txt
├── compliance/
│   ├── eu_ai_act_compliance.md / .pdf
│   └── gdpr_documentation.md / .pdf
├── poc_documentation.md
├── README.md
├── use_case_definition.md
├── strategic_plan.md
├── roi_risk_assessment.md
└── .env.example
```
