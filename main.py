from PIL import Image
import google.generativeai as genai
import streamlit as st

api_key = st.secrets["api_key"]


st.markdown("""
<div style='text-align: right'>
    <a href="https://github.com/tirthrajsg" target="_blank">
        🐙 GitHub
    </a> &nbsp; | &nbsp;
    <a href="https://www.linkedin.com/in/tirthraj-girawale-3b2470216/" target="_blank">
        💼 LinkedIn
    </a> &nbsp; | &nbsp;
    <a href="https://www.instagram.com/tirthrajsg/" target="_blank">
        🐦 Instagram
    </a> &nbsp; | &nbsp; 
    Tirthraj Girawale
</div>
""", unsafe_allow_html=True)

st.markdown("# Get description of any image")

uploaded_file = st.file_uploader("Upload a Image", type=["jpg", "jpeg", "png", "bmp", "tiff", "webp", "ico", "psd"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, use_container_width=True)

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(
        [image, "Tell me about this image"]
    )
    # pl = markdown_to_text(response.text)
    # st.code(pl)
    st.markdown(response.text)