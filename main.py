import yagmail
import pandas as pd
import datetime as dt
import time

from news import News

import os
from dotenv import load_dotenv

load_dotenv()
SENDER = os.getenv('EMAIL_SENDER')
PASSWORD = os.getenv('EMAIL_PASSWORD')

# Table data example in subscriber_dataEx.xlsx file
subscriber_data = 'emaildata.xlsx'

while True:
    # Set time for everyday execution
    if dt.datetime.now().hour == 7 and dt.datetime.now().minute == 00:
        df = pd.read_excel(subscriber_data)

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
                       subject=f"Your {row['interest'].capitalize()} daily news is here!",
                       contents=f"{row['first name']},\n\n "
                                f"Check what's on about {row['interest'].capitalize()}: \n\n"
                                f"{news.get_news()}")

        # Used to break the loop since the 60 s later = 7:01
        # So news will be sent again the next day
        time.sleep(60)

