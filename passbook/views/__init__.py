from flask import current_app as app
from flask import render_template, redirect, url_for, jsonify, request

from flask_login import current_user, login_required, LoginManager

from passbook.views import errors
from passbook.views import navigation
from passbook.views import login
from passbook.views import settings
from passbook.views import password_records
from passbook.views import wallet_records
from passbook.views import file_records
from passbook.views import note_records

from passbook.models.users import User
from passbook.models.records import PasswordRecord
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
	site_records = PasswordRecord.query.all()
	return render_template('index.html', site_records=site_records)

@app.route('/about')
def about():
	return render_template('dashboard/about.html')

@app.route('/help')
def help():
	return render_template('dashboard/help.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required.')
			return render_template('dashboard/contact.html', form=form)
		else:
			subject = form.subject.data
			msg = form.message.data
			sender = form.email.data
			sender_name = form.name.data
			# TODO: Actually send message
			flash('Successfully sent message.')
			return render_template('dasboard/contact.html', success=True)

	elif request.method == 'GET':
		return render_template('dashboard/contact.html', form=form)