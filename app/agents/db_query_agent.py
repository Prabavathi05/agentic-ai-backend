from datetime import date
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.database.models import Meeting

def get_meetings_today():
    db: Session = SessionLocal()
    today = date.today()
    meetings = db.query(Meeting).filter(Meeting.date == today).all()
    db.close()

    if not meetings:
        return "No meetings scheduled for today "

    return f"{len(meetings)} meeting(s) scheduled for today "
