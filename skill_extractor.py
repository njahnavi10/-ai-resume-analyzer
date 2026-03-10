from skills import skills_list

def extract_skills(resume_text):

    resume_text = resume_text.lower()

    found_skills = []

    for skill in skills_list:

        if skill in resume_text:
            found_skills.append(skill)

    return found_skills 
def missing_skills(resume_skills, jd_skills):

    missing = []

    for skill in jd_skills:
        if skill not in resume_skills:
            missing.append(skill)

    return missing