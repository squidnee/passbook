# -*- coding: utf-8 -*-

from passbook.features.extensions import db
from passbook.app import create_app
from passbook.webui import WebUI
from passbook.config import BaseConfig as Config
from passbook.models.users import User
from passbook.models.records import SiteRecord

## TODO: http://flask.pocoo.org/snippets/22/ for db init

## TODO: Make compatible with command line http://flask.pocoo.org/snippets/133/

## TODO: Implement Flask Security

app = create_app(config=Config)

@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'SiteRecord': SiteRecord}

if __name__ == '__main__':
	app.run()
	#ui = WebUI(app, debug=True)
	#ui.run()