import streamlit as st
# take user input---> print it , and the AIassistant will also reply same what user given the input

user_input=st.chat_input('Type here')
if user_input:
    with st.chat_message('user'):
        st.write(user_input)
    with st.chat_message('assistant'):
       st.write(user_input) 
       

# what is the issue--> every time you  take any action , entire streamlit file will re run , so the previous all values will vanished.

# # solution
# we need to save entire history in a dictionalry form and then need to dsiplay that.
# eg: {'"role"':"user","content":"Hi"}
# {"role":"assistant","content":"Hi,How Can I help you Today?"}

