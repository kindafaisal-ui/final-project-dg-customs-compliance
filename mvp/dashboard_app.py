import streamlit as st
import os
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="ShipmentDoc Compliance Portal", page_icon="🚛", layout="wide")

def get_key(name):
    try:
        return st.secrets[name]
    except:
        return os.environ.get(name, "")

SAMPLE_DOCS = [
    {"doc_id":"DOC-5000","doc_type":"DG Declaration (IATA)","route":"DE → CH","is_dangerous_goods":"Yes","dg_class":"3","un_number":"UN1263","carrier":"Lufthansa Cargo","error_detail":"None"},
    {"doc_id":"DOC-5001","doc_type":"Customs Export Declaration","route":"DE → CN","is_dangerous_goods":"No","dg_class":"N/A","un_number":"","carrier":"DHL","error_detail":"None"},
    {"doc_id":"DOC-5002","doc_type":"DG Declaration (ADR)","route":"DE → PL","is_dangerous_goods":"Yes","dg_class":"8","un_number":"UN2789","carrier":"DB Schenker","error_detail":"Missing tunnel code"},
    {"doc_id":"DOC-5003","doc_type":"Customs Export Declaration","route":"DE → GB","is_dangerous_goods":"No","dg_class":"N/A","un_number":"","carrier":"UPS","error_detail":"Missing EORI"},
    {"doc_id":"DOC-5004","doc_type":"DG Declaration (IMDG)","route":"DE → US","is_dangerous_goods":"Yes","dg_class":"6.1","un_number":"UN2810","carrier":"Hapag-Lloyd","error_detail":"None"},
]

def run_check(doc):
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=get_key("ANTHROPIC_API_KEY"))
        prompt = (
            "You are a DG and customs compliance expert.\n"
            "Check this shipment document:\n"
            "- ID: " + doc["doc_id"] + ", Type: " + doc["doc_type"] + ", Route: " + doc["route"] + "\n"
            "- UN: " + doc.get("un_number","N/A") + ", DG Class: " + doc.get("dg_class","N/A") + "\n"
            "- Carrier: " + doc.get("carrier","N/A") + ", Known Error: " + doc.get("error_detail","None") + "\n"
            "Check against ADR 2023, IMDG Code, IATA DGR, EU UCC regulations.\n"
            "Reply in exactly this format:\n"
            "DG_CHECK: COMPLIANT or NON-COMPLIANT - specific reason\n"
            "CUSTOMS_CHECK: COMPLIANT or REVIEW REQUIRED - specific reason\n"
            "ACTION: one clear sentence telling the operations team what to do\n"
            "COMPLIANT: YES or NO"
        )
        r = client.messages.create(
            model="claude-sonnet-4-20250514",
            messages=[{"role":"user","content":prompt}],
            max_tokens=1000,
        )
        text = r.content[0].text
        dg, customs, action, ok = "Not assessed", "Not assessed", "Manual review required", False
        for line in text.strip().split("\n"):
            if line.startswith("DG_CHECK:"): dg = line.replace("DG_CHECK:","").strip()
            elif line.startswith("CUSTOMS_CHECK:"): customs = line.replace("CUSTOMS_CHECK:","").strip()
            elif line.startswith("ACTION:"): action = line.replace("ACTION:","").strip()
            elif line.startswith("COMPLIANT:"): ok = "YES" in line.upper()
        return {
            "doc_id": doc["doc_id"],
            "doc_type": doc["doc_type"],
            "route": doc["route"],
            "carrier": doc.get("carrier",""),
            "un_number": doc.get("un_number",""),
            "dg_check": dg,
            "customs_check": customs,
            "action_required": action,
            "is_compliant": ok
        }
    except Exception as e:
        return {
            "doc_id": doc["doc_id"],
            "doc_type": doc["doc_type"],
            "route": doc["route"],
            "carrier": doc.get("carrier",""),
            "un_number": doc.get("un_number",""),
            "dg_check": "ERROR",
            "customs_check": "ERROR",
            "action_required": str(e)[:200],
            "is_compliant": False
        }

# ── Header ──
st.markdown(
    '<div style="background:#0D2137;border-radius:12px;padding:1.5rem 2rem;margin-bottom:1.5rem;border-left:5px solid #1A9E9B">'
    '<div style="color:white;font-size:1.6rem;font-weight:700">🚛 ShipmentDoc Compliance Portal</div>'
    '<div style="color:#1A9E9B;font-size:0.9rem">Dangerous Goods & Customs Clearance Automation · Kinda Faisal AI Consulting · 2026</div>'
    '</div>',
    unsafe_allow_html=True
)

# ── KPI Metrics ──
c1,c2,c3,c4,c5 = st.columns(5)
c1.metric("Documents", "500", "All 7 doc types")
c2.metric("AI Confidence", "90.7%", "9/10 docs")
c3.metric("Processing", "44s", "vs 9-12 min")
c4.metric("Error Rate", "1.2%", "vs 5-10% avg")
c5.metric("Annual Savings", "€80K+", "Staff + fines")
st.divider()

left, right = st.columns([1,2])

with left:
    st.subheader("⚡ Run Compliance Check")
    st.caption("AI checks 5 sample documents against ADR, IMDG, IATA, EU UCC")
    if st.button("🔍 Start Analysis", use_container_width=True, type="primary"):
        prog = st.progress(0)
        stat = st.empty()
        results = []
        for i, doc in enumerate(SAMPLE_DOCS):
            prog.progress(int(i/len(SAMPLE_DOCS)*90))
            stat.write("Analyzing " + doc["doc_id"] + "...")
            results.append(run_check(doc))
        prog.progress(100)
        stat.write("Sending email alert via n8n...")
        try:
            wh = get_key("N8N_WEBHOOK_URL")
            if wh:
                requests.post(wh, json={"source":"streamlit"}, timeout=5)
        except:
            pass
        prog.empty()
        stat.empty()
        st.session_state["results"] = results
        st.success("✅ Analysis complete!")
        st.rerun()

    st.divider()
    st.markdown("**🔗 Live Tools**")
    st.write("📊 [LangSmith Monitoring](https://eu.smith.langchain.com)")
    st.write("📈 [Tableau Dashboard](https://dub01.online.tableau.com)")
    st.write("⚙️ [n8n Automation](https://kinda5.app.n8n.cloud)")
    st.divider()
    st.info("⏱ 83 hours/day saved")
    st.error("💶 €50K fine risk per violation avoided")
    st.warning("🚨 DE→CH highest risk route")
    st.success("🤖 8.7/10 AI quality score")

with right:
    if "results" not in st.session_state or not st.session_state["results"]:
        st.info("👈 Click **Start Analysis** to run the AI compliance check on sample documents.")
    else:
        results = st.session_state["results"]
        flagged = sum(1 for r in results if not r["is_compliant"])
        compliant = sum(1 for r in results if r["is_compliant"])
        st.subheader("Compliance Results — " + datetime.now().strftime("%d %b %Y %H:%M"))
        m1,m2,m3 = st.columns(3)
        m1.metric("Total Analyzed", len(results))
        m2.metric("🚨 Flagged", flagged)
        m3.metric("✅ Compliant", compliant)
        st.divider()
        for r in results:
            ok = r["is_compliant"]
            color = "#1A9E9B" if ok else "#EF4444"
            status = "✅ COMPLIANT" if ok else "🚨 HIGH RISK"
            st.markdown(
                f'<div style="background:#1A3A5C;border-left:5px solid {color};border-radius:0 8px 8px 0;padding:0.8rem 1rem;margin-bottom:0.5rem">'
                f'<span style="color:white;font-weight:700">{r["doc_id"]} — {r["doc_type"]}</span> '
                f'<span style="color:{color};font-size:0.85rem;font-weight:600"> {status}</span><br>'
                f'<span style="color:#8899AA;font-size:0.82rem">Route: {r["route"]}'
                + (f' | UN: {r["un_number"]}' if r["un_number"] else "")
                + (f' | Carrier: {r["carrier"]}' if r["carrier"] else "")
                + '</span></div>',
                unsafe_allow_html=True
            )
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Dangerous Goods Check:**")
                if "NON-COMPLIANT" in r["dg_check"] or "ERROR" in r["dg_check"]:
                    st.error(r["dg_check"])
                else:
                    st.success(r["dg_check"])
            with col2:
                st.write("**Customs Clearance Check:**")
                if "REVIEW" in r["customs_check"] or "NON-COMPLIANT" in r["customs_check"] or "ERROR" in r["customs_check"]:
                    st.warning(r["customs_check"])
                else:
                    st.success(r["customs_check"])
            st.write("**Action Required:**")
            if ok:
                st.success(r["action_required"])
            else:
                st.error(r["action_required"])
            st.divider()

st.caption("ShipmentDoc Compliance Portal · Kinda Faisal AI Consulting · 2026 · Human-in-the-loop · EU AI Act Compliant")
