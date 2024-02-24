# For RAG
from docy import PDFProcessor
import faiss
#import torch.nn.functional as F
#from torch.utils.data import DataLoader
#from datasets import load_from_disk, dataset
import numpy as np

#pdf_processor = PDFProcessor("./87286_92960v00_Decoding_Wireless.pdf")
#chunks = pdf_processor.chunk_text(100)  # Chunk size of 100 characters


def build_index(string_list):
    """
    Build an index for a list of strings.
    
    Args:
    - string_list (list): List of strings to build the index from.
    
    Returns:
    - index (faiss.IndexFlatL2): Index built from the strings.
    - string_embeddings (np.array): Embeddings of the strings.
    """
    # Convert strings to embeddings
    string_embeddings = np.zeros((len(string_list), 256))  # Example: Assuming embeddings of length 256
    for i, string in enumerate(string_list):
        string_embeddings[i] = np.random.rand(256)  # Example: Replace with actual embedding generation
    
    # Build index
    index = faiss.IndexFlatL2(string_embeddings.shape[1])
    index.add(string_embeddings)
    
    return index, string_embeddings

def find_approximate_matches(query, index, string_list, string_embeddings, k=5):
    """
    Find approximate matches for a query within a list of strings using the built index.
    
    Args:
    - query (str): The query string.
    - index (faiss.IndexFlatL2): Index built from the strings.
    - string_list (list): List of strings to search for matches.
    - string_embeddings (np.array): Embeddings of the strings.
    - k (int): Number of nearest neighbors to return (default: 5).
    
    Returns:
    - matches (list): List of tuples (string, score) representing matches.
    """
    query_embedding = np.random.rand(256)  
    
    distances, indices = index.search(np.array([query_embedding]), k)
    
    # Retrieve matches
    matches = [(string_list[i], distances[0][j]) for j, i in enumerate(indices[0])]
    
    return matches


pdf_processor = PDFProcessor("./87286_92960v00_Decoding_Wireless.pdf")
chunks = pdf_processor.chunk_text(400)  # Chunk size of 100 characters
#chunks = ["hello", "whaterver", "apple", "car", "nigger"]
query = "radio"  # Intentionally misspelled query

index, string_embeddings = build_index(chunks)
matches = find_approximate_matches(query, index, chunks, string_embeddings)
print(matches)

