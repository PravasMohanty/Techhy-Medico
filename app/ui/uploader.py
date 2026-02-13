import streamlit as st

def upload_image():
    st.subheader("Step 2:  Upload Medical Image")

    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=["png", "jpg", "jpeg"],
        help="Upload a medical image for analysis"
    )
    
    if uploaded_file:
        # Show preview
        col1, col2 = st.columns([2, 1])
        with col1:
            st.image(uploaded_file, use_container_width=True)
        with col2:
            st.metric("Filename", uploaded_file.name)
            st.metric("Size", f"{uploaded_file.size / 1024:.1f} KB")
            st.metric("Type", uploaded_file.type.split('/')[-1].upper())
    
    st.markdown("---")
    return uploaded_file
