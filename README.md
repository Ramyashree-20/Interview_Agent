📘 AI Interview Agent (Groq + Flask + HTML)

An AI-powered Interview Agent that conducts technical interviews using Groq’s Llama 3.1 model.
The app asks real interview questions, evaluates your answers, provides expert example responses, and generates final feedback — all through a clean chat-based UI.

🚀 Features

Dynamic AI-generated interview questions

Real-time chat interface (Q&A style)

Expert example answers for every question

Final performance feedback with strengths & improvements

Fully responsive UI (Tailwind CSS)

Secure backend (Flask) to protect API keys

Uses Groq Llama 3.1 model for ultra-fast responses

🛠️ Tech Stack
Frontend

HTML

Tailwind CSS

JavaScript (ES6)

Fetch API

Backend

Python

Flask

Flask-CORS

Requests

python-dotenv

AI / LLM

Groq Cloud API

Llama 3.1 8B Instant Model

Deployment

Render / Railway

Gunicorn (Production server)

📂 Project Structure
project/
│── server.py          # Flask backend (API)
│── index.html         # Frontend UI
│── requirements.txt   # Python dependencies
│── Procfile           # Deployment start command
│── README.md          # Project documentation
│── .env (local only)  # API key (not uploaded)

▶️ Run the Project Locally

1. Install dependencies
   
pip install -r requirements.txt

3. Run the backend
   
python server.py

5. Open the frontend

Open index.html in your browser

(or access http://localhost:5000 if serving via Flask)

4. Deploy

Render will build and host both frontend and backend.

🤖 How It Works

The user enters a job role (e.g., “Python Developer”).

Groq generates the first interview question.

User answers: the system stores conversation history.

AI asks follow-up questions based on your answers.

You can click Show Example to see an expert answer.

After 5 questions, the AI gives detailed final feedback:

Summary

Strengths

Weaknesses

Final recommendation

📌 Why Groq?

Extremely fast inference

Accurate and high-quality responses

Free tier available

Great for real-time applications

👨‍💻 Author

Ramya Shree R

⭐ If you like this project

Give it a star ⭐ on GitHub!
