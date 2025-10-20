from langchain_community.utilities import SerpAPIWrapper
import os 

api_key = os.getenv("SERPAPI_API_KEY")

def Google_search(Search_topic: str) -> str:
  """Search the web for the desired topic and return the output."""
  search = SerpAPIWrapper()

  params = {
        "engine": "bing",
        "gl": "us",
        "hl": "en",
  }
  search = SerpAPIWrapper(params=params)

  output = search.run(Search_topic)

  return f"Here is what I found: {output}"