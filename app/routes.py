from flask import render_template, request, redirect
from app import app
from app.forms import SongSelectForm
from app.models import Song
from datetime import datetime
import pytz

@app.route('/')
@app.route('/index')
def index():
    all_songs = Song.query.all()
    form = SongSelectForm()
    return render_template('index.html', title='Home', form=form, songs=all_songs)

@app.route('/display', methods=['GET', 'POST'])
def display():
    form = SongSelectForm()
    if not form.validate_on_submit():
        return redirect('/index')
    else:
        all_songs = []
        selected_songs = request.form.get('ids').split(", ")
        for song_id in selected_songs:
            song = Song.query.filter_by(id=song_id).one()
            for verse in song.lyrics.split("\n\n"):
            	slide = Song(title=song.title, lyrics=verse)
            	all_songs.append(slide)
        return render_template('display.html', title='Display', slides=all_songs, 
                slide_title='Worship', subtitle=datetime.now(pytz.timezone('Asia/Singapore')).date())