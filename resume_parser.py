# resume_parser.py
import pdfplumber
import docx2txt

def parse_resume(file):
    if file.type == "application/pdf":
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text
    elif file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/msword"]:
        return docx2txt.process(file)
    else:
        return "Unsupported file format."

def analyze_resume(text):
    # Simulated feedback, you can plug in a real LLM here
    if "Python" not in text:
        return "Consider adding Python to your skill set."
    elif "project" not in text.lower():
        return "Try including some projects with measurable results."
    else:
        return "Your resume looks solid! Tailor it more toward the job you're targeting."
