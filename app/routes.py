from flask import render_template
from app import app
from app.models import Song

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/display')
def display():
    all_songs = Song.query.all()
    return render_template('display.html', title='Display', songs=all_songs)