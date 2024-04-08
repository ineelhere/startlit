import streamlit as st
import random

st.set_page_config("Fragments", "⭐", layout="wide")

st.info("Notice that the graph created with the feature does not affect the other elements in th app unlike the other graph. 💡🌐")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("## 🚀 Using st.experimental_fragment", unsafe_allow_html=True)

    @st.experimental_fragment   # This decorator marks a function to run in isolation
    def area_chart_fragment():
        st.markdown("### 📈 Area Chart 1", unsafe_allow_html=True)
        val11 = st.slider("Number of points for Area Chart 1 📏", 1, 20, 15)
        data = [random.random() for _ in range(val11)]
        st.area_chart(data, use_container_width=True, color="#666699")  # Using hex representation for green

    area_chart_fragment()

with col2:
    st.markdown("## 🛠️ Without st.experimental_fragment", unsafe_allow_html=True)

    def area_chart_no_fragment():
        st.markdown("### 📈 Area Chart 2", unsafe_allow_html=True)
        val = st.slider("Number of points for Area Chart 2 📏", 1, 20, 15)
        data = [random.random() for _ in range(val)]
        st.area_chart(data, use_container_width=True, color="#b30059")  # Using hex representation for blue

    area_chart_no_fragment()

st.markdown("""
        `st.experimental_fragment` is a game-changing feature in Streamlit that unlocks new freedoms, efficiencies, and possibilities for developers. With this innovative addition, Streamlit continues to pave the way for creating dynamic and interactive web apps with ease.
        """)
