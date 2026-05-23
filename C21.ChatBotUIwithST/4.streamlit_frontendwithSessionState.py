# use backend  chatbot from "basicchatBot" class.

import streamlit as st
from Basic_chatBot import chatBot
from langchain_core.messages import HumanMessage

# In Streamlit, st.session_state is like a persistent dictionary that remembers variables across reruns of your app.
# Acts like a dictionary — you can store and retrieve values by key:

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]
# iniitialize a list of dict in the sessionstate dictionary.

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.write(message['content'])
user_input=st.chat_input('Type here')

if user_input:
    thread_id='user123'
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.write(user_input)
    config={'configurable':{'thread_id':thread_id}}
    response=chatBot.invoke({'messages':[HumanMessage(content=user_input)]},config=config)
    ai_message=response['messages'][-1].content


    st.session_state['message_history'].append({'role':'assistant','content':ai_message})
    with st.chat_message('assistant'):
       st.write(ai_message) 
