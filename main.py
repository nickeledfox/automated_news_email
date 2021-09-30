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
        url = f'{self.URL}?'\
        'q={interest}&'\
        'from={self.from_date}&'\
        'to={self.to_date}&'\
        'language={self.language}&'\
        f'apiKey={API_KEY}'

        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + '\n' + article['url'] + '\n\n'

        return email_body

