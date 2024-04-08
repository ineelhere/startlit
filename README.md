# StartLit ⭐

**Welcome to StartLit!**

StartLit is your gateway to building Streamlit apps with ease. It brings a simple, streamlined way to start your Streamlit projects. Here's what's included in the latest release:

#### Features:
- **Package Installation**: Now you can easily install StartLit from PYPI using `pip install startlit`.
- **Simple Usage**: Import the package and run `hello()` to receive a friendly welcome message.
- **Basic help**: Use the `help()` function to get started with more support
-  **Starter App**: Use the `starter()` function to download a very simple starter app template, including an `app.py` file and a `requirements.txt` file.
-  **Multipage App**: Use the `multipage()` function to download an app template for building multipage Streamlit apps. The files/folders will be available in your working directory.
-  **Fragments App**: Use the `fragments()` function to download an app that allows you to run independent components in the streamlit app.



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


```
___

### Feedback and Contribution:
Excited to hear your feedback and suggestions for improvements. 
Feel free to open issues or submit pull requests.

Enjoy your streamlit journey with StartLit and happy coding! 🚀🎉
___

**© `Indraneel Chakraborty` | 2024** 🧑‍💻[LinkedIn](https://www.linkedin.com/in/indraneelchakraborty/) | [X/Twitter](https://twitter.com/ineelhere)


`Collaborations and Contributions are welcome 🤝`