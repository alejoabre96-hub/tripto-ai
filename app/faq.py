import json
from pathlib import Path

FAQ_PATH = Path(__file__).resolve().parent.parent / "data" / "faq.json"

def load_faq():
    try:
        return json.loads(FAQ_PATH.read_text(encoding="utf-8"))
    except Exception:
        return []

FAQ = load_faq()

def find_faq_answer(message: str):
    text = message.lower()
    for item in FAQ:
        keywords = item.get("keywords", [])
        if any(keyword.lower() in text for keyword in keywords):
            return item.get("answer")
    return None
