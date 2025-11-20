# Final Project - Albert

## Goal

I want to learn how to make agents utilizing Langchain, while messing with docling. I will attempt to make this into a neat little CLI tool. 

Essentially making a simple agent anyone with a few free api keys can use, modify and mess around with. A plus would be if I can actually make it usefull.

Goals:

- Utilize MCP
- Utilize Docling
- Create something you find interesting
- Make the CLI interesting to look at.(looks like stuff is happening when actions are being taken just to alert you the agent is doing things.)
- Model configuration 
- Structured output 
- Conversational memory 
- keep it simple and functional(hopefully)

## To-Do

- make list for each item and track separately
- make into .exe for running on pc easy
- playwright functionality
- docling functionality
- memory
- give it a place to work in(sandbox)


## Added(done)

- CLI(python)

## Wish-List

- file based checkpointers
- investigate mcp servers
- add allowed actions config file
- sandbox to wherever the user wants it in some sort of config file
- make up some creative tools for agents to use
- work on tuning model responses, I noticed the sample prompt sometimes leads to the model asking a question and not just making a file.
- previous points leads me to question, i should add a way to respond to the model. this probably involves the agent having memory.
- langchain site has a bunch of neat features, lets see what we can build with them.(consider implementing them)


## Requirements
- Python 3.12.12

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## API KEYS to use:

1. create your .env file and add these 2 lines:

- OPENROUTER_API_KEY = 
- SERPAPI_API_KEY = 


## Usefull resources: 

- https://docs.langchain.com/oss/python/langchain/quickstart
- https://rust-cli.github.io/book/index.html
- https://www.youtube.com/watch?v=5UA9UWWAagc

## features

I tried making it so you can just add custom tools to the user_tools.py file and just forget about everything else.

## Configuration

Albert uses a `config.json` file to customize the AI model settings and behavior. The file is automatically created with default values on first run, or you can create it manually.

**config.json:**

```json
{
  "model": "nvidia/nemotron-nano-9b-v2:free",
  "base_url": "https://openrouter.ai/api/v1",
  "temperature": 0.7,
  "max_tokens": 2000,
  "system_prompt": "You are a helpful assistant.\n\nYou are able to do various things:\n\n- Search Google for relevant information on a topic.\n- Create files and write to them, for things such as notes, code files, etc."
}
```

**Configuration Options:**

- **model**: The AI model to use (any model from OpenRouter)
- **base_url**: API endpoint (OpenRouter, OpenAI, etc.)
- **temperature**: Controls randomness (0.0 = deterministic, 1.0 = creative)
- **max_tokens**: Maximum response length
- **system_prompt**: Instructions that define the agent's personality and capabilities

**Note:** The config file is automatically created with defaults if it doesn't exist. You can customize any values to suit your needs!


## Output Example(You can grab just the final message but this shows everything it spits out)

```bash
============================================================
Initializing Albert agent
============================================================


============================================================
Chat model initialized
============================================================


============================================================
Agent created with tools
============================================================


============================================================
Albert is ready! Starting test conversation...
Type 'exit', 'quit', or 'q' to stop.
============================================================

{'messages': [HumanMessage(content='Can you write me some rust code that prints albert and put it in a .rs file?', additional_kwargs={}, response_metadata={}, id='2289fdbf-7975-4155-bab0-5d2af0331a02'), AIMessage(content='', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 400, 'prompt_tokens': 371, 'total_tokens': 771, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_provider': 'openai', 'model_name': 'nvidia/nemotron-nano-9b-v2:free', 'system_fingerprint': None, 'id': 'gen-1760924396-gi1nqIZvs2zfhliZyKWH', 'finish_reason': 'tool_calls', 'logprobs': None}, id='lc_run--7529fbdf-2270-4778-a13a-c2ccedc5bf1f-0', tool_calls=[{'name': 'Write_to_file', 'args': {'topic': 'Rust Code', 'file_name': 'albert.rs', 'file_content': 'fn main() {\n    println!("albert");\n}'}, 'id': 'HNb0Lo6mD', 'type': 'tool_call'}], usage_metadata={'input_tokens': 371, 'output_tokens': 400, 'total_tokens': 771, 'input_token_details': {}, 'output_token_details': {}}), ToolMessage(content='File created for Rust Code, with name: albert.rs', name='Write_to_file', id='2eb016ec-5d21-44a8-8799-8f308c47832b', tool_call_id='HNb0Lo6mD'), AIMessage(content='The Rust code has been successfully written to a file named **albert.rs**. The file contains the following code:\n\n```rust\nfn main() {\n    println!("albert");\n}\n```\n\nLet me know if you\'d like to modify the code or need help with anything else!\n', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 165, 'prompt_tokens': 468, 'total_tokens': 633, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_provider': 'openai', 'model_name': 'nvidia/nemotron-nano-9b-v2:free', 'system_fingerprint': None, 'id': 'gen-1760924400-ankJf6IWrURz1ulEa1G1', 'finish_reason': 'stop', 'logprobs': None}, id='lc_run--3d1aa015-13f4-49c8-8ead-965333a6a1d5-0', usage_metadata={'input_tokens': 468, 'output_tokens': 165, 'total_tokens': 633, 'input_token_details': {}, 'output_token_details': {}})]}

```

## Conversation Memory(none)

Albert uses **LangGraph's MemorySaver** to remember your conversation history. This means:


**Example conversation:**

```
👤 You: my name is ruben

🤖 Albert: Hello, Ruben! How can I assist you today? Let me know if you need help with anything specific, and I'll do my best to support you.


👤 You: whats my name?

🤖 Albert: I don't have access to personal information about users unless they provide it during our conversation. Could you please share your name with me? Once you do, I can store it in a file for future reference if you'd like.
```

## Conversation Memory(has memory)

```
👤 You: my name is ruben

🤖 Albert: Hello, Ruben! How can I assist you today? Would you like me to create a file, search for information, or help with something specific?


👤 You: what is my name

🤖 Albert: Your name is Ruben. 😊 Let me know if you need help with anything else!
```