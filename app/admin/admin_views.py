from app import admin_manager, db
from app.models import User, Song
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')

class UserView(ModelView):
    column_list = (User.username, User.is_admin, User.latest_slides)

    def __init__(self, session, **kwargs):
        super(UserView, self).__init__(User, session, **kwargs)

    def get_edit_form(self):
        form_class = super(UserView, self).get_edit_form()
        del form_class.password_hash
        return form_class

    def is_accessible(self):
        return (current_user.is_authenticated and current_user.is_user_admin())

class SongView(ModelView):

    def __init__(self, session, **kwargs):
        super(SongView, self).__init__(Song, session, **kwargs)

    def is_accessible(self):
        return (current_user.is_authenticated and current_user.is_user_admin())

admin_manager.add_view(UserView(db.session))
admin_manager.add_view(SongView(db.session))
admin_manager.add_view(MyView(name='Back'))
