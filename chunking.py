from llama_index.core.node_parser import SentenceSplitter

def transform_documents_to_nodes(documents):
    """
    Splits documents into smaller, overlapping semantic chunks (Nodes).
    """
    print("--- Chunking Documents into Nodes ---")
    
    # Initialize the SentenceSplitter parser
    # chunk_size is measured in tokens, chunk_overlap ensures semantic continuity
    splitter = SentenceSplitter(chunk_size=512, chunk_overlap=50)
    
    nodes = splitter.get_nodes_from_documents(documents)
    
    for idx, node in enumerate(nodes):
        print(f"Node {idx} generated.")
        print(f"Parent Doc ID: {node.parent_node.node_id if node.parent_node else 'None'}")
        print(f"Node Content: {node.text[:100]}...\n")
        
    return nodes


seo_nodes = transform_documents_to_nodes('./seo_knowledge/seo_tips.txt')
