import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('NEWSAPI_KEY')
URL = 'https://newsapi.org/v2/everything?'


class News:
    def __init__(self, subscriber_interest, from_date,
                 to_date, sort_by, language):
        self.subscriber_interest = subscriber_interest
        self.from_date = from_date
        self.to_date = to_date
        self.sort_by = sort_by
        self.language = language

    def get_news(self):
        url = f'{URL}'\
        f'q={self.subscriber_interest}&'\
        f'from={self.from_date}&'\
        f'to={self.to_date}&'\
        f'sortBy={self.sort_by}'\
        f'language={self.language}&'\
        f'apiKey={API_KEY}'

        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body = \
                email_body + article['title'] + '\n' + \
                article['url'] + '\n\n'

        return email_body

news = News(subscriber_interest='apple',
            from_date='2021-09-12',
            to_date='2020-09-13',
            sort_by='popularity',
            language='en')

