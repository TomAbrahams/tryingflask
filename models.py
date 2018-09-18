from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
#flask.ext.sqlalchemy is for the connection to the database.
#werkzeug is for the encryption of the password.
#db stores a new object of the SQLAlchemy class.
db = SQLAlchemy()

class User(db.Model):
    __tablename__= 'users'
    uid = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(109))
    lastname = db.Column(db.String(109))
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(54))
    #Initialize, Constructor, Methods
    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.set_password(password)
    #Set Password methods
    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)
    #Check Password methods
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

class Score(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120))
    imagename = db.Column(db.String(200))
    score = db.Column(db.Integer)
    #Constructor
    def __init__(self, email, imageName, score):
        self.email = email.lower()
        self.imagename = imageName.lower()
        self.score = score
