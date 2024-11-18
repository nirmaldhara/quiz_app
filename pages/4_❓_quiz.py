import streamlit as st
from PIL import Image
import base64
import time
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
add_bg_from_local("./img/q.png")

# Streamlit page layout and styling

col1, col2,  = st.columns([0.05,0.95])
with col2 :
    question_text = "Hello! Looks like you’re enjoying the discussion, but you haven’t signed up for an account yet. Tired of scrolling through the same posts? When you create an account you’ll always come back to where you left off. With an account you can also be notified of new replies, save bookmarks, and use likes to thank others. We can all work together to make this community great."
    
# Use Markdown with HTML and CSS to create a bordered box
    st.markdown(
    f"""
    <style>
    .custom-div {{
        display: inline-block;
        padding-left: 100px;
        padding-right: 100px;
        padding-top: 20px;
        border-radius: 5px;
        width: 900px;
        height: 300px;
        background-color: rgba(255, 255, 255, 0.6);
        color: #333333;
        clip-path: polygon(10% 0%, 90% 0%, 100% 50%, 90% 100%, 10% 100%, 0% 50%);
        font-size: 18px;
        transition: background-color 0.3s ease; /* Smooth transition for hover */
    }}
    .custom-div:hover {{
        background-color: rgba(200, 200, 250, 0.8); /* New color on hover */
    }}
    </style>
    <div class="custom-div">
        {question_text}
    </div>
    """,
    unsafe_allow_html=True
)
ans_1 ="Answer 1"
col1, col2,  = st.columns([0.5,0.5])
with col1 :
    import streamlit as st
    
    st.markdown(
    f"""
    <style>
    .custom-div-2 {{
        margin-top: 30px;
        padding-left: 100px;
        padding-right: 100px;
        padding-top: 20px;
        border-radius: 5px; 
        display: inline-block;
        width: 500px;
        height: 100px;
        background-color: rgba(255, 255, 255, 0.6);
        color: #333333;
        clip-path: polygon(10% 0%, 90% 0%, 100% 50%, 90% 100%, 10% 100%, 0% 50%);
        font-size: 18px;
        transition: background-color 0.3s ease; /* Smooth transition for hover */
    }}
    .custom-div-2:hover {{
        background-color: rgba(200, 250, 200, 0.8); /* New color on hover */
    }}
    </style>
    <div class="custom-div-2">
        {ans_1}
    </div>
    """,
    unsafe_allow_html=True
)


ans_2 ="Answer 2"
with col2 :
     st.markdown(
    f"""
    <style>
    .custom-div-2 {{
        margin-top: 30px;
        padding-left: 100px;
        padding-right: 100px;
        padding-top: 20px;
        border-radius: 5px; 
        display: inline-block;
        width: 500px;
        height: 100px;
        background-color: rgba(255, 255, 255, 0.6);
        color: #333333;
        clip-path: polygon(10% 0%, 90% 0%, 100% 50%, 90% 100%, 10% 100%, 0% 50%);
        font-size: 18px;
        transition: background-color 0.3s ease; /* Smooth transition for hover */
    }}
    .custom-div-2:hover {{
        background-color: rgba(200, 250, 200, 0.8); /* New color on hover */
    }}
    </style>
    <div class="custom-div-2">
        {ans_2}
    </div>
    """,
    unsafe_allow_html=True
)
col1, col2,  = st.columns([0.5,0.5])
ans_3 ="Answer 3"
with col1 :
     st.markdown(
    f"""
    <style>
    .custom-div-2 {{
        margin-top: 30px;
        padding-left: 100px;
        padding-right: 100px;
        padding-top: 20px;
        border-radius: 5px; 
        display: inline-block;
        width: 500px;
        height: 100px;
        background-color: rgba(255, 255, 255, 0.6);
        color: #333333;
        clip-path: polygon(10% 0%, 90% 0%, 100% 50%, 90% 100%, 10% 100%, 0% 50%);
        font-size: 18px;
        transition: background-color 0.3s ease; /* Smooth transition for hover */
    }}
    .custom-div-2:hover {{
        background-color: rgba(200, 250, 200, 0.8); /* New color on hover */
    }}
    </style>
    <div class="custom-div-2">
        {ans_3}
    </div>
    """,
    unsafe_allow_html=True
)
ans_4 ="Answer 4"
with col2 :
    
# Update the code to play sound on hover
        st.markdown(
    f"""
    <style>
    .custom-div-2 {{
        margin-top: 30px;
        padding-left: 100px;
        padding-right: 100px;
        padding-top: 20px;
        border-radius: 5px; 
        display: inline-block;
        width: 500px;
        height: 100px;
        background-color: rgba(255, 255, 255, 0.6);
        color: #333333;
        clip-path: polygon(10% 0%, 90% 0%, 100% 50%, 90% 100%, 10% 100%, 0% 50%);
        font-size: 18px;
        transition: background-color 0.3s ease; /* Smooth transition for hover */
    }}
    .custom-div-2:hover {{
        background-color: rgba(200, 250, 200, 0.8); /* New color on hover */
    }}
    </style>
    <script>
    var audio = new Audio('audio_file.mp3');
    audio.play();
    </script>

    <div class="custom-div-2" 
         onmouseover='new Audio("your/url/here").play();'>
        {ans_4}
    </div>
    """,
    unsafe_allow_html=True
)
