from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
            title="Home")

@app.route('/home')
def home():
    return render_template("home.html",
            title="Bum")
