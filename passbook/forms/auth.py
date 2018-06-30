# -*- coding: utf-8 -*-
"""
Forms for authenticating the user.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo

#from passbook.forms.base import BaseForm

# TODO: CSRF protection --> http://flask.pocoo.org/snippets/3/

class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired()])
	repeat_password = PasswordField('Repeat Password', alidators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Reset Password')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	repeat_password = PasswordField(
		'Repeat Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Please use a different email address.')