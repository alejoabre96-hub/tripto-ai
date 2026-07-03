from fastapi import FastAPI
from app.webhook import router as webhook_router

app = FastAPI(
    title="Tripto AI",
    description="Asistente IA para Instagram y Facebook Messenger de Tripto",
    version="1.0.0",
)

app.include_router(webhook_router)

@app.get("/")
async def health_check():
    return {
        "status": "ok",
        "service": "Tripto AI",
        "message": "Servidor activo. Usa /webhook para Meta."
    }
