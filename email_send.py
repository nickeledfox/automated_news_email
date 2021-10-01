import yagmail
import os
from dotenv import load_dotenv

load_dotenv()
SENDER = os.getenv('EMAIL_SENDER')
PASSWORD = os.getenv('EMAIL_PASSWORD')
RECEIVER = os.getenv('TEST_EMAIL_RECEIVER')


email = yagmail.SMTP(user=SENDER, password=PASSWORD)
email.send(to=RECEIVER,
           subject='Test email header',
           contents='Testing content')