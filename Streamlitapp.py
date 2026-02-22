#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st
from groq import Groq
import os

# 🔐 Paste your Groq API key here
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")

st.title("⚡Ultra-Fast Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # API call
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",   # fast & free model
        messages=st.session_state.messages,
        temperature=0.7
    )

    reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)


# In[ ]:




