# 🤖 AI Resume Analyzer

An AI-powered web application that analyzes resumes against job descriptions and provides insights such as skill matching, missing skills, resume score, and improvement suggestions.

This tool helps job seekers optimize their resumes to better match job requirements.

---

## 🚀 Live Demo

```
(https://v6ciksjekw2cq6wuckylry.streamlit.app/)
```

---

## 📌 Features

✔ Upload resume in **PDF format**
✔ Extract text from resumes automatically
✔ Compare resume with **job description**
✔ Identify **matched skills**
✔ Detect **missing skills**
✔ Calculate **resume-job match score**
✔ Provide **AI-based resume improvement suggestions**
✔ Display **visual skill match chart**

---

## 🧠 How It Works

1. User uploads a resume.
2. User pastes a job description.
3. The system extracts text from the resume.
4. Skills are identified using NLP techniques.
5. The resume is compared with job requirements.
6. The application generates:

   * Resume score
   * Matched skills
   * Missing skills
   * Resume improvement suggestions
   * Skill match visualization.

---

## 🛠 Technologies Used

* **Python**
* **Streamlit**
* **Matplotlib**
* **Natural Language Processing (NLP)**
* **PyPDF2**
* **Sentence Transformers**
* **Scikit-learn**

---

## 📂 Project Structure

```
AI-Resume-Analyzer
│
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── similarity.py
├── suggestions.py
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

Clone the repository:

```
git clone https://github.com/yourusername/ai-resume-analyzer.git
```

Navigate to the project folder:

```
cd ai-resume-analyzer
```

Create virtual environment:

```
python -m venv venv
```

Activate environment:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

---

## 📊 Example Output

The application generates:

* Resume match percentage
* Resume feedback
* Skills found in resume
* Required job skills
* Missing skills
* Skill match visualization

---

## 🎯 Future Improvements

* Automatic resume section detection
* ATS score prediction
* Resume improvement suggestions using LLM
* Resume download report (PDF)
* Job recommendation system

---

## 👩‍💻 Author

**Jahnavi N**


---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
