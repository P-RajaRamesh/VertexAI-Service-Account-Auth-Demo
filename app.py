from google import genai
from google.oauth2 import service_account
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Demo",
    page_icon="🧊"

)    

st.title("Demo App")

# SERVICE_ACCOUNT_KEY_FILE=os.getenv("SERVICE_ACCOUNT_KEY_FILE")
PROJECT_ID=os.getenv("PROJECT_ID")
LOCATION=os.getenv("LOCATION")
MODEL_NAME=os.getenv("MODEL_NAME")

# credentials=service_account.Credentials.from_service_account_file(
#     SERVICE_ACCOUNT_KEY_FILE,
#     scopes=["https://www.googleapis.com/auth/cloud-platform"]
# )

SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]
key_path = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]

credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=SCOPES
)

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
