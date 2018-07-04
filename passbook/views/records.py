from flask import Blueprint, render_template, request, jsonify
from flask import current_app as app

from passbook.features.extensions import db
from passbook.models.records import SiteRecord, WalletRecord
from passbook.forms.records import NewSiteRecordForm, NewWalletRecordForm, RecordSearchForm

records_bp = Blueprint('records', __name__, url_prefix='/records')

@records_bp.route('/', methods=['GET'])
def list_all_records():
	pass

@records_bp.route('/add_record', methods=['GET', 'POST'])
def add_record():
	form = NewSiteRecordForm()
	if form.validate_on_submit():
		name = form.name.data
		service = form.service.data
		username = form.username.data
		email = form.email.data
		description = form.email.data
		notes = form.notes.data
		reprompt = form.require_password_reprompt.data

@records_bp.route('/add_wallet', methods=['GET', 'POST'])
def add_wallet():
	pass

@records_bp.route('/<int:id>', methods=['GET','POST'])
def edit_record(id):
	pass

@records_bp.route('/results')
def search_results(search):
	pass