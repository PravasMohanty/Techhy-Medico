import streamlit as st

def download_report(result, uploaded_file):
    st.download_button(
        " Download Report",
        result,
        file_name=f"analysis_{uploaded_file.name}.txt",
        mime="text/plain",
        use_container_width=True
    )
