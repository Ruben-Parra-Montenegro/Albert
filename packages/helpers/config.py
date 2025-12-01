import json
from pathlib import Path

def load_config(config_path: str = "config.json") -> dict:
    # """Load agent configuration from JSON file."""
    default_config = {
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
    
    # Check user setting if changed and merge with defaults, overwrites differences. if not config.json is found it will create one.

    config_file = Path(config_path)
    if config_file.exists():
        with open(config_file, 'r') as f:
            user_config = json.load(f)
            default_config.update(user_config)
    else:
        
        with open(config_file, 'w') as f:
            json.dump(default_config, f, indent=2)
    
    return default_config