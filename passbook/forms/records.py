from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email, Length
from wtforms.widgets import TextArea, PasswordInput
from wtforms.ext.sqlalchemy.orm import model_form

class NewSiteRecordForm(FlaskForm):
    name = StringField('Record Name', validators=[DataRequired()])
    service = StringField('Service/Website', validators=[DataRequired()])
    username = StringField('Username')
    password = PasswordField('Password', widget=PasswordInput(hide_value=False))
    email = StringField('Email Address', validators=[Email()])
    description = StringField('Description', widget=TextArea(), validators=[Length(min=0, max=140)])
    notes = StringField('Notes', widget=TextArea(), validators=[Length(min=0, max=140)])
    require_password_reprompt = BooleanField('Require Password Reprompting?')
    submit = SubmitField('Submit')

class NewWalletRecordForm(FlaskForm):
    card_name = StringField('Record Name', validators=[DataRequired()])
    card_number = StringField('Card Number', render_kw={'maxlength':'19'}, validators=[DataRequired()])
    name_on_card = StringField('Name on Card', validators=[DataRequired()])
    expiration_date = StringField('Expiration Date', validators=[DataRequired()])
    cvc_code = IntegerField('CVC Code', render_kw={'maxlength':'3'}, validators=[DataRequired()])
    zip_code = IntegerField('Zip Code', validators=[DataRequired()])
    description = StringField('Description', widget=TextArea(), validators=[Length(min=0, max=140)])
    notes = StringField('Notes', widget=TextArea(), validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

class FileUploadForm(FlaskForm):
	file = FileField('Upload File', validators=[DataRequired()])
	submit = SubmitField('Submit')

class RecordSearchForm(FlaskForm):
    search = StringField('', validators=[Length(min=1, max=140)])