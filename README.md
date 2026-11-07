# 🤖 AI Personal Assistant

A small Flask web app powered by the OpenAI API. Ask it anything, or paste an email and get a short summary.

### 🌐 Live Demo: [https://aiassistant-main.vercel.app](https://assistantai-main.vercel.app/)

---

## ✨ Features

- **Ask Anything:** type a question and get an answer from an AI personal assistant.
- **Email Summarization:** paste a long email and get a 2-3 sentence summary.
- **Loading indicators** while the AI is thinking, with no page reloads (uses `fetch`).
- **Error handling** for empty input and failed API calls.

## 🛠️ Tech Stack

- **Backend:** Python, [Flask](https://flask.palletsprojects.com/)
- **AI:** [OpenAI API](https://platform.openai.com/) (Responses API)
- **Frontend:** HTML, CSS, vanilla JavaScript
- **Config:** python-dotenv
- **Production server:** Gunicorn

## 📁 Project Structure

```
├── main.py              # Flask app and API routes (/, /ask, /summarize)
├── requirements.txt     # Python dependencies
├── .env.example         # Template for your environment variables
├── .gitignore
├── templates/
│   └── index.html       # Page layout and JavaScript
└── static/
    └── style.css        # Styling
```

## ▶️ Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/mausami10/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   # Windows (PowerShell)
   venv\Scripts\Activate.ps1
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API key**

   Copy `.env.example` to a new file named `.env` and put your OpenAI API key in it:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   Get a key from the [OpenAI dashboard](https://platform.openai.com/api-keys). Never commit `.env` to GitHub.

5. **Run the app**

   ```bash
   python main.py
   ```

6. Open **http://127.0.0.1:5000** in your browser.

## 🔌 API Endpoints

| Method | Route | Form field | Description |
|---|---|---|---|
| GET | `/` | none | Shows the web page |
| POST | `/ask` | `question` | Returns an AI answer as JSON |
| POST | `/summarize` | `email` | Returns a short email summary as JSON |

## ☁️ Deployment

Deployed on [Render](https://render.com/) with these settings:

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `gunicorn main:app`
- **Environment variable:** `OPENAI_API_KEY`

## 👩‍💻 Author

**Mausami Chaudhari**

- GitHub: [@mausami10](https://github.com/mausami10)

---

⭐ If you like this project, consider giving the repository a star!
