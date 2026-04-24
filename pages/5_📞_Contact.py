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

h4, p {
    color: #e8f5e9 !important;
}

h1, h2, h3 {
    color: #00ffcc !important;
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

input::placeholder,
textarea::placeholder {
    color: rgba(255, 255, 255, 0.6) !important;
}

label {
    color: #26b762 !important;
    font-weight: 500;
}

div[data-baseweb="input"]:focus-within,
textarea:focus {
    border: 1px solid rgba(0, 255, 170, 0.6) !important;
    box-shadow: 0 0 10px rgba(0, 255, 170, 0.3);
}

</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.title("Contact Me")

st.write("Feel free to send me a message!")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Message")

if st.button("Send Message"):
    if name and email and message:
        st.success("✅ Message sent successfully!")
    else:
        st.error("Please fill in all fields.")

st.divider()

st.subheader("🌐 Social Links")
st.write("📧 Email: jenrichbargo11@gmail.com")
st.write("📸 Instagram: itzur_jeen")
st.write("👍 Facebook: Jen rich Bernaldo Bargo")

st.sidebar.text("Made with ❤️ by Jenrich")

st.divider()
st.markdown("<p style='text-align:center;'>JenBargo © 2026 | All Rights Reserved</p>", unsafe_allow_html=True)