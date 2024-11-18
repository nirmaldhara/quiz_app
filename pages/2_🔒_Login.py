import streamlit as st
from PIL import Image
import base64
import time
from db.db_connector import check_login

# Load Background Image
def add_bg_from_local(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add background image (adjust the filename if needed)
add_bg_from_local("./img/login.png")

# Streamlit page layout and styling
st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>Login</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 4, 2])
# Login form

with col2:
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
# Login button
    if st.button("Login"):
        # Simple authentication logic for demonstration
        student_id = check_login(username, password)

        if student_id:
            st.success("Login successful!")
            time.sleep(2)
            st.switch_page("pages\\4_❓_quiz.py")
        else:
            st.error("Invalid username or password.")