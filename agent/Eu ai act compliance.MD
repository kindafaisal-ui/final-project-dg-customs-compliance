# EU AI Act Compliance Documentation
## ShipmentDoc Compliance AI — Risk Classification and Conformity Assessment

**Consultant:** Kinda Faisal — Freelance AI Consultant
**System:** ShipmentDoc Compliance AI
**Date:** March 2026
**EU AI Act Reference:** Regulation (EU) 2024/1689

---

## 1. Risk Classification

**Classification: LIMITED RISK**

The ShipmentDoc Compliance AI system is classified as **Limited Risk** under the EU AI Act (Article 50).

---

## 2. Classification Reasoning — Step by Step

### Step 1: Check for Unacceptable Risk (Article 5)
The system does NOT fall into any unacceptable risk category:
- ❌ Not a social scoring system
- ❌ Not biometric identification
- ❌ Not subliminal manipulation
- ❌ Not used on vulnerable groups
- ❌ Not law enforcement or border control authority

**→ Not Unacceptable Risk. Continue to Step 2.**

### Step 2: Check for High Risk (Annex III)
High-risk AI systems include those used in:
- Critical infrastructure — ❌ Not applicable
- Education — ❌ Not applicable
- Employment decisions — ❌ Not applicable
- Essential services (credit, insurance) — ❌ Not applicable
- Law enforcement — ❌ Not applicable
- Migration and border control — ⚠️ **Potentially relevant — examined below**
- Administration of justice — ❌ Not applicable

**Border Control examination:**
The EU AI Act Annex III (6b) covers AI used by competent authorities for border control management. Our system is used by a **private freight company**, not by customs authorities or border control agencies. The system checks document completeness for an internal operations team — it does not interact with customs systems, does not make border crossing decisions, and is not used by government authorities.

Furthermore, Dangerous Goods and Customs Clearance operations follow strict international standards (ADR 2023, IMDG Code, IATA DGR, EU Customs Code) that define exactly what information is required on each document. The AI only checks whether this defined information is present or missing — it does not make discretionary judgements.

**→ Not High Risk. Continue to Step 3.**

### Step 3: Check for Limited Risk (Article 50)
Limited Risk applies to AI systems that interact with humans and where transparency obligations apply, including:
- AI systems that generate content
- AI systems that provide recommendations or assessments to humans

Our system **generates plain-language compliance assessments and recommendations** presented to human operators. This falls under Limited Risk transparency obligations.

**→ Classification confirmed: LIMITED RISK**

### Why not Minimal Risk?
Minimal Risk would apply if the system had no transparency obligations. Our system generates AI-produced compliance assessments that humans act upon — transparency about the AI nature of these outputs is required. Therefore Limited Risk (not Minimal Risk) is the correct classification.

---

## 3. Key Design Decision — Human-in-the-Loop

The most important design decision that keeps this system in Limited Risk territory is the **mandatory human-in-the-loop**:

> *"The system never makes a final compliance decision. Every flagged document is reviewed and approved by a qualified human before shipment dispatch. The AI is a first-line screening tool — not a compliance authority."*

This means:
- The AI **identifies** potential issues → Human **decides** what to do
- The AI **suggests** an action → Human **approves or overrides**
- The AI **explains** the violation → Human **verifies** and **acts**

---

## 4. Mandatory Requirements Summary (Limited Risk)

### 4.1 Transparency Obligations (Article 50)

| Requirement | How we address it |
|---|---|
| Users must know they are interacting with AI | Portal clearly states "AI-generated compliance assessment" on every result |
| AI-generated content must be marked | All compliance reports include "Processed by ShipmentDoc AI" footer |
| Audit trail available | LangSmith traces every AI decision with full input/output/reasoning |

### 4.2 Data and Data Governance

| Requirement | How we address it |
|---|---|
| Training data quality | System uses rule-based compliance logic — not trained on personal shipment data |
| Data minimization | Only document metadata processed — not full document text |
| Data accuracy | Rules validated against official regulation texts (ADR 2023, IATA DGR 2024) |
| EU data residency | LangSmith EU endpoint — all data stays within EU borders |

### 4.3 Human Oversight Mechanisms

| Requirement | How we address it |
|---|---|
| Human can override AI | Every flagged document shows "Human review required" — no automatic dispatch |
| Human can stop the system | Operations manager can disable n8n workflow at any time |
| Human understands AI limitations | Training program includes AI limitations and error scenarios |
| Clear escalation path | Flagged documents escalated to compliance officer for final review |

### 4.4 Transparency and Information Obligations

| Requirement | How we address it |
|---|---|
| System purpose disclosed | README and portal clearly explain what the AI does and does not do |
| Limitations disclosed | POC documentation lists all known limitations |
| Contact information | Consultant contact details available for questions |

### 4.5 Accuracy and Robustness

| Requirement | How we address it |
|---|---|
| Performance monitoring | LangSmith monitors every decision — confidence scores tracked |
| Error handling | try/except throughout — system fails gracefully, never silently |
| Evaluation | LLM-as-judge evaluation achieves 8.7/10 average quality score |
| Bias monitoring | Evaluation checks for route-specific or document-type biases |

### 4.6 Cybersecurity

| Requirement | How we address it |
|---|---|
| API keys protected | .env files excluded from GitHub — .env.example provided |
| Data transmission | HTTPS only — all API calls encrypted |
| Access control | Streamlit portal — production would require SSO authentication |
| No real personal data in POC | Synthetic dataset only — GDPR risk minimized |

---

## 5. Conformity Assessment Summary

### System Description
ShipmentDoc Compliance AI is a decision-support tool that helps operations staff at a German freight forwarding company check shipment documents for compliance with international Dangerous Goods (DG) and Customs Clearance regulations. The system reads document metadata, applies rule-based compliance checks enhanced by a large language model, and presents findings to human operators in plain language with specific action recommendations.

### Risk Classification
**LIMITED RISK** under EU AI Act Regulation (EU) 2024/1689, Article 50.

**Basis for classification:**
1. Not used by competent authorities — used by a private company's internal operations team
2. Not making autonomous compliance decisions — human approval required for all flagged documents
3. Based on internationally defined regulatory rules — not discretionary AI judgement
4. Generates AI-produced assessments presented to humans — transparency obligations apply

### Applicable Obligations
| Obligation | Status |
|---|---|
| Transparency to users | ✅ Addressed — AI nature clearly disclosed in portal and reports |
| Audit trail | ✅ Addressed — LangSmith traces all decisions |
| Human oversight | ✅ Addressed — mandatory human review before dispatch |
| Data governance | ✅ Addressed — EU servers, no real personal data in POC |
| Performance monitoring | ✅ Addressed — LangSmith monitoring + LLM evaluation |

### Identified Gaps (to resolve before production deployment)

| Gap | Resolution Plan |
|---|---|
| Formal user authentication | Implement SSO before production — Phase 3 |
| International law expert validation | Engage logistics law expert during pilot — Phase 2 |
| Formal GDPR DPIA | Complete full DPIA before production — see gdpr_documentation.md |
| Regulation update process | Establish quarterly review protocol — Phase 2 |
| Incident response procedure | Define and document before production — Phase 3 |

---

## 6. Technical Documentation Outline

The following table of contents represents what a full technical documentation package would contain before production deployment:

```
1. System Overview
   1.1 Purpose and intended use
   1.2 System architecture diagram
   1.3 Component descriptions
   1.4 Data flow diagram

2. AI Model Documentation
   2.1 Model card — GPT-3.5-Turbo
   2.2 Prompt design and rationale
   2.3 Known limitations and failure modes
   2.4 Performance benchmarks

3. Compliance Rule Base
   3.1 ADR 2023 rules implemented
   3.2 IMDG Code rules implemented
   3.3 IATA DGR rules implemented
   3.4 EU UCC rules implemented
   3.5 CMR Convention rules implemented
   3.6 Route-specific rule matrix

4. Testing and Evaluation
   4.1 Test dataset description
   4.2 LLM-as-judge evaluation results
   4.3 Edge case testing
   4.4 Bias and fairness assessment

5. Human Oversight Procedures
   5.1 Flagged document review process
   5.2 Override and escalation procedures
   5.3 Staff training materials

6. Monitoring and Maintenance
   6.1 LangSmith monitoring setup
   6.2 Performance metrics and thresholds
   6.3 Regulation update procedure
   6.4 Incident response plan

7. Security and Privacy
   7.1 Data encryption standards
   7.2 Access control design
   7.3 GDPR compliance documentation
   7.4 Data retention and deletion policy

8. Deployment Documentation
   8.1 Infrastructure specifications
   8.2 Deployment procedure
   8.3 Rollback procedure
   8.4 Change management process
```

---

*Document prepared by: Kinda Faisal — Freelance AI Consultant | AI Consulting Bootcamp — Week 9 | 2026*
*Note: This document reflects the POC stage. A full conformity assessment by a qualified legal expert is required before production deployment.*