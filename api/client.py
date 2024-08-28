import requests
import streamlit as st

def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke", json={'input':{'topic':input_text}})
    if response.status_code != 200:
        st.write(f"Error: Received status code {response.status_code}")
        st.write(response.text)  # To see the actual response body
        return None
    return response.json().get('output')

def get_ollama_response(input_text):
    response=requests.post(
    "http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

    ## streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))