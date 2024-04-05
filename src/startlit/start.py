import urllib.request

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
    print("Available commands:\n🤗 hello()\n📥 starter()\n📚 help()\n🐙 Need more help? Post an issue at https://github.com/ineelhere/startlit/issues")

def starter():
    """
    A function to download the starter app files from a specified URL and print a confirmation message.
    """
    urllib.request.urlretrieve("https://raw.githubusercontent.com/ineelhere/startlit/starter/app.py", "app.py")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/ineelhere/startlit/starter/requirements.txt", "requirements.txt")
    print("📥 Starter app downloaded!📥\n👀 Look for 'app.py' and 'requirements.txt' file in your working directory 👀")
