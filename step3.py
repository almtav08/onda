# Step 3
import streamlit as st

st.title("Custom Chatbot")

if prompt := st.chat_input("En que puedo ayudarte?"):
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        st.write("Lo siento, no puedo ayudarte con eso.")