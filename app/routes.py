from flask import render_template, request
from app import app
from app.forms import SongSelectForm
from app.models import Song
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    form = SongSelectForm()
    form.song.choices = [(s.id, s.title) for s in Song.query.order_by('title')]
    return render_template('index.html', title='Home', form=form)

@app.route('/display', methods=['GET', 'POST'])
def display():
    all_songs = []
    selected_songs = request.form.getlist('song')
    for song_id in selected_songs:
        song = Song.query.filter_by(id=song_id).one()
        for verse in song.lyrics.split("\n\n"):
        	slide = Song(title=song.title, lyrics=verse)
        	all_songs.append(slide)
    return render_template('display.html', title='Display', songs=all_songs, slide_title='Worship', subtitle=datetime.utcnow())