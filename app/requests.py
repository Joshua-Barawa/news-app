from app.configuration.config import API_KEY
import requests, json
from app.models import news_article

MOVIE_API_KEY = API_KEY
News_Article = news_article.Article


def get_news():
    request = requests.get('https://newsapi.org/v2/everything?q=bitcoin&apiKey=951ac88dc85d4aa3a2fc00d764d0f73c'
                           .format(MOVIE_API_KEY))
    response = json.loads(request.content)
    news = []
    for new in response['articles']:
        new = News_Article(new['source'], new['author'], new['title'], new['description'], new['urlToImage'], new['publishedAt'])
        news.append(new)

    print(news)
    return news
