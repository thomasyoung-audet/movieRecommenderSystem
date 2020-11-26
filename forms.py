from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import ValidationError


def validate_numbers(form, field):
    if field.data == "":
        raise ValidationError("Sorry, you haven't made a selection")


class MovieForm(FlaskForm):
    numbers = [("", "---"), (1, '1'), (2, '2'), (3, '3'),
               (4, '4'), (5, '5'), (0, 'I have not watched this movie')]  # (index, value)

    """Movie rating form."""
    movie1 = SelectField('', choices=numbers, validators=[validate_numbers])
    movie2 = SelectField('', choices=numbers, validators=[validate_numbers])
    movie3 = SelectField('', choices=numbers, validators=[validate_numbers])
    movie4 = SelectField('', choices=numbers, validators=[validate_numbers])
    movie5 = SelectField('', choices=numbers, validators=[validate_numbers])
    movie6 = SelectField('', choices=numbers, validators=[validate_numbers])
    movie7 = SelectField('', choices=numbers, validators=[validate_numbers])
    movie8 = SelectField('', choices=numbers, validators=[validate_numbers])
    movie9 = SelectField('', choices=numbers, validators=[validate_numbers])
    movie10 = SelectField('', choices=numbers, validators=[validate_numbers])
    submit_item_based = SubmitField('Calculate recommendations - User-based algorithm')
    submit_user_based = SubmitField('Calculate recommendations - Item-based algorithm')
