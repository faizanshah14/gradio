import streamlit as st
import openai
from PIL import Image
import requests
from io import BytesIO
import os
# Set up OpenAI API key
openai.api_key = os.getenv("KEY")

# Function to generate image using DALL-E API
def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"  # You can adjust the size as needed
    )
    image_url = response['data'][0]['url']
    return image_url

# Streamlit UI components
st.title("DecentraAI Image Generator")
prompt = st.text_input("Enter your prompt:")
if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image..."):
            try:
                # Generate image using DALL-E API
                image_url = generate_image(prompt)
                
                # Download and display the image
                image = Image.open(BytesIO(requests.get(image_url).content))
                st.image(image, caption="Generated Image", use_column_width=True)
            except Exception as e:
                st.error(f"Image generation failed: {e}")
    else:
        st.warning("Please enter a prompt.")
