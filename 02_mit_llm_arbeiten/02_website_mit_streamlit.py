"""Start die Datei mit streamlit run 02_website_mit_streamlit.py"""
import streamlit as st
import ollama

st.title("Lokales LLM mit Ollama")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Wie kann ich dir helfen?")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        for chunk in ollama.chat(
            model='deepseek-r1:1.5b',
            messages=st.session_state.messages,
            stream=True,
        ):
            full_response += chunk['message']['content']
            response_placeholder.markdown(full_response + "▌")
        
        response_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})