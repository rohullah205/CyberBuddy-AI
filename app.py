
import streamlit as st
import config

from modules.chatbot import render_chatbot
from modules.phishing import render_phishing_detector
from modules.safety import render_safety_advisor


# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title=f"{config.APP_NAME} | {config.APP_TAGLINE}",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------- CUSTOM THEME ----------------

st.markdown(
    config.DARK_THEME_CSS,
    unsafe_allow_html=True
)


# ---------------- SIDEBAR NAVIGATION ----------------

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
        key="navigation",
        index=0
    )

    st.markdown("---")

    st.caption(f"Version {config.VERSION}")

    st.caption("Developed for BS Cybersecurity Portfolio")


# ---------------- DASHBOARD OVERVIEW ----------------

if navigation == "🏠 Dashboard Overview":

    st.markdown(
        f"<h1 class='cyber-title'>{config.APP_NAME}</h1>",
        unsafe_allow_html=True
    )

    st.markdown(f"**{config.APP_TAGLINE}**")

    st.markdown("---")

    st.subheader("🚀 Security Features")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="cyber-card">
            <h3>🤖 AI Assistant</h3>
            <p>
            Ask questions about malware, firewalls,
            network security, and cryptography.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="cyber-card">
            <h3>🔍 Phishing Detection</h3>
            <p>
            Analyze suspicious links and email text
            to identify potential phishing threats.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="cyber-card">
            <h3>🛡️ Safety Advisor</h3>
            <p>
            Get practical recommendations about
            passwords, 2FA, and online safety.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("💡 Security Tip of the Day")

    st.info(
        "Never click suspicious links received through "
        "emails or messages. Always verify the website "
        "before entering your personal information."
    )

    st.markdown("---")

    st.caption(
        "Stay alert. Stay protected. Stay secure. 🔐"
    )


# ---------------- AI ASSISTANT ----------------

elif navigation == "💬 AI Assistant":

    st.title("💬 AI Cybersecurity Assistant")

    render_chatbot()


# ---------------- PHISHING DETECTOR ----------------

elif navigation == "🔍 Phishing Detector":

    st.title("🔍 Phishing Detection System")

    render_phishing_detector()


# ---------------- SAFETY ADVISOR ----------------

elif navigation == "🛡️ Safety Advisor":

    st.title("🛡️ Online Safety Advisor")

    render_safety_advisor()


# ---------------- ERROR HANDLING ----------------

else:

    st.error("Invalid navigation option. Please select a valid feature.")
