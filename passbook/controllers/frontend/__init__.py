from flask import current_app as app
from flask import render_template

from flask_login import current_user

from passbook.controllers.frontend import admin
from passbook.controllers.frontend import errors
from passbook.controllers.frontend import navigation
from passbook.controllers.frontend import login

from passbook.models.users import User

@app.route('/')
def index():
	if not current_user.is_authenticated:
		text = "Need to log in"
	else:
		text = "Ok you're good to go"
	return render_template('index.html', text=text)