import numpy as np
import faiss
import torch
from transformers import AutoTokenizer, AutoModel
#from docy import PDFProcessor

class TextSearch:
    def __init__(self, texts, model_name='distilbert-base-uncased'):
        # Initialize the tokenizer and model from Hugging Face
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        # Encode the texts
        self.texts = texts
        self.text_embeddings = self._encode_texts(texts)
        # Dimension of the vectors
        self.d = self.text_embeddings.shape[1]
        # Create a FAISS index
        self.index = faiss.IndexFlatL2(self.d)
        # Add the text embeddings to the FAISS index
        self.index.add(self.text_embeddings)
    
    def _encode_texts(self, texts):
        # Tokenize input texts
        encoded_input = self.tokenizer(texts, padding=True, truncation=True, return_tensors='pt')
        # Get the model's last hidden states
        with torch.no_grad():
            model_output = self.model(**encoded_input)
        # Mean pooling here, but you can also try max pooling or CLS token
        return model_output.last_hidden_state.mean(dim=1).cpu().numpy()
    
    def search(self, query, k=2):
        # Encode the query
        query_embedding = self._encode_texts([query])[0]
        # Search the index
        distances, indices = self.index.search(np.array([query_embedding]), len(self.texts))
        # Return the indices of the texts along with their distances, sorted by similarity
        ranked_texts = {self.texts[i]:distances[0][j] for j, i in sorted(enumerate(indices[0]), key=lambda x: x[1])}
        #ranked_texts = {(self.texts[i], distances[0][j]) for j, i in sorted(enumerate(indices[0]), key=lambda x: x[1])}
        top_indices = dict(sorted(ranked_texts.items(), key=lambda item: item[1])[:k])

        return ranked_texts, top_indices

    def get_top_texts(self, query, k=2):
        # Encode the query
        query_embedding = self._encode_texts([query])[0]
        # Search the index
        _, indices = self.index.search(np.array([query_embedding]), len(self.texts))
        # Get the top k indices
        top_indices = indices[0][:k]
        # Retrieve the texts corresponding to the top indices
        top_texts = [self.texts[idx] for idx in top_indices]
        return top_texts
