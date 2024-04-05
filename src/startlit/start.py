import urllib.request

def hello():
    """
    A function that prints a greeting message to the console.
    No parameters.
    No return value.
    """
    print("Hello there 👋 \nWelcome to Startlit! 🚀")

def starter():
    """
    A function to download the starter app files from a specified URL and print a confirmation message.
    """
    urllib.request.urlretrieve("https://raw.githubusercontent.com/ineelhere/startlit/starter/app.py", "app.py")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/ineelhere/startlit/starter/requirements.txt", "requirements.txt")
    print("📥 Starter app downloaded!📥\n👀 Look for 'app.py' and 'requirements.txt' file in your working directory 👀")
    