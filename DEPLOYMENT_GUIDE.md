# 🚀 Deployment Guide - All Platforms

Choose your platform and follow the instructions below.

## 🎯 Quick Comparison

| Platform | Best For | Setup Time | Cost |
|----------|----------|------------|------|
| **Replit** | Hackathon demos | 5 min | Free |
| **Vercel + Railway** | Production | 10 min | Free tier |
| **Streamlit** | Python-only UI | 15 min | Free |
| **Render** | Full-stack | 10 min | Free tier |

---

## 1️⃣ Replit (Recommended for Hackathon)

**Best for**: Quick demos, easy sharing, no credit card needed

### Steps:

1. **Go to [replit.com](https://replit.com)** and sign up

2. **Create New Repl**:
   - Click "Create Repl"
   - Choose "Import from GitHub" (if you have it on GitHub)
   - OR "Blank Repl" → Upload all files

3. **Upload Files**:
   - Make sure you have `.replit`, `replit.nix`, and `replit_start.sh` in root
   - Upload entire project structure

4. **Configure** (Optional - works in demo mode without this):
   - Click 🔒 **Secrets** tab
   - Add: `ORCHESTRATE_API_KEY`, `PORT=5000`

5. **Build Frontend** (One-time):
   ```bash
   cd frontend
   npm install
   npm run build
   ```

6. **Update Backend**:
   - Rename `backend/app_with_frontend.py` to `backend/app.py` (or update `.replit` to use it)
   - This serves frontend from backend

7. **Run**:
   - Click "Run" button
   - Your app will be live at the Replit URL!

8. **Share**:
   - Click "Share" → Copy link
   - Share with judges! 🎉

### Replit Files Created:
- ✅ `.replit` - Replit configuration
- ✅ `replit.nix` - Dependencies
- ✅ `replit_start.sh` - Startup script
- ✅ `backend/app_with_frontend.py` - Combined server

---

## 2️⃣ Vercel (Frontend) + Railway/Render (Backend)

**Best for**: Production-ready deployment

### Frontend on Vercel:

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Deploy**:
   ```bash
   cd frontend
   vercel
   ```

3. **Configure**:
   - Add environment variable: `REACT_APP_API_URL=https://your-backend-url.com`

### Backend on Railway:

1. **Go to [railway.app](https://railway.app)** and sign up

2. **New Project** → "Deploy from GitHub repo"

3. **Configure**:
   - Root directory: `backend`
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py`

4. **Add Environment Variables**:
   - `PORT` (auto-set)
   - `ORCHESTRATE_API_KEY`
   - `CORS_ORIGINS` (your Vercel URL)

5. **Get URL** and update frontend `.env`

### Alternative: Render

1. **Go to [render.com](https://render.com)** and sign up

2. **New Web Service** → Connect GitHub repo

3. **Configure**:
   - Build command: `cd backend && pip install -r requirements.txt`
   - Start command: `cd backend && python app.py`

4. **Add Environment Variables** (same as Railway)

---

## 3️⃣ Streamlit (Python-Only UI)

**Best for**: Simple Python-based demo

### Convert to Streamlit:

I'll create a Streamlit version for you:

```bash
# Install Streamlit
pip install streamlit

# Run
streamlit run streamlit_app.py
```

**Note**: This requires creating a new Streamlit UI. Would you like me to create it?

---

## 4️⃣ Other Platforms

### Heroku:
```bash
# Install Heroku CLI
heroku create your-app-name
git push heroku main
```

### Fly.io:
```bash
fly launch
fly deploy
```

### DigitalOcean App Platform:
- Connect GitHub repo
- Auto-detects Python
- Deploy!

---

## 🎯 Recommended for Hackathon: **Replit**

**Why Replit?**
- ✅ Single link to share
- ✅ No credit card needed
- ✅ Works in demo mode
- ✅ Easy to update
- ✅ Judges can see code

### Quick Replit Setup:

1. Upload project to Replit
2. Run: `cd frontend && npm install && npm run build`
3. Update `.replit` to use `app_with_frontend.py`
4. Click "Run"
5. Share link! 🎉

---

## 🔧 Environment Variables

For all platforms, you'll need (optional for demo mode):

```env
ORCHESTRATE_API_KEY=your_key
PORT=5000
FLASK_ENV=production
CORS_ORIGINS=https://your-frontend-url.com
```

**Demo Mode**: Works without any API keys! Perfect for hackathon.

---

## 📝 Which Platform Should I Choose?

- **Hackathon Demo**: **Replit** (fastest, easiest)
- **Production**: **Vercel + Railway** (best performance)
- **Python-Only**: **Streamlit** (simplest UI)
- **Full Control**: **Render** (good balance)

---

## 🆘 Need Help?

Check platform-specific guides:
- `DEPLOY_REPLIT.md` - Detailed Replit guide
- Platform docs (Vercel, Railway, Render all have great docs)

**Quick tip**: Start with Replit for the demo, then deploy to production platforms later!

