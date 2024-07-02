import streamlit as st
import openai
import os
#import requests

# Set your OpenAI API key here
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Sidebar with social profiles and model parameters
st.sidebar.markdown("Check my profiles:")
st.sidebar.markdown(
    """<a href="https://github.com/ferrarisimone94/NLP_to_SQL/edit/main/Home.py"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="60px"></a>
    <a href="https://www.linkedin.com/in/simonepaoloferrari/" target="_blank"><img src="https://cdn1.iconfinder.com/data/icons/logotypes/32/circle-linkedin-512.png" alt="LinkedIn" width="60px"></a>
   """,
    unsafe_allow_html=True,
)

# Function to interact with the GPT-3.5-turbo model with tunable parameters
def generate_response(prompt):
    messages = [
        {"role": "system", "content": ""},
        {"role": "user", "content": prompt},
    ]
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        n=2,
        stop="None",
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content

st.write("New Project")

# Main app where user enters prompt and gets the response
user_input = st.text_area("")
input_button = st.button("Ask")

if input_button:
    st.write("Assistant:")
    st.write(generate_response(user_input))
