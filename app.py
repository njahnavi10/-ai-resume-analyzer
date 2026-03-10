import streamlit as st
import matplotlib.pyplot as plt
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills, missing_skills
from similarity import calculate_similarity
from suggestions import generate_suggestions
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}

/* Main headings */
h1 {
    color: #ffffff;
}

h2, h3 {
    color: #e8f6f3;
}

/* Normal text */
p, label {
    color: #ecf0f1 !important;
}

/* Upload box text */
.css-1cpxqw2, .css-1dp5vir {
    color: #ffffff !important;
}

/* Text area */
textarea {
    background-color: #ffffff !important;
    color: #2c3e50 !important;
}

/* Button */
.stButton>button {
    background-color:#ff7e5f;
    color:white;
    border-radius:8px;
} 


/* Uploaded file name container */
[data-testid="stFileUploaderFileName"] {
    color: white !important;
}

/* Remove button (X) */
[data-testid="stFileUploaderDeleteBtn"] {
    color: red !important;
}
/* Metric cards */
[data-testid="stMetric"] {
    background-color: rgba(255,255,255,0.08);
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
"<h1 style='text-align:center;color:#00ffd5;'>AI Resume Analyzer</h1>",
unsafe_allow_html=True
)

st.write("Upload your resume and compare it with job description")

uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

job_description = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):

    if uploaded_resume and job_description:

        resume_text = extract_text_from_pdf(uploaded_resume)

        resume_skills = extract_skills(resume_text)

        jd_skills = extract_skills(job_description)

        score = calculate_similarity(resume_text, job_description)

        missing = missing_skills(resume_skills, jd_skills) 

        suggestions = generate_suggestions(score, missing)
# -------------------- SCORE --------------------

        st.divider()
        st.markdown("<h2 style='color:#f1f1f1;'>## 📊Resume Score</h2>", unsafe_allow_html=True)
        st.progress(int(score))
        st.write(f"{score}% Match")

 # -------------------- FEEDBACK --------------------

        st.divider()
        st.markdown("<h2 style='color:#f1f1f1;'>## 💬 Resume Feedback</h2>", unsafe_allow_html=True)


        if score < 50:
            st.error("Your resume is not well aligned with this job description.")

        elif score < 75:
            st.warning("Your resume partially matches this job. Add missing skills and projects.")

        else:
            st.success("Your resume is a strong match for this role!") 

# -------------------- RESUME SKILLS --------------------

        st.divider()

        st.markdown("<h2 style='color:#f1f1f1;'>## 🟢Skills Found in Resume</h2>", unsafe_allow_html=True)

        cols = st.columns(4)

        for i, skill in enumerate(resume_skills):
            cols[i % 4].success(skill)
# -------------------- JOB SKILLS --------------------

        st.divider()
        st.markdown("<h2 style='color:#f1f1f1;'>## 🔵Skills Required for Job</h2>", unsafe_allow_html=True)

        cols = st.columns(4)

        for i, skill in enumerate(jd_skills):
            cols[i % 4].info(skill)
 # -------------------- MISSING SKILLS --------------------

        st.divider()
        st.markdown("<h2 style='color:#f1f1f1;'>## 🔴Missing Skills</h2>", unsafe_allow_html=True)

        if missing:
            cols = st.columns(3)
            for i, skill in enumerate(missing):
                cols[i % 3].error(skill)
        else:
            st.success("No missing skills 🎉") 

# -------------------- MATCHED SKILLS --------------------

        st.divider()
        matched_skills = list(set(resume_skills) & set(jd_skills))

        st.markdown("<h2 style='color:#f1f1f1;'>## ✅Matched Skills</h2>", unsafe_allow_html=True)

        cols = st.columns(3)
        for i, skill in enumerate(matched_skills):
            cols[i % 3].success(skill) 
    
          # -------------------- DASHBOARD METRICS --------------------

        st.divider()
        st.markdown("<h2 style='color:#f1f1f1;'>## 📈 Analysis Summary</h2>",unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Resume Score", f"{score:.1f}%")
            

        with col2:
            st.metric("Matched Skills", len(matched_skills)) 
           

        with col3:
            st.metric("Missing Skills", len(missing))  
           
        matched = len(set(resume_skills) & set(jd_skills))
        missing_count = len(set(jd_skills) - set(resume_skills)) 

        #----------------------Suggestions---------------------------
        st.divider()
        st.markdown("<h2 style='color:#f1f1f1;'>## 🤖 AI Resume Suggestions</h2>",unsafe_allow_html=True)

        for suggestion in suggestions:
            st.markdown(f"✔ {suggestion}")

# -------------------- PIE CHART --------------------

        st.divider()
        labels = ['Matched Skills', 'Missing Skills']
        values = [matched, missing_count]
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%',colors=["#29d270",'#e74c3c'], startangle=90)

        st.subheader("Skill Match Visualization")
        st.pyplot(fig)


    else:

        st.warning("Please upload resume and job description") 


