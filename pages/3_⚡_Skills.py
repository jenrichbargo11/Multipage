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

h2, h3, h4, p {
    color: #e8f5e9 !important;
}

h1 {
    color: #00ffcc !important;
}

hr {
    border: 1px solid rgba(200,255,200,0.3);
}

</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.title("My Skills")

st.subheader("💻 Programming Skills")

st.write("Python")
st.progress(75)

st.write("HTML/CSS")
st.progress(70)

st.subheader("🎨 Design Skills")

st.write("Graphic Design")
st.progress(85)

st.write("UI/UX")
st.progress(70)

st.subheader("🛠 Tools I Use")
st.write("""
- VS Code  
- GitHub  
- Canva  
- Streamlit  
""")

skill_rating = st.slider("Rate your coding confidence:", 1, 10)
st.write(f"Confidence Level: {skill_rating}/10")

st.sidebar.text("Made with ❤️ by Jenrich")

st.divider()
st.markdown("<p style='text-align:center;'>JenBargo © 2026 | All Rights Reserved</p>", unsafe_allow_html=True)