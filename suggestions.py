def generate_suggestions(score, missing_skills):

    suggestions = []

    if score < 50:
        suggestions.append("Your resume is poorly aligned with this job description.")
        suggestions.append("Consider tailoring your resume for the specific role.")

    elif score < 75:
        suggestions.append("Your resume partially matches this job.")
        suggestions.append("Adding missing skills and projects will improve your chances.")

    else:
        suggestions.append("Great! Your resume aligns well with this job.")

    # Suggestions based on missing skills
    for skill in missing_skills:
        suggestions.append(f"Consider adding experience or projects related to {skill}.")

    return suggestions