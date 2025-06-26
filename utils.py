# utils.py

import os
from groq import Groq, GroqError
import streamlit as st  # Only for handling errors in the Streamlit UI

# --- Configuration ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY") or "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"
MODEL = "llama3-8b-8192"

# --- Initialize Groq Client ---
try:
    client = Groq(api_key=GROQ_API_KEY)
except GroqError as e:
    st.error(f"API Key Error: {e}")
    st.stop()

# --- Function to call Groq model ---
def call_groq_api(prompt: str, model: str = MODEL):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            model=model,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except GroqError as e:
        st.error(f"GROQ API Error: {e}")
        return "Sorry, I couldn't process your request right now."