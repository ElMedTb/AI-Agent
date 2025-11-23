#!/bin/bash

# Replit startup script
echo "🚀 Starting HR Onboarding Assistant..."

# Install backend dependencies
echo "📦 Installing backend dependencies..."
cd backend
pip install --user -r requirements.txt

# Install frontend dependencies
echo "📦 Installing frontend dependencies..."
cd ../frontend
npm install

# Build frontend for production
echo "🔨 Building frontend..."
cd ../frontend
# Disable CI checks and continue even if build has warnings
CI=false DISABLE_ESLINT_PLUGIN=true npm run build 2>&1 || echo "⚠️ Frontend build had issues, but continuing..."

# Start backend (this will be the main process)
echo "✅ Starting backend server..."
cd ../backend
# Ensure we can find user-installed packages
export PATH="$HOME/.local/bin:$PATH"
export PYTHONPATH="$HOME/.local/lib/python3.10/site-packages:$PYTHONPATH"
python3 app_with_frontend.py
