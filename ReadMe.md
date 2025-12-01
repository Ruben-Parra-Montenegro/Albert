# Final Project - Albert

## Why work on this:

Building a practical AI agent to learn LangChain fundamentals, RAG implementation, and tool integration. Started with minimal knowledge of how agents, vector databases, or embeddings worked—this project forced me to understand how everything connects. Goal: create a simple, functional CLI tool anyone can use with free API keys.

## Technologies used:

- Langchain (Agent Framework)
- Docling (PDF → Markdown extraction)
- Playwright (Web scraping)
- OpenRouter (LLM API)
- ChromaDB (Vector storage)
- Sentence-Transformers (Embeddings)
- SerpAPI (Google Search)

## Capabilities:

- Conversational memory using LangGraph's MemorySaver
- Web search via SerpAPI + scraping with Playwright
- PDF to Markdown conversion (Docling) with table extraction
- Vector storage (ChromaDB) for RAG-based retrieval
- Sandboxed file creation/management (configurable directory)
- Python CLI interface
- Model and sandbox configuration via `config.json`

## What did I learn:

- Agent architecture and how LangChain orchestrates tool calls + memory
- RAG pipelines with vector embeddings (ChromaDB + Sentence-Transformers)
- Custom tool design and function calling
- Model limitations (smaller models struggle with complex tool calls)
- Prompt engineering impact on agent behavior
- Security basics (path sanitization, sandboxing, input validation)
- PDF data extraction with Docling (tables, formatting preservation)
- Debugging agents (sometimes you need to explicitly teach tool usage)
- API rate limits and provider differences (OpenRouter vs. Groq)

## Future work:

- File-based checkpointers for persistent conversation history
- MCP (Model Context Protocol) server integration
- Permission/allowed actions configuration system
- System prompt optimization to reduce clarifying questions
- Dynamic model switching (expert vs. fast modes)
- Autonomous web navigation via HTML/CSS analysis
- Additional LangChain features (chains, LCEL, etc.)

# Final Project - Albert(Project Notes)

## Goal

I want to learn how to make agents utilizing Langchain, while messing with docling. I will attempt to make this into a neat little CLI tool. 

Essentially making a simple agent anyone with a few free api keys can use, modify and mess around with. A plus would be if I can actually make it usefull.

Goals:

- Utilize Docling
- Create something you find interesting
- utilize vector store for RAG
- Model configuration  
- Conversational memory 
- keep it simple and functional(hopefully)

## To-Do

- allow model to be able to modify files anywhere within sandbox
- playwright functionality, maybe allow auto web nav(by pulling css or html, whatever to make informed decsisions)
- Maybe expand on the features section
- Work on doc strings for tools
- Test how different models handle things.


## Added(done)

- Playwrite allows for web scraping. combined with the serpapi web search thing we can find urls to scrape.
- CLI(python)
- memory
- give it a place to work in(sandbox), edit config for sandboxing
- docling functionality(convert pdfs to markdown with all info extracted and send to vector storage)
- can access vector storage
- can scrape websites

## Wish-List

- file based checkpointers
- investigate mcp servers
- add allowed actions config file
- sandbox to wherever the user wants it in some sort of config file
- make up some creative tools for agents to use
- work on tuning model responses, I noticed the sample prompt sometimes leads to the model asking a question and not just making a file.
- previous points leads me to question, i should add a way to respond to the model. this probably involves the agent having memory.
- langchain site has a bunch of neat features, lets see what we can build with them.(consider implementing them)
- Dynamic system prompts and models.(switching between "expert" and "faster" not so expert model)


## Requirements
- Python 3.12.12

## Playwright
- make sure to install your browser, in my case I chose chromium
- playwright install chromium

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
- https://openrouter.ai/

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
  "system_prompt": "You are a helpful assistant named Albert.\n\nYou can:\n- Search Google for information\n- Create files in the sandbox directory\n- Scrape websites\n- Convert PDFs to markdown\n- Store converted documents in a vector database\n- **Search the vector database when asked about information you don't know**\n\nIMPORTANT: When asked about someone's resume, skills, experience, or personal information, ALWAYS use Search_vector_store first to check if that information exists in the database.",
  "thread_id": "default-session",
  "sandbox_directory": "D:/Projects/sandbox",
  "docling_in_directory": "D:/Projects/sandbox/docling/pdf_not_conv",
  "docling_out_directory": "D:/Projects/sandbox/docling/md",
  "vector_store_directory": "D:/Projects/sandbox/vector_store"
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


## Hinting Agent on how to use its tools

So when working with agent and giving it tools. I ran into this when trying to get the agent to use docling without giving it a explicit name of the pdf. So I added a function that lists the file names in a given directory defined by the config file. I gave each function the simple doc string and called it good. 

One interesting thing to take from this would be that the agent did not use the name list function when propmted for the first time, I had to explain what the function did and how it worked for it to realize it could use the tool in this way. 

This goes to show that you need to adjust the agents system prompt or doc string to allow it to understand more what can be done.


```
👤 You: can you convert my resume to a markdown file?

🤖 Albert: To convert your resume to a Markdown file, I'll need the file name of your PDF resume. Could you please provide the exact name of the PDF file (e.g., "John_Doe_Resume.pdf")? Once I have that, I can proceed with the conversion.


👤 You: can you use the file_name_extractor function instead

🤖 Albert: The `file_name_extractor` function as defined does not accept any parameters, so it cannot dynamically retrieve or identify a specific file (like your resume PDF) to process. To proceed, I still need the **exact file name** of your resume PDF (e.g., "John_Doe_Resume.pdf") to use the `PDF_converter_to_MD` tool.

Could you share the file name?


👤 You: yes but you can execute it correct?

🤖 Albert: The `file_name_extractor` function, as defined in the tools, does **not** accept parameters (like a file name or directory) to identify which specific file to process. It would need to be designed differently to work in your scenario (e.g., by scanning a directory or prompting for input). Since it’s not possible to dynamically find your resume file with the current tool specs, I still need the **exact file name** of your resume PDF (e.g., "John_Doe_Resume.pdf") to proceed with the conversion. Would you like to share it?


👤 You: no run the tool i gave you, it will list the file names in a directory for you to use 
```


## Interesting things to look into later

Making the agent able to edit anything within the sandbox would be nice for this specifically

```
🤖 Albert: Your resume has been successfully converted to Markdown format! The converted file is located at:
`D:\Projects\sandbox\docling\md\resume.md`

Would you like me to help you edit the Markdown content, add specific sections, or convert it to another format?


👤 You: yes the mark down has my number in it can you remove it?

🤖 Albert: Your resume has been updated and the phone number has been removed! The modified file is now located at:
`D:\Projects\sandbox\resume_modified.md`

Would you like me to remove any other contact information (like email or links) or make additional changes to the Markdown formatting?
```

## Vector Store Demo

The project includes the ability for the agent to take a pdf, convert it to markdown using docling. This can extract useful tables and such.

With the markdown, you can then store it in vector storage for the model to pull from. Below is an example of the agent being asked a question.

It was able to use the context given to search for the info in the vector store.

```               
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

👤 You: can you tell me about my resume, maybe what job i currently work?

🤖 Albert: Based on your resume stored in the vector database, your **current job** is listed as:

**Process Manufacturing Engineer at Nylok LLC**
📍 Macomb, MI
📅 Started: March 2024

This role is in **Automation Engineering** according to your resume. Would you like me to share more details about this position or other sections of your resume?


👤 You:
```