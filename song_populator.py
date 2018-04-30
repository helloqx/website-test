from app import app, db
from app.models import Song
import os	
import psycopg2

if app.config['IS_HEROKU']:
    connection = psycopg2.connect(app.config['SQLALCHEMY_DATABASE_URI'], sslmode='require')

if app.config['RESET_DATABASE']:
	songs = Song.query.all()
	for s in songs:
		db.session.delete(s)
	db.session.commit()

	file_path = "./app/static/samplesongs.txt"
	title = ""
	lyrics = ""
	with open(file_path, 'r', encoding='utf-8') as in_file:
		for line in in_file:
			if line.startswith("/"):
				if lyrics != "":
					s = Song(title=title, lyrics=lyrics.strip())
					db.session.add(s)
					lyrics = ""
				title = line.strip()[1:]
			else:
				lyrics += line

	s = Song(title=title, lyrics=lyrics)
	db.session.add(s)
	db.session.commit()
