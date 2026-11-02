import config
from modules.chatbot import render_chatbot
from modules.phishing import render_phishing_detector
from modules.safety import render_safety_advisor
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title=f"{config.APP_NAME} | {config.APP_TAGLINE}",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load Custom Theme CSS
st.markdown(config.DARK_THEME_CSS, unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
  st.title(f"🛡️ {config.APP_NAME}")
  st.caption(config.APP_TAGLINE)
  st.markdown("---")

  navigation = st.radio(
      "Navigate Features",
      [
          "🏠 Dashboard Overview",
          "💬 AI Assistant",
          "🔍 Phishing Detector",
          "🛡️ Safety Advisor",
      ],
      index=0,
  )

  st.markdown("---")
  st.caption(f"Version {config.VERSION}")
  st.caption("Developed for BS Cybersecurity Portfolio")

# --- NAVIGATION ROUTING ---

if navigation == "🏠 Dashboard Overview":
  st.markdown(
      f"<h1 class='cyber-title'>{config.APP_NAME}</h1>", unsafe_allow_html=True
  )
  st.markdown(f"**{config.APP_TAGLINE}**")
  st.write("---")

  # Quick Security Metrics / Cards
  col1, col2, col3 = st.columns(3)

  with col1:
    st.markdown("""
        <div class="cyber-card">
            <h3>🤖 AI Assistant</h3>
            <p>Ask questions about malware, firewalls, network security, and cryptography.</p>
        </div>
        """, unsafe_allow_html=True)

  with col2:
    st.markdown("""
        <div class="cyber-card">
            <h3>🔍 Phishing Detection</h3>
            <p>Analyze suspicious links and email body text for potential phishing indicators.</p>
        </div>
        """, unsafe_allow_html=True)

  with col3:
    st.markdown("""
        <div class="cyber-card">
            <h3>🛡️ Safety Advisor</h3>
            <p>Get practical recommendations for password management, 2FA, and social media.</p>
        </div>
        """, unsafe_allow_html=True)

  st.write("### 💡 Quick Security Tip of the Day")
  st.markdown("""
    > **Never click unsolicited link shorteners (e.g., bit.ly, tinyurl) in emails or messages.** Always inspect the underlying URL before entering credentials or sensitive data.
    """)

elif navigation == "💬 AI Assistant":
  render_chatbot()

elif navigation == "🔍 Phishing Detector":
  render_phishing_detector()

elif navigation == "🛡️ Safety Advisor":
  render_safety_advisor()
