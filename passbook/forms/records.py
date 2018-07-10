from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField, FieldList, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email, Length
from wtforms.widgets import TextArea, PasswordInput
from wtforms.ext.sqlalchemy.orm import model_form

class NewPasswordRecordForm(FlaskForm):
    name = StringField('Record Name', validators=[DataRequired()])
    service = StringField('Service/Website', validators=[DataRequired()])
    username = StringField('Username')
    password = PasswordField('Password', widget=PasswordInput(hide_value=False))
    email = StringField('Email Address', validators=[Email()])
    description = StringField('Description', widget=TextArea(), validators=[Length(min=0, max=140)])
    notes = StringField('Notes', widget=TextArea(), validators=[Length(min=0, max=140)])
    require_password_reprompt = BooleanField('Require Password Reprompting?')
    submit = SubmitField('Submit')

class EditPasswordRecordForm(FlaskForm):
    name = StringField('Record Name')
    service = StringField('Service')
    domain = StringField('Service Name')
    email = StringField('Email Address', validators=[Email()])
    username = StringField('Username')
    password = PasswordField('Password', widget=PasswordInput(hide_value=True))
    description = StringField('Description', widget=TextArea(), validators=[Length(min=0, max=140)])
    notes = StringField('Notes', widget=TextArea(), validators=[Length(min=0, max=140)])
    require_password_reprompt = BooleanField('Require Password Reprompt')
    starred = BooleanField('Star this Record')
    add_tag = StringField('Add Tag')
    attachment = FileField('Add Attachment')
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
    name = StringField('Name of File', validators=[DataRequired(), Length(max=100)])
    uploads = FieldList(FileField(), validators=[FileRequired(), FileAllowed(['jpg', 'png', 'txt', 'gif', 'pdf'])])
    submit = SubmitField('Upload')

class RecordSearchForm(FlaskForm):
    search = StringField('', validators=[Length(min=1, max=140)])