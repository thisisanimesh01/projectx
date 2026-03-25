import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"


def call_ai(prompt):
    try:
        response = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:8000",
                "X-Title": "Legal AI Assistant"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [
                {"role": "user", "content": prompt[:2000]}
                ]
            }
        )

        data = response.json()
        print("DEBUG:", data)

        if "choices" in data:
            return data["choices"][0]["message"]["content"]

        elif "error" in data:
            return f"⚠️ API Error: {data['error']['message']}"

        return "⚠️ No response received."

    except Exception as e:
        return f"⚠️ Exception: {str(e)}"


def get_summary(text):
    prompt = f"""
You are a legal expert.

Summarize this legal document clearly in:

1. Overview
2. Key Terms
3. Obligations
4. Risks

Document:
{text[:2000]}
"""
    return call_ai(prompt)


def ask_question(text, question):
    prompt = f"""
You are a professional legal assistant.

Document:
{text[:2000]}

Question:
{question}

Give a precise and structured answer.
"""
    return call_ai(prompt)