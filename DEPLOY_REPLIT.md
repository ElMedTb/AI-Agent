# 🚀 Deploy to Replit - Complete Guide

## ⚡ Super Quick Setup (3 Steps!)

### Step 1: Upload to Replit
1. Go to [replit.com](https://replit.com) and sign up
2. Click **"Create Repl"**
3. Choose **"Import from GitHub"** OR **"Blank Repl"**
4. Upload all project files

### Step 2: Build Frontend
Open the Shell and run:
```bash
cd frontend
npm install
npm run build
cd ..
```

### Step 3: Update Backend
Replace `backend/app.py` with `backend/app_with_frontend.py`:
```bash
cd backend
mv app.py app_original.py
cp ../backend/app_with_frontend.py app.py
cd ..
```

### Step 4: Run!
Click the **"Run"** button. Your app is live! 🎉

---

## 📋 Detailed Setup

### Prerequisites
- Replit account (free)
- All project files uploaded

### File Structure in Replit
Make sure you have:
```
/
├── .replit              ✅ (already created)
├── replit.nix          ✅ (already created)
├── replit_start.sh     ✅ (already created)
├── backend/
│   ├── app_with_frontend.py  ✅ (serves frontend)
│   ├── app.py
│   ├── orchestrate_client.py
│   ├── sample_data.py
│   └── requirements.txt
├── frontend/
│   ├── build/          (will be created)
│   ├── src/
│   └── package.json
└── orchestrate/
```

### Step-by-Step

#### 1. Upload Project
- **Option A**: Import from GitHub (if you pushed it)
- **Option B**: Upload files manually via Replit's file upload

#### 2. Install Dependencies

**Backend:**
```bash
cd backend
pip install -r requirements.txt
```

**Frontend:**
```bash
cd frontend
npm install
```

#### 3. Build Frontend
```bash
cd frontend
npm run build
```
This creates the `frontend/build/` folder with static files.

#### 4. Configure Backend to Serve Frontend

**Option A**: Use the combined app (Recommended)
```bash
# Backup original
mv backend/app.py backend/app_original.py

# Use combined version
cp backend/app_with_frontend.py backend/app.py
```

**Option B**: Update `.replit` file:
```toml
run = "cd backend && python app_with_frontend.py"
```

#### 5. Set Environment Variables (Optional)
Click the 🔒 **Secrets** tab and add:
- `PORT=5000` (optional, defaults to 5000)
- `ORCHESTRATE_API_KEY` (optional for demo mode)
- `FLASK_ENV=production`

**Note**: Demo mode works without any API keys!

#### 6. Run the App
Click the **"Run"** button (or press `Ctrl+Enter`)

#### 7. Access Your App
- Replit will show your app in the webview panel
- Or visit the URL shown in console (e.g., `https://your-repl-name.username.repl.co`)

#### 8. Share Your Demo
1. Click **"Share"** button (top right)
2. Copy the link
3. Share with judges! 🎉

---

## 🎨 Replit-Specific Features

### Always On (Pro Feature)
- In Replit settings, enable "Always On"
- Keeps your app running 24/7
- Free tier: App sleeps after inactivity

### Webview
- Replit automatically shows your app in the webview
- No need to open external browser
- Perfect for demos!

### Multiple Terminals
- Click **"+"** to add new terminal
- Run frontend and backend separately if needed
- Or use the combined app (easier!)

---

## 🔧 Troubleshooting

### Port Already in Use
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9
```

### Frontend Not Loading
1. Check `frontend/build/` exists
2. Verify `app_with_frontend.py` is being used
3. Check browser console for errors

### Dependencies Not Installing
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Backend Errors
```bash
# Check Python version
python --version  # Should be 3.8+

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### CORS Errors
- Make sure `CORS(app)` is enabled in Flask
- Check `CORS_ORIGINS` environment variable

---

## 🚀 Production Tips

### 1. Use Combined App
`app_with_frontend.py` serves both API and frontend from one process - simpler!

### 2. Enable Demo Mode
The app works in demo mode without API keys - perfect for hackathon!

### 3. Pin Important Files
In Replit, pin:
- `backend/app_with_frontend.py`
- `frontend/src/App.js`
- `.replit`

### 4. Use Secrets
Store API keys in Replit Secrets (🔒 tab), not in code!

### 5. Test Before Sharing
- Click "Load Sample Data"
- Click "Start Onboarding"
- Verify it works!

---

## 📝 Quick Checklist

- [ ] All files uploaded to Replit
- [ ] Frontend built (`npm run build`)
- [ ] Using `app_with_frontend.py` as main app
- [ ] Dependencies installed
- [ ] App runs without errors
- [ ] Can access in webview
- [ ] Share link works

---

## 🎯 Demo Mode

**Good news!** The app works in **demo mode** without any API keys:

- ✅ Simulates workflow execution
- ✅ Returns realistic responses
- ✅ Perfect for hackathon demos
- ✅ No setup required!

Just run the app and it works! 🎉

---

## 🔗 Next Steps

1. **Test locally first** (see `QUICKSTART.md`)
2. **Upload to Replit**
3. **Build and run**
4. **Share the link!**

---

**Need help?** The app runs in demo mode by default - no configuration needed for basic demo!
