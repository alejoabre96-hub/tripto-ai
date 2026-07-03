from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import PlainTextResponse
from app.config import META_VERIFY_TOKEN
from app.meta import send_text_message
from app.openai_client import generate_reply
from app.memory import get_history, add_message
from app.faq import find_faq_answer

router = APIRouter()

@router.get("/webhook")
async def verify_webhook(request: Request):
    params = request.query_params
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == META_VERIFY_TOKEN:
        return PlainTextResponse(challenge or "")

    raise HTTPException(status_code=403, detail="Verification failed")

@router.post("/webhook")
async def receive_webhook(request: Request):
    body = await request.json()

    # Meta envía distintos formatos para Messenger e Instagram.
    for entry in body.get("entry", []):
        messaging_events = entry.get("messaging", [])

        for event in messaging_events:
            sender = event.get("sender", {}).get("id")
            message = event.get("message", {})
            text = message.get("text")

            # Ignorar ecos, adjuntos sin texto y eventos no soportados.
            if not sender or not text or message.get("is_echo"):
                continue

            add_message(sender, "user", text)

            faq_answer = find_faq_answer(text)
            if faq_answer:
                reply = faq_answer
            else:
                reply = generate_reply(text, get_history(sender))

            add_message(sender, "assistant", reply)
            send_text_message(sender, reply)

    return {"status": "ok"}
