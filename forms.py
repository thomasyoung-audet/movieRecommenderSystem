from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
import re


class MyValidator(object):
    def __init__(self):
        self.min = 0
        self.max = 5
        self.message = "Enter a number from 1 to 5. "

    def __call__(self, form, field):
        l = field.data and len(field.data) or 0
        if self.min >= l >= self.max:
            raise ValidationError(self.message)


class MovieForm(FlaskForm):
    """Movie rating form."""
    movie1 = StringField('a', [MyValidator()])
    movie2 = StringField('b', [MyValidator()])
    movie3 = StringField('c', [MyValidator()])
    movie4 = StringField('d', [MyValidator()])
    movie5 = StringField('a', [MyValidator()])
    movie6 = StringField('a', [MyValidator()])
    movie7 = StringField('a', [MyValidator()])
    movie8 = StringField('a', [MyValidator()])
    movie9 = StringField('a', [MyValidator()])
    movie10 = StringField('a', [MyValidator()])
    submit_item_based = SubmitField('Calculate recommendations - User-based algorithm')
    submit_user_based = SubmitField('Calculate recommendations - Item-based algorithm')


