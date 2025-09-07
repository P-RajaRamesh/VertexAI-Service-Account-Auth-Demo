import vertexai
# UserWarning: This feature is deprecated as of June 24, 2025 and will be removed on June 24, 2026. 
# For details, see https://cloud.google.com/vertex-ai/generative-ai/docs/deprecations/genai-vertexai-sdk.
# This old version depends on google-cloud-aiplatform
from vertexai.generative_models import GenerativeModel
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

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    credentials=credentials
)

model=GenerativeModel(MODEL_NAME)

response=model.generate_content("What is the capital of India? Tell me something about it.")

if response.text:
    print(response.text)
