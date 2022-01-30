from app.configuration.config import API_KEY
import requests, json
from app.models import news_article, news_source

MOVIE_API_KEY = API_KEY
News_Article = news_article.Article
News_Source = news_source.Source


def get_news_sources():
    request = requests.get('https://newsapi.org/v2/top-headlines/sources?apiKey={}'
                           .format(MOVIE_API_KEY))
    response = json.loads(request.content)
    news_sources = []
    for source in response['sources']:
        source = News_Source(source['id'], source['name'])
        news_sources.append(source)

    return news_sources


def get_news():
    request = requests.get('https://newsapi.org/v2/everything?q=technology&apiKey={}'
                           .format(MOVIE_API_KEY))
    response = json.loads(request.content)
    news = []
    for new in response['articles']:
        new = News_Article(new['source'], new['author'], new['title'], new['description'], new['urlToImage'], new['url'], new['publishedAt'])
        news.append(new)

    return news
