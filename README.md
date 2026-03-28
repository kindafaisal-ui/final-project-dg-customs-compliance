# ShipmentDoc Compliance AI
### Dangerous Goods and Customs Clearance Automation

**Consultant:** Kinda Faisal - Freelance AI Consultant
**Client:** Medium German Freight Forwarder (50-200 employees)
**Live Demo:** https://final-project-dg-customs-compliance-mffpsnzkusr6pmhcb6e8xv.streamlit.app/
**GitHub:** https://github.com/kindafaisal-ui/final-project-dg-customs-compliance

## The Story
I met Chleo at a dinner. She runs a medium-sized freight forwarding company in Germany. Her team spends 9-12 minutes manually checking every shipment document for compliance with international Dangerous Goods and Customs regulations. She told me: I am scared of AI - I do not trust it. Two days later I came back with this.

## What Problem Does This Solve?
Every international shipment must comply with strict regulations before goods can cross borders: ADR 2023, IMDG Code, IATA DGR, EU Customs Code. Missing a tunnel restriction code or wrong HS code can cause fines up to 50,000 EUR and customs holds of 1-2 days. Current process: 9-12 minutes per document manually with 5-10 percent error rate.

## Results
| Metric | Before | After | Improvement |
|---|---|---|---|
| Processing time | 603 seconds | 44 seconds | 93 percent faster |
| Error rate | 5-10 percent | 1.2 percent | 94 percent reduction |
| AI confidence | - | 90.7 percent | - |
| Annual savings | - | EUR 80,000+ | ROI 1,589 percent |
| AI quality score | - | 8.7/10 | LLM-as-judge |

## Repository Structure
- use_case_definition.md + pdf - Business problem, JTBD, MoSCoW, stakeholders
- roi_risk_assessment.md + pdf - ROI 12+36 months, risk matrix, Green Tech
- strategic_plan.md + pdf - GTM, phases, pricing, Green Tech
- poc/ - n8n workflow + poc documentation
- compliance/ - EU AI Act + GDPR documentation
- mvp/ - Working Streamlit application + code

## EU AI Act Classification
LIMITED RISK - Human-in-the-loop, private company use, internationally defined rules, full LangSmith audit trail.

## How to Run
git clone https://github.com/kindafaisal-ui/final-project-dg-customs-compliance.git
cd final-project-dg-customs-compliance/mvp
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python generate_dataset.py
streamlit run dashboard_app.py

## About
Kinda Faisal is a freelance AI consultant with 6 years of hands-on experience in international logistics. After completing an AI Consulting Bootcamp, she combines deep domain expertise with practical AI implementation skills.

Final Project - AI Consulting Bootcamp - Week 9 - 2026
