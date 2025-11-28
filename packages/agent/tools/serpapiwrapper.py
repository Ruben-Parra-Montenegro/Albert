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

  results = search.results(Search_topic)

  organic_results = results.get("organic_results", [])

  if not organic_results:
      return "No results found."
  
  output = ""     
  for i, result in enumerate(organic_results[:3], 1):
      title = result.get("title", "No title")
      snippet = result.get("snippet", "No snippet")
      link = result.get("link", "No link")
      output += f"Result {i}:\nTitle: {title}\nSnippet: {snippet}\nLink: {link}\n\n"

  print(output)
  return f"Here is what I found: {output}"