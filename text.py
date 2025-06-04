from matcher import get_match_analysis
from resume_parser import extract_text_pdf
from jd_pasrser import load_jd_text
resume_text = extract_text_pdf("sample_resume.pdf")
jd_text = load_jd_text("sample_jd.txt")

result = get_match_analysis(resume_text, jd_text)
print(result)
