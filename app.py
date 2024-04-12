import streamlit as st
import random
import time


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
            "Hey! What can I do for you today?",
            "Greetings! How can I be of service?",
            "Good to see you! What do you need help with?",
            "Hi! Is there anything on your mind today?",
            "Welcome! Let me know how I can help you.",
            "Hi! What's on your mind?",
            "Hey there! What can I do to assist you?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("A dummy chatbot")

with st.sidebar:
    st.header("Information 💬")
    st.info('''
        Welcome to the chat application! 👋\n
        Type your message in the chat input box and hit Enter to chat. 💬\n
        Your conversation history will be displayed below. 📜
    ''')
    st.markdown("Read more at [official docs](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps )📚")
    st.success('Get this app project in your workspace with the `basic_chat()` function of [StartLit](https://pypi.org/project/startlit/) package')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Write your message here"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

