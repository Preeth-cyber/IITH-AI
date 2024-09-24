import pandas as pd
from dotenv import load_dotenv ,find_dotenv
import openai
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI, OpenAI
import os

load_dotenv(find_dotenv(),override=True)
openai.api_key=os.environ["OPENAI_API_KEY"]

def csv_query(filename,question):
    agent = create_csv_agent(
    ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"),temperature=0, model="gpt-4"),
    filename,
    verbose=False,
    allow_dangerous_code=True,
    agent_type=AgentType.OPENAI_FUNCTIONS)
    result=agent.run(question)
    return result