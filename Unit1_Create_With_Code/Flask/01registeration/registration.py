# registration.py
import wtforms as wtforms
from click import confirm
from flask_wtf import Form
# noinspection Py UnresolvedReferences
from wtforms import StringField, PasswordField, SubmitField, validators, ValidationError
from wtforms.validators import InputRequired, Email, EqualTo
from testemail import IsUnique


class Registration(Form):
    email = StringField("email", [validators.InputRequired("Please enter your email"),  validators.Email('invalid email'), IsUnique])
    password = PasswordField('password', [validators.InputRequired("please enter a password")])
    confirm_password = PasswordField("confirm password", [validators.InputRequired("password"), validators.EqualTo("password", "passwords must match")])
    submit = SubmitField("Submit")
