from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate #intial prompt template
from langchain_core.output_parsers import StrOutputParser # parse any llm response

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
## LangSmith Tracking purpose
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user questions"),
        ("user", "Question:{questions}")
    ]
)

## Streamlit framework
st.title('Langchain Demo with OPENAI API')
input_text = st.text_input("Search the topic you want")

## OpenAI LLM
llm = ChatOpenAI(model = "gpt-3.5-turbo")
output_parser =  StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'questions':input_text}))
