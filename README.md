# StartLit ⭐
![PyPI - Version](https://img.shields.io/pypi/v/startlit?style=plastic) ![GitHub License](https://img.shields.io/github/license/ineelhere/startlit?style=plastic) ![PyPI - Downloads](https://img.shields.io/pypi/dm/startLit?style=plastic&logoColor=blue&color=blue) ![example workflow](https://github.com/ineelhere/startlit/actions/workflows/python-publish.yml/badge.svg?style=plastic) 

**Welcome to StartLit!**

StartLit is your gateway to building Streamlit apps with ease. It brings a simple, streamlined way to start your Streamlit projects. Here's what's included in the latest release:

#### Features:
- **Package Installation**: Now you can easily install StartLit from PYPI using `pip install startlit`.

* 🤗 `hello()` - Just a welcome text. 
* 📥 `starter()` - A very simple starter app template. Quick-peek: https://startlit-starter.streamlit.app/
* 📃 `multipage()` - An app template for building multipage Streamlit apps. Quick-peek: https://startlit-multipage.streamlit.app/
* 📚 `fragments()` - An app that allows you to run independent components in the streamlit app. Quick-peek: https://startlit-fragments.streamlit.app/
* 💬 `chat()`- A dummy chatbot app. Quick-peek: https://startlit-chat.streamlit.app/
* 📜 `list_streamlit_apps()` - List running Streamlit apps.
* 🔪 `kill_streamlit_apps()` - Kill running Streamlit apps.
* 💡 `help()` - Display help menu with list of available functions.
* 🐙 Need more help? Post an issue at https://github.com/ineelhere/startlit/issues

### Install the package from PYPI

```python
pip install startlit
```
### Import the package

```python
from startlit import *
hello()
```
Running `hello()` should give you a simple welcome message -
```
Hello there 👋 
Welcome to Startlit! 🚀
```
### Download a very simple starter app

```python
starter()
```
Output - 
```
📥 Starter app downloaded!📥
👀 Look for 'app.py' and 'requirements.txt' file in your working directory 👀
💡 Visit https://startlit-starter.streamlit.app/ for a quick look to the starter app
```

If you look up in your local/working directory, you should find the 2 files present as mentioned above.

___

```bash
# just to check - files have been downloaded
!ls
```
Output - 
```
app.py	requirements.txt
```
___
``` bash
# just to check - app.py actually has streamlit code
!cat app.py
```
Output - 
```python
import streamlit as st

# Display a title
st.title('Hello, World! 🌎🚀')

# Add a description with an inline comment
st.write("This is my first app in Streamlit! 📝")  # Comment: Don't forget to smile
```

___
### Other functions
```python

# get a list of available ftrs
help()

# Download a starter app template
starter()

# Download a multipage app template
multipage()

# Download a fragment app template
fragments()

# Download a dummy chatbot app template
chat()

# List all active apps
list_streamlit_apps()

# Kill a specific app by app_id
kill_streamlit_apps(app_id)
```
___

### Feedback and Contribution:
Excited to hear your feedback and suggestions for improvements.

Collaborations and Contributions are welcome 🤝
Feel free to open issues or submit pull requests.

Enjoy your streamlit journey with StartLit and happy coding! 🚀🎉

*Check package download stats at https://pypistats.org/packages/startlit*
___

**© `Indraneel Chakraborty` | 2024** 🧑‍💻[LinkedIn](https://www.linkedin.com/in/indraneelchakraborty/) | [X/Twitter](https://twitter.com/ineelhere)
