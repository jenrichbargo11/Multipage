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

h1, h2 {
    color: #00ffcc !important;
}

hr {
    border: 1px solid rgba(200,255,200,0.3);
}
            
div[data-baseweb="input"],
input {
    background: #26392e !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 10px !important;
    color: #ffffff !important;
    backdrop-filter: blur(8px);
}

</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.title("FAQ Center")

faqs = [
    {
        "question": "What is this app for?",
        "answer": "This app is designed to provide tools, information, or services depending on the project."
    },
    {
        "question": "How do I use this app?",
        "answer": "Navigate using the sidebar and follow the instructions in each section."
    },
    {
        "question": "Is this app free?",
        "answer": "Yes, this app is free to use unless stated otherwise."
    },
    {
        "question": "Can I contact support?",
        "answer": "Yes, you can add your email or contact form for support."
    },
    {
        "question": "Who developed this app?",
        "answer": "This app was built using Streamlit and Python."
    }
]

search = st.text_input("🔍 Search FAQ (type a keyword)")

filtered_faqs = [
    faq for faq in faqs
    if search.lower() in faq["question"].lower() or search.lower() in faq["answer"].lower()
]

if filtered_faqs:
    for faq in filtered_faqs:
        with st.expander(faq["question"]):
            st.write(faq["answer"])
else:
    st.warning("No matching FAQ found.")

st.sidebar.text("Made with ❤️ by Jenrich")

st.divider()
st.markdown("<p style='text-align:center;'>JenBargo © 2026 | All Rights Reserved</p>", unsafe_allow_html=True)