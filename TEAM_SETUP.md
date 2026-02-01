# 👥 Group Setup Commands - Copy & Paste

Use these commands to set up the project for your team members. No personal paths or secrets included.

---

## 🚀 For Each Team Member

### Clone Repository
```bash
git clone https://github.com/MwMwM-2428/Gemini-Hackathon.git
cd Gemini-Hackathon
```

### Get Your API Key
1. Go to: https://aistudio.google.com/app/apikey
2. Click "Create API key"
3. Copy the key

### Create Environment File
```bash
cp .env.example .env
```

Then edit `.env` and add your API key:
```bash
# Open .env in your editor and change this line:
GEMINI_API_KEY=your_actual_api_key_here
```

### Install Dependencies

**Option A: Using pip**
```bash
pip install -r requirements.txt
```

**Option B: Using conda**
```bash
conda env create -f environment.yml
conda activate Gemini
```

---

## ▶️ Running the Application

### Terminal 1: Start Backend
```bash
source .env
python backend.py
```

Expected output: `Running on http://127.0.0.1:5002`

### Terminal 2: Start Frontend
```bash
python -m http.server 3000
```

Expected output: `Serving HTTP on 0.0.0.0 port 3000`

### Terminal 3 (Optional): Check Health
```bash
curl http://localhost:5002/api/health
```

Expected output: `{"status": "Backend is running!", "port": 5002}`

### Open Browser
```
http://localhost:3000
```

---

## ✅ Verify Everything Works

- [ ] Backend starts without errors
- [ ] Frontend loads in browser
- [ ] Can select interview goal
- [ ] Can record audio OR type text
- [ ] Submit button works
- [ ] Get evaluation results back

---

## 🛑 Stop Services

**Backend:**
```bash
# Press Ctrl+C in the backend terminal
```

**Frontend:**
```bash
# Press Ctrl+C in the frontend terminal
```

---

## 🔧 Troubleshooting

### "Port 5002 already in use"
```bash
lsof -ti :5002 | xargs kill -9
```

### "Port 3000 already in use"
```bash
lsof -ti :3000 | xargs kill -9
```

### "Backend not responding"
```bash
# Check backend is running
ps aux | grep "python backend.py"

# Restart it
python backend.py
```

### "GEMINI_API_KEY not found"
```bash
# Make sure .env file exists
ls -la .env

# Make sure you ran source
source .env

# Verify it was loaded
echo $GEMINI_API_KEY
```

### "Can't connect frontend to backend"
```bash
# Test the health endpoint
curl http://localhost:5002/api/health

# Should return JSON response
```

---

## 📁 What Each File Does

| File | Purpose |
|------|---------|
| `backend.py` | Flask API server |
| `index.html` | Web interface |
| `App.css` | Styling |
| `requirements.txt` | Python dependencies |
| `environment.yml` | Conda environment |
| `.env.example` | Template for secrets |
| `.env` | Your actual API key (never commit!) |

---

## 📚 Documentation

- **README.md** - Project overview
- **SETUP.md** - Detailed setup guide
- **BACKEND_MONITORING.md** - How to monitor backend
- **SETUP_AND_FIX_SUMMARY.md** - Technical details

---

## 🔐 IMPORTANT: API Key Security

✅ **DO:**
- Keep your API key in `.env` file
- Add `.env` to `.gitignore` (already done)
- Use different keys for development vs production
- Rotate keys if they get exposed

❌ **DON'T:**
- Share your API key in Slack/email
- Commit `.env` file to GitHub
- Use same key across all projects
- Paste key in chat messages

---

## 💬 Common Issues & Solutions

| Issue | Fix |
|-------|-----|
| Module not found | Run `pip install -r requirements.txt` |
| Port in use | Kill process: `lsof -ti :5002 \| xargs kill -9` |
| No API key | Create `.env` from `.env.example` |
| Backend slow | Normal on first run, restart it |
| Can't record audio | Check browser permissions |

---

## 🎯 API Endpoints

### Check Backend Health
```bash
curl http://localhost:5002/api/health
```

### Submit Interview Response
```bash
curl -X POST http://localhost:5002/api/evaluate \
  -F "goal=job_tech" \
  -F "text_input=Tell me about your experience" \
  -F "sub_type=Interview"
```

---

## 🎉 You're Ready!

All team members should now be able to:
1. Clone the repo
2. Set up their environment
3. Run the application
4. Test interviews

**Questions?** Check the documentation files or ask the team lead.

---

**Version**: 1.0  
**Last Updated**: January 31, 2026  
**Status**: Production Ready ✅
