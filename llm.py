from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def analyze_failure(question, context):

    prompt = f"""
You are a Senior Industrial Maintenance Engineer.

Use ONLY the maintenance knowledge provided below.

Do NOT invent information.

Machine Problem:
{question}

Retrieved Knowledge:
{context}

Generate a professional report using markdown.

# 🔍 Root Cause Analysis

List all likely causes.

# 🛠 Recommended Troubleshooting

Provide step-by-step troubleshooting.

# ⚠ Safety Precautions

Mention important safety checks before maintenance.

# ✅ Recommended Maintenance Actions

Provide corrective actions.

# 📊 Confidence

High / Medium / Low

Explain why.
"""
    MODEL = os.getenv("OPENROUTER_MODEL")

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content