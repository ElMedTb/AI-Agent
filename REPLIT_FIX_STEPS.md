# 🔧 Replit Setup - Action Plan

## ✅ What's Already Fixed

1. **replit.nix** - Updated from Node.js 18 (EOL) to `pkgs.nodejs` (latest stable)
2. **replit_start.sh** - Startup script is ready
3. **.replit** - Configuration file is set up

## 🚀 What You Need to Do Now

### Step 1: Verify the Fix in Replit

The Replit agent couldn't edit `replit.nix` directly. You need to verify it's fixed:

1. **Open your Replit project**
2. **Check `replit.nix`** - It should look like this:
   ```nix
   { pkgs }: {
     deps = [
       pkgs.python310
       pkgs.python310Packages.pip
       pkgs.nodejs          # ✅ Should be this (not nodejs-18_x)
       pkgs.nodePackages.npm
     ];
   }
   ```

3. **If it still says `nodejs-18_x`**, replace it with `nodejs`

### Step 2: Rebuild Nix Environment

After fixing `replit.nix`, you need to rebuild:

1. **Open the Shell** in Replit
2. **Run this command**:
   ```bash
   # This will rebuild the Nix environment with the correct Node.js version
   # Just wait for it to complete (may take 2-3 minutes)
   ```

   **OR** simply:
   - Click **"Stop"** if anything is running
   - Click **"Run"** again - this will trigger a rebuild

### Step 3: Wait for Environment Setup

The Nix environment needs to build. You'll see:
- "Building Nix environment..." 
- This takes 2-5 minutes the first time
- Be patient! ☕

### Step 4: Test the Setup

Once the environment is built, test in the Shell:

```bash
# Check Python
python3 --version
# Should show: Python 3.10.x

# Check Node.js
node --version
# Should show: v20.x.x or v22.x.x (NOT v18!)

# Check npm
npm --version
```

### Step 5: Run the Application

Once Python and Node.js are available:

1. **Click the "Run" button** in Replit
   - OR run manually: `bash replit_start.sh`

2. **The script will:**
   - Install backend dependencies (`pip install`)
   - Install frontend dependencies (`npm install`)
   - Build the frontend (`npm run build`)
   - Start the Flask server

3. **Wait for:** "Running on http://0.0.0.0:5000"

### Step 6: Access Your App

- Replit will show your app in the **webview panel**
- Or visit the URL shown in console
- The app works in **demo mode** - no API keys needed!

---

## 🐛 If You Still Have Issues

### Issue: "Node.js 18.x has reached End-Of-Life"

**Solution:** Make sure `replit.nix` uses `pkgs.nodejs` (not `nodejs-18_x`)

### Issue: "python3: command not found"

**Solution:** 
1. Wait for Nix environment to finish building
2. Try restarting the Replit workspace
3. Check that `replit.nix` is correct

### Issue: "npm: command not found"

**Solution:**
1. Same as above - wait for Nix build
2. Verify `replit.nix` includes `pkgs.nodePackages.npm`

### Issue: Script fails with PATH errors

**Solution:** The `replit_start.sh` script should work once the Nix environment is built. If it doesn't:

1. Try running commands manually:
   ```bash
   cd backend
   pip install -r requirements.txt
   cd ../frontend
   npm install
   npm run build
   cd ../backend
   python app_with_frontend.py
   ```

---

## 📋 Quick Checklist

- [ ] `replit.nix` uses `pkgs.nodejs` (not `nodejs-18_x`)
- [ ] Nix environment has finished building
- [ ] `python3 --version` works
- [ ] `node --version` shows v20+ (not v18)
- [ ] `npm --version` works
- [ ] Clicked "Run" button
- [ ] App starts successfully
- [ ] Can access app in webview

---

## 🎯 Expected Result

After following these steps, you should see:

```
🚀 Starting HR Onboarding Assistant...
📦 Installing backend dependencies...
📦 Installing frontend dependencies...
🔨 Building frontend...
✅ Starting backend server...
 * Running on http://0.0.0.0:5000
```

Then your app will be live! 🎉

---

## 💡 Pro Tips

1. **First build takes time** - Be patient (2-5 minutes)
2. **Demo mode works** - No API keys needed for hackathon demo
3. **Check logs** - If something fails, check the Shell output
4. **Restart if needed** - Sometimes a fresh start helps

---

## 🔗 Your Replit URL

Once running, your app will be at:
- `https://ai-agent-mehditabrani.replit.app` (or similar)

Share this link for your hackathon demo! 🚀

