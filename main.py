# main.py

import streamlit as st
from model_utils import get_career_recommendations
from resume_parser import parse_resume, analyze_resume

# Set up Streamlit page
st.set_page_config(page_title="AI Career Mentor Bot", layout="wide")

st.title("🎓 AI Career Mentor Bot")

# Create tabs
tab1, tab2 = st.tabs(["🧠 Career Suggestion", "📄 Resume Analyzer"])

# ========== Career Suggestion Tab ==========
with tab1:
    st.header("Tell us about yourself")
    
    interests = st.text_area("Your Interests", placeholder="e.g., AI, robotics, healthcare...")
    skills = st.text_area("Your Skills", placeholder="e.g., Python, writing, teamwork...")
    goals = st.text_area("Your Career Goals", placeholder="e.g., remote job, high salary, research...")

    if st.button("Get Career Suggestions"):
        if interests and skills and goals:
            results = get_career_recommendations(interests, skills, goals)
            st.subheader("🔍 Recommended Careers")
            for career in results:
                st.markdown(f"### {career['title']}")
                st.write(f"**Why this fits you:** {career['summary']}")
                st.write(f"**Learning Roadmap:**\n{career['roadmap']}")
                st.write(f"**Estimated Salary:** ${career['salary']:,}")
                st.markdown("---")
        else:
            st.warning("Please fill out all fields before clicking the button.")

# ========== Resume Analyzer Tab ==========
with tab2:
    st.header("Upload Your Resume for Feedback")
    
    file = st.file_uploader("Choose a resume file (PDF or DOCX)", type=["pdf", "docx"])

    if file:
        with st.spinner("Reading your resume..."):
            resume_text = parse_resume(file)
            if resume_text.strip():
                feedback = analyze_resume(resume_text)
                st.markdown("### 📋 Resume Feedback")
                st.write(feedback)
            else:
                st.error("Could not extract text from the resume. Please try a different file.")
