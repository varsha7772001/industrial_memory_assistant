import os
import requests
from dotenv import load_dotenv
import tempfile
import os

load_dotenv()

BASE_URL = os.getenv("COGNEE_BASE_URL")
API_KEY = os.getenv("COGNEE_API_KEY")

headers = {
    "X-Api-Key": API_KEY,
    "Content-Type": "application/json"
}

def remember_incident(question, context, answer):

    report = f"""
Machine Problem
================

{question}

Retrieved Knowledge
===================

{context}

AI Troubleshooting Report
=========================

{answer}
"""

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".txt",
        delete=False,
        encoding="utf-8"
    ) as f:

        f.write(report)
        temp_file = f.name

    try:

        files = {
            "data": open(temp_file, "rb")
        }

        data = {
            "datasetName": "default_dataset"
        }

        response = requests.post(
            f"{BASE_URL}/api/v1/add",
            headers={
                "X-Api-Key": API_KEY
            },
            files=files,
            data=data
        )

        response.raise_for_status()

        files["data"].close()

        cognify = requests.post(
            f"{BASE_URL}/api/v1/cognify",
            headers=headers,
            json={
                "datasets": ["default_dataset"]
            }
        )

        cognify.raise_for_status()

        return True

    finally:

        if os.path.exists(temp_file):
            os.remove(temp_file)
            
def search_memory(question):

    payload = {
        "query": question
    }

    response = requests.post(
        f"{BASE_URL}/api/v1/search",
        headers=headers,
        json=payload
    )

    response.raise_for_status()

    data = response.json()

    if len(data) == 0:
        return ""

    results = data[0]["search_result"]

    return "\n\n".join(results)