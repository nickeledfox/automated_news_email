import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('NEWSAPI_KEY')


class News:
    URL = 'https://newsapi.org/v2/everything?'

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get_news(self):
        url = f'{self.URL}'\
        f'q={self.interest}&'\
        f'from={self.from_date}&'\
        f'to={self.to_date}&'\
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

news = News(interest='apple',
            from_date='2021-09-12',
            to_date='2020-09-13',
            language='en')

print(news.get_news())

