import streamlit as st

# Define the pages
main_page = st.Page("main_page.py", title="WeEar", icon="🎈")
page_2 = st.Page("page_2.py", title="WeEar's Speech2Text", icon="❄️")
st.button("Press me!", key="start_recording")
st.button("Stop Recording", key="stop_recording")
page_3 = st.Page("page_3.py", title="WeEar's Sign2Text", icon="🎉")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3])

# Run the selected page
pg.run()


st.cache_data

#streamlit run app.py 