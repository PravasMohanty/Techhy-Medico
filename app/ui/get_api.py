import streamlit as st

def find_api():
    """Display API key instructions"""
    
    with st.expander("❓ How to get a Gemini API key?"):
        st.markdown("""
        ### 🔑 Get Your Free API Key
        
        **Visit:** [Google AI Studio](https://aistudio.google.com/)
        
        **Steps:**
        1. Sign in with Google
        2. Click on Dashboard on the left side
        3. Click "Create API Key"  
        4. It will then ask for an imported project to select 
        5. Create a new projet by clicking Create Project
        6. Select your Project
        7. Click "Create Key Button" 
        8. Copy your key (starts with `AIza...`)
        9. Paste it in the field above
        """)