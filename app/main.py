from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from app.reasoning_agent import route_question
from app import state
import shutil
import os
from app.database import db


app = FastAPI(title="Agentic AI Backend")

# store last uploaded document path


class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask(req: QuestionRequest):
    response = route_question(req.question)
    return {"response": response}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    state.LAST_UPLOADED_DOC = file_path   # 👈 shared update

    return {
        "message": "File uploaded successfully",
        "path": file_path
    }
