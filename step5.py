# Step 5
import random
import time
import streamlit as st


def response_generator():
    response = random.choice(
        [
            "Hola! En que puedo ayudarte?",
            "Hola, humano! Hay algo en lo que pueda ayudarte?",
            "Necesitas ayuda?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Custom Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("En que puedo ayudarte?"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())

    st.session_state.messages.append({"role": "assistant", "content": response})
