# modules/emailer.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_summary_email(sender, recipient, password, summary_text):
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = "🎙️ Podcast Summary"
    msg.attach(MIMEText(summary_text, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
            return "✅ Summary emailed successfully!"
    except Exception as e:
        return f"❌ Email failed: {e}"
