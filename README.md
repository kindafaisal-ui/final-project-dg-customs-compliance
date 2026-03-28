# Lead Qualification Agent — Minimal Prototype

A working prototype of the Lead Qualification Agent for marketing/consulting agencies.

## Architecture

```
Lead Form Input
      ↓
[Node 1] retrieve_context   → RAG: queries ChromaDB for relevant agency knowledge
      ↓
[Node 2] ask_questions      → LLM generates follow-up questions + simulates answers
      ↓
[Node 3] make_decision      → LLM qualifies or disqualifies with reasoning
      ↓
Slack-style summary output
```

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set your OpenAI API key
```bash
# Mac/Linux
export OPENAI_API_KEY=your_key_here

# Windows
set OPENAI_API_KEY=your_key_here
```

### 3. Run the prototype
```bash
python agent.py
```

## What you'll see

The agent processes 2 sample leads:
- **Lead 1** (Sarah Chen): B2B SaaS company with $4M revenue → should QUALIFY
- **Lead 2** (Mike Torres): B2C e-commerce with $200K revenue → should DISQUALIFY

For each lead, you'll see:
1. RAG retrieval from the agency knowledge base
2. Generated qualifying questions
3. Simulated lead answers
4. Final qualify/disqualify decision with reasoning
5. A Slack-style notification preview

## Key Files

| File | Purpose |
|------|---------|
| `agent.py` | Main agent code — all logic lives here |
| `requirements.txt` | Python dependencies |
| `README.md` | This file |

## What's simulated (vs. production)

| Prototype | Production equivalent |
|-----------|----------------------|
| Inline text knowledge base | Real agency PDFs ingested into ChromaDB |
| `SAMPLE_LEADS` dict | n8n webhook receiving live form submissions |
| `sim_answer_*` fields | Lead replies collected via Gmail integration |
| Console print output | Actual Slack message sent via n8n |
| ChromaDB local | Pinecone cloud vector DB |

## Extending this prototype

To connect to n8n, replace the `run_prototype()` call with a Flask endpoint:

```python
from flask import Flask, request
app = Flask(__name__)

@app.route("/qualify", methods=["POST"])
def qualify_lead():
    lead_data = request.json
    result = agent.invoke(AgentState(lead_info=lead_data, ...))
    # n8n calls this endpoint, gets result, routes to Slack
    return {"decision": result["decision"], "summary": result["summary"]}
```

Then in n8n: Form Trigger → HTTP Request (this endpoint) → Slack node
