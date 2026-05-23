{
    # 🗨️ List of all messages in the current conversation
    'message_history': [
        {'role': 'user', 'content': 'Hi'},
        {'role': 'assistant', 'content': 'Hello! How can I help you?'},
        {'role': 'user', 'content': 'How to make pasta?'},
        {'role': 'assistant', 'content': 'Step 1: Boil water...\nStep 2: Add pasta...'}
    ],

    # 🆔 Current active conversation thread's UUID
    'thread_id': UUID('c71c9ef2-b0f1-4e15-a96a-09c5e2a4e478'),

    # 📜 List of all thread IDs for saved conversations
    'chat_threads': [
        UUID('c71c9ef2-b0f1-4e15-a96a-09c5e2a4e478'),
        UUID('a9d71a43-1df2-4b49-a2ec-46b6a76e95b3')
    ],

    # 🖱️ (Optional) Stores last clicked button's value from sidebar
    'New Chat': False,

    # 🖱️ (Optional) Stores last clicked thread button's value
    'a9d71a43-1df2-4b49-a2ec-46b6a76e95b3': False,

    # 📦 Any other temporary variables you add
    'username': 'Rocky',
    'login_count': 3,
    'preferences': {
        'theme': 'dark',
        'language': 'English'
    }
}
