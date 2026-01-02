from PyPDF2 import PdfReader

def read_document(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def answer_from_document(question: str, document_text: str) -> str:
    q = question.lower()

    if q in document_text.lower():
        return "Answer found in document 📄"
    
    return "Answer not found in document. Need web search 🌐"
