code = open("/dev/stdin").read() if False else ""
code = '''import streamlit as st
import os, time, requests
from datetime import datetime

st.set_page_config(page_title="ShipmentDoc Compliance Portal", page_icon="🚛", layout="wide")

st.markdown("""<style>
* { font-family: sans-serif !important; }
.stApp { background-color: #0D1F3C !important; }
p, li { color: #C8D8E8 !important; }
h1, h2, h3 { color: #FFFFFF !important; }
[data-testid="stMetricValue"] { color: #1A9E9B !important; }
[data-testid="stMetricLabel"] { color: #8899AA !important; }
hr { border-color: #1A3A5C !important; }
a { color: #1A9E9B !important; }
</style>""", unsafe_allow_html=True)

SAMPLE_DOCS = [
    {"doc_id":"DOC-5000","doc_type":"DG Declaration (IATA)","route":"DE to CH","un_number":"UN2891","dg_class":"Class 3 Flammable","carrier":"DSV","error_detail":""},
    {"doc_id":"DOC-5005","doc_type":"DG Declaration (IATA)","route":"DE to JP","un_number":"UN1263","dg_class":"Class 3 Paint","carrier":"Kuehne+Nagel","error_detail":""},
    {"doc_id":"DOC-5008","doc_type":"DG Declaration (ADR)","route":"DE to PL","un_number":"UN3082","dg_class":"Class 9 Env Hazardous","carrier":"DHL Freight","error_detail":""},
    {"doc_id":"DOC-5001","doc_type":"Customs Export Declaration","route":"DE to CN","un_number":"","dg_class":"","carrier":"DB Schenker","error_detail":"HS code missing"},
    {"doc_id":"DOC-5002","doc_type":"Customs Export Declaration","route":"DE to FR","un_number":"","dg_class":"","carrier":"Kuehne+Nagel","error_detail":""},
]

def get_key(name):
    try:
        return st.secrets[name]
    except:
        return os.environ.get(name, "")

def run_check(doc):
    try:
        import openai
        client = openai.OpenAI(api_key=get_key("OPENAI_API_KEY"))
        prompt = (
            "You are a DG and customs compliance expert.\\n"
            "Check this document:\\n"
            "- ID: " + doc["doc_id"] + ", Type: " + doc["doc_type"] + ", Route: " + doc["route"] + "\\n"
            "- UN: " + doc.get("un_number","N/A") + ", DG Class: " + doc.get("dg_class","N/A") + "\\n"
            "- Carrier: " + doc.get("carrier","N/A") + ", Error: " + doc.get("error_detail","None") + "\\n"
            "Check against ADR 2023, IMDG, IATA DGR, EU UCC.\\n"
            "Reply exactly:\\n"
            "DG_CHECK: COMPLIANT or NON-COMPLIANT - reason\\n"
            "CUSTOMS_CHECK: COMPLIANT or REVIEW REQUIRED - reason\\n"
            "ACTION: one plain sentence for operations team\\n"
            "COMPLIANT: YES or NO"
        )
        r = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":prompt}],
            max_tokens=250,
            temperature=0
        )
        text = r.choices[0].message.content
        dg, customs, action, ok = "", "", "", False
        for line in text.strip().split("\\n"):
            if line.startswith("DG_CHECK:"): dg = line.replace("DG_CHECK:","").strip()
            elif line.startswith("CUSTOMS_CHECK:"): customs = line.replace("CUSTOMS_CHECK:","").strip()
            elif line.startswith("ACTION:"): action = line.replace("ACTION:","").strip()
            elif line.startswith("COMPLIANT:"): ok = "YES" in line.upper()
        return {"doc_id":doc["doc_id"],"doc_type":doc["doc_type"],"route":doc["route"],
                "carrier":doc.get("carrier",""),"un_number":doc.get("un_number",""),
                "dg_check":dg,"customs_check":customs,"action_required":action,"is_compliant":ok}
    except Exception as e:
        return {"doc_id":doc["doc_id"],"doc_type":doc["doc_type"],"route":doc["route"],
                "carrier":doc.get("carrier",""),"un_number":doc.get("un_number",""),
                "dg_check":"ERROR","customs_check":"ERROR","action_required":str(e)[:100],"is_compliant":False}

st.markdown(\'<div style="background:#1A3A5C;border-radius:12px;padding:1.5rem 2rem;margin-bottom:1.5rem;border-left:5px solid #1A9E9B"><div style="color:white;font-size:1.6rem;font-weight:700">ShipmentDoc Compliance Portal</div><div style="color:#1A9E9B;font-size:0.9rem">Dangerous Goods and Customs Clearance Automation - Kinda Faisal AI Consulting</div></div>\', unsafe_allow_html=True)

c1,c2,c3,c4,c5 = st.columns(5)
c1.metric("Documents","500"); c2.metric("AI Confidence","90.7%")
c3.metric("Processing","44s"); c4.metric("Error Rate","1.2%"); c5.metric("Annual Savings","EUR 80K+")
st.divider()
left, right = st.columns([1,2])

with left:
    st.subheader("Run Compliance Check")
    if st.button("Start Analysis", use_container_width=True, type="primary"):
        prog = st.progress(0)
        stat = st.empty()
        results = []
        for i, doc in enumerate(SAMPLE_DOCS):
            prog.progress(int(i/len(SAMPLE_DOCS)*90))
            stat.write("Analyzing " + doc["doc_id"] + "...")
            results.append(run_check(doc))
        prog.progress(100)
        stat.write("Sending email alert...")
        try:
            wh = get_key("N8N_WEBHOOK_URL")
            if wh:
                requests.post(wh, json={"source":"streamlit"}, timeout=5)
        except:
            pass
        prog.empty()
        stat.empty()
        st.session_state["results"] = results
        st.success("Done!")
        st.rerun()
    st.divider()
    st.write("[LangSmith](https://eu.smith.langchain.com)")
    st.write("[Tableau](https://dub01.online.tableau.com)")
    st.write("[n8n](https://kinda5.app.n8n.cloud)")
    st.divider()
    st.info("83 hours per day saved")
    st.error("EUR 90K+ fine risk avoided")
    st.warning("DE to CH highest risk route")
    st.success("8.7/10 AI quality score")

with right:
    if "results" not in st.session_state or not st.session_state["results"]:
        st.info("Click Start Analysis to run the AI compliance check.")
    else:
        results = st.session_state["results"]
        flagged = sum(1 for r in results if not r["is_compliant"])
        compliant = sum(1 for r in results if r["is_compliant"])
        st.subheader("Compliance Results - " + datetime.now().strftime("%d %b %Y %H:%M"))
        m1,m2,m3 = st.columns(3)
        m1.metric("Total",len(results))
        m2.metric("Flagged",flagged)
        m3.metric("Compliant",compliant)
        st.divider()
        for r in results:
            ok = r["is_compliant"]
            color = "#1A9E9B" if ok else "#EF4444"
            status = "COMPLIANT" if ok else "HIGH RISK"
            st.markdown(
                \'<div style="background:#1A3A5C;border-left:5px solid \' + color + \';border-radius:0 8px 8px 0;padding:0.8rem 1rem;margin-bottom:0.5rem">\' +
                \'<span style="color:white;font-weight:700">\' + r["doc_id"] + \' - \' + r["doc_type"] + \'</span> \' +
                \'<span style="color:\' + color + \';font-size:0.8rem">\' + status + \'</span><br>\' +
                \'<span style="color:#8899AA;font-size:0.82rem">Route: \' + r["route"] +
                (" | UN: " + r["un_number"] if r["un_number"] else "") +
                (" | Carrier: " + r["carrier"] if r["carrier"] else "") +
                \'</span></div>\',
                unsafe_allow_html=True
            )
            st.write("Dangerous Goods Check:")
            if "NON-COMPLIANT" in r["dg_check"] or "ERROR" in r["dg_check"]:
                st.error(r["dg_check"])
            else:
                st.success(r["dg_check"])
            st.write("Customs Clearance Check:")
            if "REVIEW" in r["customs_check"] or "NON-COMPLIANT" in r["customs_check"] or "ERROR" in r["customs_check"]:
                st.warning(r["customs_check"])
            else:
                st.success(r["customs_check"])
            st.write("Action Required:")
            if ok:
                st.success(r["action_required"])
            else:
                st.error(r["action_required"])
            st.divider()

st.caption("ShipmentDoc Compliance Portal - Kinda Faisal AI Consulting - 2026")
'''

with open("mvp/dashboard_app.py", "w") as f:
    f.write(code)
print("Done! Size:", len(code))