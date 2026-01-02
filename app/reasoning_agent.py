from app.agents.weather_agent import get_weather
from app.agents.meeting_agent import schedule_meeting_if_weather_good
from app.agents.db_query_agent import get_meetings_today
from app import state

def route_question(question: str):
    q = question.lower()

    if "meeting" in q and "schedule" in q:
        return schedule_meeting_if_weather_good()

    # meeting queries (read-only)
    if ("meeting" in q or "meetings" in q) and "today" in q:
        return get_meetings_today()

    # improved weather detection
    if "weather" in q or "temperature" in q or "climate" in q:
        return get_weather("Chennai", "today")

    # document agent
    if state.LAST_UPLOADED_DOC:
        from app.agents.document_agent import read_document, answer_from_document
        doc_text = read_document(state.LAST_UPLOADED_DOC)
        return answer_from_document(question, doc_text)


    return "I don't know which agent to use yet "
