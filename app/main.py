
import streamlit as st
from services.gemini_service import GeminiService
from ui.uploader import upload_image
from ui.api_input import upload_api_key
from ui.get_api import find_api
from ui.download_report import download_report
from ui.analysis_page import analysis_page
from ui.footer import footer
from ui.css import basic_decorations


basic_decorations()

st.set_page_config(
    page_title="Vital Image Analytics",
    page_icon="🤖",
    layout="centered"  
)




st.title("🏥 Vital Image Analytics")
st.caption("AI-powered medical image analysis")
st.markdown("---")


uploaded_api = upload_api_key()


uploaded_file = upload_image()


ready_to_analyze = analysis_page(uploaded_api, uploaded_file)

 
submit = st.button(
    "🔬 Analyze Image Now!" if ready_to_analyze else " Complete inputs first",
    type="primary",
    disabled=not ready_to_analyze,
    use_container_width=True
)


if submit:
    try:
        with st.spinner(" Analyzing image... Please wait."):
            ai = GeminiService(uploaded_api)
            result = ai.analyze_image(
                uploaded_file.getvalue(),
                uploaded_file.type,
                "Analyze this medical image thoroughly. Identify any visible abnormalities, provide a detailed assessment, and suggest potential findings."
            )
        
        st.success(" Analysis Complete!")
        
        st.markdown("---")
        st.markdown("### Medical Analysis Report")
        
        with st.container():
            st.markdown(result)
        
        download_report(result, uploaded_file)
    except Exception as e:
        st.error(f" Error: {str(e)}")
        
        # Helpful messages
        error_lower = str(e).lower()
        if "api key" in error_lower or "401" in error_lower:
            st.error(" Invalid API key. Please check and try again.")
        elif "quota" in error_lower:
            st.error(" API quota exceeded. Wait a minute and retry.")
        
        with st.expander(" Technical Details"):
            st.code(str(e))


footer()
