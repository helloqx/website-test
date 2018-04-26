from flask_wtf import FlaskForm
from wtforms import HiddenField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class SongSelectForm(FlaskForm):
    ids = HiddenField(label='IDs', render_kw={'readonly': True})
    selected = TextAreaField(label='Selected Songs', render_kw={'readonly': True}, validators=[DataRequired()])
    submit = SubmitField(label='Display')