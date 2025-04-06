# 🤖 AI-Powered Resume Analyzer

A smart resume analyzer built with **Streamlit** and **Python** that extracts skills from uploaded resumes and matches them against predefined job roles like AI Engineer, Full Stack Developer, and more.

---

## 🚀 Features
- 📄 PDF Resume Upload
- 🧠 Skill Extraction from Resume
- 🎯 Role Fit Analysis for CSE-related roles
- ⚡ Clean, Responsive UI using Streamlit

---

## 🛠️ Tech Stack
- Python 🐍
- Streamlit 🎈
- Regex & NLP for skill extraction
- Role Matching Logic with Category-wise Scores

---

## 📂 Project Structure

```bash
resume_analyzer/
│
├── app.py                # Streamlit frontend
├── resume_parser.py      # Text extraction from PDF
├── skills.py             # Skill categories & extractor
├── role_matcher.py       # Role matching logic
├── requirements.txt      # Python dependencies
└── README.md             # You’re here!
# Resume_analyzer
```

## 🧪 Run Locally
```bash
git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer
pip install -r requirements.txt
streamlit run app.py
