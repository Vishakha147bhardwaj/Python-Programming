import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader

# Load API keys from .env file
load_dotenv()

def load_seo_documents(directory_path: str):
    """
    Loads raw text/markdown documents from a specific folder 
    and converts them into LlamaIndex Document objects.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        # Create a dummy file for execution stability
        with open(f"{directory_path}/seo_tips.txt", "w") as f:
            f.write("SEO Tip: Always use descriptive H1 tags.\nKeep target keywords in the first 100 words.")
            
    print(f"--- Loading documents from: {directory_path} ---")
    
    # SimpleDirectoryReader automatically detects file types in a directory
    reader = SimpleDirectoryReader(input_dir=directory_path)
    documents = reader.load_data()
    
    for idx, doc in enumerate(documents):
        print(f"Document {idx} Loaded successfully!")
        print(f"Metadata: {doc.metadata}")
        print(f"Content Snippet: {doc.text[:70]}...\n")
        
    return documents

# Execute loading
seo_docs = load_seo_documents("./seo_knowledge")
