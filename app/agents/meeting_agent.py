from datetime import date
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.database.models import Meeting
from app.agents.weather_agent import get_weather

def create_meeting(title: str, meeting_date: date):
    db: Session = SessionLocal()

    meeting = Meeting(
        title=title,
        date=meeting_date
    )

    db.add(meeting)
    db.commit()
    db.close()

    return "Meeting created successfully "

def schedule_meeting_if_weather_good():
    weather_info = get_weather("Chennai", "today")

    if "rain" in weather_info.lower() or "storm" in weather_info.lower():
        return "Weather is bad . Meeting not scheduled."

    db: Session = SessionLocal()
    today = date.today()

    # check if meeting already exists
    existing_meeting = db.query(Meeting).filter(Meeting.date == today).first()

    if existing_meeting:
        db.close()
        return "Meeting already scheduled for today "

    meeting = Meeting(
        title="Team Sync Meeting",
        date=today
    )

    db.add(meeting)
    db.commit()
    db.close()

    return "Meeting created successfully "