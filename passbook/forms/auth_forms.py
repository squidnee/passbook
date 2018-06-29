# -*- coding: utf-8 -*-
"""
Forms for authenticating the user.
"""

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

from passbook.forms.base import BaseForm

# TODO: CSRF protection --> http://flask.pocoo.org/snippets/3/

class RecoverPasswordForm(BaseForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

class MasterPasswordForm(RecoverPasswordForm):
    master = PasswordField('Password', validators=[DataRequired()])

class SignUpForm(MasterPasswordForm):
	verify_master = PasswordField('Verify Password', validators=[DataRequired()]) ## TODO : Fix this