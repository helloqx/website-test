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
        all_songs.append(Song.query.filter_by(id=song_id).one())
    return render_template('display.html', title='Display', songs=all_songs, slide_title='Worship', subtitle=datetime.utcnow())