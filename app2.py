from flask import Flask, render_template, request, send_from_directory, render_template, jsonify
import os
from flask_cors import CORS
from src.index  import ...
from src.doc_process ...

UPLOAD_FOLDER = "uploads"
app = Flask(__name__)
CORS(app)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def index():
    uploads = os.path.join(app.root_path, app.config["UPLOAD_FOLDER"])
    files = [f for f in os.listdir(uploads) if os.path.isfile(os.path.join(uploads, f))]

    return render_template("index.html")



@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    filename = file.filename
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    return "File uploaded successfully."


@app.route("/download/<filename>")
def download(filename):
    uploads = os.path.join(app.root_path, app.config["UPLOAD_FOLDER"])
    return send_from_directory(directory=uploads, path=filename)


@app.route("/chat", methods=["POST", "GET"])
def chating():
    from llama_cpp import Llama
    chat = request.form.get("chat")
    top_texts = text_search.get_top_texts(query, 5)

    from_user = request.form.get("from_user")
    llm = Llama(model_path="/home/dumball/gemma-2b-it-q4_k_m.gguf")
    output = llm(f"context: {top_texts} answers based on this context only \nuser: {chat_input}", max_tokens=80, stop=["Q:"], echo=True)

    return jsonify(output=output['choices'][0]['text'])


@app.route("/getembeddings", methods=["GET"])
def getcaptions():
    return 0






if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)


#@app.route("/rename/<img>", methods=["POST"])
#def rename(img):
#    import predict_step from renamefiles
#    predict_step
