from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask import current_app as app

from passbook.features.extensions import db
from passbook.models.records import PasswordRecord
from passbook.forms.records import NewPasswordRecordForm, EditPasswordRecordForm

@app.route('/list_password_records')
def list_password_records():
	site_records = PasswordRecord.query.all()
	return render_template('index.html', site_records=site_records)

@app.route('/add_password_record', methods=['GET', 'POST'])
def add_password_record():
	add_record = True
	form = NewPasswordRecordForm()
	if form.validate_on_submit():
		name = form.name.data
		service = form.service.data
		username = form.username.data
		email = form.email.data
		description = form.description.data
		notes = form.notes.data
		reprompt = form.require_password_reprompt.data
	record = PasswordRecord(name=name, username=username, email=email, service_name=service, description=description, notes=notes, reprompt=reprompt)
	try:
		db.session.add(record)
		db.session.commit()
		flash('Record was successfully added')
	except:
		flash('There was an error when adding your password record')
	return render_template('dashboard/add_password_record.html', action="Add", add_record=add_record, form=form)

@app.route('/edit_password_record/<int:id>', methods=['GET','POST'])
def edit_password_record(id):
	add_record = False
	record = PasswordRecord.query.get_or_404(id)
	form = EditPasswordRecordForm(obj=record)
	if form.validate_on_submit():
		record.name = form.name.data
		record.service_name = form.service.data
		record.service_domain = form.domain.data
		record.email = form.email.data
		record.username = form.username.data
		record.description = form.description.data
		record.notes = form.notes.data
		record.reprompt = form.require_password_reprompt.data
		record.attachments = form.attachment.data
		record.starred = form.starred.data
		db.session.commit()
		flash('You have successfully edited this record.')
	else:
		flash('There was an error when editing your password record')
	return render_template('dashboard/edit_password_record.html', action="Edit", add_record=add_record, form=form, record=record)

@app.route('/delete_password_record/<int:id>', methods=['GET','POST'])
def delete_password_record(id):
	record = PasswordRecord.query.get_or_404(id)
	db.session.delete(record)
	db.session.commit()
	flash('Successfully deleted password record')
	return render_template("index.html")
