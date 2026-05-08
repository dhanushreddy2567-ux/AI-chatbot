# 🎓 UniHelp Bot: AI-Powered Student Helpdesk Chatbot

> An AI-powered full-stack chatbot designed to provide automated university support using Google Gemini LLMs, Flask REST APIs, and a modern responsive frontend.

---

# 📑 Table of Contents

1. [Project Overview](#-project-overview)
2. [Problem Statement](#-problem-statement)
3. [Solution](#-solution)
4. [System Architecture](#-system-architecture)
5. [Modules](#-modules)
6. [Technology Stack](#-technology-stack)
7. [Features](#-features)
8. [Project Structure](#-project-structure)
9. [Installation & Setup](#-installation--setup)
10. [API Configuration](#-api-configuration)
11. [Running the Application](#-running-the-application)
12. [Error Handling & Reliability](#-error-handling--reliability)
13. [Future Enhancements](#-future-enhancements)
14. [Results](#-results)
15. [GitHub Hosting Guide](#-github-hosting-guide)
16. [Author](#-author)

---

# 📖 Project Overview

UniHelp Bot is a modern AI-powered student support chatbot developed to automate university administrative assistance. The application uses Google's Gemini Large Language Models (LLMs) to provide real-time responses to student queries regarding admissions, exams, schedules, fee payments, and campus-related information.

The project follows a **decoupled full-stack architecture**, where the frontend and backend are independently managed for better scalability, maintainability, and security.

---

# ❗ Problem Statement

Traditional university helpdesks often experience:

- Long waiting times during peak hours
- Limited availability outside office hours
- Repetitive handling of common student queries
- Static FAQ pages that lack conversational interaction
- Delayed responses for urgent administrative questions

These issues reduce efficiency and negatively impact the student experience.

---

# ✅ Solution

UniHelp Bot solves these issues by providing:

- 24/7 automated support
- AI-powered conversational responses
- Instant query handling
- Modern and responsive user interface
- Reliable backend communication using REST APIs
- Secure API key management
- Intelligent fallback handling during API failures

The chatbot integrates Google Gemini AI models through a Flask backend server and offers a smooth user experience using asynchronous frontend communication.

---

# 🏗️ System Architecture

The project follows a **Decoupled Full-Stack Architecture**.

```text
+-------------------+
|   Frontend UI     |
| HTML + Tailwind   |
| JavaScript Fetch  |
+---------+---------+
          |
          | HTTP Requests (JSON)
          v
+-------------------+
| Flask REST API    |
| Python Backend    |
| Flask-CORS        |
+---------+---------+
          |
          | API Calls
          v
+-------------------+
| Google Gemini AI  |
| Generative Model  |
+-------------------+
```

---

# ⚙️ Modules

## 1. Frontend Module (UI)

Responsible for handling the user interface and interactions.

### Functionalities
- Responsive chatbot interface
- Real-time typing animations
- Auto-scroll chat functionality
- Async communication using Fetch API
- Smooth user experience with Tailwind CSS

### Technologies Used
- HTML5
- Tailwind CSS
- JavaScript (Async/Await)

---

## 2. Backend Module (Flask API)

Acts as the middleware between frontend and Gemini AI services.

### Functionalities
- Handles API routing
- Receives user queries
- Sends requests to Gemini API
- Returns AI-generated responses
- Protects sensitive API keys
- Enables secure CORS communication

### Technologies Used
- Python
- Flask
- Flask-CORS

---

## 3. Artificial Intelligence Module

Handles communication with Google Gemini LLMs.

### Functionalities
- Processes user prompts
- Generates contextual AI responses
- Uses prompt engineering for university-focused conversations
- Handles rate limits and API errors gracefully

### AI Model Used
- `gemini-flash-latest`

---

# 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Frontend | HTML5, Tailwind CSS, JavaScript |
| Backend | Python, Flask, Flask-CORS |
| AI Integration | Google Gemini API |
| Communication | REST API, JSON |
| Development Tools | VS Code, macOS Terminal |

---

# ✨ Features

- 🤖 AI-powered chatbot support
- 🌐 Decoupled frontend-backend architecture
- ⚡ Fast asynchronous communication
- 📱 Responsive UI design
- 🔒 Secure API key handling
- 🧠 Gemini AI integration
- 🚨 API error handling and fallback responses
- 🔄 Real-time chat updates
- 📡 RESTful API communication
- 🎯 University-specific prompt engineering

---

# 📁 Project Structure

```text
unihelp-bot/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── style.css
│
├── README.md
│
└── assets/
    └── screenshots/
```

---

# 🚀 Installation & Setup

## Prerequisites

Before starting, ensure the following are installed:

- Python 3.x
- VS Code (Recommended)
- Google Gemini API Key
- Modern web browser

---

# 🔧 Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/unihelp-bot.git
cd unihelp-bot
```

---

# 📦 Step 2: Install Backend Dependencies

Install the required Python libraries.

```bash
pip install flask flask-cors google-generativeai
```

Or using requirements.txt:

```bash
pip install -r requirements.txt
```

---

# 🔑 Step 3: Configure API Key

Open `app.py` and replace the placeholder API key with your own Gemini API key.

```python
genai.configure(api_key="YOUR_GOOGLE_API_KEY_HERE")
```

---

# ▶️ Step 4: Run the Backend Server

Start the Flask backend server.

```bash
python3 app.py
```

Expected terminal output:

```text
🚀 Backend is running on http://127.0.0.1:5001
```

> Note: Port `5001` is used to avoid conflicts with macOS system services such as AirPlay Receiver.

---

# 🌐 Step 5: Launch the Frontend

Open the `index.html` file in your browser.

You can also use the **Live Server Extension** in VS Code.

---

# 🔌 API Configuration

Example Flask API Route:

```python
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    response = model.generate_content(user_message)

    return jsonify({
        "reply": response.text
    })
```

---

# 🧠 Prompt Engineering

The chatbot uses custom system instructions to maintain a professional university helpdesk behavior.

Example:

```python
system_prompt = """
You are UniHelp Bot, a professional university support assistant.
Only answer university-related questions politely and clearly.
"""
```

---

# ⚠️ Error Handling & Reliability

The system includes robust error-handling mechanisms to improve reliability.

## Implemented Solutions

### API Rate Limit Handling
Handles:
- HTTP 429 Errors
- Temporary API overloads

### Fail-Soft Strategy
Provides user-friendly fallback messages instead of crashing.

Example:

```python
try:
    response = model.generate_content(prompt)
except Exception:
    return jsonify({
        "reply": "⚠️ The AI service is currently busy. Please try again shortly."
    })
```

### Network Reliability
- Backend timeout handling
- Asynchronous frontend requests
- Safe JSON parsing

---

# 📊 Results

The final system successfully demonstrates:

- Seamless frontend-backend communication
- Real-time AI-generated responses
- Secure cloud AI integration
- Stable API interaction
- Responsive modern UI
- Reliable error management

The chatbot effectively reduces dependency on manual university support systems.

---

# 🔮 Future Enhancements

Potential future improvements include:

- 🎤 Voice-based chatbot interaction
- 🌍 Multi-language support
- 🗄️ Database integration for student records
- 🔐 Student authentication system
- 📅 Appointment booking integration
- 📱 Mobile application development
- ☁️ Cloud deployment using AWS or Render
- 📊 Chat analytics dashboard
- 🧾 Conversation history storage

---

# 🐙 GitHub Hosting Guide

## Step 1: Initialize Git

```bash
git init
```

---

## Step 2: Add Files

```bash
git add .
```

---

## Step 3: Commit Changes

```bash
git commit -m "Initial Commit"
```

---

## Step 4: Connect GitHub Repository

```bash
git remote add origin https://github.com/yourusername/unihelp-bot.git
```

---

## Step 5: Push to GitHub

```bash
git branch -M main
git push -u origin main
```

---

# 👨‍💻 Author

## Dhanush Reddy

### Skills Demonstrated
- Full-Stack Web Development
- REST API Development
- Flask Backend Engineering
- AI/LLM Integration
- Prompt Engineering
- Error Handling & Reliability
- Responsive Frontend Design
- Asynchronous JavaScript
- Tailwind CSS

---

# 📜 License

This project is developed for educational and learning purposes.

---

# ⭐ Acknowledgements

- Google Gemini AI
- Flask Documentation
- Tailwind CSS
- Open Source Developer Community

---
