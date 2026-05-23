import streamlit as st

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

message_history=[]  
 # this dictionary is also getting executed everytime.
# even we are saving it all the time , it is getting initiated the list of dict as null every time we are running it
#  so nothing is being saved at the moment even we are saving it.

# solution:
#  need to use session object, the element inside it will not get erased even all script will run the script exlpicitly.
# st.session is also a dictionary. {}


# here you print entire history then below current user and assistant message will printed

for message in message_history:
    with st.chat_message(message['role']):
        st.write(message['content'])

user_input=st.chat_input('Type here')
if user_input:
    message_history.append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.write(user_input)

    message_history.append({'role':'assistant','content':user_input})
    with st.chat_message('assistant'):
       st.write(user_input) 
