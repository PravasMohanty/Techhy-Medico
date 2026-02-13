import streamlit as st

def analysis_page(uploaded_api, uploaded_file):
    st.subheader("Step 3:  Generate Analysis")

    # Check what's missing
    ready_to_analyze = uploaded_api and uploaded_file

    if not ready_to_analyze:
        missing = []
        if not uploaded_api:
            missing.append(" API key")
        if not uploaded_file:
            missing.append(" Image")
        
        st.warning(f"Missing: {' and '.join(missing)}")
        st.info(" Complete steps 1 and 2 above to enable analysis")
        return False

    return True
