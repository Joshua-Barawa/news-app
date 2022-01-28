from flask import render_template
from app import app


@app.route("/")
def index():
    title = "Welcome - Home"
    return render_template('base.html', title=title)
