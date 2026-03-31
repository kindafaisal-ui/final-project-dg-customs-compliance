import streamlit as st
import os

st.set_page_config(page_title="ShipDoc — Shipper Document Portal", page_icon="📦", layout="wide")

def get_key(name):
    try:
        return st.secrets[name]
    except:
        return os.environ.get(name, "")


st.markdown(f"""
<style>
[data-testid="stAppViewContainer"], p, li, ul, ol, .stMarkdown, .stMarkdown p, .stMarkdown li {{
    background-image: linear-gradient(rgba(10,25,47,0.82), rgba(10,25,47,0.82)), url("data:image/png;base64,{BG_IMAGE}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
[data-testid="stHeader"] {{ background: transparent; }}
[data-testid="stSidebar"] {{ background: rgba(10,25,47,0.95); }}
.main-title {{ color: white; font-size: 2.2rem; font-weight: 800; }}
.sub-title {{ color: #1A9E9B; font-size: 1rem; }}
.card {{ background: rgba(255,255,255,0.07); border: 1px solid rgba(255,255,255,0.15); border-radius: 12px; padding: 1.5rem; margin-bottom: 1rem; }}
label, .stSelectbox label, .stTextInput label, .stRadio label {{ color: white !important; font-weight: 600 !important; }}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📦 ShipDoc — Shipper Document Portal</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Powered by ShipmentDoc Compliance AI · Kinda Faisal AI Consulting · 2026</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<p style="color:#FFFFFF">Fill in your shipment details below. Our AI will generate the exact document checklist you need to submit to your freight forwarder.</p>', unsafe_allow_html=True)
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p style="color:#1A9E9B;font-weight:700;font-size:1.1rem">📍 Shipment Details</p>', unsafe_allow_html=True)
    route = st.selectbox("Route", ["DE → CH", "DE → GB", "DE → US", "DE → CN", "DE → FR", "DE → PL", "DE → TR"])
    goods_description = st.text_input("Goods Description", placeholder="e.g. Paint and varnish products")
    transport_mode = st.selectbox("Transport Mode", ["Road (ADR)", "Sea (IMDG)", "Air (IATA)"])
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p style="color:#1A9E9B;font-weight:700;font-size:1.1rem">⚠️ Dangerous Goods</p>', unsafe_allow_html=True)
    is_dg = st.radio("Is this a Dangerous Goods shipment?", ["No", "Yes"])
    dg_class = None
    un_number = None
    if is_dg == "Yes":
        dg_class = st.selectbox("DG Class", ["1 — Explosives", "2 — Gases", "3 — Flammable Liquids", "4 — Flammable Solids", "5 — Oxidizing Substances", "6.1 — Toxic Substances", "6.2 — Infectious Substances", "7 — Radioactive Material", "8 — Corrosives", "9 — Miscellaneous"])
        dg_class = dg_class.split(" — ")[0]
        un_number = st.text_input("UN Number", placeholder="e.g. UN1263")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Generate Document Checklist", type="primary", use_container_width=True):
    with st.spinner("AI is generating your document checklist..."):
        try:
            import openai
            client = openai.OpenAI(api_key=get_key("OPENAI_API_KEY"))

            prompt = f"""You are a logistics compliance expert for a German freight forwarder.

A shipper needs to send:
- Route: {route}
- Goods: {goods_description or 'General cargo'}
- Transport: {transport_mode}
- Dangerous Goods: {is_dg}
- DG Class: {dg_class or 'N/A'}
- UN Number: {un_number or 'N/A'}

Generate a precise document checklist. IMPORTANT: Use ONLY numbered lists (1. 2. 3.) - never use * or - for bullets. For each document state:
1. Document name and regulation (ADR 2023 / IMDG / IATA DGR / EU UCC)
2. Exact required fields
3. One common mistake to avoid

Format:
DOCUMENTS REQUIRED:
1. [Document Name] — [Regulation]
   Required fields: [fields]
   Common mistake: [mistake]

CRITICAL WARNINGS:
1. [warning]
2. [warning]
SUBMISSION CHECKLIST:
1. [check]
2. [check]"""

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                max_tokens=1500,
                messages=[{"role": "user", "content": prompt}]
            )

            result = response.choices[0].message.content

            st.markdown('<div style="background:rgba(26,158,155,0.15);border:1px solid #1A9E9B;border-radius:12px;padding:1.5rem;margin-top:1rem">', unsafe_allow_html=True)
            st.markdown(f'<p style="color:#1A9E9B;font-weight:700;font-size:1.1rem">📋 Document Checklist — {route}</p>', unsafe_allow_html=True)
            st.markdown(f'<div style="color:white;white-space:pre-wrap;font-size:0.95rem;line-height:1.7">{result.replace(chr(10), "<br>").replace("* ", "• ")}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.success("✅ Checklist generated! Please prepare all documents before submitting to your freight forwarder.")
            st.info("💡 Once your documents are ready, send them to your freight forwarder. They will run a final AI compliance check before dispatch.")

        except Exception as e:
            st.error(f"Error: {str(e)}")

st.divider()
st.markdown('<p style="color:#AABBCC;text-align:center;font-size:0.8rem">ShipDoc · Powered by ShipmentDoc Compliance AI · Kinda Faisal AI Consulting · 2026 · EU AI Act Compliant · Human-in-the-loop</p>', unsafe_allow_html=True)
# This line intentionally left blank
