# 🚀 Quick Start Guide

Get the HR Onboarding Assistant running in 5 minutes!

## Prerequisites

- Python 3.8+ installed
- Node.js 14+ installed
- npm or yarn installed

## Step 1: Clone and Navigate

```bash
cd "Hackathon IBM"
```

## Step 2: Backend Setup

```bash
# Navigate to backend
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Create .env file (copy from SETUP.md or create manually)
# For demo mode, you can skip API keys - the system will simulate responses

# Start the backend server
python app.py
```

The backend will start on `http://localhost:5000`

## Step 3: Frontend Setup (New Terminal)

```bash
# Navigate to frontend
cd frontend

# Install Node dependencies
npm install

# Create .env file with:
# REACT_APP_API_URL=http://localhost:5000

# Start the frontend
npm start
```

The frontend will open automatically at `http://localhost:3000`

## Step 4: Test It!

1. Open `http://localhost:3000` in your browser
2. Click "Load Sample Data" to fill the form
3. Click "Start Onboarding"
4. Watch the magic happen! ✨

## Demo Mode

If you don't have IBM watsonx Orchestrate credentials yet, the system runs in **demo mode**:
- Simulates workflow execution
- Returns realistic responses
- Perfect for testing the UI and understanding the flow

## Next Steps

1. **Get Orchestrate Credentials**: Sign up for IBM watsonx Orchestrate
2. **Configure Skills**: Set up API credentials for Gmail, Slack, etc.
3. **Import Workflow**: Import the workflow from `orchestrate/workflows/`
4. **Test with Real APIs**: Connect to actual services

## Troubleshooting

### Backend won't start
- Check Python version: `python --version` (should be 3.8+)
- Install dependencies: `pip install -r requirements.txt`
- Check port 5000 is available

### Frontend won't start
- Check Node version: `node --version` (should be 14+)
- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`
- Check port 3000 is available

### API connection errors
- Verify backend is running on port 5000
- Check `.env` file has correct `REACT_APP_API_URL`
- Check browser console for CORS errors

## Need Help?

Check the main [README.md](README.md) for detailed documentation.


