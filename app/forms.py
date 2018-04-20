from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, SubmitField
from wtforms.validators import DataRequired

class SongSelectForm(FlaskForm):
    song = SelectMultipleField(label='Song')
    submit = SubmitField(label='Display')