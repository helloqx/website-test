from flask import render_template, request, redirect, flash, url_for
from app import app, db
from app.forms import SongSelectForm, SongAddForm
from app.models import Song
from datetime import datetime
import pytz

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Praise the Lord - Slide Generator')

@app.route('/catalogue')
def catalogue():
    all_songs = Song.query.all()
    form = SongSelectForm()
    return render_template('catalogue.html', title='Home', form=form, songs=all_songs)

@app.route('/display', methods=['GET', 'POST'])
def display():
    form = SongSelectForm()
    if not form.validate_on_submit():
        flash('Pick at least one song!')
        return redirect(url_for('catalogue'))
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

@app.route('/add_song', methods=['GET', 'POST'])
def add_song():
    form = SongAddForm()
    if form.validate_on_submit():
        lyrics = form.lyrics.data
        lyrics = lyrics.replace("\r\n", "\n")
        song = Song(title=form.title.data, lyrics=lyrics)
        db.session.add(song)
        db.session.commit()
        flash('Congratulations, you have added a new song!')
        return redirect(url_for('add_song'))
    return render_template('add_song.html', title='Add a song', form=form)

@app.route('/help')
def help():
    return "Coming Soon"


@app.route('/contribute')
def contribute():
    return render_template('contribute.html', title='Contribute')