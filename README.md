
# 🛡️ CyberShield AI

### Your Intelligent Cybersecurity Companion

CyberShield AI is an AI-powered cybersecurity dashboard
developed using Python, Streamlit and Google Gemini Flash.

## Features

### 1. AI Cybersecurity Assistant
- Answers cybersecurity questions.
- Explains malware, firewalls and encryption.
- Provides educational security guidance.

### 2. Phishing Detection System
- Analyzes suspicious URLs.
- Examines suspicious email messages.
- Identifies possible phishing indicators.
- Provides AI-based security analysis.

### 3. Online Safety Advisor
- Password security recommendations.
- Two-factor authentication guidance.
- Social media privacy.
- Email and mobile security.
- Online scam prevention.

## Technologies Used

- Python
- Streamlit
- Google Gemini Flash
- Google Gen AI SDK

## Project Structure

CyberShield-AI/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── modules/
    ├── __init__.py
    ├── ai_helper.py
    ├── chatbot.py
    ├── phishing.py
    └── safety.py

## Installation

Install the dependencies:

pip install -r requirements.txt

## API Configuration

Create a Gemini API key from:

https://aistudio.google.com/apikey

For local execution, set the GEMINI_API_KEY
environment variable.

For Streamlit Cloud, add the key under
App Settings > Secrets.

Example:

GEMINI_API_KEY = "your_api_key_here"

## Run the Application

streamlit run main.py

## Deployment

Deploy using Streamlit Community Cloud
and connect your GitHub repository.

## Disclaimer

CyberShield AI is an educational cybersecurity
assistant. Its phishing analysis is preliminary
and should not replace professional security tools.

The application does not guarantee that a URL,
email or website is safe.

## Developer

BS Cybersecurity Portfolio Project
