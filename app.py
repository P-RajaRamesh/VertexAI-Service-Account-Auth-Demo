from google import genai
from google.oauth2 import service_account
import streamlit as st
import os
from dotenv import load_dotenv

import tempfile
import base64

load_dotenv()

# Decode your Base64 key
encoded_key = os.getenv("SERVICE_ACCOUNT_KEY_BASE64")
decoded_bytes = base64.b64decode(encoded_key)

# Write to a temporary file
with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
    temp_file.write(decoded_bytes)
    temp_file_path = temp_file.name

st.set_page_config(
    page_title="Demo",
    page_icon="🧊"

)    

st.title("Demo App")

# SERVICE_ACCOUNT_KEY_FILE=os.getenv("SERVICE_ACCOUNT_KEY_FILE")
PROJECT_ID=os.getenv("PROJECT_ID")
LOCATION=os.getenv("LOCATION")
MODEL_NAME=os.getenv("MODEL_NAME")

credentials=service_account.Credentials.from_service_account_file(
    # SERVICE_ACCOUNT_KEY_FILE,
    temp_file_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

# Deleting temp file after authentication from Temp folder
os.remove(temp_file_path)

client = genai.Client(
    vertexai=True, 
    project=PROJECT_ID, 
    location=LOCATION, 
    credentials=credentials
)

st.header("Vertex AI Serive Account authentication Demo")

input=st.text_input("Ask anything...")

response=client.models.generate_content(
    model=MODEL_NAME,
    contents=input
)

if st.button("Submit"):
    st.markdown(response.text)
