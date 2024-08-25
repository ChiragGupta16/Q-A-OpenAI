import streamlit as st
from QA import interface,process

btn, inp = interface()

if(btn == True):
    process(inp)
