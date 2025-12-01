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

def file_name_extractor(pdf_to_markdown: bool) -> str:
    """
    When someone asks to convert pdfs to markdown, you will use this function to find the available pdf files. Use context to decide which pdf to convert.

    Or If someone wants to add to the vector store, use this to find the available markdown files. While making the pdf_to_markdown parameter False.

    Extract the file names from a given file, for use by the agent.

    When prompted to pick a PDF to convert, this function will list the available PDF files in the sandboxed directory.

    Decide whether this operation is for Docling input or output based on the for_docling parameter. True or False. If it is False you will use the name for the vector store adding.
    """

    config = load_config()

    if pdf_to_markdown:

        docling_in_sandbox = Path(config.get("docling_in_directory", "./sandbox")).resolve()
        pdf_files = list(docling_in_sandbox.glob("*.pdf"))
    else:
        docling_out_sandbox = Path(config.get("docling_out_directory", "./sandbox")).resolve()
        pdf_files = list(docling_out_sandbox.glob("*.pdf"))

    

    return "\n".join([os.path.basename(pdf) for pdf in pdf_files])


def PDF_converter_to_MD(file_name: str) -> str:
    """
    Convert a PDF file to Markdown format using Docling, using the file_name_extractor function for pdf names to pick.
    """

    from docling.document_converter import DocumentConverter

    config = load_config()
    docling_in_sandbox = Path(config.get("docling_in_directory", "./sandbox")).resolve()
    docling_out_sandbox = Path(config.get("docling_out_directory", "./sandbox")).resolve()

    safe_filename = os.path.basename(file_name)

    input_file = docling_in_sandbox / safe_filename

    try:
        result = DocumentConverter().convert(input_file)

        output_filename = f"{input_file.stem}.md"
        output_path = docling_out_sandbox / output_filename

        markdown_content = result.document.export_to_markdown()

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)


        preview = markdown_content[:500] if len(markdown_content) > 500 else markdown_content
        return f"Converted: {safe_filename}\n Output: {output_path}\n\n Preview:\n{preview}..."
        
    except Exception as e:
            return f"Error converting {safe_filename}: {str(e)}"