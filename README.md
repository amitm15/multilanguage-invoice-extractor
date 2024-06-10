# MultiLanguage Invoice Extractor

## Overview

The MultiLanguage Invoice Extractor is a Streamlit web application that leverages Google Generative AI to analyze invoice images and provide detailed responses based on the extracted information. This tool supports multiple languages, making it versatile for various use cases.

## Features

- Upload and display invoice images.
- Input custom questions or prompts related to the invoice.
- Generate detailed responses using the Gemini AI model from Google.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/multilanguage-invoice-extractor.git
   cd multilanguage-invoice-extractor

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt


4. **Set up your environment variables:**
   Modify the .env file in the root directory of the project and add your Google API key:
   ```bash
   GOOGLE_API_KEY=your_google_api_key


## Features
1. **Run the Streamlit application:**
   ```bash
   streamlit run app.py

2. **Open your web browser and navigate to:**
   ```bash
   http://localhost:8501

3. **Upload an invoice image and input your query:**

- Use the file uploader to select an image (supported formats: JPG, JPEG, PNG).
- Enter your query or prompt in the input field.
- Click the "Tell me about the invoice" button to generate a response.
