import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

ROUTES = {
    "DE → CH": {"notes": "EUR.1 certificate required. ADR tunnel restriction code for alpine routes."},
    "DE → GB": {"notes": "Post-Brexit: UKIMS declaration required. GB EORI needed."},
    "DE → US": {"notes": "ISF 10+2 filing required 24h before loading. AES filing for exports over $2,500."},
    "DE → CN": {"notes": "China CIQ inspection certificate required."},
    "DE → FR": {"notes": "EU internal: SAD document. Intrastat if above threshold."},
    "DE → PL": {"notes": "EU internal: SAD document. Intrastat if above threshold."},
    "DE → TR": {"notes": "A.TR or EUR.1 for preferential tariff. Turkish customs value declaration."},
}

CUSTOMS_DOCS = {
    "DE → CH": ["Commercial Invoice", "Packing List", "EORI Number", "EUR.1 Movement Certificate", "Customs Export Declaration (ATLAS)", "Swiss Import Declaration"],
    "DE → GB": ["Commercial Invoice", "Packing List", "GB EORI Number", "UKIMS Declaration", "Customs Export Declaration", "Rules of Origin Certificate"],
    "DE → US": ["Commercial Invoice", "Packing List", "EORI Number", "AES/EEI Filing", "ISF 10+2 Filing", "Certificate of Origin"],
    "DE → CN": ["Commercial Invoice", "Packing List", "EORI Number", "CIQ Inspection Certificate", "Certificate of Origin", "Customs Export Declaration"],
    "DE → FR": ["Commercial Invoice", "Packing List", "EORI Number", "SAD Document", "Intrastat Declaration"],
    "DE → PL": ["Commercial Invoice", "Packing List", "EORI Number", "SAD Document", "Intrastat Declaration"],
    "DE → TR": ["Commercial Invoice", "Packing List", "EORI Number", "A.TR or EUR.1 Certificate", "Turkish Customs Value Declaration"],
}


def get_required_documents(
    route,
    goods_description,
    transport_mode,
    is_dg,
    dg_class=None,
    un_number=None,
    hs_code=None,
    eori_number=None,
    commercial_invoice=False,
    packing_list=False,
):
    validation_errors = []

    # Pre-validation
    if hs_code and len(hs_code.strip()) != 8:
        validation_errors.append(f"HS Code '{hs_code}' is {len(hs_code.strip())} digits — EU exports require exactly 8 digits.")
    if eori_number and not eori_number.strip().upper().startswith("DE"):
        validation_errors.append(f"EORI Number '{eori_number}' invalid — German EORI numbers must start with 'DE'.")
    if is_dg == "Yes" and un_number and not un_number.strip().upper().startswith("UN"):
        validation_errors.append(f"UN Number '{un_number}' format incorrect — must start with 'UN' (e.g. UN3480).")

    route_notes = ROUTES.get(route, {}).get("notes", "")
    required_customs_docs = CUSTOMS_DOCS.get(route, ["Commercial Invoice", "Packing List", "EORI Number", "Customs Export Declaration"])

    docs_prepared = []
    if commercial_invoice:
        docs_prepared.append("Commercial Invoice")
    if packing_list:
        docs_prepared.append("Packing List")

    dg_section = ""
    if is_dg == "Yes":
        reg = "ADR 2023" if "Road" in transport_mode else "IMDG Code" if "Sea" in transport_mode else "IATA DGR"
        dg_section = f"""
DANGEROUS GOODS:
- DG Class: {dg_class}
- UN Number: {un_number}
- Applicable Regulation: {reg}
"""

    prompt = f"""You are an expert international logistics compliance officer specialising in dangerous goods and customs clearance for German exporters.

SHIPMENT DETAILS:
- Route: {route}
- Goods: {goods_description}
- Transport Mode: {transport_mode}
- HS Code: {hs_code if hs_code else "Not provided"}
- EORI Number: {eori_number if eori_number else "Not provided"}
- Documents already prepared: {", ".join(docs_prepared) if docs_prepared else "None"}
{dg_section}

Provide a compliance checklist with these 4 sections:

1. CUSTOMS COMPLIANCE
Required documents for this route. Flag any HS code or EORI issues. Reference EU UCC where relevant.

2. DANGEROUS GOODS COMPLIANCE
{"Check " + ("ADR 2023" if "Road" in transport_mode else "IMDG Code" if "Sea" in transport_mode else "IATA DGR") + " compliance for Class " + str(dg_class) + ", " + str(un_number) + ". List all required DG documents, markings, and labels." if is_dg == "Yes" else "No dangerous goods declared."}

3. CRITICAL FLAGS
Any critical issues that must be resolved before dispatch.

4. SUBMISSION CHECKLIST
Complete list of documents to submit to the freight forwarder.

Be specific and cite exact regulations (e.g. ADR 2023 Section 5.4.1, EU UCC Article 162).
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=1200,
        )

        return {
            "success": True,
            "ai_guidance": response.choices[0].message.content,
            "validation_errors": validation_errors,
            "required_customs_docs": required_customs_docs,
            "route_notes": route_notes,
            "eori_required": True,
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "validation_errors": validation_errors,
        }
