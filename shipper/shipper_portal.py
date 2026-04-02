import streamlit as st
from shipper_agent import get_required_documents

st.set_page_config(page_title="ShipDoc — Shipper Compliance Portal", page_icon="🚛", layout="wide")

bg_url = "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=1600&q=80"

st.markdown(f"""
<style>
.stApp {{
    background-image: linear-gradient(rgba(5,15,30,0.38), rgba(5,15,30,0.38)), url("{bg_url}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
/* Cards */
.card{{background:rgba(10,20,40,0.65);border:1px solid rgba(94,232,228,0.35);border-radius:12px;padding:1.2rem 1.4rem;margin-bottom:1rem;backdrop-filter:blur(8px)}}
.section-header{{color:#5EE8E4;font-weight:700;font-size:1.05rem;margin-bottom:0.6rem}}
/* Result boxes */
.result-box{{background:rgba(10,20,40,0.70);border:1px solid rgba(94,232,228,0.5);border-radius:12px;padding:1.5rem;margin-top:1rem;backdrop-filter:blur(8px)}}
.flag-box{{background:rgba(245,158,11,0.25);border-left:4px solid #F59E0B;border-radius:0 8px 8px 0;padding:0.7rem 1rem;margin-bottom:0.5rem;color:#FEF3C7;font-size:0.92rem}}
.error-box{{background:rgba(239,68,68,0.25);border-left:4px solid #EF4444;border-radius:0 8px 8px 0;padding:0.7rem 1rem;margin-bottom:0.5rem;color:#FEE2E2;font-size:0.92rem}}
.success-box{{background:rgba(34,197,94,0.20);border-left:4px solid #22C55E;border-radius:0 8px 8px 0;padding:0.7rem 1rem;margin-bottom:0.5rem;color:#DCFCE7;font-size:0.92rem}}
/* Button */
.stButton>button{{background:linear-gradient(135deg,#1A9E9B,#0D7C7A);color:white;border:none;border-radius:8px;padding:0.6rem 2rem;font-weight:700;font-size:1rem;width:100%}}
/* ALL text labels white */
label, .stRadio label, .stCheckbox label, .stSelectbox label, .stTextInput label,
div[data-testid="stMarkdownContainer"] p,
.stRadio div[role="radiogroup"] label span p {{color:#F1F5F9 !important;font-weight:500}}
/* Input fields — white text, semi-dark background */
input, textarea, .stSelectbox div[data-baseweb="select"] > div {{
    color: #F1F5F9 !important;
    background-color: rgba(15,25,50,0.75) !important;
}}
/* Selectbox text */
div[data-baseweb="select"] span {{color:#F1F5F9 !important}}
/* Headings */
h1,h2,h3{{color:white !important}}
/* Checkbox text */
.stCheckbox span {{color:#F1F5F9 !important}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;padding:1rem 0 0.5rem">
<p style="color:#5EE8E4;font-size:2rem;font-weight:800;margin:0;text-shadow:0 2px 8px rgba(0,0,0,0.8)">🚛 ShipDoc</p>
<p style="color:#F1F5F9;font-size:0.95rem;margin:0;text-shadow:0 1px 6px rgba(0,0,0,0.9)">Shipper Compliance Portal — Dangerous Goods & Customs Clearance</p>
<p style="color:#94A3B8;font-size:0.8rem;margin-top:0.3rem">EU AI Act Compliant · Human-in-the-loop · GDPR Compliant · 2026</p>
</div>
<hr style="border-color:rgba(94,232,228,0.3);margin:0.8rem 0"/>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-header">📍 Shipment Details</p>', unsafe_allow_html=True)
    route = st.selectbox("Route", ["DE → CH","DE → GB","DE → US","DE → CN","DE → FR","DE → PL","DE → TR"])
    goods_description = st.text_input("Goods Description", placeholder="e.g. Lithium-ion batteries (UN3480)")
    transport_mode = st.selectbox("Transport Mode", ["Road (ADR)","Sea (IMDG)","Air (IATA)"])
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-header">🛃 Customs Information</p>', unsafe_allow_html=True)
    hs_code = st.text_input("HS Code (8 digits required)", placeholder="e.g. 85076000")
    eori_number = st.text_input("EORI Number", placeholder="e.g. DE123456789")
    st.markdown('<p style="color:#94A3B8;font-size:0.82rem;margin:0.3rem 0 0.6rem">Documents already prepared:</p>', unsafe_allow_html=True)
    commercial_invoice = st.checkbox("Commercial Invoice")
    packing_list = st.checkbox("Packing List")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-header">⚠️ Dangerous Goods</p>', unsafe_allow_html=True)
    is_dg = st.radio("Is this a Dangerous Goods shipment?", ["No","Yes"])
    dg_class = None
    un_number = None
    if is_dg == "Yes":
        dg_class = st.selectbox("DG Class", ["1 — Explosives","2 — Gases","3 — Flammable Liquids","4 — Flammable Solids","5 — Oxidizing Substances","6.1 — Toxic Substances","6.2 — Infectious Substances","7 — Radioactive Material","8 — Corrosives","9 — Miscellaneous"])
        un_number = st.text_input("UN Number", placeholder="e.g. UN3480")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col_btn1, col_btn2, col_btn3 = st.columns([1,2,1])
with col_btn2:
    generate = st.button("🔍 Check Compliance & Generate Checklist")

if generate:
    if not goods_description:
        st.warning("Please enter a goods description before generating the checklist.")
    else:
        with st.spinner("AI agent checking compliance against ADR · IMDG · IATA · EU UCC · CMR · EUR.1 ..."):
            result = get_required_documents(
                route=route,
                goods_description=goods_description,
                transport_mode=transport_mode,
                is_dg=is_dg,
                dg_class=dg_class,
                un_number=un_number,
                hs_code=hs_code,
                eori_number=eori_number,
                commercial_invoice=commercial_invoice,
                packing_list=packing_list,
            )

        if result["success"]:
            if result.get("validation_errors"):
                st.markdown("### ⛔ Validation Issues Found")
                for err in result["validation_errors"]:
                    st.markdown(f'<div class="error-box">❌ {err}</div>', unsafe_allow_html=True)

            dg_label = f"DG Class {dg_class}" if is_dg == "Yes" else "Non-DG Shipment"
            eori_status = "✅ EORI provided" if eori_number else ("⚠️ EORI required — not provided" if result.get("eori_required") else "ℹ️ EORI not required")
            hs_status = "✅ HS Code provided" if hs_code else "⚠️ HS Code not provided"

            st.markdown(f"""
            <div style="background:rgba(10,20,40,0.70);border:1px solid rgba(94,232,228,0.4);border-radius:10px;padding:0.8rem 1.2rem;margin-bottom:1rem;display:flex;gap:2rem;flex-wrap:wrap;backdrop-filter:blur(6px)">
                <span style="color:#5EE8E4;font-weight:700">🗺️ {route}</span>
                <span style="color:#F1F5F9">🚛 {transport_mode}</span>
                <span style="color:#F1F5F9">⚠️ {dg_label}</span>
                <span style="color:#F1F5F9">{hs_status}</span>
                <span style="color:#F1F5F9">{eori_status}</span>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### 🛃 Required Customs Documents for This Route")
            for doc in result.get("required_customs_docs", []):
                st.markdown(f'<div class="success-box">📄 {doc}</div>', unsafe_allow_html=True)

            if result.get("route_notes"):
                st.markdown(f'<div class="flag-box">ℹ️ {result["route_notes"]}</div>', unsafe_allow_html=True)

            st.markdown("### 📋 Full Compliance Checklist")
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown(f'<p style="color:#F1F5F9;white-space:pre-wrap;font-size:0.92rem;line-height:1.7">{result["ai_guidance"]}</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.success("✅ Checklist generated. Review all items before submitting documents to your freight forwarder.")
            st.info("💡 Once your documents are ready, send them to your freight forwarder. They will run a final AI compliance check before dispatch.")
        else:
            st.error(f"Error: {result.get('error', 'Unknown error')}")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<p style="color:#94A3B8;text-align:center;font-size:0.8rem">ShipDoc · Powered by ShipmentDoc Compliance AI · Kinda Faisal AI Consulting · 2026 · EU AI Act Compliant · Human-in-the-loop</p>', unsafe_allow_html=True)
