README - AI Interview Prep Tool

QUICK START

1. Clone repository
   git clone https://github.com/MwMwM-2428/Gemini-Hackathon.git
   cd Gemini-Hackathon

2. Get API key
   Go to: https://aistudio.google.com/app/apikey
   Create new API key (free)

3. Setup
   cp .env.example .env
   Edit .env and add your API key
   pip install -r requirements.txt

4. Run backend (Terminal 1)
   source .env
   python backend.py

5. Run frontend (Terminal 2)
   python -m http.server 3000

6. Open browser
   http://localhost:3000


FEATURES

- Audio recording and playback
- File upload (resume/job description)
- Text input for responses
- AI-powered evaluation with scoring
- Detailed feedback metrics
- Responsive web interface


SYSTEM REQUIREMENTS

- Python 3.8+
- Google Gemini API key (free)
- Modern web browser
- Port 5002 and 3000 available


PROJECT STRUCTURE

backend.py                  Flask API server (port 5002)
index.html                  Web interface
App.css                     Styling
Frontend.jsx / Frontend.js  Component versions
requirements.txt            Python dependencies
environment.yml             Conda environment
.env.example               Environment template


CONFIGURATION

Copy .env.example to .env:
   cp .env.example .env

Edit .env and set:
   GEMINI_API_KEY=your_key_here
   FLASK_ENV=development
   BACKEND_PORT=5002
   FRONTEND_PORT=3000

IMPORTANT: Never commit .env file. It's in .gitignore.


API ENDPOINTS

GET /api/health
Check if backend is running
Response: {"status": "Backend is running!", "port": 5002}

POST /api/evaluate
Submit interview response for evaluation
Parameters:
- goal: "university", "club", or "job_tech"
- text_input: User's response (string)
- context_text: Interview context (optional)
- file: Resume PDF (optional)
- audio_response: Audio file (optional)


TROUBLESHOOTING

Port already in use (5002)
   lsof -ti :5002 | xargs kill -9

Port already in use (3000)
   lsof -ti :3000 | xargs kill -9

Backend not responding
   curl http://localhost:5002/api/health

API key not working
   Check .env file has correct key
   Verify key is enabled in Google Cloud


FOR TEAM MEMBERS

1. Clone the repo
2. Copy .env.example to .env
3. Add your own Google API key to .env
4. Run: pip install -r requirements.txt
5. Terminal 1: source .env && python backend.py
6. Terminal 2: python -m http.server 3000
7. Open http://localhost:3000

IMPORTANT: Never commit .env file. Each person uses their own API key.


DOCUMENTATION REFERENCE

Backend monitoring: See BACKEND_MONITORING.md
Extended setup: See SETUP.md
Implementation details: See SETUP_AND_FIX_SUMMARY.md


LICENSE

Add your license information here
