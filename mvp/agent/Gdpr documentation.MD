# GDPR Documentation
## ShipmentDoc Compliance AI — Data Privacy and Protection

**Consultant:** Kinda Faisal — Freelance AI Consultant
**System:** ShipmentDoc Compliance AI
**Date:** March 2026
**GDPR Reference:** Regulation (EU) 2016/679

---

## 1. Data Flow Map

The following describes all personal and business data that flows through the system:

### Data Flow Diagram (Table Format)

| Step | Data Type | From | To | Personal Data? |
|---|---|---|---|---|
| 1 | Shipment document metadata | Google Sheets / TMS | Python agent | Partially — EORI (company identifier) |
| 2 | Shipper name + address | Document | AI agent | ✅ Yes — personal data |
| 3 | Consignee name + address | Document | AI agent | ✅ Yes — personal data |
| 4 | Driver name | CMR waybill | AI agent | ✅ Yes — personal data |
| 5 | Emergency contact name + phone | ADR declaration | AI agent | ✅ Yes — personal data |
| 6 | EORI number | Export declaration | AI agent + LangSmith | ⚠️ Business identifier — linked to person/company |
| 7 | Product description + HS code | Commercial invoice | AI agent | Business data |
| 8 | Compliance assessment result | AI agent | CSV file + LangSmith | Derived data |
| 9 | Compliance report | AI agent | Gmail (email) | Summary only — no personal data |
| 10 | AI traces | LangSmith | LangSmith EU servers | Includes input data |

### Data Flow Summary
```
Shipment Documents
      ↓
Python AI Agent (local processing)
      ↓                    ↓
CSV Results          LangSmith EU
(local storage)      (audit trail)
      ↓                    ↓
Streamlit Portal     LangSmith Dashboard
(operations team)    (manager oversight)
      ↓
Gmail Alert
(management summary)
```

---

## 2. ROCA Framework

The ROCA framework defines how we handle data: **Retain · Obtain · Control · Archive/Delete**

### Retain — How long do we keep the data?

| Data Type | Retention Period | Justification |
|---|---|---|
| Shipment document metadata | 90 days | Compliance audit requirements |
| Compliance results (CSV) | 90 days | Operational reference |
| LangSmith AI traces | 30 days | Monitoring and debugging |
| Gmail compliance reports | 30 days | Management reference |
| Personal data (shipper/consignee) | Minimum necessary — deleted after compliance check | Data minimization principle |

**Auto-deletion policy:** The system will implement automatic deletion of processed CSV files after 90 days. Personal data fields (shipper name, consignee name, driver name, emergency contact) are not stored in result files — only document IDs and compliance outcomes are retained.

### Obtain — How do we collect the data?

| Data Source | Collection Method | Legal Basis |
|---|---|---|
| Shipment documents | Provided by client's TMS / Google Sheets | Contract performance (Article 6(1)(b)) |
| EORI numbers | From export declarations | Legal obligation (Article 6(1)(c)) — required by EU UCC |
| Shipper/consignee details | From CMR / commercial invoice | Legitimate interest (Article 6(1)(f)) — compliance checking |
| Driver details | From ADR transport document | Legal obligation (Article 6(1)(c)) — required by ADR 2023 |
| Emergency contact | From ADR declaration | Legal obligation (Article 6(1)(c)) — required by ADR 2023 |

### Control — Who has access and how is it protected?

| Access Level | Who | What they can see | Protection |
|---|---|---|---|
| Operations staff | Day-to-day users | Current compliance results only | Streamlit portal login (Phase 3: SSO) |
| Management (Chleo) | Overview | Daily email summary — no personal data | Gmail account security |
| IT administrator | Full system access | All data | Admin credentials, 2FA |
| AI consultant | Maintenance access | Logs and traces | LangSmith credentials |
| OpenAI | API processing | Document text sent in API call | OpenAI data processing agreement |
| LangSmith | Trace storage | All AI inputs/outputs | EU server, data processing agreement |

**Technical controls:**
- All API keys stored in `.env` files — never committed to GitHub
- HTTPS for all API communications
- LangSmith EU endpoint — data stays in EU
- No real personal data in POC — synthetic dataset only

### Archive/Delete — When and how do we delete data?

| Trigger | Action | Who is responsible |
|---|---|---|
| 90 days after compliance check | Auto-delete processed CSV files | Automated script (to be implemented in Phase 3) |
| 30 days after creation | LangSmith traces archived | LangSmith automatic retention policy |
| Data subject erasure request | Manual deletion within 30 days | IT administrator |
| End of contract | Full data deletion within 30 days | Consultant + IT administrator |
| System decommission | All data permanently deleted | IT administrator — confirmed in writing |

---

## 3. Processing Activities Register

### Activity 1 — DG Compliance Checking

| Field | Details |
|---|---|
| **What data** | Document type, UN number, DG class, route, carrier name |
| **Purpose** | Check dangerous goods document compliance against ADR/IMDG/IATA regulations |
| **Legal basis** | Legitimate interest (Article 6(1)(f)) — preventing fines and safety incidents |
| **Retention period** | 90 days |
| **Third-party recipients** | OpenAI API (processing), LangSmith EU (monitoring) |
| **Personal data involved** | Minimal — carrier name only |

### Activity 2 — Customs Compliance Checking

| Field | Details |
|---|---|
| **What data** | Document type, route, EORI number, HS code, Incoterms, country of origin |
| **Purpose** | Check customs documentation compliance against EU UCC, CMR, EUR.1 requirements |
| **Legal basis** | Legal obligation (Article 6(1)(c)) — EU customs law compliance |
| **Retention period** | 90 days |
| **Third-party recipients** | OpenAI API (processing), LangSmith EU (monitoring) |
| **Personal data involved** | EORI number (company/person identifier) |

### Activity 3 — Compliance Report Generation and Distribution

| Field | Details |
|---|---|
| **What data** | Compliance outcomes, flagged document IDs, action recommendations |
| **Purpose** | Notify management and operations team of compliance issues |
| **Legal basis** | Legitimate interest (Article 6(1)(f)) — business operations |
| **Retention period** | 30 days (email) |
| **Third-party recipients** | Gmail / Google (email delivery) |
| **Personal data involved** | None — reports contain document IDs and compliance outcomes only |

### Activity 4 — AI Decision Logging (LangSmith)

| Field | Details |
|---|---|
| **What data** | Full AI input/output traces including document data sent to AI |
| **Purpose** | Transparency, audit trail, monitoring, debugging |
| **Legal basis** | Legitimate interest (Article 6(1)(f)) — system transparency and accountability |
| **Retention period** | 30 days |
| **Third-party recipients** | LangSmith (Langchain Inc.) — EU endpoint |
| **Personal data involved** | Potentially — if document data includes personal identifiers |

---

## 4. Data Protection Impact Assessment (DPIA)

### Highest-Risk Activity: AI Processing of Shipment Documents via OpenAI API

#### 4.1 Description of the Processing
Shipment document metadata — including potentially personal data such as shipper names, consignee addresses, driver names, and EORI numbers — is sent to the OpenAI API for compliance analysis. This data leaves the client's internal systems and is processed by a US-based third-party AI provider.

#### 4.2 Necessity and Proportionality Assessment

**Is this processing necessary?**
Yes. The compliance checking capability requires an AI language model to interpret regulatory requirements and generate plain-language explanations. This cannot be achieved with simple rule-based systems alone.

**Is the scope proportionate?**
Partially. In the POC, only document metadata is sent to the API — not full document text. In production, data minimization should be further enforced by stripping personal identifiers before API calls where possible.

**Could the same purpose be achieved with less data?**
In some cases yes — for example, shipper/consignee names are not needed to check HS code validity. A production version should anonymize personal identifiers before sending to the API.

#### 4.3 Risks to Data Subjects

| Risk | Likelihood | Severity | Risk Level |
|---|---|---|---|
| Personal data sent to US-based AI provider | Medium | Medium | **Medium** |
| Data retained by OpenAI for model training | Low | High | **Medium** |
| Unauthorized access to LangSmith traces | Low | Medium | **Low** |
| Data subject unaware their data is processed | Medium | Low | **Low** |
| Inaccurate AI output affecting shipment | Medium | High | **Medium** |

#### 4.4 Mitigation Measures

| Risk | Mitigation |
|---|---|
| Data sent to OpenAI | OpenAI data processing agreement in place · Zero Data Retention option available for API |
| OpenAI training | API data not used for model training by default (per OpenAI API policy) |
| LangSmith access | EU endpoint · Access restricted to consultant and IT admin · 30-day retention |
| Data subject awareness | Privacy notice to be added to portal in production |
| Inaccurate AI output | Human-in-the-loop mandatory · Disclaimer in UI · Human reviews all flagged documents |

#### 4.5 Residual Risk Rating
After mitigation measures: **LOW TO MEDIUM**

The primary residual risk is the transfer of data to OpenAI's US-based infrastructure. This is mitigated by the OpenAI DPA but not fully eliminated. In production, a Data Transfer Impact Assessment (DTIA) should be completed and Standard Contractual Clauses (SCCs) confirmed.

---

## 5. Data Subject Rights

The system supports the following GDPR data subject rights:

| Right | How supported |
|---|---|
| **Right to access** | IT administrator can retrieve all data associated with a data subject within 30 days of request |
| **Right to erasure** | IT administrator can delete all personal data associated with a data subject — automated deletion after 90 days |
| **Right to rectification** | Source data (Google Sheets) can be corrected — compliance check re-run with corrected data |
| **Right to portability** | Compliance results available in CSV format for export |
| **Right to object** | Data subject can request their data is not processed — requires manual workflow adjustment |
| **Right to restrict processing** | IT administrator can pause processing for specific data subjects |

**Contact for data subject requests:**
Kinda Faisal — Freelance AI Consultant
[Contact details to be added before production]

---

## 6. Third-Party Data Transfers

| Service | Data sent | Legal mechanism | Data location |
|---|---|---|---|
| **OpenAI API** | Document metadata including potentially personal data | OpenAI Data Processing Addendum (DPA) + Standard Contractual Clauses (SCCs) | USA (OpenAI servers) |
| **LangSmith (Langchain)** | Full AI input/output traces | LangSmith DPA + SCCs | EU (eu.api.smith.langchain.com) |
| **Google (Gmail)** | Compliance report summaries — no personal data | Google Workspace DPA | EU servers |
| **Google (Sheets)** | Shipment document metadata | Google Workspace DPA | EU servers |
| **Streamlit Cloud** | Compliance results displayed in portal | Streamlit Cloud terms | USA (Streamlit servers) |

### Data Transfer Risk Assessment

**OpenAI (USA)** — Highest risk. Personal data potentially transferred to US. Mitigated by DPA and SCCs. In production, consider OpenAI's Zero Data Retention API option, or anonymize personal fields before API call.

**LangSmith (EU)** — Low risk. EU endpoint ensures data stays within EU. GDPR-compliant by design.

**Streamlit Cloud (USA)** — Medium risk. Portal displays data from local CSV — no direct data transfer in current design. In production, consider EU-hosted alternative.

---

## 7. Privacy by Design Principles Applied

| Principle | How applied |
|---|---|
| Data minimization | Only document metadata processed — not full document text |
| Purpose limitation | Data used only for compliance checking — not for any other purpose |
| Storage limitation | 90-day automatic deletion policy |
| Integrity and confidentiality | HTTPS, encrypted API calls, .env file protection |
| EU data residency | LangSmith EU endpoint for all AI traces |
| Transparency | LangSmith audit trail — every AI decision visible to authorized users |
| Human oversight | Human-in-the-loop — no autonomous decisions affecting data subjects |

---

*Document prepared by: Kinda Faisal — Freelance AI Consultant | AI Consulting Bootcamp — Week 9 | 2026*
*Note: This GDPR documentation reflects the POC stage. A full legal review by a qualified data protection officer (DPO) is required before production deployment.*