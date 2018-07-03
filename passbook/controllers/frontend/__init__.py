from flask import current_app as app
from flask import render_template, redirect, url_for

from flask_login import current_user, login_required, LoginManager

from passbook.controllers.frontend import errors
from passbook.controllers.frontend import navigation
from passbook.controllers.frontend import login
from passbook.controllers.frontend import settings

from passbook.models.users import User

#from passbook.managers.auth import login_manager
login_manager = LoginManager(app)

# Redirects to the login form if user is not logged in
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'

@app.route('/')
@app.route('/index')
#@login_required
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/help')
def help():
	return render_template('help.html')