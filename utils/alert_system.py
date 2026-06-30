import os
from twilio.rest import Client

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

def asthma_alert(aqi):
    if aqi <= 100:
        return "Air quality is safe for most users."

    elif aqi <= 150:
        return "Sensitive groups should reduce outdoor exposure."

    elif aqi <= 200:
        return "⚠ Warning: Unsafe air for asthma patients!"

    else:
        return "🚨 Severe Alert: Asthma patients must stay indoors!"


def send_whatsapp_alert(message_text):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message_text,
        to='whatsapp:+919315061880'
    )
    return message.sid