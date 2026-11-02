import os
import streamlit as st

# Application Details
APP_NAME = "CyberBuddy AI"
APP_TAGLINE = "Learn. Detect. Protect."
VERSION = "1.0.0"

# Custom CSS for Dark Navy Cybersecurity Theme
DARK_THEME_CSS = """
<style>
    /* Main Background & Text Color */
    .stApp {
        background-color: #0B0E14;
        color: #E2E8F0;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #1F2937;
    }
    
    /* Cybersecurity Card Styling */
    .cyber-card {
        background-color: #131B2E;
        border: 1px solid #1E293B;
        border-left: 4px solid #00F0FF;
        border-radius: 8px;
        padding: 18px;
        margin-bottom: 15px;
    }
    
    /* Custom Title Accents */
    .cyber-title {
        color: #00F0FF;
        font-weight: 700;
        letter-spacing: 0.5px;
    }

    /* Warning Indicators */
    .warning-box {
        background-color: #2D1517;
        border: 1px solid #7F1D1D;
        border-left: 4px solid #EF4444;
        border-radius: 8px;
        padding: 15px;
        color: #FCA5A5;
    }
    
    /* Safe Indicators */
    .safe-box {
        background-color: #062C1E;
        border: 1px solid #065F46;
        border-left: 4px solid #10B981;
        border-radius: 8px;
        padding: 15px;
        color: #A7F3D0;
    }
</style>
"""


def get_api_key():
  """Retrieves the API key securely from Streamlit secrets or OS environment variables."""
  # First try Streamlit secrets (useful for local .streamlit/secrets.toml or Streamlit Cloud)
  if "GEMINI_API_KEY" in st.secrets:
    return st.secrets["GEMINI_API_KEY"]
  elif "GROQ_API_KEY" in st.secrets:
    return st.secrets["GROQ_API_KEY"]

  # Fallback to system environment variables
  return os.getenv("GEMINI_API_KEY") or os.getenv("GROQ_API_KEY")
