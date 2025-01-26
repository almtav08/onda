# Step 2
import streamlit as st

st.title("Custom Chatbot")

with st.chat_message("user"):
    st.write("Hola! 👋")


with st.chat_message("assistant"):
    st.write("Hola humano! 🤖")
