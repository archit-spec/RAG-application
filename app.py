from flask import Flask, render_template, request, send_from_directory, render_template, jsonify
import os
from flask_cors import CORS
from llama_cpp import Llama
from src.indexing import TextSearch
from src.doc_process import PDFProcessor
#from flask_cors import CORS

app = Flask(__name__)
CORS(app)

current_directory = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(current_directory, "src", "87286_92960v00_Decoding_Wireless.pdf")
pdf_processor = PDFProcessor(pdf_path)
corpus = pdf_processor.chunk_text(100)  # Chunk size of 100 characters
text_search = TextSearch(corpus)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data['query']
    top_texts = text_search.get_top_texts(query, 5)
    chat_input = request.form.get("chat")

    #chat_input = data['chat']

    llm = Llama(model_path="/home/dumball/gemma-2b-it-q4_k_m.gguf")
    output = llm(f"context: {top_texts} answers based on this context only \nuser: {chat_input}", max_tokens=60, stop=["Q:"], echo=True)
    response = output
    
    return jsonify({'response': response})

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)


