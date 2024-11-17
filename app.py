from flask import Flask, request, jsonify,render_template
from llm_handler import get_prompt_result


app = Flask(__name__)
app.secret_key = "secret_key"
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["ALLOWED_EXTENSIONS"] = {"pdf"}


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/query-pdf', methods=['POST'])
def query_pdf():
    try:
        # Retrieve file and query from request
        pdf_file = request.files.get('pdf')
        query = request.form.get('query')

        if not pdf_file or not query:
            return jsonify({"error": "PDF file and query are required"}), 400

        # Process the PDF and query using the function
        result = get_prompt_result(pdf_file, query)

        # Return the response
        return jsonify({"query": query, "answer": result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
