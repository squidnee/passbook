from flask_login import LoginManager
from flask import current_app as app

login_manager = LoginManager(app)

login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'