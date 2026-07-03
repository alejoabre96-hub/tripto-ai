# Tripto AI

Backend para conectar Facebook Messenger e Instagram Messaging con OpenAI.

## Endpoints principales

- `GET /` prueba de salud.
- `GET /webhook` verificación de webhook de Meta.
- `POST /webhook` recepción de mensajes de Meta.

## Variables de entorno

Copia `.env.example` y configura:

```bash
OPENAI_API_KEY=
META_VERIFY_TOKEN=tripto2026
META_PAGE_ACCESS_TOKEN=
OPENAI_MODEL=gpt-4o-mini
```

## Render

Build Command:

```bash
pip install -r requirements.txt
```

Start Command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

## Webhook en Meta

Callback URL:

```text
https://TU-SERVICIO.onrender.com/webhook
```

Verify Token:

```text
tripto2026
```

## Nota

Esta versión es una base funcional. Para producción, conviene agregar base de datos, manejo avanzado de errores, dashboard, límites de uso y revisión de permisos de Meta.
