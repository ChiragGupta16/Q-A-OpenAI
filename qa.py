from langchain.llms import OpenAI

import streamlit as st
import os


def getresponse(question):
    llm=OpenAI(model_name="text-davinci-003",temperature=0.5)
    response=llm(question)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
response=getresponse(input)

submit=st.button("Ask the question")


if submit:
    st.subheader("The Response is")
    st.write(response)
