import requests
from config import SENDGRID_API_KEY, FROM_EMAIL, TO_EMAIL


def send_email(report_message):
    url = "https://api.sendgrid.com/v3/mail/send"

    headers = {
        "Authorization": f"Bearer {SENDGRID_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "personalizations": [
            {
                "to": [{"email": TO_EMAIL}],
                "subject": "Weekly GitHub Performance Report"
            }
        ],
        "from": {"email": FROM_EMAIL},
        "content": [
            {
                "type": "text/plain",
                "value": report_message
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data, timeout=5)
    response.raise_for_status()
