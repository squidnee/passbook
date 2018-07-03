from flask import Blueprint, render_template

from passbook.models.records import SiteRecord, WalletRecord, EncryptedFileRecord
from passbook.forms.records import NewSiteRecordForm, NewWalletRecordForm, FileUploadForm

records = Blueprint('records', __name__, url_prefix='/records')

@records.route('/all/', methods=['GET'])
def list_all_records():
	pass

@records.route('/add/', methods=['GET', 'POST'])
def add_record():
	pass

@records.route('/<int:id>/', methods=['GET','POST'])
def edit_record(id):
	pass