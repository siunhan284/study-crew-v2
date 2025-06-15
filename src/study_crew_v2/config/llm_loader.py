import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

def get_azure_llm():
    # Required environment vars
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

    if not all([api_key, api_base, api_version, deployment]):
        raise EnvironmentError("Missing required Azure OpenAI env vars!")

    return LLM(
        model=f"azure/{deployment}",
        api_key=api_key,
        api_base=api_base,
        api_version=api_version
    )


# from langchain_openai import AzureChatOpenAI
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()

# def get_azure_openai_llm():
#     api_key = os.getenv("AZURE_OPENAI_API_KEY")
#     api_version = os.getenv("AZURE_OPENAI_API_VERSION")
#     deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
#     azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

#     if not all([api_key, api_version, deployment_name, azure_endpoint]):
#         raise EnvironmentError("One or more required environment variables are missing.")

#     return AzureChatOpenAI(
#         api_key=api_key,
#         azure_endpoint=azure_endpoint,
#         openai_api_version=api_version,
#         deployment_name=deployment_name
#     )
