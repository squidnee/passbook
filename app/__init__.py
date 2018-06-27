from flask import Flask, render_template#, url_for, request, make_response
from .extensions import db
from .endpoints import register_endpoints
from .config import Config

app = Flask(__name__, instance_relative_config=True)

def create_app(config=Config):
	app.config.from_object(config)
	app.config.from_pyfile('config.py')
	print(app.config)
	register_extensions()
	return app

def register_extensions():
	db.init_app(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('./errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('./errors/500.html'), 500

@app.route('/')
#@login_required
def index():
    return render_template("index.html")
