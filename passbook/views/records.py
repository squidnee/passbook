from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask import current_app as app

from passbook.features.extensions import db
from passbook.models.records import Record, WalletRecord
from passbook.forms.records import NewSiteRecordForm, NewWalletRecordForm, RecordSearchForm

records_bp = Blueprint('records', __name__, url_prefix='/records')

@records_bp.route('/')
def list_all_records():
	return render_template('index.html')

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
	record = Record(name=name, username=username, email=email)
	db.session.add(record)
	db.session.commit()
	flash('Record was successfully added')
	return redirect(url_for('list_all_records'))

@records_bp.route('/add_wallet', methods=['GET', 'POST'])
def add_wallet():
	pass

@records_bp.route('/<int:id>', methods=['GET','POST'])
def edit_record(id):
	pass

@records_bp.route('/results')
def search_results(search):
	pass