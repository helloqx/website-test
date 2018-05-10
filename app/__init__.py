from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_admin import Admin

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

login = LoginManager(app)
login.login_view = 'auth.login'
login.login_message_category = "info"

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

admin_manager = Admin(app)
from app.admin import admin_views

from app import routes, models
