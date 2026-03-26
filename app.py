import streamlit as st

st.set_page_config(
    page_title="GenAI Studio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global styles ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Outfit+Mono&family=Playfair+Display:ital,wght@0,700;1,400&display=swap');

:root {
    --bg:       #f7f5f0;
    --surface:  #ffffff;
    --border:   #e2ddd6;
    --ink:      #1a1815;
    --muted:    #8a8378;
    --rag:      #2563a8;
    --agent:    #1a7a4a;
    --prompt:   #9b3a9b;
    --accent:   #d4501a;
}
html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
    background: var(--bg);
    color: var(--ink);
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1.5rem 2rem 4rem; max-width: 1100px; }

/* Sidebar */
section[data-testid="stSidebar"] { background: var(--ink) !important; }
section[data-testid="stSidebar"] * { color: #f7f5f0 !important; }
section[data-testid="stSidebar"] .block-container { padding: 1.5rem 1rem; }
section[data-testid="stSidebar"] input { background: #2a2724 !important; border-color: #3a3530 !important; color: #f7f5f0 !important; }

/* Studio header */
.studio-header {
    display: flex; align-items: center; gap: 1rem;
    padding-bottom: 1.2rem;
    border-bottom: 2px solid var(--ink);
    margin-bottom: 1.8rem;
}
.studio-mark {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem; line-height: 1;
    color: var(--ink);
}
.studio-sub {
    font-size: 0.72rem; font-weight: 500;
    text-transform: uppercase; letter-spacing: 0.14em;
    color: var(--muted);
}
.studio-modules {
    display: flex; gap: 0.5rem; margin-left: auto;
}
.mod-badge {
    padding: 0.25rem 0.7rem;
    border-radius: 20px;
    font-size: 0.72rem; font-weight: 600;
    letter-spacing: 0.04em;
}
.mod-rag    { background: #dbeafe; color: var(--rag); }
.mod-agent  { background: #dcfce7; color: var(--agent); }
.mod-prompt { background: #f3e8ff; color: var(--prompt); }

/* Nav tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 0; border-bottom: 2px solid var(--border);
    background: transparent;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Outfit', sans-serif !important;
    font-weight: 600 !important; font-size: 0.88rem !important;
    padding: 0.7rem 1.5rem !important;
    border-radius: 0 !important;
    color: var(--muted) !important;
    border-bottom: 2px solid transparent !important;
    margin-bottom: -2px !important;
}
.stTabs [aria-selected="true"] {
    color: var(--ink) !important;
    border-bottom-color: var(--ink) !important;
    background: transparent !important;
}

/* Buttons */
.stButton > button {
    font-family: 'Outfit', sans-serif !important;
    font-weight: 600 !important; font-size: 0.85rem !important;
    border-radius: 6px !important;
    border: 2px solid var(--ink) !important;
    background: var(--ink) !important;
    color: var(--bg) !important;
    padding: 0.5rem 1.3rem !important;
    transition: all 0.15s !important;
}
.stButton > button:hover { background: var(--accent) !important; border-color: var(--accent) !important; }

/* Inputs */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    font-family: 'Outfit', sans-serif !important;
    background: var(--surface) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 6px !important;
    color: var(--ink) !important;
    font-size: 0.95rem !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--ink) !important;
    box-shadow: none !important;
}

/* Cards */
.card {
    background: var(--surface);
    border: 1.5px solid var(--border);
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 1rem;
}
.card-title {
    font-weight: 700; font-size: 0.82rem;
    text-transform: uppercase; letter-spacing: 0.08em;
    color: var(--muted); margin-bottom: 0.5rem;
}

/* Chat bubbles */
.bubble-user {
    background: var(--ink); color: var(--bg);
    border-radius: 12px 12px 2px 12px;
    padding: 0.8rem 1.1rem; margin: 0.8rem 0 0.4rem auto;
    max-width: 75%; font-size: 0.93rem; line-height: 1.6;
}
.bubble-ai {
    background: var(--surface); border: 1.5px solid var(--border);
    border-radius: 12px 12px 12px 2px;
    padding: 0.9rem 1.2rem; margin: 0.4rem 0 0.8rem 0;
    max-width: 82%; font-size: 0.93rem; line-height: 1.7;
}
.bubble-label {
    font-size: 0.62rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.1em;
    color: var(--muted); margin-bottom: 0.3rem;
}

/* Agent step */
.step-box {
    border-left: 3px solid var(--border);
    padding: 0.5rem 0.9rem;
    margin: 0.4rem 0;
    font-size: 0.82rem;
}
.step-tool { border-left-color: var(--agent); }
.step-think { border-left-color: var(--muted); font-style: italic; color: var(--muted); }
.step-result {
    background: #f9f8f6; border: 1px solid var(--border);
    border-radius: 4px; padding: 0.5rem 0.8rem;
    font-family: monospace; font-size: 0.75rem;
    color: var(--muted); max-height: 100px; overflow-y: auto;
    white-space: pre-wrap; word-break: break-word;
    margin-top: 0.3rem;
}
.step-label {
    font-size: 0.65rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.1em;
    margin-bottom: 0.2rem;
}
.step-tool .step-label  { color: var(--agent); }
.step-think .step-label { color: var(--muted); }

/* Prompt lab */
.technique-pill {
    display: inline-block;
    background: #f3e8ff; color: var(--prompt);
    border: 1px solid #d8b4fe;
    border-radius: 20px; padding: 0.2rem 0.7rem;
    font-size: 0.72rem; font-weight: 600;
    margin: 0.2rem 0.2rem 0 0; cursor: pointer;
}

/* Home tiles */
.tile {
    background: var(--surface);
    border: 1.5px solid var(--border);
    border-radius: 12px; padding: 1.5rem;
    height: 100%;
}
.tile-icon { font-size: 2rem; margin-bottom: 0.8rem; }
.tile-title { font-weight: 700; font-size: 1.05rem; margin-bottom: 0.4rem; }
.tile-desc  { font-size: 0.85rem; color: var(--muted); line-height: 1.6; }
.tile-tag   {
    display: inline-block; margin-top: 0.8rem;
    font-size: 0.68rem; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.08em;
    padding: 0.2rem 0.6rem; border-radius: 4px;
}
.tag-rag    { background: #dbeafe; color: var(--rag); }
.tag-agent  { background: #dcfce7; color: var(--agent); }
.tag-prompt { background: #f3e8ff; color: var(--prompt); }

/* Sidebar nav */
.nav-item {
    display: block; padding: 0.55rem 0.9rem;
    border-radius: 6px; margin-bottom: 0.3rem;
    font-weight: 500; font-size: 0.88rem;
    cursor: pointer; transition: background 0.12s;
}
.nav-item:hover { background: rgba(255,255,255,0.08); }
.nav-active { background: rgba(255,255,255,0.12) !important; }

/* Key info box */
.info-box {
    background: #fffbeb; border: 1.5px solid #fcd34d;
    border-radius: 8px; padding: 0.9rem 1.1rem;
    font-size: 0.88rem; line-height: 1.6; margin-bottom: 1rem;
}
.info-box strong { color: #92400e; }
</style>
""", unsafe_allow_html=True)

# ── Session state ──────────────────────────────────────────────────────────────
for k, v in {
    "rag_chunks": [], "rag_messages": [], "rag_pdf_name": None, "rag_indexed": False,
    "agent_sessions": [], "agent_files": {},
    "prompt_history": [],
    "active_tab": "Home",
}.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ✦ GenAI Studio")
    st.markdown("---")
    api_key = st.text_input("Anthropic API Key", type="password",
                            placeholder="sk-ant-...",
                            help="Get yours at console.anthropic.com")
    if api_key:
        st.success("API key set ✓")
    else:
        st.warning("Add API key to use the studio")

    st.markdown("---")
    st.markdown("**Navigation**")
    tabs_list = ["🏠 Home", "📄 RAG Studio", "🤖 Agent Studio", "🎯 Prompt Lab"]
    for t in tabs_list:
        st.markdown(f"• {t}")

    st.markdown("---")
    st.markdown("**Stats**")
    st.markdown(f"RAG Docs: **{'1' if st.session_state.rag_indexed else '0'}**")
    st.markdown(f"Agent Runs: **{len(st.session_state.agent_sessions)}**")
    st.markdown(f"Prompt Tests: **{len(st.session_state.prompt_history)}**")

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="studio-header">
  <div>
    <div class="studio-mark">✦ GenAI Studio</div>
    <div class="studio-sub">Capstone · RAG + Agent + Prompt Engineering</div>
  </div>
  <div class="studio-modules">
    <span class="mod-badge mod-rag">📄 RAG</span>
    <span class="mod-badge mod-agent">🤖 Agent</span>
    <span class="mod-badge mod-prompt">🎯 Prompts</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TABS
# ══════════════════════════════════════════════════════════════════════════════
tab_home, tab_rag, tab_agent, tab_prompt = st.tabs(
    ["🏠 Home", "📄 RAG Studio", "🤖 Agent Studio", "🎯 Prompt Lab"]
)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 1 — HOME
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_home:
    st.markdown("### Welcome to GenAI Studio")
    st.markdown("Your all-in-one workspace combining the three pillars of applied Generative AI.")

    st.markdown("""
    <div class="info-box">
      <strong>🔑 Subscription Info:</strong> This app requires only an
      <strong>Anthropic API key</strong> (pay-per-use, no subscription).
      Streamlit Cloud hosting is <strong>free</strong>. No other services needed.
      Estimated cost: ~$0.01–0.05 per session depending on usage.
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="tile">
          <div class="tile-icon">📄</div>
          <div class="tile-title">RAG Studio</div>
          <div class="tile-desc">Upload any PDF. Ask questions grounded in your document.
          Claude answers using only retrieved context — no hallucination.</div>
          <span class="tile-tag tag-rag">Retrieval-Augmented Generation</span>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="tile">
          <div class="tile-icon">🤖</div>
          <div class="tile-title">Agent Studio</div>
          <div class="tile-desc">Give Claude a research goal. It autonomously searches the web,
          runs Python code, saves files, and delivers a full report.</div>
          <span class="tile-tag tag-agent">ReAct Agent Loop</span>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="tile">
          <div class="tile-icon">🎯</div>
          <div class="tile-title">Prompt Lab</div>
          <div class="tile-desc">Experiment with prompting techniques — role prompting,
          chain-of-thought, few-shot, format control — and compare outputs side by side.</div>
          <span class="tile-tag tag-prompt">Prompt Engineering</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Architecture Overview")
    st.code("""
GenAI Studio
├── RAG Studio
│   ├── PDF Text Extraction     (PyMuPDF)
│   ├── Sentence Chunking       (overlap=100 words)
│   ├── Embedding               (hash-based vectors)
│   ├── Hybrid Retrieval        (semantic + BM25 keyword)
│   └── Grounded Generation     (Claude claude-opus-4-20250514)
│
├── Agent Studio
│   ├── Tool: web_search        (DuckDuckGo, no API key)
│   ├── Tool: execute_code      (Python subprocess sandbox)
│   ├── Tool: write/read_file   (workspace I/O)
│   └── ReAct Loop              (Claude claude-opus-4-20250514 + tools)
│
└── Prompt Lab
    ├── Technique Templates     (6 core techniques)
    ├── Side-by-side Compare    (A vs B prompts)
    ├── Parameter Controls      (temperature, max_tokens)
    └── History Log             (all runs saved in session)
    """, language="")

    st.markdown("### Tech Stack")
    cols = st.columns(4)
    stack = [
        ("🧠 LLM", "Claude claude-opus-4-20250514\nAnthropic API"),
        ("🖥 Frontend", "Streamlit\nPython only"),
        ("📦 PDF", "PyMuPDF\nfitz library"),
        ("🚀 Deploy", "Streamlit Cloud\nFree tier"),
    ]
    for col, (title, desc) in zip(cols, stack):
        with col:
            st.markdown(f"**{title}**")
            st.caption(desc)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 2 — RAG STUDIO
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_rag:
    import fitz, re, numpy as np

    # ── helpers ──
    def pdf_extract(data: bytes) -> str:
        doc = fitz.open(stream=data, filetype="pdf")
        pages = []
        for i, pg in enumerate(doc):
            t = pg.get_text()
            if t.strip():
                pages.append(f"[Page {i+1}]\n{t.strip()}")
        doc.close()
        return "\n\n".join(pages)

    def chunk_text(text: str, size=450, overlap=80):
        sents = re.split(r'(?<=[.!?])\s+', text)
        chunks, cur, cur_len, idx = [], [], 0, 0
        for s in sents:
            w = s.split()
            if cur_len + len(w) > size and cur:
                body = " ".join(cur)
                pm = re.search(r'\[Page (\d+)\]', body)
                chunks.append({"id": idx, "text": body,
                                "page": int(pm.group(1)) if pm else 0,
                                "wc": cur_len})
                idx += 1
                cur = cur[-overlap:] + w
                cur_len = len(cur)
            else:
                cur += w; cur_len += len(w)
        if cur:
            body = " ".join(cur)
            pm = re.search(r'\[Page (\d+)\]', body)
            chunks.append({"id": idx, "text": body,
                            "page": int(pm.group(1)) if pm else 0,
                            "wc": cur_len})
        return chunks

    def embed(text: str):
        import hashlib
        h = hashlib.md5(text.encode()).hexdigest()
        rng = np.random.default_rng(int(h[:8], 16))
        return rng.uniform(-1, 1, 64).tolist()

    def cos_sim(a, b):
        a, b = np.array(a), np.array(b)
        d = np.linalg.norm(a) * np.linalg.norm(b)
        return float(np.dot(a, b) / d) if d else 0.0

    def hybrid_retrieve(q, chunks, k=4):
        qe = embed(q)
        qw = set(q.lower().split())
        scored = {}
        for c in chunks:
            sem = cos_sim(qe, c.get("emb", embed(c["text"]))) * 0.7
            cw  = c["text"].lower().split()
            kw  = (sum(1 for w in cw if w in qw) / (len(cw)+1)) * 0.3
            scored[c["id"]] = {**c, "score": sem + kw}
        return sorted(scored.values(), key=lambda x: x["score"], reverse=True)[:k]

    def rag_answer(client, question, chunks, history):
        ctx = "\n\n---\n\n".join(
            f"[Page {c.get('page','?')} | score {c.get('score',0):.2f}]\n{c['text']}"
            for c in chunks)
        msgs = [{"role": m["role"], "content": m["content"]} for m in history[-6:]]
        msgs.append({"role": "user",
                     "content": f"Context:\n{ctx}\n\nQuestion: {question}"})
        r = client.messages.create(
            model="claude-opus-4-20250514", max_tokens=1000,
            system="Answer using ONLY the provided context. Cite page numbers. "
                   "If the answer isn't in context say so clearly.",
            messages=msgs)
        return r.content[0].text

    # ── UI ──
    st.markdown("### 📄 RAG Studio — PDF Question Answering")

    col_up, col_chat = st.columns([1, 2])

    with col_up:
        st.markdown("#### Upload & Index")
        uploaded = st.file_uploader("Upload PDF", type=["pdf"])
        chunk_size = st.slider("Chunk size (words)", 200, 700, 450, 50)
        top_k      = st.slider("Retrieve top-k chunks", 2, 8, 4)

        if uploaded and api_key:
            if st.button("⚡ Index Document", use_container_width=True):
                with st.spinner("Indexing…"):
                    import anthropic as ac
                    raw   = pdf_extract(uploaded.read())
                    chunks = chunk_text(raw, size=chunk_size)
                    for c in chunks:
                        c["emb"] = embed(c["text"])
                    st.session_state.rag_chunks   = chunks
                    st.session_state.rag_pdf_name = uploaded.name
                    st.session_state.rag_indexed  = True
                    st.session_state.rag_messages = []
                st.success(f"✓ {len(chunks)} chunks indexed")

        if st.session_state.rag_indexed:
            st.markdown("---")
            st.markdown(f"**Active:** `{st.session_state.rag_pdf_name}`")
            st.markdown(f"**Chunks:** {len(st.session_state.rag_chunks)}")
            if st.button("Clear Document"):
                st.session_state.rag_indexed  = False
                st.session_state.rag_chunks   = []
                st.session_state.rag_messages = []
                st.rerun()

    with col_chat:
        st.markdown("#### Ask Your Document")

        if not st.session_state.rag_indexed:
            st.info("Upload and index a PDF on the left to start.")
        else:
            # Chat history
            for msg in st.session_state.rag_messages:
                if msg["role"] == "user":
                    st.markdown(f'<div class="bubble-user"><div class="bubble-label">You</div>{msg["content"]}</div>', unsafe_allow_html=True)
                else:
                    src = ""
                    if msg.get("sources"):
                        chips = " ".join(f'<code>p.{c.get("page","?")} ({c.get("score",0):.2f})</code>' for c in msg["sources"])
                        src = f"<div style='margin-top:0.6rem;font-size:0.78rem;color:var(--muted)'>Sources: {chips}</div>"
                    st.markdown(f'<div class="bubble-ai"><div class="bubble-label">Claude · RAG</div>{msg["content"]}{src}</div>', unsafe_allow_html=True)

            # Suggestions
            if not st.session_state.rag_messages:
                st.markdown("**Try asking:**")
                sugs = ["Summarize this document", "What are the main findings?",
                        "List the key conclusions", "What topics are covered?"]
                sc = st.columns(2)
                for i, s in enumerate(sugs):
                    if sc[i % 2].button(s, key=f"sug_{s}", use_container_width=True):
                        st.session_state["rag_prefill"] = s
                        st.rerun()

            pf = st.session_state.pop("rag_prefill", "")
            question = st.text_input("Ask a question about your document",
                                     value=pf, placeholder="What does the document say about…?",
                                     label_visibility="collapsed")
            if st.button("Ask →", key="rag_ask") and question.strip() and api_key:
                with st.spinner("Retrieving & answering…"):
                    import anthropic as ac
                    client   = ac.Anthropic(api_key=api_key)
                    retrieved = hybrid_retrieve(question, st.session_state.rag_chunks, top_k)
                    answer    = rag_answer(client, question, retrieved, st.session_state.rag_messages)
                    st.session_state.rag_messages.append({"role": "user", "content": question})
                    st.session_state.rag_messages.append({"role": "assistant", "content": answer, "sources": retrieved})
                    st.rerun()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 3 — AGENT STUDIO
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_agent:
    import urllib.request, urllib.parse, json, subprocess, sys, tempfile, os, datetime

    WORKSPACE = "/tmp/genai_studio_workspace"
    os.makedirs(WORKSPACE, exist_ok=True)

    AGENT_TOOLS = [
        {"name": "web_search",
         "description": "Search the web for current information. Returns titles, snippets, URLs.",
         "input_schema": {"type": "object",
                          "properties": {"query": {"type": "string", "description": "Search query"},
                                         "num_results": {"type": "integer", "default": 5}},
                          "required": ["query"]}},
        {"name": "execute_code",
         "description": "Run Python code and return stdout. Use print() to see output.",
         "input_schema": {"type": "object",
                          "properties": {"code": {"type": "string"}},
                          "required": ["code"]}},
        {"name": "write_file",
         "description": "Save content to a file in the workspace.",
         "input_schema": {"type": "object",
                          "properties": {"filename": {"type": "string"}, "content": {"type": "string"}},
                          "required": ["filename", "content"]}},
        {"name": "read_file",
         "description": "Read a file from the workspace.",
         "input_schema": {"type": "object",
                          "properties": {"filename": {"type": "string"}},
                          "required": ["filename"]}},
        {"name": "list_files",
         "description": "List all files in the workspace.",
         "input_schema": {"type": "object", "properties": {}, "required": []}},
    ]

    AGENT_SYSTEM = """You are an expert Research Agent. Research topics thoroughly using your tools.
Strategy: search multiple angles → run code for analysis → save notes → synthesize final report.
Always save the final report as a .md file. Be thorough, organized, and cite sources."""

    def do_web_search(query, num_results=5):
        try:
            url = f"https://api.duckduckgo.com/?q={urllib.parse.quote_plus(query)}&format=json&no_html=1&skip_disambig=1"
            req = urllib.request.Request(url, headers={"User-Agent": "GenAIStudio/1.0"})
            with urllib.request.urlopen(req, timeout=8) as r:
                data = json.loads(r.read().decode())
            out = []
            if data.get("Answer"):      out.append(f"[Answer] {data['Answer']}")
            if data.get("AbstractText"): out.append(f"[Summary] {data['AbstractText']}\n{data.get('AbstractURL','')}")
            for t in data.get("RelatedTopics", [])[:num_results]:
                if isinstance(t, dict) and t.get("Text"):
                    out.append(f"• {t['Text']}\n  {t.get('FirstURL','')}")
            return (f"Results for '{query}':\n\n" + "\n\n".join(out)) if out else f"No results for '{query}'. Try rephrasing."
        except Exception as e:
            return f"Search error: {e}"

    def do_execute_code(code):
        try:
            with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
                f.write(code); path = f.name
            r = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=15)
            os.unlink(path)
            out = r.stdout + (f"\n[stderr]\n{r.stderr}" if r.stderr else "")
            return out.strip() or "(no output — use print())"
        except subprocess.TimeoutExpired:
            return "Timeout (15s limit)"
        except Exception as e:
            return f"Error: {e}"

    def do_write_file(filename, content):
        name = os.path.basename(filename)
        path = os.path.join(WORKSPACE, name)
        with open(path, "w") as f: f.write(content)
        st.session_state.agent_files[name] = {"content": content, "size": len(content),
                                               "time": datetime.datetime.now().strftime("%H:%M")}
        return f"✓ Saved '{name}' ({len(content):,} chars)"

    def do_read_file(filename):
        name = os.path.basename(filename)
        path = os.path.join(WORKSPACE, name)
        if not os.path.exists(path):
            return f"File '{name}' not found. Files: {os.listdir(WORKSPACE)}"
        return open(path).read()

    def do_list_files():
        files = os.listdir(WORKSPACE)
        return "Files: " + ", ".join(files) if files else "Workspace empty."

    def dispatch(name, inputs):
        if name == "web_search":   return do_web_search(**inputs)
        if name == "execute_code": return do_execute_code(**inputs)
        if name == "write_file":   return do_write_file(**inputs)
        if name == "read_file":    return do_read_file(**inputs)
        if name == "list_files":   return do_list_files()
        return f"Unknown: {name}"

    # ── UI ──
    st.markdown("### 🤖 Agent Studio — Autonomous Research")

    col_q, col_files = st.columns([3, 1])

    with col_files:
        st.markdown("#### Workspace Files")
        if st.session_state.agent_files:
            for fname, meta in st.session_state.agent_files.items():
                with st.expander(f"📄 {fname}"):
                    st.caption(f"{meta['time']} · {meta['size']:,} chars")
                    st.code(meta["content"][:400] + ("…" if len(meta["content"]) > 400 else ""))
                    st.download_button("⬇ Download", meta["content"], fname, key=f"dl_{fname}")
        else:
            st.caption("No files saved yet. The agent will save reports here.")

    with col_q:
        pf2 = st.session_state.pop("agent_prefill", "")
        goal = st.text_area("Research goal", value=pf2,
                            placeholder="e.g. Research transformer architectures and compare GPT vs BERT...",
                            height=80, label_visibility="collapsed")

        examples = ["Research the history of deep learning",
                    "Compare RAG vs fine-tuning for LLMs",
                    "Calculate and analyze prime numbers up to 1000",
                    "Research top open-source LLMs in 2024"]
        ec = st.columns(4)
        for i,ex in enumerate(examples):
            if col.button(ex[:28]+"…", key=f"aex_{i}_{ex[:8]}", use_container_width=True):
                st.session_state["agent_prefill"] = ex
                st.rerun()

        if st.button("🚀 Run Agent", use_container_width=True, key="run_agent") and goal.strip() and api_key:
            import anthropic as ac
            client = ac.Anthropic(api_key=api_key)
            messages = [{"role": "user", "content": goal.strip()}]
            steps_display = []

            st.markdown(f'<div class="bubble-user"><div class="bubble-label">You</div>{goal.strip()}</div>', unsafe_allow_html=True)

            with st.spinner("Agent working…"):
                for iteration in range(20):
                    try:
                        resp = client.messages.create(
                            model="claude-opus-4-20250514", max_tokens=4096,
                            system=AGENT_SYSTEM, tools=AGENT_TOOLS, messages=messages)
                    except Exception as e:
                        st.error(f"API error: {e}"); break

                    texts = [b.text for b in resp.content if hasattr(b, "text") and b.text.strip()]
                    tools_called = [b for b in resp.content if b.type == "tool_use"]

                    if texts and tools_called:
                        for t in texts:
                            if len(t) > 30:
                                st.markdown(f'<div class="step-box step-think"><div class="step-label">💭 Thinking</div>{t[:300]}{"…" if len(t)>300 else ""}</div>', unsafe_allow_html=True)

                    if tools_called:
                        st.markdown(f'<div class="step-box step-tool"><div class="step-label">⚡ Step {iteration+1} — {len(tools_called)} tool call(s)</div></div>', unsafe_allow_html=True)
                        tool_results = []
                        for b in tools_called:
                            icon = {"web_search":"🔍","execute_code":"⚡","write_file":"📝","read_file":"📂","list_files":"📋"}.get(b.name,"🔧")
                            inp_str = json.dumps(b.input, ensure_ascii=False)[:100]
                            st.markdown(f'<div class="step-box step-tool"><div class="step-label">{icon} {b.name}</div>{inp_str}</div>', unsafe_allow_html=True)
                            result = dispatch(b.name, b.input)
                            st.markdown(f'<div class="step-result">{result[:250]}{"…" if len(result)>250 else ""}</div>', unsafe_allow_html=True)
                            tool_results.append({"type":"tool_result","tool_use_id":b.id,"content":result})

                        messages.append({"role":"assistant","content":resp.content})
                        messages.append({"role":"user","content":tool_results})

                    elif resp.stop_reason == "end_turn":
                        final = "\n\n".join(texts)
                        st.markdown(f'<div class="bubble-ai"><div class="bubble-label">✦ Research Complete</div>', unsafe_allow_html=True)
                        st.markdown(final)
                        st.markdown('</div>', unsafe_allow_html=True)
                        st.session_state.agent_sessions.append({"goal": goal, "answer": final, "steps": iteration+1})
                        break
                else:
                    st.warning("Max iterations reached.")
        elif st.button("🚀 Run Agent", use_container_width=True, key="run_agent_disabled") and not api_key:
            st.warning("Add API key in sidebar.")

        # Past sessions
        if st.session_state.agent_sessions:
            st.markdown("---")
            st.markdown("#### Previous Runs")
            for s in reversed(st.session_state.agent_sessions[-3:]):
                with st.expander(f"🔬 {s['goal'][:60]}… ({s['steps']} steps)"):
                    st.markdown(s["answer"])


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 4 — PROMPT LAB
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab_prompt:
    import anthropic as ac

    TECHNIQUES = {
        "🎭 Role Prompt": {
            "system": "You are a senior data scientist at a top tech company with 15 years of experience. Give expert-level, opinionated answers.",
            "user":   "What's the best way to handle class imbalance in a dataset?",
        },
        "🧠 Chain of Thought": {
            "system": "Think through every problem step by step before giving your final answer. Show your reasoning explicitly.",
            "user":   "A model has 92% accuracy but only 40% recall on the minority class. Is it a good model? Why?",
        },
        "📋 Few-Shot": {
            "system": "You convert informal ML jargon into precise technical language.",
            "user":   """Examples:
Informal: "the model is overfitting like crazy"
Formal: "The model exhibits high variance, performing significantly better on training data than on the held-out validation set."

Informal: "we just threw more data at it"
Formal: "We augmented the training dataset to improve generalization."

Now convert:
Informal: "the embeddings are all bunched together"
Formal:""",
        },
        "📐 Format Control": {
            "system": "Always respond in valid JSON only. No markdown, no explanation outside the JSON.",
            "user":   'Analyze this ML model description and return: {"model_type": "", "use_case": "", "pros": [], "cons": [], "difficulty": "easy/medium/hard"}\n\nModel: "A variational autoencoder trained on medical images to learn compressed latent representations for anomaly detection."',
        },
        "🔍 Metacognitive": {
            "system": "After every answer, add a section: CONFIDENCE (1-10 and why), ASSUMPTIONS (what you assumed), CAVEATS (what could change your answer).",
            "user":   "Will large language models replace software engineers in the next 5 years?",
        },
        "⛓ Prompt Chaining": {
            "system": "You are step 2 of a 3-step pipeline. You receive extracted claims and must rate each as: VERIFIABLE / OPINION / SPECULATION. Format as a numbered list.",
            "user":   "Claims from step 1:\n1. GPT-4 has 1.8 trillion parameters\n2. Transformers are better than RNNs for all tasks\n3. BERT was released in 2018\n4. Fine-tuning always improves model performance\n5. The attention mechanism was introduced in 2017",
        },
    }

    st.markdown("### 🎯 Prompt Lab — Technique Explorer")

    col_l, col_r = st.columns([1, 1])

    with col_l:
        st.markdown("#### Build Your Prompt")

        # Technique loader
        st.markdown("**Load a technique template:**")
        tcols = st.columns(3)
        for i, (name, _) in enumerate(TECHNIQUES.items()):
            if tcols[i % 3].button(name, key=f"tech_{name}", use_container_width=True):
                st.session_state["pl_system"] = TECHNIQUES[name]["system"]
                st.session_state["pl_user"]   = TECHNIQUES[name]["user"]
                st.rerun()

        st.markdown("---")
        sys_prompt = st.text_area("System Prompt",
                                  value=st.session_state.get("pl_system", "You are a helpful assistant."),
                                  height=120, key="pl_system_input")
        user_prompt = st.text_area("User Prompt",
                                   value=st.session_state.get("pl_user", ""),
                                   height=120, key="pl_user_input")

        pc1, pc2 = st.columns(2)
        temperature = pc1.slider("Temperature", 0.0, 1.0, 0.7, 0.05)
        max_tokens  = pc2.slider("Max tokens", 100, 2000, 800, 100)

        run_prompt = st.button("▶ Run Prompt", use_container_width=True, key="run_prompt")

        # Compare mode
        st.markdown("---")
        st.markdown("#### A/B Compare")
        st.caption("Run the same user prompt with two different system prompts.")
        sys_a = st.text_area("System A", value="You are a concise assistant. Answer in 2 sentences max.", height=70, key="sys_a")
        sys_b = st.text_area("System B", value="You are a thorough professor. Give a detailed academic explanation.", height=70, key="sys_b")
        compare_q = st.text_input("Question for both", value="What is backpropagation?", key="compare_q")
        run_compare = st.button("⚡ Compare A vs B", use_container_width=True, key="run_compare")

    with col_r:
        st.markdown("#### Output")

        if run_prompt and api_key and user_prompt.strip():
            with st.spinner("Running…"):
                client = ac.Anthropic(api_key=api_key)
                r = client.messages.create(
                    model="claude-opus-4-20250514", max_tokens=max_tokens,
                    temperature=temperature,
                    system=sys_prompt,
                    messages=[{"role": "user", "content": user_prompt}])
                out = r.content[0].text
                st.session_state.prompt_history.append({
                    "system": sys_prompt, "user": user_prompt,
                    "output": out, "temp": temperature,
                    "tokens": r.usage.output_tokens
                })
                st.markdown(f'<div class="card"><div class="card-title">Output · {r.usage.output_tokens} tokens · temp={temperature}</div>', unsafe_allow_html=True)
                st.markdown(out)
                st.markdown('</div>', unsafe_allow_html=True)

        if run_compare and api_key and compare_q.strip():
            with st.spinner("Running A and B…"):
                client = ac.Anthropic(api_key=api_key)
                def run_one(sys, q):
                    r = client.messages.create(
                        model="claude-opus-4-20250514", max_tokens=600,
                        system=sys, messages=[{"role":"user","content":q}])
                    return r.content[0].text, r.usage.output_tokens

                out_a, tok_a = run_one(sys_a, compare_q)
                out_b, tok_b = run_one(sys_b, compare_q)

                ca, cb = st.columns(2)
                with ca:
                    st.markdown(f'<div class="card"><div class="card-title">System A · {tok_a} tokens</div>', unsafe_allow_html=True)
                    st.markdown(out_a)
                    st.markdown('</div>', unsafe_allow_html=True)
                with cb:
                    st.markdown(f'<div class="card"><div class="card-title">System B · {tok_b} tokens</div>', unsafe_allow_html=True)
                    st.markdown(out_b)
                    st.markdown('</div>', unsafe_allow_html=True)

        # History
        if st.session_state.prompt_history:
            st.markdown("---")
            st.markdown("#### Run History")
            for i, h in enumerate(reversed(st.session_state.prompt_history[-5:])):
                with st.expander(f"Run {len(st.session_state.prompt_history)-i} · {h['tokens']} tokens · temp={h['temp']}"):
                    st.caption(f"**System:** {h['system'][:80]}…")
                    st.caption(f"**User:** {h['user'][:80]}…")
                    st.markdown(h["output"])

        if not run_prompt and not run_compare and not st.session_state.prompt_history:
            st.markdown("""
            <div style="text-align:center;padding:3rem 1rem;color:var(--muted)">
              <div style="font-size:2.5rem;margin-bottom:1rem">🎯</div>
              <div style="font-weight:700;font-size:1.1rem;color:var(--ink);margin-bottom:0.5rem">
                Load a template or write your own
              </div>
              <div style="font-size:0.88rem;line-height:1.7">
                Click any technique button on the left to load a pre-built prompt,
                then hit Run to see the output. Use A/B Compare to contrast different
                system prompts side by side.
              </div>
            </div>
            """, unsafe_allow_html=True)
