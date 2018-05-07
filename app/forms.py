from flask_wtf import FlaskForm
from wtforms import HiddenField, TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired

class SongSelectForm(FlaskForm):
    selected_placeholder = "Click '+' to add a song!"
    ids = HiddenField(label='IDs', render_kw={'readonly': True})
    selected = TextAreaField(label='Selected Songs', render_kw={'readonly': True, 'placeholder': selected_placeholder}, validators=[DataRequired()])
    submit = SubmitField(label='Display')

class SongAddForm(FlaskForm):
    title_placeholder = "Title"
    lyrics_placeholder = "Leave a blank line between verses:\nVerse 1 Verse 1\nVerse 1 Verse 1\n\nVerse 2 Verse 2\nVerse 2 Verse 2"
    title = StringField(label='Title', render_kw={'placeholder': title_placeholder}, validators=[DataRequired()])
    lyrics = TextAreaField(label='Lyrics', render_kw={'rows': 20, 'placeholder': lyrics_placeholder, 'white-space': "pre-wrap"}, validators=[DataRequired()])
    submit = SubmitField(label='Add')

class SongEditForm(FlaskForm):
    ids = HiddenField(label='ID', render_kw={'readonly': True})
    title = StringField(label='Title', validators=[DataRequired()])
    lyrics = TextAreaField(label='Lyrics', render_kw={'rows': 20}, validators=[DataRequired()])
    link = StringField(label='Link')
    password = StringField(label='Secret Admin Password', validators=[DataRequired()])
    submit = SubmitField(label='Edit')