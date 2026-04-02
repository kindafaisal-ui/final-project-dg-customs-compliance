import streamlit as st
import os
from shipper_agent import get_required_documents

st.set_page_config(page_title="ShipDoc — Shipper Compliance Portal", page_icon="🚛", layout="wide")

st.markdown("""
<style>
.card{background:rgba(26,158,155,0.07);border:1px solid rgba(26,158,155,0.25);border-radius:12px;padding:1.2rem 1.4rem;margin-bottom:1rem}
.section-header{color:#1A9E9B;font-weight:700;font-size:1.05rem;margin-bottom:0.6rem}
.result-box{background:rgba(26,158,155,0.10);border:1px solid #1A9E9B;border-radius:12px;padding:1.5rem;margin-top:1rem}
.flag-box{background:rgba(245,158,11,0.12);border-left:4px solid #F59E0B;border-radius:0 8px 8px 0;padding:0.7rem 1rem;margin-bottom:0.5rem;color:white;font-size:0.92rem}
.error-box{background:rgba(239,68,68,0.12);border-left:4px solid #EF4444;border-radius:0 8px 8px 0;padding:0.7rem 1rem;margin-bottom:0.5rem;color:white;font-size:0.92rem}
.success-box{background:rgba(34,197,94,0.10);border-left:4px solid #22C55E;border-radius:0 8px 8px 0;padding:0.7rem 1rem;margin-bottom:0.5rem;color:white;font-size:0.92rem}
.stButton>button{background:linear-gradient(135deg,#1A9E9B,#0D7C7A);color:white;border:none;border-radius:8px;padding:0.6rem 2rem;font-weight:700;font-size:1rem;width:100%}
label{color:#CBD5E1 !important}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;padding:1rem 0 0.5rem">
<p style="color:#1A9E9B;font-size:2rem;font-weight:800;margin:0">🚛 ShipDoc</p>
<p style="color:#94A3B8;font-size:0.95rem;margin:0">Shipper Compliance Portal — Dangerous Goods & Customs Clearance</p>
<p style="color:#556677;font-size:0.8rem;margin-top:0.3rem">EU AI Act Compliant · Human-in-the-loop · GDPR Compliant · 2026</p>
</div>
<hr style="border-color:rgba(26,158,155,0.2);margin:0.8rem 0"/>
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
            <div style="background:rgba(26,158,155,0.08);border:1px solid rgba(26,158,155,0.3);border-radius:10px;padding:0.8rem 1.2rem;margin-bottom:1rem;display:flex;gap:2rem;flex-wrap:wrap">
                <span style="color:#1A9E9B;font-weight:700">🗺️ {route}</span>
                <span style="color:#94A3B8">🚛 {transport_mode}</span>
                <span style="color:#94A3B8">⚠️ {dg_label}</span>
                <span style="color:#94A3B8">{hs_status}</span>
                <span style="color:#94A3B8">{eori_status}</span>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### 🛃 Required Customs Documents for This Route")
            for doc in result.get("required_customs_docs", []):
                st.markdown(f'<div class="success-box">📄 {doc}</div>', unsafe_allow_html=True)

            if result.get("route_notes"):
                st.markdown(f'<div class="flag-box">ℹ️ {result["route_notes"]}</div>', unsafe_allow_html=True)

            st.markdown("### 📋 Full Compliance Checklist")
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown(f'<p style="color:white;white-space:pre-wrap;font-size:0.92rem;line-height:1.7">{result["ai_guidance"]}</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.success("✅ Checklist generated. Review all items before submitting documents to your freight forwarder.")
            st.info("💡 Once your documents are ready, send them to your freight forwarder. They will run a final AI compliance check before dispatch.")
        else:
            st.error(f"Error: {result.get('error', 'Unknown error')}")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<p style="color:#556677;text-align:center;font-size:0.8rem">ShipDoc · Powered by ShipmentDoc Compliance AI · Kinda Faisal AI Consulting · 2026 · EU AI Act Compliant · Human-in-the-loop</p>', unsafe_allow_html=True)
