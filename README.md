# StartLit

Get started with a streamlit app template code in style.

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
