import yagmail
import pandas as pd
import datetime as dt

from news import News

import os
from dotenv import load_dotenv

load_dotenv()
SENDER = os.getenv('EMAIL_SENDER')
PASSWORD = os.getenv('EMAIL_PASSWORD')

df = pd.read_excel('emaildata.xlsx')

for index, row in df.iterrows():
    today = dt.datetime.now()
    yesterday = today - dt.timedelta(days=1)
    news = News(subscriber_interest=row['interest'],
                yesterday=yesterday.strftime('%Y-%m-%d'),
                today=today.strftime('%Y-%m-%d'),
                sort_by=row['sort by'],
                language=row['language'])
    email = yagmail.SMTP(user=SENDER, password=PASSWORD)
    email.send(to=row['email'],
               subject=f"{row['interest'].capitalize()} daily news",
               contents=f"{row['name']},\n "
                        f"Check what's on about {row['interest'].capitalize()}! \n\n"
                        f"{news.get_news()}")

