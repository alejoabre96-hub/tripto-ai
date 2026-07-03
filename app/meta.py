import requests
from app.config import META_PAGE_ACCESS_TOKEN

GRAPH_URL = "https://graph.facebook.com/v21.0/me/messages"

def send_text_message(recipient_id: str, text: str) -> dict:
    if not META_PAGE_ACCESS_TOKEN:
        return {"error": "META_PAGE_ACCESS_TOKEN is missing"}

    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text[:1900]},
        "messaging_type": "RESPONSE",
    }

    response = requests.post(
        GRAPH_URL,
        params={"access_token": META_PAGE_ACCESS_TOKEN},
        json=payload,
        timeout=15,
    )

    try:
        return response.json()
    except Exception:
        return {"status_code": response.status_code, "text": response.text}
