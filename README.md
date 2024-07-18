# StartLit ⭐
![PyPI - Version](https://img.shields.io/pypi/v/startlit?style=plastic) ![GitHub License](https://img.shields.io/github/license/ineelhere/startlit?style=plastic) ![PyPI - Downloads](https://img.shields.io/pypi/dm/startLit?style=plastic&logoColor=blue&color=blue) ![example workflow](https://github.com/ineelhere/startlit/actions/workflows/python-publish.yml/badge.svg?style=plastic) 

![image](https://github.com/user-attachments/assets/55c9c269-dd7f-4f7d-8eca-00f2290f3c7d)

**Welcome to StartLit!**

StartLit is your gateway to building Streamlit apps with ease. It brings a simple, streamlined way to start your Streamlit projects. Here's what's included in the latest release:

#### Features:
- **Package Installation**: Now you can easily install StartLit from PYPI using `pip install startlit`.

* 🤗 `hello()` - Just a welcome text. 
* 📥 `starter()` - A very simple starter app template. Quick-peek: https://startlit-starter.streamlit.app/
* 📃 `multipage()` - An app template for building multipage Streamlit apps. Quick-peek: https://startlit-multipage.streamlit.app/
* 📚 `fragments()` - An app that allows you to run independent components in the streamlit app. Quick-peek: https://startlit-fragments.streamlit.app/
* 💬 `chat()`- A dummy chatbot app. Quick-peek: https://startlit-chat.streamlit.app/
* ❄️ `snowflake_demo_app("app_keyword","destination_directory")` - Download demos for streamlit apps on snowflake. Quick-peek: https://github.com/Snowflake-Labs/snowflake-demo-streamlit
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
### Snowflake Demo Apps

#### Usage

```python
app_keyword = "chat_app"
destination_directory = "./folder"
snowflake_demo_app(app_keyword, destination_directory)
```
Output 
```log
Cloning from https://github.com/Snowflake-Labs/snowflake-demo-streamlit.git 📦
Using the main branch 🌿
Target directory created: ./folder 🛠️
Fetched folder: Chat app using Snowflake Cortex 📁
Fetched LICENSE file 📜
Fetched README.md file 📖
Demo app files fetched successfully to /content/folder 🎉🎊
Please make sure to read the README.md 📖 and LICENSE 📜 files for important information.
```

The following table lists the app keywords (used in the above example) and their corresponding folder names in the repository:

| Keyword                   | Folder Description                                       |
|---------------------------|----------------------------------------------------------|
| chat_app                  | Chat app using Snowflake Cortex                          |
| email_generator           | LLM Email Generator                                      |
| ci_demo                   | Continuous Integration - Summit Demo                     |
| customer_engagement       | Customer Engagement App                                  |
| rag                       | Retrieval Augmented Generation (RAG)                     |
| external_access_chat_app  | External Access: Chat app using 3rd party LLM            |
| github_insights           | Github Popularity Insights                               |
| h3_mapping                | H3 Mapping and Timeseries Visualization                  |
| sql_optimizer             | SQL Query Optimizer App using Snowflake Cortex           |
| inventory_tracker         | Inventory Tracker                                        |
| usage_monitoring          | Streamlit in Snowflake Usage Monitoring                  |
| metrics_app               | Key Metrics App                                          |
| retention_analytics       | User Retention Analytics App                             |
| language_insights         | Language Usage Insights                                  |
| data_io                   | Writing and reading data back to Snowflake               |


### Feedback and Contribution:
Excited to hear your feedback and suggestions for improvements.

Collaborations and Contributions are welcome 🤝
Feel free to open issues or submit pull requests.

Enjoy your streamlit journey with StartLit and happy coding! 🚀🎉

*Check package download stats at https://pypistats.org/packages/startlit*
___

**© `Indraneel Chakraborty` | 2024** 🧑‍💻[LinkedIn](https://www.linkedin.com/in/indraneelchakraborty/) | [X/Twitter](https://twitter.com/ineelhere)
