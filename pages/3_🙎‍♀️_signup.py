import streamlit as st
from PIL import Image
import base64
import time
from db.db_connector import  register_student
st.set_page_config(layout='wide')

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
st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>New user</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 4, 2])
# Login form

with col2:
    regno = st.text_input("REG NO.", placeholder="Enter your REG NO.")
    username = st.text_input("Name", placeholder="Enter your name")
    house = st.selectbox('House', ('','JAL', 'VAYU', 'AGNI', 'PRITHIBI'))
    class_name = st.selectbox('Class', ('','1', '2', '3', '4','5','6','7','8','9','10','11','12'))
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    if st.button("Create User"):
        # Simple authentication logic for demonstration
        regisered = register_student(regno, username, house, class_name,password)
        if regisered:
            
           st.toast(''':green[Registration successfull!]''')
           
        else:
            st.toast(''':red[Registration Failed.]''') 
# Login button
    