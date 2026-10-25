import streamlit as st

from pdf_helper import extract_pdf_text
from gemini_helper import analyze_resume_and_jd, extract_score

st.set_page_config(
    page_title="Resume Job Match Scorer",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Resume Job Match Scorer")
st.write( "Upload your Resume and a Job Description to receive an AI-powered ATS analysis." )

st.divider()

# Resume Upload
resume_pdf = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

# JD Input
st.subheader("Job Description")

jd_option = st.selectbox( "Choose Job Description Input Method", ["Upload JD PDF" , "Paste Job Description" ] )

jd_pdf = None
jd_text = ""

if jd_option == "Upload JD PDF":
    jd_pdf = st.file_uploader( "Upload Job Description PDF", type=["pdf"] )
else:
    jd_text = st.text_area( "Paste Job Description", height=250 )

st.divider()

analyze_btn = st.button( "🚀 Analyze Resume", use_container_width=True )

# ANALYSIS
if analyze_btn:
    if resume_pdf is None:
        st.error("Please upload your Resume PDF.")
        st.stop()

    if jd_option == "Upload JD PDF" and jd_pdf is None:
        st.error("Please upload the Job Description PDF.")
        st.stop()

    if jd_option == "Paste Job Description" and jd_text.strip() == "":
        st.error("Please paste the Job Description.")
        st.stop()

    with st.spinner("Extracting Resume..."):
        resume_text = extract_pdf_text(resume_pdf)

    if not resume_text.strip():
        st.error(
            "Couldn't extract any text from the Resume PDF. "
            "It may be a scanned image rather than a text-based PDF — "
            "try a different file or an OCR'd version."
        )
        st.stop()

    if jd_option == "Upload JD PDF":

        with st.spinner("Extracting Job Description..."):
            jd_content = extract_pdf_text(jd_pdf)

        if not jd_content.strip():
            st.error(
                "Couldn't extract any text from the Job Description PDF. "
                "It may be a scanned image rather than a text-based PDF."
            )
            st.stop()

    else:

        jd_content = jd_text

    with st.spinner("Analyzing with Gemini..."):

        analysis = analyze_resume_and_jd(
            resume_text,
            jd_content
        )

    if analysis.strip().startswith("❌ ERROR "):
        st.error(analysis)
        st.stop()

    st.success("Analysis Completed Successfully!")

    st.divider()

    score = extract_score(analysis)

    if score is not None:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.metric("ATS Match Score", f"{score}%")
        with col2:
            st.progress(score / 100)

        st.divider()

    st.subheader("Analysis Report")
    st.markdown(analysis)

    st.divider()

    st.download_button(
        label="📥 Download Analysis",
        data=analysis,
        file_name="Resume_Analysis.txt",
        mime="text/plain",
        use_container_width=True
    )