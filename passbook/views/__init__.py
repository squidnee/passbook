from flask import current_app as app
from flask import render_template, redirect, url_for, jsonify, request

from flask_login import current_user, login_required, LoginManager

from passbook.views import errors
from passbook.views import navigation
from passbook.views import login
from passbook.views import settings
from passbook.views import manager
from passbook.views import wallet
from passbook.views import contact

from passbook.models.users import User
from passbook.models.records import PasswordRecord, WalletRecord, NoteRecord
from passbook.forms.mail import ContactForm
from passbook.features.mail import send_email

#from passbook.managers.auth import login_manager
login_manager = LoginManager(app)

# Redirects to the login form if user is not logged in
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'

@app.route('/')
@app.route('/index')
#@login_required
def index():
	password_records = PasswordRecord.query.all()
	wallet_records = WalletRecord.query.all()
	note_records = NoteRecord.query.all()
	return render_template('index.html', password_records=password_records, wallet_records=wallet_records, note_records=note_records)

@app.route('/about')
def about():
	return render_template('app/tabs/other/about.html')

@app.route('/help')
def help():
	return render_template('app/tabs/other/help.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required.')
			return render_template('app/tabs/other/contact.html', form=form)
		else:
			subject = form.subject.data
			msg = form.message.data
			sender = form.email.data
			sender_name = form.name.data
			# TODO: Actually send message
			flash('Successfully sent message.')
			return render_template('app/tabs/other/contact.html', success=True)

	elif request.method == 'GET':
		return render_template('app/tabs/other/contact.html', form=form)