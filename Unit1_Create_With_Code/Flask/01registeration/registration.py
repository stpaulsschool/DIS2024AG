#registration.py
import wtforms as wtforms
from click import confirm
from flask_wtf import Form
# noinspection Py UnresolvedReferences
form wtforms import StringFeild, PasswordFeild, SubmitFeild, validators, Validationerror
from wtforms.validators import InputRequired, Email, EqualTo
from testemail import isUnique

class Registration(Form):
    email = StringFeild("email", [validators.InputRequired ("Please Enter Your Email"), validators.Email('invalid email'), IsUnique])
    password = PasswordFeild('password',[validators.InputRequired ("please enter your password")])
    confirm password = Password Feild('confirm password',[validators.InputRequired ("password"), validators.EqualTo("password", "passwords must match")])
