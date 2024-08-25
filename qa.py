import streamlit as st
import os
from langchain_huggingface import HuggingFaceEndpoint
#os.environ["HUGGINGFACEHUB_API_TOKEN"] = "xyz"
llm = HuggingFaceEndpoint(repo_id="mistralai/Mistral-Nemo-Instruct-2407")

def interface():
    form = st.form("Type yor Question")
    inp = form.text_input("Ask meeee !!")
    btn = form.form_submit_button("Submit")
    return btn, inp

def process(inp):
    out = llm.invoke(inp)
    st.write(inp+out)
    


