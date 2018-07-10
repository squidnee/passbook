import re

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, TextField, TextAreaField, validators, ValidationError

class ContactForm(FlaskForm):
	name = TextField("Name", [validators.Required("Please enter your name.")])
	email = TextField("Email", [validators.Required("Please enter your email."), validators.Email("Please enter your email.")])
	subject = TextField("Subject", [validators.Required("Please enter a subject line.")])
	message = TextAreaField("Message", [validators.Required("Please enter a message.")])
	submit = SubmitField("Send")

class ShareRecordForm(FlaskForm):
	records_to_share = StringField("Records to Share", [validators.Required("Please enter the name(s) of the record(s) you'd like to share.")])
	recipients = StringField("Recipients", [validators.Required("Please enter some recipients.")])
	#permissions = SelectField()
	submit = SubmitField("Share")

	def validate_recipients(form, field):
		regex = re.compile(r'^.+@([^.@][^@]+)$', re.IGNORECASE)
		emails = field.data.split(';')
		for email in emails:
			email = email.strip()
			if email:
				match = regex.match(email or '')
				if not match:
					raise ValidationError("Please separate emails using semicolons.")