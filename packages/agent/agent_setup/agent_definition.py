import os

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI 

from packages.agent.tools import user_tools, serpapiwrapper
from packages.helpers.tool_getter import get_all_tools
from packages.helpers.config import load_config


def agent_definition():
    """Initialize the chat model with config settings."""
    
    config = load_config()
    
    chat_model = ChatOpenAI(
        model=config.get("model", "nvidia/nemotron-nano-9b-v2:free"),
        base_url=config.get("base_url", "https://openrouter.ai/api/v1"),
        api_key=os.getenv('OPENROUTER_API_KEY'),
        temperature=config.get("temperature", 0.7),
        max_tokens=config.get("max_tokens", 2000),
    )
    return chat_model


def start_agent(chat_model):
    """Create an agent with the chat model and tools."""
    config = load_config()
    tools = get_all_tools(user_tools, serpapiwrapper)

    agent = create_agent(
        model=chat_model, 
        tools=tools,
        system_prompt=config.get("system_prompt", "You are a helpful assistant.")
    )
    return agent

# Change this later once we figure out the cli user input stuff
# def call_agent(agent):
#    return agent.invoke(
#         {"messages": [{"role": "user", "content": "Can you write me some rust code that prints albert and put it in a .rs file?"}]}
#     )
def call_agent(agent, message: str):
    return agent.invoke(
        {"messages": [{"role": "user", "content": message}]}
    )