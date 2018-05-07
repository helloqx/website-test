from app import db

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    lyrics = db.Column(db.String(512), index=True)
    link = db.Column(db.String(128))
    def __repr__(self):
        return '{}\n{}'.format(self.title, self.lyrics) 