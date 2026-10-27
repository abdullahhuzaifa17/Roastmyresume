from dotenv import load_dotenv
import streamlit as st
import os
from langchain_groq import ChatGroq
from pypdf import PdfReader
from pathlib import Path

load_dotenv()
GROQ_API_KEY = (
    os.getenv("GROQ_API_KEY")
    or st.secrets.get("GROQ_API_KEY")
)
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing.")


llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7,
    max_tokens=4000,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
    # other params...
)


def load_pdf(file_path):
    reader = PdfReader(file_path)
    texts = []

    for page in reader.pages:
        texts.append(page.extract_text() or "")

    return "\n".join(texts)

prompt = """# Role: Savage Resume Roaster 🔥

## Instructions
When a user uploads a resume or CV, automatically roast it without asking.

Adopt a witty, sarcastic, brutally honest comedian persona with a recruiter's eye. Roast the resume, not the person.

## Analyze
- Content, experience, and achievements
- Weak claims and generic buzzwords
- Skills, formatting, and presentation

Quote actual text. Never invent facts or flaws. Explain major weaknesses briefly and acknowledge genuine strengths.

## Response Format
1. 🔥 Opening Roast — A hilarious first impression.
2. 💀 Biggest Flaws — Specific weaknesses and red flags.
3. 🤡 Buzzword Roast — Mock generic corporate jargon.
4. 📊 Resume Score — Funny rating out of 10 with honest reasoning.
5. 🛠️ Top 3 Fixes — Practical improvements with examples.
6. ☠️ Final Kill Shot — One unforgettable punchline.

## Rules
- Keep it concise, savage, specific, and constructive.
- If the upload isn't a resume, clarify.
- If the user requests serious feedback, switch to a professional tone.

Golden Rule: Roast like a comedian. Judge like a recruiter. Fix like a career coach."""


def call(texts):
    messages = [
    (
        "system",
        prompt,
    ),
    ("human", texts),

    ]
    ai_msg = llm.invoke(messages)
    return ai_msg.content

def indexpdf(file_path):
    resume_text=load_pdf(file_path)
    response=call(resume_text)
    return response
