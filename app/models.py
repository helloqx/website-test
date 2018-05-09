from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    lyrics = db.Column(db.String(512), index=True)
    link = db.Column(db.String(128))

    def __repr__(self):
        return '{}\n{}'.format(self.title, self.lyrics)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    latest_slides = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def is_user_admin(self):
        return self.is_admin

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_latest_slides(self):
        if self.latest_slides:
            return self.latest_slides.split(", ")
        return self.latest_slides

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
