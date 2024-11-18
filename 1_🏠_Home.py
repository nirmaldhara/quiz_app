import streamlit as st
page_bg_css = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #dacbb7; /* Set your desired color here */
}
</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    st.image("./img/welcome.gif", use_container_width =True)
    st.image("./img/logo.png", use_container_width =True)

#st.image("./img/logo.webp", width=500 )