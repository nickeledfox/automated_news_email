import yagmail
import pandas as pd
from news import News

df = pd.read('emaildata.xlsx')

for index, row in df.iterrows():
    news = News(subscriber_interest=row['interest'],
                from_date='2021-09-28', to_date='2021-09-29',
                sort_by='popularity', language='en')
    email = yagmail.SMTP(user=SENDER, password=PASSWORD)
    email.send(to=row['email'],
               subject='f{row[interest]} daily news',
               contents='f{row[name]}, n\
                Check what\'s on about {row[subscriber_interest]}.' \
                                                                ' {news.get()}')

print(df)
