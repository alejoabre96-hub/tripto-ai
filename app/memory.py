from collections import defaultdict
from typing import Dict, List

# Memoria simple en RAM para MVP.
# En producción conviene reemplazar por Redis, Postgres o Supabase.
_conversations: Dict[str, List[dict]] = defaultdict(list)

MAX_HISTORY = 12

def get_history(user_id: str) -> List[dict]:
    return _conversations[user_id][-MAX_HISTORY:]

def add_message(user_id: str, role: str, content: str) -> None:
    _conversations[user_id].append({"role": role, "content": content})
    _conversations[user_id] = _conversations[user_id][-MAX_HISTORY:]
