from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure the Google Generative AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")

# Define a function to get a response from the generative model
def get_gemini_response(input_text, image, prompt):
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

# Define a function to process the uploaded image
def process_uploaded_image(uploaded_file):
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": image_data}]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded.")

# Set Streamlit page configuration
st.set_page_config(page_title="MultiLanguage Invoice Extractor")
st.header("MultiLanguage Invoice Extractor")

# Create input fields for user input and file upload
input = st.text_input("Input: ", key="input")
uploaded_file = st.file_uploader("Choose an invoice image...", type=['jpg', 'jpeg', 'png'])
image = ""

# Display the uploaded image if available
if uploaded_file is not None:
    image = Image.open(uploaded_file)   
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Define the prompt for the generative model
input_prompt = """
You are an expert in invoice analysis. We will upload an image of an invoice, and you will need to answer questions based on the details found in the uploaded invoice image.
"""

# Process the input when the submit button is clicked
submit = st.button("Tell me about the invoice")
if submit:
    if uploaded_file is not None:
        image_data = process_uploaded_image(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, input)
        st.subheader("Response:-")
        st.write(response)
    else:
        st.error("Please upload an invoice image.")