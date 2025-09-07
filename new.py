# https://github.com/googleapis/python-genai
# This new version depends on google-genai
from google import genai
from google.oauth2 import service_account
import os
from dotenv import load_dotenv

load_dotenv()

SERVICE_ACCOUNT_KEY_FILE=os.getenv("SERVICE_ACCOUNT_KEY_FILE")
PROJECT_ID=os.getenv("PROJECT_ID")
LOCATION=os.getenv("LOCATION")
MODEL_NAME=os.getenv("MODEL_NAME")

credentials=service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_KEY_FILE,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

# Only run this block for Vertex AI API
client = genai.Client(
    vertexai=True, 
    project=PROJECT_ID, 
    location=LOCATION, 
    credentials=credentials
)

response=client.models.generate_content(
    model=MODEL_NAME,
    contents="What is the capital of India? Tell me something about it."
    # contents="What is the capital of Andhra Pradesh? Tell me something about it."
)

if response.text:
    print(response.text)
