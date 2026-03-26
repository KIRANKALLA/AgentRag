# ✦ GenAI Studio — Capstone Project
### All-in-one AI app: RAG + Agent + Prompt Engineering · Powered by Claude

---

## Cost & Subscription Info

| Service | Cost | Required? |
|---|---|---|
| Anthropic API | Pay-per-use (~$0.01-0.05/session) | Yes |
| Streamlit Cloud | FREE | Yes (hosting) |
| GitHub | FREE | Yes (to deploy) |
| DuckDuckGo Search | FREE | Yes (built-in) |

Total fixed cost: $0/month. You only pay Anthropic per API call.
Get your API key at: https://console.anthropic.com

---

## Deploy to Streamlit Cloud

### Step 1 - Push to GitHub
  git init
  git add .
  git commit -m "GenAI Studio capstone"
  git remote add origin https://github.com/YOUR_USERNAME/genai-studio.git
  git push -u origin main

### Step 2 - Deploy on Streamlit Cloud
1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select your repo, set main file to app.py
5. Click Deploy

### Step 3 - Add API Key as Secret
In Streamlit Cloud: app Settings > Secrets > add:
  ANTHROPIC_API_KEY = "sk-ant-your-key-here"

Then update app.py line:
  api_key = st.secrets.get("ANTHROPIC_API_KEY","") or st.text_input("API Key",type="password")

---

## Run Locally
  pip install -r requirements.txt
  streamlit run app.py
  open http://localhost:8501

---

## File Structure
  genai-studio/
  app.py
  requirements.txt
  .streamlit/config.toml
  README.md
