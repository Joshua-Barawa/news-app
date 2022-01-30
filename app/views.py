from flask import render_template
from app import app
from app import requests


@app.route("/")
def index():
    news = requests.get_news()
    return render_template('index.html', news=news)

