from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class UserPreferences(FlaskForm):
	first_name = StringField('First Name')
	last_name = StringField('Last Name')
	phone_number = StringField('Phone Number')
	password_hint = StringField('Password Hint')

class BasicSettings(FlaskForm):
	master_password = SubmitField('Change')
	master_password_reminder = SubmitField('View')
	email = SubmitField('Change')
	language = SelectField('Language', choices=[('en', 'English')])
	timezone = SelectField('Timezone', choices=[('PT', 'Pacific Time'), ('CT', 'Central Time'), ('ET', 'Eastern Time')]) # TODO
	submit = SubmitField('Save')