# Agentic AI Backend

This project implements an Agentic AI backend using FastAPI.  
A central reasoning agent routes user queries to specialized agents such as weather, document understanding, meeting scheduling, and database querying.

## Features
- Weather Intelligence Agent
- Document Upload & Question Answering
- Weather-based Meeting Scheduling
- Natural Language to Database Queries
- Central Reasoning Agent for routing

## Tech Stack
- Python
- FastAPI
- SQLite
- SQLAlchemy
- OpenWeather API

## How to Run the Project

### 1. Create and activate virtual environment
```bash
python -m venv venv

Windows:
```bash
.\venv\Scripts\activate

### 2. Install dependencies
```bash
pip install -r requirements.txt

### 3. Run the FastAPI server
```bash
python -m uvicorn app.main:app --reload

### Open Swagger UI in browser:
http://127.0.0.1:8000/docs


## API Usage Examples

### Upload a Document
POST `/upload`  
Upload a PDF file (e.g., resume).

### Ask a Question
POST `/ask`

Example request body:
```json
{
  "question": "What is the weather in Chennai today?"
}
