from PIL import Image
from google import genai
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

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[image, "Tell me about this image"]
    )
    # pl = markdown_to_text(response.text)
    # st.code(pl)
    st.markdown(response.text)