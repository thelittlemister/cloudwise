import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

## Validate OpenAI connection ##

completion = client.chat.completions.create(
    model="gpt-4o-mini", messages=[{"role": "user", "content": "What is Streamlit?"}]
)

st.write(completion.choices[0].message.content)
