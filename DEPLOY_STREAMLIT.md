# 🚀 Deploy to Streamlit Cloud

## Quick Setup

### Step 1: Install Streamlit
```bash
pip install streamlit
```

### Step 2: Run Locally
```bash
streamlit run streamlit_app.py
```

### Step 3: Deploy to Streamlit Cloud

1. **Push to GitHub**
   - Make sure `streamlit_app.py` is in root
   - Push your repo to GitHub

2. **Go to [share.streamlit.io](https://share.streamlit.io)**
   - Sign in with GitHub
   - Click "New app"

3. **Configure**:
   - Repository: Your GitHub repo
   - Branch: `main` (or your branch)
   - Main file: `streamlit_app.py`
   - Python version: 3.8+

4. **Add Secrets** (if needed):
   - Click "Advanced settings"
   - Add secrets:
     ```toml
     [secrets]
     API_URL = "https://your-backend-url.com"
     ```

5. **Deploy!**
   - Click "Deploy"
   - Your app will be live at `https://your-app-name.streamlit.app`

## Backend Setup

You still need the backend running. Deploy it to:
- Railway
- Render
- Heroku
- Or any Python hosting

Then update `API_URL` in Streamlit secrets.

## Advantages

✅ Python-only (no Node.js needed)
✅ Easy deployment
✅ Free hosting
✅ Auto-updates on git push
✅ Built-in UI components

## Disadvantages

⚠️ Different UI from React version
⚠️ Still needs backend separately
⚠️ Less customizable than React

---

**Note**: This is an alternative to the React frontend. The React version is recommended for hackathon demos!

