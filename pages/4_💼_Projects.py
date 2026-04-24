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

h3, h4, p {
    color: #e8f5e9 !important;
}

h1, h2{
    color: #00ffcc !important;
}

hr {
    border: 1px solid rgba(200,255,200,0.3);
}

</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.title("My Projects")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🏠Boarding House Management System")
    st.image("img/Project1.png", width=200)
    st.write("A Python-based reservation system.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
        st.subheader("🌍Mandaon Explore Zone")
        st.image("img/Project3.png", width=200)
        st.write("Tourism website showcasing local spots.")
        st.markdown('</div>', unsafe_allow_html=True)

with col3:
        st.subheader("🗳Voting Management System")
        st.image("img/Project2.png", width=200)
        st.write("Database system using MS Access.")
        st.markdown('</div>', unsafe_allow_html=True)


st.subheader("📊 Project Interest Poll")

choice = st.radio(
    "Which project do you like most?",
    [
        "🏠 Boarding House Management System",
        "🗳 Voting Management System",
        "🌍 Mandaon Explore Zone"
    ]
)

st.success(f"You selected: {choice}")

st.sidebar.text("Made with ❤️ by Jenrich")

st.divider()
st.markdown("<p style='text-align:center;'>JenBargo © 2026 | All Rights Reserved</p>", unsafe_allow_html=True)