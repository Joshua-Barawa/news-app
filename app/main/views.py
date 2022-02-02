from flask import render_template
from app import requests
from . import main


@main.route("/")
def index():
    news = requests.get_news()
    sources = requests.get_news_sources()
    return render_template('index.html', news=news, sources=sources)


@main.route('/news/<string:source>')
def filter_news(source):
    news = requests.get_news_from_source(source)
    sources = requests.get_news_sources()
    return render_template('index.html', news=news, sources=sources)

