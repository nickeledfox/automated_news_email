import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('NEWSAPI_KEY')
URL = 'https://newsapi.org/v2/everything?'


class News:
    def __init__(self, subscriber_interest, yesterday,
                 today, sort_by, language):
        self.subscriber_interest = subscriber_interest
        self.yesterday = yesterday
        self.today = today
        self.sort_by = sort_by
        self.language = language

    def get_news(self):
        url = self._build_url()

        articles = self._get_articles(url)
        email_body = ''
        for article in articles:
            email_body = \
                email_body + article['title'] + '\n' + \
                article['url'] + '\n\n'

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f'{URL}' \
              f'q={self.subscriber_interest}&' \
              f'from={self.yesterday}&' \
              f'to={self.today}&' \
              f'sortBy={self.sort_by}' \
              f'language={self.language}&' \
              f'apiKey={API_KEY}'
        return url


if __name__ == '__main__':
    news = News(subscriber_interest='apple',
                yesterday='2021-09-12',
                today='2020-09-13',
                sort_by='popularity',
                language='en')

