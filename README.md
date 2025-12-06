# 📚 EduGame - AI-Powered Educational Content Generator

EduGame is an intelligent educational platform that transforms PDF course materials into interactive learning experiences. Using OpenAI's GPT-4 and LangChain, it automatically generates quizzes, flashcards, matching exercises, and content summaries from any uploaded PDF document.

## ✨ Features

- **📝 Quiz Generation** - Automatically creates multiple-choice questions with explanations
- **🃏 Flashcards** - Generates flip cards for key terms and definitions
- **🔗 Matching Exercises** - Creates element-matching activities
- **📖 Content Summaries** - Produces detailed short content summaries for key concepts
- **🌐 Multi-language Support** - Generates content in the same language as the source PDF
- **🐳 Docker Ready** - Easy deployment with Docker and Cloud Run support

## 🏗️ Architecture
<img width="334" height="173" alt="image" src="https://github.com/user-attachments/assets/80dc2084-557a-408e-a6cd-1f08e3c7c948" />

```
EduGame/
├── app.py              # Flask application with REST API endpoints
├── llm_handler.py      # OpenAI/LangChain integration for PDF processing
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container configuration for deployment
├── templates/
│   └── index.html      # Web interface for PDF upload
├── static/
│   └── style.css       # Styling for the web interface
└── json.json           # Sample JSON output structure
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- OpenAI API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YounesAO/EduGame.git
   cd EduGame
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

   The server will start on `http://localhost:8080`

### 🐳 Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build --build-arg OPENAI_API_KEY=your_key -t edugame .
   ```

2. **Run the container**
   ```bash
   docker run -p 8080:8080 edugame
   ```

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Web interface for PDF upload |
| `/query-pdf` | POST | Generate all content types (quiz, flashcards, match, summary) |
| `/quiz-query` | POST | Generate quiz questions only |
| `/flipcards-query` | POST | Generate flashcards only |
| `/match-query-pdf` | POST | Generate matching exercises only |
| `/short-content-query-pdf` | POST | Generate content summaries only |
| `/health` | GET | Health check endpoint |

### Request Format

All content generation endpoints accept a PDF file:

```bash
curl -X POST -F "pdf=@your_file.pdf" http://localhost:8080/query-pdf
```

### Response Format

```json
{
  "answer": {
    "chapterName": "Title of the Chapter",
    "description": "Short description of the chapter",
    "quiz": [
      {
        "question": "What is the main concept?",
        "answers": ["Option A", "Option B", "Option C", "Option D"],
        "correctAnswer": ["Option B"],
        "explanation": "Explanation of why Option B is correct"
      }
    ],
    "flipcards": [
      {
        "front": "Key Term",
        "back": "Definition or description"
      }
    ],
    "match": [
      {
        "element": "Element to match",
        "matchText": "Correct match"
      }
    ],
    "shortContent": [
      "Detailed summary of an important concept",
      "Another detailed summary"
    ]
  }
}
```

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **AI/ML**: OpenAI GPT-4, LangChain
- **Vector Store**: FAISS
- **PDF Processing**: PyPDF2
- **Deployment**: Docker, Gunicorn

## ⚙️ Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `PORT` | Server port | 8080 |
| `MAX_CONTENT_LENGTH` | Max upload file size | 16MB |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Younes AO**

---

⭐ Star this repository if you find it helpful!
