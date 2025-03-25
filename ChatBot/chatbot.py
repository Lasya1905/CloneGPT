import streamlit as st
import requests

st.title("CloneGPT")


# Store Chat history
if "message" not in st.session_state:
    st.session_state.message = [] 


# Loops through prev messages
for message in st.session_state.message:
    # displays each message in chat bubble
    with st.chat_message(message['role']):
        # each message has role or text
        st.write(message['content'])



# st.chat_input creates input box for user
if prompt := st.chat_input('Ask anything...'):
    with st.chat_message('user'):
        st.write(prompt)
    # input stored in session state
    st.session_state.message.append({'role':'user', 'content': prompt})

if prompt:
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyA4sf85cDis6N0FTszZIOkJnnWGCGwW7oY"
    data = {'contents': [{'parts':[{'text': prompt}]}]}
    response = requests.post(url,json=data)
    response = response.json()
    response = response['candidates'][0]['content']['parts'][0]['text']


# To prevent error for no response   
try:
    with st.chat_message('assistant'):
        st.write(response)
    st.session_state.message.append({'role': 'assistant','content': response})
except:
    pass