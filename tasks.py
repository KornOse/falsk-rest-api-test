import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_simple_message(to, subject, body):
  domain = os.getenv("MAILGUN_DOMAIN")
  api_key = os.getenv("MAILGUN_API_KEY")

  return requests.post(
    f"https://api.mailgun.net/v3/{domain}/messages",
    auth=("api", api_key),
    data={
        "from": f"Mailgun Sandbox <postmaster@{domain}>",
        "to": [to],
        "subject": subject,
        "text": body
      }
    )

def send_user_registration_email(email, username):
  return send_simple_message(
    email,
    "Successfully signed up",
    f"Hi {username}, you have successfully signed up to the Stores REST API."
  )