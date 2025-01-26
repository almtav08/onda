# Step 5
import random
import time
import streamlit as st
from gradio_client import Client


def response_generator(prompt):
    response = st.session_state.client.predict(
        message={"text": prompt, "files": []},
        api_name="/chat_4",
    )
    response = response.replace("<s>", "").replace("</s>", "").strip()
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Custom Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "client" not in st.session_state:
    st.session_state.client = Client("AiActivity/AI-Assistant")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("En que puedo ayudarte?"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = ""
        with st.spinner(""):
            for assintant_response in response_generator(prompt):
                response += assintant_response
                message_placeholder.markdown(response + "▌")
        message_placeholder.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
