
import streamlit as st
import config

from modules.chatbot import render_chatbot
from modules.phishing import render_phishing_detector
from modules.safety import render_safety_advisor


# Page configuration
st.set_page_config(
    page_title=f"{config.APP_NAME} | {config.APP_TAGLINE}",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown(config.DARK_THEME_CSS, unsafe_allow_html=True)


# Sidebar
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
            "🛡️ Safety Advisor"
        ],
        key="navigation"
    )

    st.markdown("---")
    st.caption(f"Version {config.VERSION}")
    st.caption("BS Cybersecurity Portfolio")


# Dashboard
if navigation == "🏠 Dashboard Overview":

    st.markdown(
        f"<h1 class='cyber-title'>{config.APP_NAME}</h1>",
        unsafe_allow_html=True
    )

    st.markdown(f"**{config.APP_TAGLINE}**")

    st.write("---")
    st.subheader("🚀 Our Security Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="cyber-card">
            <h3>🤖 AI Assistant</h3>
            <p>Ask cybersecurity questions about malware,
            firewalls, cryptography and network security.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="cyber-card">
            <h3>🔍 Phishing Detector</h3>
            <p>Analyze suspicious URLs and email messages
            for possible phishing indicators.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="cyber-card">
            <h3>🛡️ Safety Advisor</h3>
            <p>Learn about strong passwords, two-factor
            authentication and online privacy.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("💡 Security Tip of the Day")

    st.info(
        "Never enter your password after clicking an "
        "unexpected link. Open the official website "
        "directly and verify the address."
    )

    st.markdown("---")

    st.success("Stay alert. Stay protected. Stay secure. 🔐")


# AI Assistant
elif navigation == "💬 AI Assistant":
    render_chatbot()


# Phishing Detector
elif navigation == "🔍 Phishing Detector":
    render_phishing_detector()


# Safety Advisor
elif navigation == "🛡️ Safety Advisor":
    render_safety_advisor()
