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
from flask_bootstrap import Bootstrap
from flask_nav import Nav

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
compress = Compress()
csrf = CSRFProtect()
boot = Bootstrap()
nav = Nav()