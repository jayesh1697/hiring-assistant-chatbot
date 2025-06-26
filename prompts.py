# prompts.py

def greeting_prompt():
    return "Hello! I'm TalentScout Bot, your virtual hiring assistant. I’ll help collect your info and assess your skills."

def tech_question_prompt(tech_stack, experience):
    return f"""
You are a senior technical interviewer. A candidate has {experience} years of experience and is skilled in: {tech_stack}.
Generate 3 to 5 technical interview questions to evaluate the candidate's depth in each mentioned technology.
Make sure the questions are practical and aligned with real-world scenarios.
"""