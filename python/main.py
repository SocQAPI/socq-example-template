import json
import os

import requests


api_key = os.environ.get("SOCQ_API_KEY")
base_url = (os.environ.get("SOCQ_BASE_URL") or "https://api.socq.ai").rstrip("/")
endpoint_path = os.environ.get("SOCQ_ENDPOINT_PATH") or "/v1/platform/resource"

if not api_key or api_key == "your-api-key":
    raise ValueError("Set SOCQ_API_KEY before running this example.")

with open("payload.example.json", "r", encoding="utf-8") as payload_file:
    payload = json.load(payload_file)

response = requests.post(
    "{}{}".format(base_url, endpoint_path),
    headers={
        "Authorization": "Bearer {}".format(api_key),
        "Content-Type": "application/json",
    },
    json=payload,
    timeout=30,
)

try:
    body = response.json()
except ValueError:
    body = None

if not response.ok:
    message = "HTTP {}".format(response.status_code)
    if isinstance(body, dict) and isinstance(body.get("error"), dict):
        message = body["error"].get("message") or message
    raise RuntimeError("SocQ request failed: {}".format(message))

print(json.dumps(body, indent=2))
