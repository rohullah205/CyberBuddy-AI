
import os
import streamlit as st
from google import genai


MODEL_NAME = "gemini-flash-latest"


def get_api_key():
    """Get Gemini API key from Streamlit secrets or environment."""

    try:
        api_key = st.secrets.get("GEMINI_API_KEY", "")
    except Exception:
        api_key = ""

    if not api_key:
        api_key = os.getenv("GEMINI_API_KEY", "")

    return api_key


def ask_gemini(prompt, system_instruction):
    """Send a prompt to Gemini and return its response."""

    api_key = get_api_key()

    if not api_key:
        return (
            "Gemini API key is missing. "
            "Please add GEMINI_API_KEY in Streamlit Secrets."
        )

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config={
                "system_instruction": system_instruction,
                "temperature": 0.4,
                "max_output_tokens": 1500
            }
        )

        if response.text:
            return response.text

        return "Gemini did not return a text response. Please try again."

    except Exception as error:
        return (
            "Unable to connect to Gemini. "
            "Please check your API key, model access, "
            "internet connection and API quota. "
            f"Technical details: {str(error)[:300]}"
        )
