import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

st.title("AI SDR Assistant")

user_input = st.text_area("Enter your prompt")

def generate_response(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an AI SDR assistant specialized in personalized cold outreach and company research."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=800
    )

    return response.choices[0].message.content

if st.button("Generate"):
    if user_input:
        output = generate_response(user_input)
        st.write(output)