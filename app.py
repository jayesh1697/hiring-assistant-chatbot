# app.py

import streamlit as st
from prompts import greeting_prompt, tech_question_prompt
from utils import call_groq_api

# --- Page Config ---
st.set_page_config(
    page_title="TalentScout 🤖 Hiring Assistant",
    page_icon="💼",
    layout="centered"
)

# --- Styling ---
st.markdown(
    """
    <style>
        .stTextInput>div>div>input {
            border-radius: 0.5rem;
        }
        .stTextArea>div>textarea {
            border-radius: 0.5rem;
        }
        .main {
            background-color: #f9f9f9;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title ---
st.title("💼 TalentScout: AI Hiring Assistant")
st.markdown("### 🤖 Smart Screening | 📋 Custom Questions | 🔐 Private & Secure")

# --- Session State ---
if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False

# --- Candidate Form ---
if not st.session_state['submitted']:
    st.markdown("##### 👋 Welcome! Please fill out your details below to start the screening process.")
    with st.form("candidate_form"):
        st.markdown("### 📝 Candidate Information")
        name = st.text_input("👤 Full Name")
        email = st.text_input("📧 Email Address")
        phone = st.text_input("📱 Phone Number")
        experience = st.slider("🕓 Years of Experience", 0, 30, 1)
        position = st.text_input("💼 Desired Position(s)")
        location = st.text_input("📍 Current Location")

        st.markdown("### 🧠 Tech Stack")
        tech_stack = st.text_area("💻 List the technologies you're skilled in (e.g., Python, Django, SQL)")

        submitted = st.form_submit_button("🚀 Submit & Generate Questions")
        if submitted:
            st.session_state['submitted'] = True
            st.session_state['data'] = {
                "name": name,
                "email": email,
                "phone": phone,
                "experience": experience,
                "position": position,
                "location": location,
                "tech_stack": tech_stack
            }

# --- After Form Submission ---
if st.session_state['submitted']:
    st.success(f"✅ Thanks {st.session_state['data']['name']}! We're generating your custom interview questions...")

    data = st.session_state['data']
    prompt = tech_question_prompt(data['tech_stack'], data['experience'])
    questions = call_groq_api(prompt)

    st.markdown("### 🎯 Custom Interview Questions")
    st.markdown(questions)

    with st.expander("📝 Summary of Your Submission"):
        st.write(f"**Name:** {data['name']}")
        st.write(f"**Email:** {data['email']}")
        st.write(f"**Phone:** {data['phone']}")
        st.write(f"**Experience:** {data['experience']} years")
        st.write(f"**Position:** {data['position']}")
        st.write(f"**Location:** {data['location']}")
        st.write(f"**Tech Stack:** {data['tech_stack']}")

    if st.button("🔚 End Conversation"):
        st.balloons()
        st.success("🎉 Thank you for applying! We'll be in touch soon.")
        st.session_state['submitted'] = False