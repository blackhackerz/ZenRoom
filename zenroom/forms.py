from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea

class Diary(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=200)])
    note = StringField('Note',
                           validators=[DataRequired(), Length(min=3, max=2000)], widget=TextArea())
    submit = SubmitField('Submit')


class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=3, max=200)])
    password = StringField('Password',
                           validators=[DataRequired(), Length(min=3, max=2000)], widget=TextArea())
    submit = SubmitField('Submit')