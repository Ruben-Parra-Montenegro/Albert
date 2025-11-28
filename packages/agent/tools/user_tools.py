import os
from pathlib import Path
from packages.helpers.config import load_config
from playwright.sync_api import sync_playwright, Playwright


def Write_to_file(topic: str, file_name: str, file_content: str) -> str:
    """
    Create MarkDown or Text file with notes based on what context was given.
    
    """

    config = load_config()

    sandbox_path = config.get("sandbox_directory", "./sandbox")

    sandbox = Path(sandbox_path).resolve()

    sandbox.mkdir(parents=True, exist_ok=True)

    # File names include entire paths, so we nee to get only the file name. Leaving the entire path allows the LLM to put a file anywhere, if you explicitly want that. But that isnt safe.
    safe_filename = os.path.basename(file_name)

    file_path = sandbox / safe_filename

    if not file_path.resolve().is_relative_to(sandbox.resolve()):
        return f"Security Error: Cannot write outside sandbox directory"

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(file_content)

    return f"File created for {topic}, with name: {safe_filename} in {sandbox}"

def Web_scrape(url: str) -> str:
    """
    Extract text content from a webpage using Playwright.
    """

    try:
        with sync_playwright() as playwright:
            chromium = playwright.chromium 
            browser = chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(url, timeout=30000)
            print(f"Navigated to {url}")
            # content = page.content()
            content = page.inner_text("body")

            page.wait_for_timeout(5000)

            browser.close()
            print("Webpage content extracted successfully.")
        if len(content) > 2000:
            print("Webpage content extracted successfully.")
            return f"Webpage text (first 2000 chars):\n\n{content[:2000]}...\n\n(Total length: {len(content)} characters)"
        return f"Webpage text:\n\n{content}"

    
    except Exception as e:
        return f"Error: {str(e)}"