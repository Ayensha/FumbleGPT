import streamlit as st 
import pandas as pd 

#from safe import respone
st.title("FumbleGPT")
#
st.header("Welome to FumbleGPT")
import time
import numpy as np
import pandas as pd
import streamlit as st

_LOREM_IPSUM = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""




#st.text_area("let's get started!", height=200)
#st.text_area("let's get started!", height=300)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
with st.form("form"):
    
    #tessst = (response['message']['content'])
 
    text = st.text_area("Start Texting", value="", key="input_text")
    from ollama import chat
    from ollama import ChatResponse
    def response(text):
        response: ChatResponse = chat(model='tinydolphin:latest', messages=[
        {
            'role': 'user',
            'content': text,
        },
        ])
        return response['message']['content']
    def stream_data():
        #response(text=text)
        for word in response(text=text).split(" "):
            yield word + " "
            time.sleep(0.02)

        
  
    col1, col3, col4, col5, col6, col7, col2 = st.columns(7)

    with col1:
        submitted = st.form_submit_button("Submit")

    with col2:
        clear = st.form_submit_button("Clear", type='secondary')

    if clear:
        st.session_state.chat_history=[]
    
    if submitted and text.strip():
       
        st.session_state.chat_history.append(("user", text.strip()))
        st.session_state.chat_history.append(("assistant", response(text=text)))
        #st.session_state.input_text = "" 

#
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.write(message)#
    #text = st.text_area("Start Texting", value="", key="input_text")