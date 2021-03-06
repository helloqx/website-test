from flask import render_template, request, redirect, flash, url_for
from app import app, db
from flask_login import current_user, login_required
from app.forms import SongSelectForm, SongAddForm, SongEditForm
from app.models import Song
from datetime import datetime
from pytz import timezone

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Praise the Lord - Slide Generator')

@app.route('/catalogue')
def catalogue():
    all_songs = Song.query.all()
    form = SongSelectForm()
    return render_template('catalogue.html', title='Make Slides', form=form, songs=all_songs)

@app.route('/display', methods=['GET', 'POST'])
def display():
    form = SongSelectForm()
    if not form.validate_on_submit():
        flash('Pick at least one song!', category='danger')
        return redirect(url_for('catalogue'))
    else:
        ids = request.form.get('ids')
        current_user.latest_slides = ids
        db.session.commit()
        selected_songs = ids.split(", ")
        all_songs = get_slides(selected_songs)
        return render_template('display.html', title='Display', slides=all_songs, 
                slide_title='Worship', subtitle=datetime.now(timezone('Asia/Singapore')).date())

@app.route('/add_song', methods=['GET', 'POST'])
@login_required
def add_song():
    form = SongAddForm()
    if form.validate_on_submit():
        lyrics = form.lyrics.data
        lyrics = lyrics.replace("\r\n", "\n")
        song = Song(title=form.title.data, lyrics=lyrics)
        db.session.add(song)
        db.session.commit()
        flash('Congratulations, you have added a new song!', category='success')
        return redirect(url_for('add_song'))
    return render_template('add_song.html', title='Add a Song', form=form)

@app.route('/edit_song', methods=['GET', 'POST'])
@login_required
def edit_song():
    all_songs = Song.query.all()
    form = SongEditForm()
    if form.validate_on_submit() and (current_user.is_user_admin() or form.password.data == app.config['SECRET_ADMIN_PASSWORD']):
        song = Song.query.filter_by(id=form.ids.data).one()
        song.title = form.title.data
        song.lyrics = form.lyrics.data.replace("\r\n", "\n")
        song.link = form.link.data
        db.session.commit()
        flash('Your changes have been saved.', category='info')
        return redirect(url_for('edit_song'))
    if not current_user.is_user_admin():
        flash('Admin password is required to edit songs.', category='warning')
    return render_template('edit_song.html', title='Edit Song', form=form, songs=all_songs)

@app.route('/latest_slides')
@login_required
def latest_slides():
    latest_slides = current_user.get_latest_slides()
    if not latest_slides:
        flash('You have not made any slides yet!', category='warning')
        return redirect(url_for('catalogue'))
    else:
        all_songs = get_slides(latest_slides)
        return render_template('display.html', title='Display', slides=all_songs, 
                slide_title='Worship', subtitle=datetime.now(timezone('Asia/Singapore')).date())

@app.route('/help')
def help():
    return render_template('help.html', title='How to Use')

@app.route('/contribute')
def contribute():
    return render_template('contribute.html', title='Contribute')

def get_slides(song_list):
    all_songs = []
    for song_id in song_list:
        song = Song.query.filter_by(id=song_id).one()
        for verse in song.lyrics.split("\n\n"):
            slide = Song(title=song.title, lyrics=verse)
            all_songs.append(slide)
    return all_songs