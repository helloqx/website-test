from flask import render_template
from app import app
from app.forms import SongSelectForm
from app.models import Song

@app.route('/')
@app.route('/index')
def index():
    form = SongSelectForm()
    form.song.choices = [(s, s.title) for s in Song.query.order_by('title')]
    return render_template('index.html', title='Home', form=form)

@app.route('/display', methods=['GET', 'POST'])
def display():
    all_songs = Song.query.all()
    return render_template('display.html', title='Display', songs=all_songs)