from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField, IntegerField

class UserPreferences(FlaskForm):
	first_name = StringField('First Name')
	last_name = StringField('Last Name')
	phone_number = StringField('Phone Number')
	password_hint = StringField('Password Hint')