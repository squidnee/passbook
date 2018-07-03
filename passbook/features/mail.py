# -*- coding: utf-8 -*-
"""
For asynchronous emailing from within the application.
"""

from threading import Thread
from flask import current_app as app
from flask import render_template
from flask_mail import Message
from passbook.features.extensions import mail

mail.init_app(app)

def send_async_email(app, msg):
	with app.app_context():
		mail.send(msg)

def send_email(title, sender, recipients, text, html):
	msg = Message(title, sender=sender, recipients=recipients)
	msg.body = text
	msg.html = html
	Thread(target=send_async_email, args=(app, msg)).start()

def send_password_reset_email(user):
	token = user.get_reset_password_token()
	send_email('[Password Manager] Reset Your Password', sender=app.config['MAIL_FROM_EMAIL'], recipients=[user.email],
				text=render_template('mail/reset_password.txt', user=user, token=token),
				html=render_template('mail/reset_password.html', user=user, token=token)
				)