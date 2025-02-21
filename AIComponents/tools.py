from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from crewai_tools import WebsiteSearchTool

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI GPT model
openaigpt4 = ChatOpenAI(model='gpt-4', 
                        temperature=0.2, 
                        api_key=os.getenv('openapi_key'))

# Initialize GoogleSerperAPIWrapper with the API key from environment variables
WebsiteSearchTool = WebsiteSearchTool()

# Initialize GoogleSerperAPIWrapper with the API key from environment variables
google_serper = GoogleSerperAPIWrapper(api_key=os.getenv('serper_api_key'))
