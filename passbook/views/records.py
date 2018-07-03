from flask import Blueprint, render_template
from flask import current_app as app

from passbook.features.extensions import db
from passbook.models.records import SiteRecord, WalletRecord
from passbook.forms.records import NewSiteRecordForm, NewWalletRecordForm, RecordSearchForm

records_bp = Blueprint('records', __name__, url_prefix='/records')

@records_bp.route('/all/', methods=['GET'])
def list_all_records():
	pass

@records_bp.route('/add/', methods=['GET', 'POST'])
def add_record():
	pass

@records_bp.route('/<int:id>/', methods=['GET','POST'])
def edit_record(id):
	pass

@records_bp.route('/results')
def search_results(search):
	pass