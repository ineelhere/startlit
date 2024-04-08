import urllib.request
import os

def hello():
    """
    A function that prints a greeting message to the console.
    No parameters required.
    """
    print("Hello there 👋 \nWelcome to Startlit! 🚀")

def help():
    """
    A function that prints a list of available commands to the console.
    """
    print("Available commands:\n🤗 hello()\n📥 starter()\n📥 multipage()\n📚 fragments()\n🐙 Need more help? Post an issue at https://github.com/ineelhere/startlit/issues")

def starter():
    """
    A function to download the starter app files from a specified URL and print a confirmation message.
    """
    urllib.request.urlretrieve("https://raw.githubusercontent.com/ineelhere/startlit/starter/app.py", "app.py")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/ineelhere/startlit/starter/requirements.txt", "requirements.txt")
    print("📥 Starter app downloaded!📥\n👀 Look for 'app.py' and 'requirements.txt' file in your working directory 👀")
    print("💡 Visit https://startlit-starter.streamlit.app/ for a quick look to the starter app")

def multipage():
    """
    A function to download the multipage app files from a specified URL and print a confirmation message.
    """
    urllib.request.urlretrieve("https://raw.githubusercontent.com/ineelhere/startlit/multipage/1_Home_Page.py", "1_Home_Page.py")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/ineelhere/startlit/starter/requirements.txt", "requirements.txt")
    os.mkdir("pages")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/ineelhere/startlit/multipage/pages/1_Page_1.py", "pages/1_Page_1.py")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/ineelhere/startlit/multipage/pages/2_Page_2.py", "pages/2_Page_2.py")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/ineelhere/startlit/multipage/pages/3_Page_3.py", "pages/3_Page_3.py")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/ineelhere/startlit/multipage/pages/4_Page_4.py", "pages/4_Page_4.py")    
    print("📥 Multipage app downloaded!📥\n👀 Look for the files in your working directory 👀")
    print("💡 Visit https://startlit-multipage.streamlit.app/ for a quick look to the multipage app")

def fragments():
    """
    A function to download the fragments app files from a specified URL and print a confirmation message.
    """
    urllib.request.urlretrieve("https://raw.githubusercontent.com/ineelhere/startlit/fragments/app.py", "app.py")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/ineelhere/startlit/starter/requirements.txt", "requirements.txt")
    print("📥 Fragments app downloaded!📥\n👀 Look for 'app.py' and 'requirements.txt' file in your working directory 👀")
    print("💡 Visit https://startlit-fragments.streamlit.app/ for a quick look to the deployed app")
