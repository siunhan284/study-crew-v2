from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os

# Load from .env file
load_dotenv()

# Get environment variables
api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

# Create LLM instance
llm = AzureChatOpenAI(
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    openai_api_version=api_version,
    deployment_name=deployment_name
)

# Run a test
response = llm.invoke("What are you?")
print(response.content)


# from langchain_openai import AzureChatOpenAI

# llm = AzureChatOpenAI(
#     azure_endpoint="https://<endpoint_name>.openai.azure.com/",
#     api_key="YOUR_API_KEY",
#     deployment_name="gpt-35-turbo",  # Your actual deployment name
#     api_version="2024-05-01-preview"
# )

# response = llm.invoke("Who are you?")
# print(response.content)
