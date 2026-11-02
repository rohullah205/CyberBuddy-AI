
import os
import time
import streamlit as st
from google import genai


# Primary and backup Gemini Flash models
PRIMARY_MODEL = "gemini-3.8-flash"
BACKUP_MODEL = "gemini-3.5-flash-lite"


def get_api_key():

    try:
        api_key = st.secrets.get("GEMINI_API_KEY", "")
    except Exception:
        api_key = ""

    if not api_key:
        api_key = os.getenv("GEMINI_API_KEY", "")

    return api_key


def ask_gemini(prompt, system_instruction):

    api_key = get_api_key()

    if not api_key:
        return (
            "Gemini API key is missing. "
            "Please add GEMINI_API_KEY in "
            "Streamlit Cloud Secrets."
        )

    try:
        client = genai.Client(api_key=api_key)

    except Exception as error:
        return f"Gemini client initialization failed: {error}"

    models = [PRIMARY_MODEL, BACKUP_MODEL]

    for model in models:

        for attempt in range(2):

            try:

                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                    config={
                        "system_instruction": system_instruction,
                        "temperature": 0.4,
                        "max_output_tokens": 1500
                    }
                )

                if response.text:
                    return response.text

                return "Gemini returned an empty response. Please try again."

            except Exception as error:

                error_message = str(error)
                error_lower = error_message.lower()

                temporary_error = any(
                    word in error_lower
                    for word in [
                        "503",
                        "unavailable",
                        "overloaded",
                        "429",
                        "resource_exhausted",
                        "500",
                        "internal server error"
                    ]
                )

                if temporary_error:

                    if attempt == 0:
                        time.sleep(2)
                        continue

                    # Try the backup model
                    break

                return (
                    f"Gemini API Error: {error_message[:400]}"
                )

    return (
        "Both Gemini Flash models are temporarily unavailable. "
        "Please wait a few minutes and try again."
    )
