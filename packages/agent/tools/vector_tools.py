from pathlib import Path
from packages.helpers.config import load_config
import chromadb
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter 

def Add_to_vector_store(file_name: str) -> str:
    """
    Before this tool is run, run the file_name_extractor function to get available markdown files.

    Make sure to change this value to false: pdf_to_markdown=False

    Use given context from my instruction and the file_name_extractor function to decide which markdown file to add.

    Add a converted markdown file to the vector database for later retrieval.
    Use this after converting PDFs to markdown.
    """
    
    config = load_config()
    docling_output = Path(config.get("docling_out_directory", "./sandbox")).resolve()
    vector_store_path = Path(config.get("vector_store_directory", "./sandbox/vector_store")).resolve()
    
    safe_filename = file_name if file_name.endswith('.md') else f"{file_name}.md"
    md_file = docling_output / safe_filename
    
    if not md_file.exists():
        return f"Markdown file not found: {safe_filename}"
    
    try:
     
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_text(content)
        
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        vectorstore = Chroma(
            persist_directory=str(vector_store_path),
            embedding_function=embeddings
        )
        
        vectorstore.add_texts(
            texts=chunks,
            metadatas=[{"source": safe_filename, "chunk": i} for i in range(len(chunks))]
        )
        
        return f"Added {len(chunks)} chunks from {safe_filename} to vector store"
    
    except Exception as e:
        return f"Error: {str(e)}"
    

def Search_vector_store(query: str, top_k: int = 3) -> str:
    """

    Search the vector database for information from previously stored documents.
    
    USE THIS TOOL when asked about:
    - Resume information (name, experience, skills, education)
    - Personal information stored in converted documents
    - Any specific details from PDFs that were converted and added to the database
    
    Do NOT use this for general knowledge - use Google search instead.

    """
    
    config = load_config()
    vector_store_path = Path(config.get("vector_store_directory", "./sandbox/vector_store")).resolve()
    
    if not vector_store_path.exists():
        return "Vector store not found. Convert and add PDFs first using Add_to_vector_store."
    
    try:
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        vectorstore = Chroma(
            persist_directory=str(vector_store_path),
            embedding_function=embeddings
        )
        
        results = vectorstore.similarity_search(query, k=top_k)
        
        if not results:
            return f"No results found for: {query}"
        
        output = f" {len(results)} relevant chunks:\n\n"
        for i, doc in enumerate(results, 1):
            source = doc.metadata.get('source', 'Unknown')
            output += f"**{i}. From {source}:**\n"
            output += f"{doc.page_content}\n\n"
        
        return output
    
    except Exception as e:
        return f"Error searching: {str(e)}"
    

def List_vector_store() -> str:
    """

    Before searching the vector store, use this tool to see what documents are stored.

    With given context, decide what information is available to search.

    List all documents currently stored in the vector database.
    Use this to see what information is available to search.
    """
    
    config = load_config()
    vector_store_path = Path(config.get("vector_store_directory", "./sandbox/vector_store")).resolve()
    
    if not vector_store_path.exists():
        return "Vector store not found."
    
    try:
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        vectorstore = Chroma(
            persist_directory=str(vector_store_path),
            embedding_function=embeddings
        )
        
        all_docs = vectorstore.get()
        
        if not all_docs['ids']:
            return "Vector store is empty"
        
        sources = {}
        for metadata in all_docs['metadatas']:
            source = metadata.get('source', 'Unknown')
            sources[source] = sources.get(source, 0) + 1
        
        output = f"Vector Store Contents ({len(all_docs['ids'])} total chunks):\n\n"
        for source, count in sources.items():
            output += f"  • {source}: {count} chunks\n"
        
        return output
    
    except Exception as e:
        return f"Error: {str(e)}"