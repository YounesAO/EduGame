from flask import Flask, request, jsonify, render_template
import os
from llm_handler import get_prompt_result
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "secret_key"
app.config["UPLOAD_FOLDER"] = "/tmp"  # Changed to /tmp for Cloud Run
app.config["ALLOWED_EXTENSIONS"] = {"pdf"}
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max file size
# Enable CORS for specific origin and route
CORS(app, resources={
    r"/query-pdf": {"origins": "http://localhost:3000"}
})

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/query-pdf', methods=['POST'])
def query_pdf():
    try:
        # Retrieve file and query from request
        pdf_file = request.files.get('pdf')

        if not pdf_file :
            return jsonify({"error": "PDF file is required"}), 400

        if not allowed_file(pdf_file.filename):
            return jsonify({"error": "Invalid file type. Only PDF files are allowed."}), 400

        # Save file temporarily
        filename = secure_filename(pdf_file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        pdf_file.save(filepath)

        try:
            # Process the PDF and query using the function
            result = get_prompt_result(filepath)
           
            print("Type of result:", type(result))
            print("Raw result:", repr(result))
            # Clean up
            if os.path.exists(filepath):
                os.remove(filepath)
            print(result)

            return jsonify({
            "answer": result
            }), 200

        except Exception as e:
            # Clean up in case of error
            if os.path.exists(filepath):
                os.remove(filepath)
            raise e

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)