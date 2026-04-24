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

h2, h4, p {
    color: #e8f5e9 !important;
}

h1, h3 {
    color: #00ffcc !important;
}

hr {
    border: 1px solid rgba(200,255,200,0.3);
}

</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.title("About Me")

col1, col2 = st.columns(2)

with col1:
    st.subheader("💡 Introduction")
    st.write("""
    I am a passionate Computer Science student who enjoys:
    - Designing creative graphics 🎨
    - Building simple web applications 💻
    - Learning new technologies 🚀
    - Learning photography techniques and angles 📸
    """)

    st.subheader("🎯 Personal Goals")
    st.write("""
    - To work at an IT company  
    - Improve UI/UX Design Skills  
    - Build real-world applications
    - To become a successful woman  
    """)

with col2:
    st.subheader("🏆 Experience & Achievements")
    st.write("""
    - Dean's Lister
    - 3rd runner up during WebDev HACKATHON 2025-S3 
    - Crypto Alchemist Awardee during the PicoCTF Cyber Challenge 2025
    - Top 3 Attacker (34 Attacks) | SQL Injection Challenge
    - Rank 4 during GDF (Graphic Design Festival - Season 5)
    - Most Elegant Graphic Craetion - GDF Season 5
    - Best in Free Style Art - GDF Season 5
    """)

    st.subheader("🎓 Education")
    st.write("""
    • BS Computer Science (3rd yr - Ongoing)  
    • Senior High School - GAS Strand
    """)

st.sidebar.text("Made with ❤️ by Jenrich")

st.divider()
st.markdown("<p style='text-align:center;'>JenBargo © 2026 | All Rights Reserved</p>", unsafe_allow_html=True)