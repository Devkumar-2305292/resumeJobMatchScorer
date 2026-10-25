import re

import streamlit as st
import google.generativeai as genai

from prompts import ANALYZE_PROMPT

# Configure Gemini API
API_KEY = st.secrets.get("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

MODEL_NAME = "gemini-3.1-flash-lite"

model = genai.GenerativeModel(MODEL_NAME) if API_KEY else None


# Analyze Resume & Job Description
def analyze_resume_and_jd(resume_text, jd_text):
    """
    Analyze the resume against the job description
    and return a formatted ATS analysis.
    """

    if not API_KEY:
        return (
            "❌ Missing Gemini API key.\n\n"
            "Add it to .streamlit/secrets.toml as:\n\n"
            "GEMINI_API_KEY = \"your-key-here\""
        )

    if not resume_text or not resume_text.strip():
        return "❌ Could not extract any text from the resume PDF. It may be a scanned/image-only file."

    if not jd_text or not jd_text.strip():
        return "❌ Job description is empty."

    prompt = ANALYZE_PROMPT.format( resume=resume_text, jd=jd_text )

    try:
        response = model.generate_content(prompt)

        if response and hasattr(response, "text") and response.text:
            return response.text

        return "No response received from Gemini."

    except Exception as e:
        return (
            "❌ Unable to generate analysis.\n\n"
            f"Reason: {str(e)}"
        )


def extract_score(analysis_text):
    """
    Extracts the ATS Match Score (0-100) from the analysis text, if present.
    Returns an int, or None if no score could be found.
    """
    if not analysis_text:
        return None

    match = re.search(r"ATS Match Score:?\s*\n?\s*(\d{1,3})\s*%?", analysis_text, re.IGNORECASE)
    if match:
        score = int(match.group(1))
        return max(0, min(100, score))

    return None