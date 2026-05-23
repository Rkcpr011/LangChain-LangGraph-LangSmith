session_state = {
    # ----- APP STATE -----
    "thread_id": "fd2376d0-628f-4098-a10b-fcfa463043c5",  
        # The ID of the currently active conversation
    "chat_threads": [
        "970cee39-05de-4976-9f09-1c4dd7cd79db",
        "fd2376d0-628f-4098-a10b-fcfa463043c5",
        "44deaec8-e5d6-4d1c-a657-df4f2d5ef21a"
    ],
        # List of all thread IDs created in this session
    "chat_titles": {
        "970cee39-05de-4976-9f09-1c4dd7cd79db": "Weather Bot Test",
        "fd2376d0-628f-4098-a10b-fcfa463043c5": "charitha",
        "44deaec8-e5d6-4d1c-a657-df4f2d5ef21a": "SQL Query Practice"
    },
        # Human-friendly titles for each conversation
    # ----- MESSAGE HISTORY -----
    "message_history": [
        {"role": "user", "content": "charitha", "avatar": "user_avatar.png"},
        {"role": "assistant", "content": "Hello! It looks like you've typed 'charitha'. How can I assist?", "avatar": "bot_avatar.png"}
    ]
}
        # Messages for the currently active thread (displayed in main area)
print(session_state["chat_titles"]['970cee39-05de-4976-9f09-1c4dd7cd79db'])
   
  