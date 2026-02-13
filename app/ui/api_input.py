import streamlit as st

def upload_api_key():
    st.subheader("Step 1:  Enter API Key")

    uploaded_api = st.text_input(
        "Gemini API Key",
        type="password",
        placeholder="AIza...",
        help="Get your API key from https://aistudio.google.com/"
    )

    if uploaded_api:
        if uploaded_api.startswith("AIza"):
            st.success(" API key looks valid!")
        else:
            st.warning(" API keys usually start with 'AIza'")
    else:

        with st.expander(" How to get an API key?"):
            st.markdown("""
            **Quick Steps:**
            1. Sign in with Google
            2. Click on Dashboard on the left side
            3. Click "Create API Key"  
            4. It will then ask for an imported project to select 
            5. Create a new projet by clicking Create Project
            6. Select your Project
            7. Click "Create Key Button" 
            8. Copy your key (starts with `AIza...`)
            9. Paste it in the field above

            Your key will look like: `AIzaSyA...`
            """)

    st.markdown("---")
    return uploaded_api