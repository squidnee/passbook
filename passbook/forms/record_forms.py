from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

from ..forms import BaseForm

class NewRecordForm(BaseForm):
    service = StringField('Service', validators=[DataRequired()])
    username = StringField('Username')
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email Address')
    notes = StringField('Notes')
    submit = SubmitField('Submit')