from openai import OpenAI
from app.config import OPENAI_API_KEY, OPENAI_MODEL
from pathlib import Path

client = OpenAI(api_key=OPENAI_API_KEY)

PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "system_prompt.md"

def load_system_prompt() -> str:
    try:
        return PROMPT_PATH.read_text(encoding="utf-8")
    except Exception:
        return "Eres Tripto AI. Responde de forma breve, clara y profesional."

def generate_reply(user_message: str, history: list[dict]) -> str:
    if not OPENAI_API_KEY:
        return "Gracias por escribirnos. En este momento el asistente está en configuración. Un asesor de Tripto te responderá pronto."

    messages = [{"role": "system", "content": load_system_prompt()}]
    messages.extend(history)
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=messages,
        temperature=0.4,
        max_tokens=350,
    )

    return response.choices[0].message.content.strip()
