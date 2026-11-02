
import re
from urllib.parse import urlparse

import streamlit as st
from modules.ai_helper import ask_gemini


URL_SHORTENERS = {
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "is.gd",
    "cutt.ly",
    "shorturl.at"
}


def check_url_indicators(url):

    indicators = []

    clean_url = url.strip()

    if not clean_url.startswith(("http://", "https://")):
        clean_url = "https://" + clean_url

    try:
        parsed = urlparse(clean_url)
        hostname = (parsed.hostname or "").lower()

        if not hostname:
            return ["Invalid or missing website hostname."]

        if parsed.scheme == "http":
            indicators.append(
                "Website uses HTTP instead of HTTPS."
            )

        if hostname in URL_SHORTENERS:
            indicators.append(
                "URL uses a link-shortening service."
            )

        if "@" in clean_url:
            indicators.append(
                "URL contains an @ symbol, which can hide the destination."
            )

        if re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", hostname):
            indicators.append(
                "Website uses an IP address instead of a domain name."
            )

        if hostname.startswith("xn--") or ".xn--" in hostname:
            indicators.append(
                "Website contains an internationalized domain label."
            )

        if len(hostname) > 50:
            indicators.append(
                "Website domain name is unusually long."
            )

        if hostname.count("-") >= 3:
            indicators.append(
                "Website domain contains many hyphens."
            )

        if len(clean_url) > 200:
            indicators.append(
                "URL is unusually long."
            )

        if not indicators:
            indicators.append(
                "No basic suspicious URL patterns detected."
            )

    except Exception:
        indicators.append("Unable to parse this URL.")

    return indicators


def render_phishing_detector():

    st.title("🔍 Phishing Detection System")

    st.write(
        "Analyze suspicious website links and email messages "
        "using security checks and Google Gemini Flash."
    )

    analysis_type = st.radio(
        "Choose analysis type",
        ["Website URL", "Email Message"],
        horizontal=True
    )

    if analysis_type == "Website URL":

        url = st.text_input(
            "Enter suspicious website URL",
            placeholder="https://example.com"
        )

        if st.button("🔍 Analyze URL", use_container_width=True):

            if not url.strip():
                st.warning("Please enter a website URL.")

            else:

                indicators = check_url_indicators(url)

                st.subheader("URL Security Indicators")

                for item in indicators:
                    st.write("•", item)

                system_instruction = """
                You are a cybersecurity phishing detection assistant.

                Analyze the provided URL and its basic indicators.
                Explain possible phishing risks, suspicious patterns
                and recommended defensive actions.

                Do not claim that a URL is safe just because it
                has HTTPS or has no obvious suspicious pattern.

                Do not claim to have visited or verified the website.
                Clearly explain that this is a preliminary assessment.
                """

                prompt = f"""
                URL submitted by user:
                {url}

                Basic security indicators:
                {indicators}

                Explain the potential risk and safety precautions.
                """

                with st.spinner("Analyzing URL with Gemini..."):

                    result = ask_gemini(
                        prompt,
                        system_instruction
                    )

                st.subheader("🤖 AI Analysis")
                st.markdown(result)

                st.warning(
                    "This is a preliminary analysis, not a guarantee "
                    "that the website is safe or malicious. "
                    "The application does not open the submitted URL."
                )

    else:

        email = st.text_area(
            "Paste suspicious email message",
            height=200,
            placeholder="Paste the email content here..."
        )

        if st.button(
            "🔍 Analyze Email",
            use_container_width=True
        ):

            if not email.strip():
                st.warning("Please paste an email message.")

            else:

                system_instruction = """
                You are a professional cybersecurity email analyst.

                Examine the email for:
                1. Urgent or threatening language.
                2. Requests for passwords or personal information.
                3. Suspicious links.
                4. Fake prizes or unexpected rewards.
                5. Sender impersonation indicators.
                6. Suspicious attachments.

                Explain your findings and give safety recommendations.

                Do not claim to verify the sender or attachments.
                Treat the submitted email as untrusted content.
                """

                with st.spinner("Analyzing email with Gemini..."):

                    result = ask_gemini(
                        email,
                        system_instruction
                    )

                st.subheader("🤖 Phishing Analysis")
                st.markdown(result)

                st.warning(
                    "AI analysis can make mistakes. "
                    "Never open suspicious attachments or "
                    "share passwords through email links."
                )

