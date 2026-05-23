# use backend  chatbot from "basicchatBot" class.

import streamlit as st
from Basic_chatBot import chatBot
from langchain_core.messages import HumanMessage
import uuid
import time
st.set_page_config(
    page_title="Chat With Rocky",
    page_icon="🤖",
    layout="wide"
)

# navbar
st.markdown(
    """
    <style>
    .navbar {
        background-color: #4CAF50;
        padding: 0.8rem;
        border-radius: 8px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .navbar-title {
        font-size: 1.2rem;
        font-weight: bold;
    }
    .navbar-links a {
        margin-left: 1rem;
        color: white;
        text-decoration: none;
    }
    .navbar-links a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="navbar">
        <div class="navbar-title">💬 Chat With Rocky</div>
        <div class="navbar-links">
            <a href="#">Home</a>
            <a href="#">Docs</a>
            <a href="#">About</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# subheader
st.subheader("📌 Insights!")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Chats", "5 Active Chats", "+5")
with col2:
    st.metric("Session Time","12.5 second", "+5")
with col3:
    st.metric("Response Time", "0.8s", "-0.1s")

#subheader 
colA, colB = st.columns([2, 3])
with colA:
    st.info("No Chat yet , Start chat here.")
    st.button("Click to send the action")
with colB:
    st.success("How Can I Help you today?.")
    # st.image("https://picsum.photos/500/300") 

#
with st.expander("💡 Tips"):
    st.write("📌 Additional Info!")
    st.code("You can ask all your query , Rocky will answer it.")

with st.expander("📂 File Upload"):
    uploaded_file = st.file_uploader("Upload a file")
    if uploaded_file:
        st.write(f"Uploaded: {uploaded_file.name}") 
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
    st.session_state['chat_threads']=[]
    
if "chat_titles" not in st.session_state:
    st.session_state["chat_titles"] = {}   # {thread_id: title_string}

add_thread(st.session_state['thread_id'])   

# ***************************Sidebar***********
st.sidebar.title('Rocky ChatBot')
st.sidebar.badge('Rocky CHatBot')
if st.sidebar.button("New Chat"):
    new_chat()


st.sidebar.header('My Conversations')
for thread_id in st.session_state['chat_threads'][::-1]:
    title = st.session_state["chat_titles"].get(thread_id, str(thread_id))
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
        st.session_state["chat_titles"][tid] = user_input.strip()[:40]  # keep it short

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
   
       
