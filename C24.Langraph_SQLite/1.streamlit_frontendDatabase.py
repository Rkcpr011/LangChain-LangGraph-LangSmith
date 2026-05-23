# use backend  chatbot from "basicchatBot" class.

import streamlit as st
from Langgraph_backend_withSqliteDB import chatBot , retrieve_allExistingThreads
from langchain_core.messages import HumanMessage
import uuid
import time



# **************************utility functions******************#

def generate_thread_id():
    thread_id=uuid.uuid4()
    return thread_id


def new_chat():
    thread_id=generate_thread_id()
    st.session_state['thread_id']=thread_id
    st.session_state["chat_titles"][thread_id] = f"Chat {len(st.session_state['chat_threads']) + 1}"
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history']=[]


def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)


def load_conversation(thread_id):
    state = chatBot.get_state(config={'configurable': {'thread_id': thread_id}})
    messages = state.values.get('messages', [])  # Safe access with default []
    return messages
    # return chatBot.get_state(config={'configurable':{'thread_id':thread_id}}).values['messages']

# *******************************************session setup**********************

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]


if 'thread_id' not in st.session_state:
    st.session_state['thread_id']=generate_thread_id()


if "chat_threads" not in st.session_state:
    st.session_state['chat_threads']=retrieve_allExistingThreads()  # we were assigning it a emptly list everytime running it.
    # now  since we have establish the permanent db , we will check all previous threads.

    
if "chat_titles" not in st.session_state:
    st.session_state["chat_titles"] = {}   # {thread_id: title_string}

add_thread(st.session_state['thread_id'])   

# ***************************Sidebar***********
st.sidebar.badge('Rocky CHatBot')
if st.sidebar.button("New Chat"):
    new_chat()


st.sidebar.header('My Conversations')
for thread_id in st.session_state['chat_threads'][::-1]:
    title = st.session_state["chat_titles"].get(thread_id, str(thread_id))
    # st.session_state['chat_titles']=title
    if st.sidebar.button(title, key=f"btn-{thread_id}"):

    # if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id']=thread_id
        messages=load_conversation(thread_id)

        temp_messages=[]
        for msg in messages:
            if isinstance(msg , HumanMessage):
                role='user'
            else:
                role='assistant'
            temp_messages.append({'role':role , 'content':msg.content})  

        st.session_state['message_history']=temp_messages


# **************************main UI*************************

# Loading previous conversation history.
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.write(message['content'])
user_input=st.chat_input('Ask Anything:')


if user_input:
    
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.write(user_input)  


    tid = st.session_state["thread_id"]
    current_title = st.session_state["chat_titles"].get(tid, "")
    # If it’s still the placeholder, replace it with a trimmed version of the first user message
    if not current_title or current_title.startswith("Chat "):
        new_title=user_input.strip()[:40] 
        st.session_state["chat_titles"][tid] =new_title  # keep it short
    CONFIG={'configurable':{'thread_id':st.session_state['thread_id']}}
#getting return the assistant message as well as writing it
    with st.chat_message('assistant'):
       ai_message=st.write_stream(
          message_chunk.content for message_chunk , metadata in chatBot.stream(
                {'messages':[HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode='messages'
               
           )
       )
# appending the final answer once streaming done , to sessionstate
    st.session_state['message_history'].append({'role':'assistant','content':ai_message})
   
       
