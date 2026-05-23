# use backend  chatbot from "basicchatBot" class.

import streamlit as st
from Basic_chatBot import chatBot
from langchain_core.messages import HumanMessage
import uuid

# **************************utility functions******************#

# this will return new thread whenever it will be called.
def generate_thread_id():
    thread_id=uuid.uuid4()
    return thread_id

# on call of this function
# generate a current chat thread
# add it to session state as key value
# then add the same thread_id in chat_thread
# reset the chat history.
def new_chat():
    thread_id=generate_thread_id()
    st.session_state['thread_id']=thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history']=[]

# this will take a thread_id and that id not there in thread_id , it will add.
def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

# this function will add the conversation for a particular thread id.
def load_conversation(thread_id):
    return chatBot.get_state(config={'configurable':{'thread_id':thread_id}}).values['messages']

# *******************************************session setup**********************
# create a new message history list if already not exist in session state
if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

# create a thread_id if not in session state
if 'thread_id' not in st.session_state:
    st.session_state['thread_id']=generate_thread_id()

# create a chat_thread to store all the threads going forward , current and previous.
if "chat_threads" not in st.session_state:
    st.session_state['chat_threads']=[]
    
add_thread(st.session_state['thread_id'])    
# ***************************Sidebar***********
st.sidebar.title('Rocky ChatBot')

if st.sidebar.button("New Chat"):
    new_chat()


st.sidebar.header('My Conversations')
for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
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
user_input=st.chat_input('Type here')



if user_input:
    thread_id='user123'
# first adding the  user input to the session state. 
    st.session_state['message_history'].append({'role':'user','content':user_input})

# displaying on the UI page, what user entered.
    with st.chat_message('user'):
        st.write(user_input)  
        
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
   
       
