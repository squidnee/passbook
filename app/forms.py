from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

class MasterPasswordForm(Form):
    master = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class SignUpForm(Form):
	email = StringField('Email', validators=[DataRequired(), Email()])
	master = PasswordField('Password', validators=[DataRequired()])
	verify_master = PasswordField('Verify Password', validators=[DataRequired()])
	submit = SubmitField('Sign Up')

class NewEntryForm(Form):
    service = StringField('Service', validators=[DataRequired()])
    username = StringField('Username')
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email Address')
    notes = StringField('Notes')
    submit = SubmitField('Submit')