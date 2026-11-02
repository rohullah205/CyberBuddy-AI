
import streamlit as st
from modules.ai_helper import ask_gemini


def render_chatbot():

    st.title("💬 AI Cybersecurity Assistant")

    st.write(
        "Ask questions about cybersecurity, "
        "network security, malware and ethical hacking."
    )

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    col1, col2 = st.columns([4, 1])

    with col1:
        st.caption("Powered by Google Gemini Flash")

    with col2:
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()

    st.markdown("---")

    # Display previous messages
    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    user_input = st.chat_input(
        "Ask a cybersecurity question..."
    )

    if user_input:

        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input
        })

        with st.chat_message("user"):
            st.markdown(user_input)

        system_instruction = """
        You are CyberShield AI, a helpful cybersecurity
        education assistant.

        Your responsibilities:
        1. Explain cybersecurity topics in simple language.
        2. Help users understand malware and phishing.
        3. Explain firewalls, encryption and network security.
        4. Promote ethical hacking and legal security practices.
        5. Give practical defensive security advice.

        Do not help with unauthorized access, malware
        deployment, credential theft or cyber attacks.
        Keep answers educational, clear and organized.
        """

        # Include previous conversation for context
        conversation = []

        for message in st.session_state.chat_history[-12:]:
            conversation.append(
                f"{message['role'].upper()}: "
                f"{message['content']}"
            )

        prompt = "\n\n".join(conversation)

        with st.chat_message("assistant"):

            with st.spinner("CyberShield AI is thinking..."):

                answer = ask_gemini(
                    prompt,
                    system_instruction
                )

                st.markdown(answer)

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": answer
        })
