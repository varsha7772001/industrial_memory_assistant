import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("COGNEE_BASE_URL")
API_KEY = os.getenv("COGNEE_API_KEY")

with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Hello Cognee")

with open("sample.txt", "rb") as f:
    response = requests.post(
        f"{BASE_URL}/api/v1/add",
        headers={
            "X-Api-Key": API_KEY
        },
        files={
            "data": f
        },
        data={
            "datasetName": "default_dataset"
        }
    )

print(response.status_code)
print(response.text)