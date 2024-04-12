def help():
    """
    A function that returns a long string of available commands.
    """
    help_text = """
    Available commands:
    🤗 hello() - Just a welcome text. 
    📥 starter() - A very simple starter app template. Quick-peek: https://startlit-starter.streamlit.app/
    📥 multipage() - An app template for building multipage Streamlit apps. Quick-peek: https://startlit-multipage.streamlit.app/
    📚 fragments() - An app that allows you to run independent components in the streamlit app. Quick-peek: https://startlit-fragments.streamlit.app/
    💬 chat() - A dummy chatbot app. Quick-peek: https://startlit-chat.streamlit.app/
    📜 list_streamlit_apps() - List running Streamlit apps.
    🔪 kill_streamlit_apps() - Kill running Streamlit apps.
    🐙 Need more help? Post an issue at https://github.com/ineelhere/startlit/issues
    """
    print(help_text)
