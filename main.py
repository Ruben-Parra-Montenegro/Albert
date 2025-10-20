"""
Main script to run the Albert agent.
This script initializes and runs the AI agent with configured tools.
"""

import os
from dotenv import load_dotenv

from packages.agent.agent_setup import agent_definition, start_agent, call_agent

def main():
    """Initialize and run the agent."""
    
    load_dotenv()

    print("\n" + "="*60)
    print("Initializing Albert agent")
    print("="*60 + "\n")

    # Initialize the chat model
    chat_model = agent_definition()
    print("\n" + "="*60)
    print("Chat model initialized")
    print("="*60 + "\n")
    
    # Create the agent with tools
    agent = start_agent(chat_model)
    print("\n" + "="*60)
    print("Agent created with tools")
    print("="*60 + "\n")
    
    print("\n" + "="*60)
    print("Albert is ready! Starting test conversation...")
    print("="*60 + "\n")
    
    response = call_agent(agent)
    print(response)
if __name__ == "__main__":
    main()
