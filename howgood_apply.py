#!/usr/bin/env python3
"""Submit a job application to HowGood via a signed (HMAC-SHA256) POST request."""

import hashlib
import hmac
import json
import requests

SECRET = "hg2026_python_engineer@!"
ENDPOINT = "https://howgood-apply-api.howgood.workers.dev/apply"

payload = {
    "name": "Sivasanthosh Vempali",
    "email": "vepalisantosh@gmail.com",
    "resume": "https://github.com/vempalisantosh-lang/HowGood/raw/refs/heads/main/Sivasanthosh_Vempali_Resume_v2.docx",
    "location": "Tadepalligudem, India",
    "linkedin": "https://www.linkedin.com/in/santhosh-vempali-6bba4a16a/",
    "codeLink": "https://github.com/vempalisantosh-lang/HowGood",
    "yearsPython": 5,
    "yearsDjango": 3,
    "repos": "https://github.com/santhoshvempali",
}


def main():
    # Sign the EXACT bytes we send. compact separators keep body and signature consistent.
    body = json.dumps(payload, separators=(",", ":"))
    signature = hmac.new(SECRET.encode(), body.encode(), hashlib.sha256).hexdigest()

    resp = requests.post(
        ENDPOINT,
        data=body,
        headers={
            "Content-Type": "application/json",
            "X-HMAC-Signature": signature,
        },
        timeout=30,
    )
    print(resp.status_code)
    try:
        print(json.dumps(resp.json(), indent=2))
    except ValueError:
        print(resp.text)


if __name__ == "__main__":
    main()
