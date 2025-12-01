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

    if not os.getenv('OPENROUTER_API_KEY'):
        print("Error: OPENROUTER_API_KEY not found in .env file")
        print("Please create a .env file with your API keys")
        return
    
    if not os.getenv('SERPAPI_API_KEY'):
        print("Warning: SERPAPI_API_KEY not found in .env file")
        print("Web search functionality will not work without this key.\n")

    print("\n" + "="*60)
    print("Initializing Albert agent")
    print("="*60 + "\n")

  
    chat_model = agent_definition()
    print("\n" + "="*60)
    print("Chat model initialized")
    print("="*60 + "\n")
    
   
    agent = start_agent(chat_model)
    print("\n" + "="*60)
    print("Agent created with tools")
    print("="*60 + "\n")
    
    print("\n" + "="*60)
    print("Albert is ready! Starting test conversation...")
    print("Type 'exit', 'quit', or 'q' to stop.")
    print("="*60 + "\n")
    
    
    while True:
        try:
            user_input = input("👤 You: ")
            
            if user_input.lower().strip() in ['exit', 'quit', 'q']:
                print("\n👋 Goodbye!")
                break
    
            if not user_input.strip():
                continue
          
            response = call_agent(agent, user_input)
        
            final_message = response['messages'][-1].content
            print(f"\n🤖 Albert: {final_message}\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}\n")
            print("Please try again or type 'exit' to quit.\n")


# you can adjust what you take from the output of the LLM by setting something equal to:
# final_message = response['messages'][-1].content, the number in brackets means the index of the message in the list
# so if you wanted the first message you would do [0], if you wanted the second

# response = {
#     'messages': [
#         HumanMessage("Create a todo list"),      # [0] Your message
#         AIMessage(""),                            # [1] Agent deciding
#         ToolMessage("File created..."),           # [2] Tool result
#         AIMessage("I created todo.txt for you!") # [3] ← [-1] Final answer
#     ]
# }

    # response = call_agent(agent)
    # print(response)
if __name__ == "__main__":
    main()
