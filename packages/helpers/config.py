import json
from pathlib import Path

def load_config(config_path: str = "config.json") -> dict:
    """Load agent configuration from JSON file."""
    default_config = {
        "model": "nvidia/nemotron-nano-9b-v2:free",
        "base_url": "https://openrouter.ai/api/v1",
        "temperature": 0.7,
        "max_tokens": 2000,
    }
    
    # Check user setting if changed and merge with defaults, overwrites differences. if not config.josn is found it will create one.

    config_file = Path(config_path)
    if config_file.exists():
        with open(config_file, 'r') as f:
            user_config = json.load(f)
            default_config.update(user_config)
    else:
        # Create default config file
        with open(config_file, 'w') as f:
            json.dump(default_config, f, indent=2)
    
    return default_config