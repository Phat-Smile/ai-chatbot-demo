# Deployment Guide

## Current Demo

This project is currently a Python CLI chatbot demo.

Run locally:

```bash
python app.py
```

## Future API Deployment Plan

A future version can expose the chatbot as an API using FastAPI:

```txt
POST /api/chatbot/message
```

Example request:

```json
{
  "message": "How much is the shipping fee?"
}
```

Example response:

```json
{
  "detectedIntent": "shipping_fee",
  "answer": "Shipping fee depends on your delivery location and order value."
}
```

## Future Improvements

- Add FastAPI backend
- Add frontend chatbot UI
- Add OpenAI API generation
- Add conversation history
- Add vector database retrieval
- Add deployment with Docker
