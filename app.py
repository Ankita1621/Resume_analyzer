import streamlit as st
from resume_parser import extract_text_from_pdf
from skills import extract_skills
from role_matcher import calculate_role_fit

st.set_page_config(page_title="AI-Powered Resume Analyzer", layout="wide")

st.title("🤖 AI-Powered Resume Analyzer")
st.markdown("Upload your resume and we'll extract relevant skills from it!")

# File Upload
uploaded_file = st.file_uploader("📄 Upload your Resume (PDF)", type=["pdf"])

# Process the file
if uploaded_file:
    try:
        with st.spinner("⏳ Extracting text..."):
            text = extract_text_from_pdf(uploaded_file)

        st.subheader("📄 Extracted Resume Text")
        st.write(text)

        # Extract and display skills
        st.subheader("🧠 Skills Detected")
        skills = extract_skills(text)

        if skills:
            for category, matched_skills in skills.items():
                st.markdown(f"**🔹 {category}:**")
                st.success(", ".join(matched_skills))
        else:
            st.warning("⚠️ No relevant skills found in the resume.")

        # Analyze role fit
        st.subheader("🎯 Role Fit Analysis")
        role_scores = calculate_role_fit(skills)

        for role, data in role_scores.items():
            st.markdown(f"**🔸 {role}: {data['score']}% match**")
            if data['matched_skills']:
                st.markdown("✅ Matching Skills: " + ", ".join(data['matched_skills']))
            else:
                st.markdown("⚠️ No strong skill matches found.")

    except Exception as e:
        st.error(f"An error occurred: {e}")

    st.markdown("---")
    st.caption("Built with 💻 Streamlit | Made by Ankita 💚")
