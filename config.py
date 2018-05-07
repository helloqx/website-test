import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET_KEY'
    SECRET_ADMIN_PASSWORD = os.environ.get('SECRET_ADMIN_PASSWORD') or 'SECRET_ADMIN_PASSWORD'
    IS_HEROKU = os.environ.get('HEROKU') or False
    RESET_DATABASE = os.environ.get('RESET_DATABASE') or False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    	'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False