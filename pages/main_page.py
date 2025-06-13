import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

# Set the theme for the app by configuring .streamlit/config.toml or Streamlit settings
st.set_page_config(
    page_title="WeEar",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

add_vertical_space(10)
# Center and display the local logo image using Streamlit columns
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("pages/startlogo.jpeg", width=500)

#`streamlit run pages/main_page.py`