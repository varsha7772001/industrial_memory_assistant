import os
import tempfile
from datetime import datetime

import requests
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

BASE_URL = os.getenv("COGNEE_BASE_URL") or st.secrets["COGNEE_BASE_URL"]
API_KEY = os.getenv("COGNEE_API_KEY") or st.secrets["COGNEE_API_KEY"]

headers = {
    "X-Api-Key": API_KEY,
    "Content-Type": "application/json"
}


def search_memory(question):
    payload = {
        "query": question
    }

    response = requests.post(
        f"{BASE_URL}/api/v1/search",
        headers=headers,
        json=payload,
        timeout=60
    )

    response.raise_for_status()

    data = response.json()

    if not data:
        return ""

    results = data[0]["search_result"]

    return "\n\n".join(results)


def remember_incident(question, context, answer):

    report = f"""
===============================
Industrial Maintenance Incident
===============================

Timestamp:
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

--------------------------------

Machine Problem

{question}

--------------------------------

Retrieved Maintenance Knowledge

{context}

--------------------------------

AI Root Cause Analysis

{answer}

--------------------------------

Status

Validated by Engineer

Source

Cognee Factory Brain
"""

    temp_file = None

    try:

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".txt",
            delete=False,
            encoding="utf-8"
        ) as f:

            f.write(report)
            temp_file = f.name

        with open(temp_file, "rb") as fp:

            files = {
                "data": (
                    "incident_report.txt",
                    fp,
                    "text/plain"
                )
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
                data=data,
                timeout=60
            )

        print("=" * 50)
        print("COGNEE ADD RESPONSE")
        print("=" * 50)
        print(response.status_code)
        print(response.text)
        print("=" * 50)

        response.raise_for_status()

        return response.status_code, response.text

    except Exception as e:

        print("Remember Incident Error")
        print(e)

        raise

    finally:

        if temp_file and os.path.exists(temp_file):
            os.remove(temp_file)