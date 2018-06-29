# -*- coding: utf-8 -*-
"""
Downloads all of the Flask extensions outside of the initial creation of the app.
This is better for managing the application context.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_compress import Compress
from flask_wtf import CSRFProtect
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_restful import Api

from celery import Celery

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
compress = Compress()
csrf = CSRFProtect()
toolbar = DebugToolbarExtension()
boot = Bootstrap()
nav = Nav()
topbar = Navbar('',
    View('Home', 'main.index'),
    View('Login', 'auth.login'),
    View('Register', 'auth.signup')
)
nav.register_element('top', topbar)
api = Api()

celery = Celery()