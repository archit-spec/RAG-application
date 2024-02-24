from llama_cpp import Llama
from indexing import TextSearch
from process_document import PDFProcessor

pdf_processor = PDFProcessor("./87286_92960v00_Decoding_Wireless.pdf")
corpus = pdf_processor.chunk_text(100)  # Chunk size of 100 characters
text_search = TextSearch(corpus)
query = "what is radio"
results, ti = text_search.search(query)
print(ti, results)
#context = ti
chat = input("ask a question: ")
llm = Llama(model_path="/home/dumball/gemma-2b-it-q4_k_m.gguf")
output = llm(f"context: {ti}  answers based on this context only \nuser: {chat} \nAssistant:", max_tokens=60, stop=["Q:"], echo=True)
output=output['choices'][0]['text']
print(output)
