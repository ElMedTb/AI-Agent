#!/bin/bash

# Replit startup script
echo "🚀 Starting HR Onboarding Assistant..."

# Install backend dependencies
echo "📦 Installing backend dependencies..."
cd backend
pip install -r requirements.txt

# Install frontend dependencies
echo "📦 Installing frontend dependencies..."
cd ../frontend
npm install

# Build frontend for production
echo "🔨 Building frontend..."
npm run build

# Start backend (this will be the main process)
echo "✅ Starting backend server..."
cd ../backend
python app_with_frontend.py

