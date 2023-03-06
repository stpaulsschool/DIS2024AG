from Unit1_Create_With_Code.microblog2.app import db


class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), idex=True, unique=True)
    password_hash = db.Column(db.String(128))


def __repr__(self):
    return '<User {}>'.format(self.username)

