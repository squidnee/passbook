import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
#from flask_cache import Cache

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
print(app.config)
#app.config.from_envvar('APP_CONFIG_FILE')

CORS(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view =  "signin"

from app import views, models
#db.create_all()

@app.errorhandler(404)
def not_found(error):
    return render_template('./errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('./errors/500.html'), 500