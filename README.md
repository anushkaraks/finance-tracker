# AI-Powered Personal Finance Tracker

An intelligent finance tracker that parses bank statements, 
categorizes spending using AI, detects patterns, and flags anomalies.

## Features
- Upload CSV bank statements
- AI-powered transaction categorization
- Spending pattern analysis
- Anomaly detection
- Clean web dashboard

## Tech Stack
- **Backend:** Python, Pandas
- **AI:** LLM API (Claude/OpenAI)
- **Frontend:** HTML, CSS, JavaScript

## Setup
# Clone the repo
git clone https://github.com/YOUR_USERNAME/finance-tracker.git
cd finance-tracker

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install pandas

# Run
cd backend
python main.py

## Project Structure
Finance Tracker/
├── backend/
│   ├── main.py        # Entry point
│   ├── parser.py      # CSV parser
│   └── ai_engine.py   # AI integration
├── frontend/          # Web UI 
├── sample_data/       # Test statements
└── README.md
