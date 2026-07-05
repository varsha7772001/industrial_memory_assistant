import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("COGNEE_BASE_URL")
API_KEY = os.getenv("COGNEE_API_KEY")

headers = {
    "X-Api-Key": API_KEY,
    "Content-Type": "application/json"
}

payload = {
    "query": "What causes low oil pressure in reciprocating air compressors?"
}

print("BASE_URL =", BASE_URL)

response = requests.post(
    f"{BASE_URL}/api/v1/search",
    headers=headers,
    json=payload
)

print(response.status_code)
print(response.text)