from wtforms import ValidationError
def IsUnique(Form, feild):
    if (len(feild.data) % 2 == 1):
        raise ValidationError('email already exists')
