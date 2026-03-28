# Use Case Definition
## ShipmentDoc Compliance AI — Dangerous Goods & Customs Clearance Automation

**Consultant:** Kinda Faisal — Freelance AI Consultant
**Client:** Chleo — CEO, Medium German Freight Forwarder (50–200 employees)
**Date:** March 2026
**Industry:** Logistics / Supply Chain

---

## 1. Business Problem Statement

A medium-sized German freight forwarder processes 50–300 international shipments daily. Each shipment generates multiple compliance-critical documents — Dangerous Goods (DG) declarations and Customs Clearance paperwork — that must comply with strict international regulations before goods can cross borders.

Currently, operations staff spend 9–12 minutes manually checking each document against ADR, IMDG, IATA, and EU Customs regulations. This manual process leads to:

- **Compliance errors** on 5–10% of documents — causing ADR fines of up to €50,000 per violation
- **Customs holds** of 1–2 days at borders due to missing HS codes, EORI numbers, or EUR.1 certificates
- **83+ hours of staff time** lost daily to manual document checking
- **Staff frustration** and high error rates under time pressure

The client, Chleo, approached the consultant with a specific concern: *"I am scared of AI — I don't trust it. I need to see exactly what it's doing and why."* This transparency requirement is central to the solution design.

---

## 2. Company Profile

| Field | Details |
|---|---|
| Industry | International logistics / freight forwarding |
| Company size | Medium — 50–200 employees |
| Location | Germany |
| Current state | Manual document processing, no AI tools in use |
| Daily volume | 50–300 international shipments per day |
| Key routes | DE→TR · DE→GB · DE→US · DE→CN · DE→CH · DE→FR · DE→JP · DE→PL · DE→NL · DE→IT |
| Regulation exposure | ADR 2023 · IMDG Code · IATA DGR · EU UCC · CMR Convention · EUR.1 |
| Main pain point | 9–12 min per document manually, 5–10% error rate, €50,000+ fine exposure |

---

## 3. Jobs-To-Be-Done (JTBD)

### Functional
Operations staff need to identify missing or incorrect information in DG and customs documents **before shipments are dispatched** — reducing errors, fines, and customs delays.

### Emotional
Staff want to feel **confident and in control** when approving shipments. They want to start each day knowing which documents need attention, rather than discovering problems at the border.

### Social
Chleo wants the company to be seen as a **modern, reliable, tech-forward freight forwarder** — one that uses AI responsibly and transparently, not as a black box.

---

## 4. Proposed AI Solution

**ShipmentDoc Compliance AI** is a decision-support system that automatically checks shipment documents against international compliance rules and presents findings to human operators in a structured, actionable format.

**Type of AI system:** Automation + Natural Language Generation (rule-based compliance checking enhanced by LLM for plain-language explanations)

**What the AI does:**
- Reads shipment document data (document type, route, UN number, DG class, HS code, EORI)
- Checks each document against the applicable regulations (ADR/IMDG/IATA for DG, EU UCC/CMR/EUR.1 for customs)
- Identifies missing or incorrect fields
- Generates a plain-language explanation of each violation
- Suggests a specific action for the operations team
- Sends a consolidated daily compliance report to management via email
- Displays all findings in a web portal for the operations team

**What the AI does NOT do:**
- Approve or reject shipments autonomously
- Make legal compliance decisions
- Replace a qualified compliance officer
- Guarantee regulatory compliance (human review is always required)

---

## 5. Key Stakeholders

| Stakeholder | Role | Interest | When involved |
|---|---|---|---|
| Chleo (CEO) | Decision maker | ROI, transparency, liability | Daily email summary |
| Operations staff | Daily users | Ease of use, accuracy, speed | Morning portal check |
| Compliance officer | Reviewer | Regulatory accuracy, audit trail | Flagged document review |
| IT manager | Technical owner | System reliability, integrations | Setup and maintenance |
| Carriers (DHL, Kuehne+Nagel etc.) | External | Correct documentation | When corrections needed |
| Customs authorities | Regulatory | Legal compliance | At border crossing |
| Legal counsel | Risk management | Liability, GDPR, EU AI Act | Before production deployment |
| International law expert | Validation | Regulatory accuracy | Pilot phase validation |

---

## 6. Success Criteria

### Measurable Outcome 1 — Error Rate Reduction
**Target:** Reduce compliance document error rate from 5–10% to below 2%
**Measurement:** Compare flagged document rate before and after system deployment over 90 days
**Current baseline:** 5–10% industry average error rate
**Our POC result:** 1.2% error rate on 500-document test dataset

### Measurable Outcome 2 — Processing Time Reduction
**Target:** Reduce average document processing time from 9–12 minutes to under 60 seconds
**Measurement:** Time from document entry to compliance decision
**Current baseline:** 603 seconds average manual processing time
**Our POC result:** 44 seconds average AI processing time (93% reduction)

### Additional Success Indicators
- Zero missed ADR violations causing fines during pilot phase
- 100% of flagged documents reviewed by human before dispatch
- Operations staff satisfaction score above 7/10 after 30 days
- Management email report opened and actioned every morning

---

## 7. Out-of-Scope Boundaries

The following are explicitly **not** in scope for this solution:

| Out of scope | Reason |
|---|---|
| Autonomous shipment approval | Human oversight is mandatory — legal liability |
| Real-time TMS integration | Requires enterprise API access — Phase 3+ |
| Carrier API connections | Third-party dependency — Phase 3+ |
| Legal compliance guarantee | AI is a support tool, not a legal authority |
| Driver training or certification | Operational HR matter, not a software problem |
| Financial auditing or invoicing | Different system, different compliance domain |
| Customs authority submission | Requires licensed customs broker |
| Non-German routes (non-EU origin) | Out of scope for initial deployment |
| Languages other than German/English | Phase 2 expansion |

---

## 8. MoSCoW Feature Prioritization

| Priority | Feature | Justification |
|---|---|---|
| **Must** | DG compliance check (ADR/IMDG/IATA) | Core legal requirement — prevents fines |
| **Must** | Customs compliance check (UCC/CMR/EUR.1) | Core legal requirement — prevents holds |
| **Must** | LangSmith audit trail | Addresses client transparency concern |
| **Must** | Human-in-the-loop design | EU AI Act Limited Risk requirement |
| **Should** | Consolidated daily email alert | Management oversight — Chleo's overview |
| **Should** | Streamlit compliance portal | Operations staff daily workspace |
| **Should** | Plain-language action messages | Non-technical staff usability |
| **Could** | Tableau KPI dashboard | Management statistics — nice to have |
| **Could** | LLM-as-judge evaluation | Quality assurance — bonus feature |
| **Could** | Streamlit Cloud deployment | Accessibility — bonus feature |
| **Won't** | Autonomous approval | Out of scope — legal liability |
| **Won't** | Real-time TMS integration | Phase 3 — requires enterprise access |

---

## 9. Validation Summary

| Validation Type | Confidence | Evidence |
|---|---|---|
| Market | High | McKinsey: 20% logistics cost reduction with AI · IATA: $6.7T air cargo market · EU: 50% faster customs with automation |
| User | Medium | 6 years direct logistics industry experience — formal user interviews planned for pilot phase |
| Competitive | High | No affordable combined DG+Customs AI solution exists for SME German freight forwarders |
| Feasibility | High | Working POC built and deployed in 2 days — Streamlit portal live at public URL |

*Note on user validation gap: Formal user interviews with operations staff were not conducted before the POC. This is a known limitation. The pilot phase (Phase 2) includes a structured feedback program with 5 operations staff members to validate assumptions.*

---

*Document prepared by: Kinda Faisal — Freelance AI Consultant | AI Consulting Bootcamp — Week 9 | 2026*