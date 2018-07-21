from flask import current_app as app
from passbook.models.records import WalletRecord
from passbook.forms.records import NewWalletRecordForm

@app.route('/list_wallet_records')
def list_wallet_records():
	pass

@app.route('/add_wallet_record')
def add_wallet_record():
	pass

@app.route('/edit_wallet_record/<int:id>')
def edit_wallet_record(id):
	pass

@app.route('/delete_wallet_record/<int:id>')
def delete_wallet_record(id):
	pass