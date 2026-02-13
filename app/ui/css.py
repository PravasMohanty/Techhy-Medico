import streamlit as st

def basic_decorations():
    st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
    }
    
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.6rem;
    }
    
    .stButton>button:hover {
        background-color: #1557a0;
    }
    
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)