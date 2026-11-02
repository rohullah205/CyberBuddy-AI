
import streamlit as st
from modules.ai_helper import ask_gemini


def render_safety_advisor():

    st.title("🛡️ Online Safety Advisor")

    st.write(
        "Get practical recommendations to improve "
        "your online security and privacy."
    )

    topics = [
        "Password Security",
        "Two-Factor Authentication",
        "Social Media Privacy",
        "Email Security",
        "Mobile Phone Security",
        "Wi-Fi and Network Security",
        "Online Scam Prevention",
        "Personal Data Protection"
    ]

    selected_topic = st.selectbox(
        "Select a security topic",
        topics
    )

    user_question = st.text_area(
        "Describe your security concern (optional)"
    )

    if st.button("Get Safety Recommendations"):

        system_instruction = """
        You are CyberShield AI, an online safety advisor.

        Give practical cybersecurity recommendations.
        Explain common risks and how to prevent them.
        Use simple English and clear steps.
        Never ask users for passwords or OTPs.
        """

        prompt = f"""
        Topic: {selected_topic}

        User concern: {user_question}

        Provide useful security recommendations.
        """

        with st.spinner("Generating recommendations..."):

            result = ask_gemini(
                prompt,
                system_instruction
            )

        st.subheader("🔐 Security Recommendations")
        st.markdown(result)
