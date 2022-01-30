from flask import render_template
from app import app
from app import requests


@app.route("/")
def index():
    news = requests.get_news()
    sources = requests.get_news_sources()
    return render_template('index.html', news=news, sources=sources)

