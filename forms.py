from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Length, NumberRange

class SignUpForm(Form):
  first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
  last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
  submit = SubmitField('Sign up')
#New Class for Login form
class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
    password =  PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
    submit = SubmitField("Sign in")
class PicScoreForm(Form):
    #score = IntegerField('Score from 1 to 5', validators=[DataRequired("Please enter a number"),MinValueValidator(1), MaxValueValidator(5)])
    score = IntegerField('Score from 1 to 5', validators=[DataRequired("Please enter a number"),NumberRange(min=0,max=5)])
    score00 = IntegerField('Score from 1 to 5', validators=[DataRequired("Please enter a number"),NumberRange(min=0,max=5)])
    score01 = IntegerField('Score from 1 to 5', validators=[DataRequired("Please enter a number"),NumberRange(min=0,max=5)])
    score02 = IntegerField('Score from 1 to 5', validators=[DataRequired("Please enter a number"),NumberRange(min=0,max=5)])
    score03 = IntegerField('Score from 1 to 5', validators=[DataRequired("Please enter a number"),NumberRange(min=0,max=5)])
    score04 = IntegerField('Score from 1 to 5', validators=[DataRequired("Please enter a number"),NumberRange(min=0,max=5)])
    score05 = IntegerField('Score from 1 to 5', validators=[DataRequired("Please enter a number"),NumberRange(min=0,max=5)])
    score06 = IntegerField('Score from 1 to 5', validators=[DataRequired("Please enter a number"),NumberRange(min=0,max=5)])
    score07 = IntegerField('Score from 1 to 5', validators=[DataRequired("Please enter a number"),NumberRange(min=0,max=5)])
    score08 = IntegerField('Score from 1 to 5', validators=[DataRequired("Please enter a number"),NumberRange(min=0,max=5)])
    score09 = IntegerField('Score from 1 to 5', validators=[DataRequired("Please enter a number"),NumberRange(min=0,max=5)])
    score10 = IntegerField('Score from 1 to 5', validators=[DataRequired("Please enter a number"),NumberRange(min=0,max=5)])

    submission = SubmitField("Submit Scores")
