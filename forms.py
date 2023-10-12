from flask_wtf import FlaskForm
from wtforms import (IntegerField,DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
    RadioField)
from wtforms.validators import URL, DataRequired, Email, EqualTo, Length


class Login(FlaskForm):
    userN = StringField("Username:", validators=[DataRequired(), Length(max=20)])
    passW = StringField("Password:", validators=[DataRequired()])
    submitB = SubmitField("Submit")