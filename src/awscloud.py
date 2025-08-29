from openai import OpenAI
import streamlit as st
from prompts import get_system_prompt


client = OpenAI(api_key=st.secrets.OPENAI_API_KEY)

st.title("🔮 AWS Certified Cloud Practitioner")

# Initialize the chat messages history
if "messages" not in st.session_state:
    # system prompt includes table information, rules, and prompts the LLM to produce
    # a welcome message to the user.
    st.session_state.messages = [{"role": "system", "content": get_system_prompt()}]

# Prompt for user input and save
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})

# display the existing chat messages
for message in st.session_state.messages:
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if "results" in message:
            st.dataframe(message["results"])


# If last message is not from assistant, we need to generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        response = ""
        resp_container = st.empty()
        for delta in client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            content = delta.choices[0].delta.content
            if content is not None:
                response += content
                resp_container.markdown(response)

        message = {"role": "assistant", "content": response}

        st.session_state.messages.append(message)
