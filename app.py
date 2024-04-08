import streamlit as st
import random

st.set_page_config("Fragments", "⭐", layout="wide")

st.info("Notice that the graph created with the feature does not affect the other elements in th app unlike the other graph. 💡🌐")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("## 🚀 Using st.experimental_fragment", unsafe_allow_html=True)

    @st.experimental_fragment   # This decorator marks a function to run in isolation
    def simple_charts():
        st.markdown("### 📊 Bar Chart 1", unsafe_allow_html=True)
        val11 = st.slider("Number of bars for Bar Chart1 📏", 1, 20, 4)
        data = [random.random() for _ in range(val11)]
        st.bar_chart(data)

    simple_charts()

with col2:
    st.markdown("## 🛠️ Without st.experimental_fragment", unsafe_allow_html=True)

    def simple_charts1():
        st.markdown("### 📊 Bar Chart 2", unsafe_allow_html=True)
        val = st.slider("Number of bars for Bar Chart2 📏", 1, 20, 4)
        data = [random.random() for _ in range(val)]
        st.bar_chart(data)

    simple_charts1()

st.markdown("""
        `st.experimental_fragment` is a game-changing feature in Streamlit that unlocks new freedoms, efficiencies, and possibilities for developers. With this innovative addition, Streamlit continues to pave the way for creating dynamic and interactive web apps with ease.
        """)
