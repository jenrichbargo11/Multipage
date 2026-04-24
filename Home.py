import streamlit as st

st.markdown("""
<style>

.stApp {
    background-image: url("https://wallpaperaccess.com/full/2835209.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    pointer-events: none;
}

section[data-testid="stSidebar"] {
    background: rgba(0, 50, 0, 0.55) !important;
    backdrop-filter: blur(12px);
    box-shadow: inset 0 0 10px rgba(0,0,0,0.3);
}

h1, h2, h3, h4, p {
    color: #e8f5e9 !important;
}

hr {
    border: 1px solid rgba(200,255,200,0.3);
}
div[data-baseweb="input"],
textarea,
input {
    background: #26392e !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 10px !important;
    color: #ffffff !important;
    backdrop-filter: blur(8px);
}
div[data-baseweb="input"]:focus-within{
    border: 1px solid rgba(0, 255, 170, 0.6) !important;
    box-shadow: 0 0 10px rgba(0, 255, 170, 0.3);
}
div.stButton {
    justify-content: center;
}

div.stButton > button {
    background-color: #0d6e2c;
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: 600;
    border: none;
    transition: 0.3s;
}

div.stButton > button:hover {
    background-color: #06c559;
    transform: scale(1.05);
}
.image-wrapper {
    position: relative;
    display: inline-block;
    padding: 10px;
    border-radius: 25px;
    background: linear-gradient(45deg, #a8f5c2, #6ee7a8); /* light green gradient */
    box-shadow: 0 0 25px rgba(0, 255, 170, 0.5);
}

.image-wrapper img {
    width: 260px;
    border-radius: 20px;
    display: block;
}

/* glowing effect */
.image-wrapper:hover {
    box-shadow: 0 0 40px rgba(0, 255, 170, 0.9);
    transform: scale(1.03);
    transition: 0.3s ease;
}

            
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Jenrich Portfolio", page_icon="🌐")

col1, col2, col3 = st.columns([1,2,1])

import base64

def get_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_base64 = get_base64("img/main.jpg")

with col2:
    st.markdown(f"""
    <div class="image-wrapper">
        <img src="data:image/png;base64,{img_base64}">
    </div>
    """, unsafe_allow_html=True)
st.title("Hi, I'm Jenrich Bargo")

st.write("💻 Computer Science Student | 🎨 Graphic Designer | 📸 Photographer | 🎥 Videographer")
st.write(
        "I love Graphic Arts, building websites, and learning frontend and backend techniques."
    )
col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("Do you want to know About Me? ➜"):
        st.switch_page("pages/2_👤_About.py")

st.info("Feel free to explore and visit my projects, skills, and experiences!")

name = st.text_input("Enter your name:")

if name:
    st.success(f"Welcome {name}! Thanks for visiting my portfolio 🚀")


st.sidebar.text("Made with ❤️ by Jenrich")

st.divider()

st.markdown("<p style='text-align:center;'>JenBargo © 2026 | All Rights Reserved</p>", unsafe_allow_html=True)