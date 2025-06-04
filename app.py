import streamlit as st
from resume_parser import extract_text_pdf
from matcher import get_match_analysis
from fpdf import FPDF
import os
import re

def remove_emojis(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)  # removes non-ASCII characters like emojis

st.set_page_config(page_title="Resume Match Bot", layout="centered")
st.title("🧠 Resume Match Bot")

# Upload resume
resume_file = st.file_uploader("📄 Upload your Resume (PDF)", type=["pdf"])

# Enter JD text
jd_text_input = st.text_area("📋 Paste the Job Description here")

# Button
if st.button("🔍 Match Now"):
    if resume_file is not None and jd_text_input.strip():
        with st.spinner("Matching your resume with the job description..."):
            resume_bytes = resume_file.read()
            with open("temp_resume.pdf", "wb") as f:
                f.write(resume_bytes)
            resume_text = extract_text_pdf("temp_resume.pdf")
            result = get_match_analysis(resume_text, jd_text_input)

        st.subheader("📊 Match Result:")
        st.markdown(result, unsafe_allow_html=True)

        # ✅ PDF generation + download
        from fpdf import FPDF
        import re

        def remove_emojis(text):
            return re.sub(r'[^\x00-\x7F]+', '', text)

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        safe_result = remove_emojis(result)
        for line in safe_result.split("\n"):
            pdf.multi_cell(0, 10, line)

        os.makedirs("outputs", exist_ok=True)
        pdf_path = "outputs/match_report.pdf"
        pdf.output(pdf_path)

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📥 Download Match Report as PDF",
                data=f,
                file_name="match_report.pdf",
                mime="application/pdf"
            )

        st.success(f"📁 PDF saved at: `{pdf_path}`")

    else:
        st.error("❌ Please upload a resume **and** paste a job description before clicking 'Match Now'.")
