# AudienceIQ - AI Powered Audience Validation Platform

**Developed by:** Khushi Wadhwa

---

# Overview

InsightLens-AI is an AI-powered audience validation platform designed to help speakers, trainers, educators, and mentors evaluate audience understanding during or after a learning session.

The platform automatically generates topic-specific assessment questions, evaluates participant responses using a locally running Large Language Model (LLM), and provides detailed analytics and learning insights.

Unlike cloud-based solutions, AudienceIQ runs completely offline using **Ollama**, ensuring privacy, lower latency, and zero API costs.

---

# Features

## AI Question Generation

* Generate assessment questions instantly from any topic.
* Supports Easy, Medium, and Hard difficulty levels.
* Uses Ollama with Qwen2.5 3B model.

---

## AI-Based Answer Evaluation

Participant responses are evaluated automatically using AI based on:

* Conceptual understanding
* Technical accuracy
* Completeness
* Relevance
* Clarity

Each answer receives:

* Score (0–20)
* Feedback
* Strengths
* Areas for improvement

---

## Session Management

Speakers can:

* Create new sessions
* Generate AI questions
* Review generated questions
* Edit questions before publishing
* Add custom questions
* Delete unwanted questions

Every session receives a unique Session ID.

---

## Audience Portal

Participants can:

* Join using Session ID
* Submit answers
* Receive instant AI evaluation
* View final score
* Receive personalized feedback

---

## Analytics Dashboard

Provides:

* Total Participants
* Total Responses
* Average Score
* Highest Score
* Performance Distribution
* Audience Understanding

---

## Learning Insights

Automatically identifies:

* Strong concepts
* Moderate concepts
* Weak concepts

Helping speakers understand which topics require additional explanation.

---

## Leaderboard

Displays:

* Top performers
* Participant rankings
* Final scores

---

## AI Insights

Generates an AI-powered teaching report including:

* Overall audience understanding
* Strong topics
* Weak topics
* Teaching suggestions
* Revision recommendations
* Next learning focus

---

# Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Database

* SQLite

### AI Model

* Ollama
* Qwen2.5:3B

### Libraries

* streamlit
* ollama
* sqlite3
* json

---

# Project Structure

```text
AudienceIQ
│
├── Home.py
│
├── Pages
│   ├── 1_Create_Session.py
│   ├── 2_Join_Session.py
│   ├── 3_Analytics.py
│   ├── 4_Learning_Insights.py
│   ├── 5_My_Sessions.py
│   ├── 6_Leaderboard.py
│   └── 8_AI_Insights.py
│
├── ai
│   ├── question_generator.py
│   └── ollama_evaluator.py
│
├── database
│
├── utils
│
└── data
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd AudienceIQ
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download and install Ollama from:

https://ollama.com/download

---

# Download the AI Model

```bash
ollama pull qwen2.5:3b
```

Verify installation

```bash
ollama list
```

You should see

```text
qwen2.5:3b
```

---

# Run Ollama

Start the Ollama service

```bash
ollama serve
```

Leave this terminal running.

---

# Run the Project

Open another terminal.

Activate the virtual environment.

Run

```bash
streamlit run Home.py
```

The application will open automatically in your browser.

---

# Workflow

1. Create a session.
2. Enter the session topic.
3. Select the difficulty level.
4. Generate AI questions.
5. Review and edit questions.
6. Publish the session.
7. Share the Session ID with participants.
8. Participants join the session.
9. Participants answer the questions.
10. AI evaluates every response.
11. View Analytics, Learning Insights, Leaderboard, and AI Insights.

---

# Requirements

* Python 3.10 or later
* Ollama
* Qwen2.5:3B model
* Streamlit
* SQLite

---

# Future Improvements

* PDF/PPT based question generation
* Speech-based evaluation
* Multi-session comparison
* Export reports to PDF and Excel
* Authentication for speakers and participants

---

# Author

**Khushi Wadhwa**

Computer Science Engineering Student

Passionate about Artificial Intelligence, Machine Learning, Open Source, and Full Stack Development.

---

# License

This project is intended for educational and research purposes.
