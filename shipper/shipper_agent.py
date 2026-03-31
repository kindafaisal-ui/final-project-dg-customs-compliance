"""
Shipper Document Agent
Guides shippers to prepare correct DG & customs documents
before submitting to Chleo's freight forwarding company.
"""

import os




ROUTES = {
    "DE → CH": {"customs": ["Export Declaration", "EUR.1 Certificate"], "notes": "EU-Switzerland customs union — EUR.1 required for preferential tariff"},
    "DE → GB": {"customs": ["Export Declaration", "Commercial Invoice", "Packing List"], "notes": "Post-Brexit — full UK customs declaration required. EORI number mandatory."},
    "DE → US": {"customs": ["Export Declaration", "Commercial Invoice", "Packing List", "AES Filing"], "notes": "EEI filing required for shipments over $2,500. HS code mandatory."},
    "DE → CN": {"customs": ["Export Declaration", "Commercial Invoice", "Packing List", "Certificate of Origin"], "notes": "China customs requires Chinese description of goods."},
    "DE → FR": {"customs": ["CMR Waybill"], "notes": "Intra-EU — CMR waybill sufficient for road transport."},
    "DE → PL": {"customs": ["CMR Waybill"], "notes": "Intra-EU — CMR waybill sufficient for road transport."},
    "DE → TR": {"customs": ["Export Declaration", "EUR.1 Certificate", "Commercial Invoice"], "notes": "EU-Turkey customs union — EUR.1 required."},
}

DG_CLASSES = {
    "1": {"name": "Explosives", "regulations": ["ADR", "IMDG", "IATA"], "extra_docs": ["Explosive Transport Permit", "Competent Authority Approval"]},
    "2": {"name": "Gases", "regulations": ["ADR", "IMDG", "IATA"], "extra_docs": ["Pressure Test Certificate"]},
    "3": {"name": "Flammable Liquids", "regulations": ["ADR", "IMDG", "IATA"], "extra_docs": []},
    "4": {"name": "Flammable Solids", "regulations": ["ADR", "IMDG", "IATA"], "extra_docs": []},
    "5": {"name": "Oxidizing Substances", "regulations": ["ADR", "IMDG", "IATA"], "extra_docs": []},
    "6.1": {"name": "Toxic Substances", "regulations": ["ADR", "IMDG", "IATA"], "extra_docs": ["MSDS Sheet", "Medical Certificate if required"]},
    "6.2": {"name": "Infectious Substances", "regulations": ["ADR", "IMDG", "IATA"], "extra_docs": ["Biological Substance Permit", "MSDS Sheet"]},
    "7": {"name": "Radioactive Material", "regulations": ["ADR", "IMDG", "IATA"], "extra_docs": ["Radiation Safety Certificate", "Competent Authority Approval"]},
    "8": {"name": "Corrosives", "regulations": ["ADR", "IMDG", "IATA"], "extra_docs": ["MSDS Sheet"]},
    "9": {"name": "Miscellaneous", "regulations": ["ADR", "IMDG", "IATA"], "extra_docs": []},
}

TRANSPORT_MODES = {
    "Road (ADR)": "ADR",
    "Sea (IMDG)": "IMDG",
    "Air (IATA)": "IATA",
}


def get_required_documents(route, is_dangerous_goods, dg_class=None, transport_mode=None, un_number=None, goods_description=None):
    """
    AI Agent that determines exactly what documents a shipper needs.
    Returns a structured checklist.
    """
    try:
        import openai
        client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY", ""))

        route_info = ROUTES.get(route, {"customs": ["Export Declaration"], "notes": "Standard customs documentation required"})
        dg_info = DG_CLASSES.get(dg_class, {}) if dg_class else {}

        prompt = f"""You are a logistics compliance expert specializing in dangerous goods and customs documentation for German freight forwarders.

A shipper needs to send a shipment with the following details:
- Route: {route}
- Goods Description: {goods_description or 'Not specified'}
- Dangerous Goods: {'Yes' if is_dangerous_goods else 'No'}
- DG Class: {dg_class or 'N/A'} {f"({dg_info.get('name', '')})" if dg_info else ''}
- UN Number: {un_number or 'N/A'}
- Transport Mode: {transport_mode or 'Not specified'}
- Route Notes: {route_info.get('notes', '')}

Generate a precise document checklist for this shipper. For each document:
1. State exactly what information must be included
2. Flag any common mistakes to avoid
3. Note the regulation it comes from (ADR 2023 / IMDG / IATA DGR / EU UCC)

Format your response as:

DOCUMENTS REQUIRED:
1. [Document Name] — [Regulation]
   Required fields: [list key fields]
   Common mistake: [one specific mistake to avoid]

CRITICAL WARNINGS:
- [Any critical compliance warnings]

SUBMISSION CHECKLIST:
- [Final checklist items before submitting]"""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            max_tokens=1500,
            messages=[{"role": "user", "content": prompt}]
        )

        return {
            "success": True,
            "route": route,
            "is_dangerous_goods": is_dangerous_goods,
            "dg_class": dg_class,
            "transport_mode": transport_mode,
            "un_number": un_number,
            "ai_guidance": response.choices[0].message.content,
            "standard_customs_docs": route_info.get("customs", []),
            "route_notes": route_info.get("notes", ""),
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "route": route,
        }


def main():
    """Test the Shipper Agent with sample shipments"""
    print("=" * 65)
    print("Shipper Document Agent")
    print("Guides shippers to prepare correct documents for Chleo")
    print("=" * 65)

    test_cases = [
        {
            "route": "DE → CH",
            "is_dangerous_goods": True,
            "dg_class": "3",
            "transport_mode": "Road (ADR)",
            "un_number": "UN1263",
            "goods_description": "Paint and varnish products"
        },
        {
            "route": "DE → GB",
            "is_dangerous_goods": False,
            "dg_class": None,
            "transport_mode": "Road (ADR)",
            "un_number": None,
            "goods_description": "Automotive parts"
        },
    ]

    for i, shipment in enumerate(test_cases, 1):
        print(f"\n{'='*65}")
        print(f"SHIPMENT {i}: {shipment['route']} — {'DG Class ' + shipment['dg_class'] if shipment['is_dangerous_goods'] else 'Non-DG'}")
        print("=" * 65)
        result = get_required_documents(**shipment)
        if result["success"]:
            print(f"\nStandard Customs Docs: {', '.join(result['standard_customs_docs'])}")
            print(f"Route Notes: {result['route_notes']}")
            print(f"\nAI Guidance:\n{result['ai_guidance']}")
        else:
            print(f"Error: {result['error']}")


if __name__ == "__main__":
    main()
