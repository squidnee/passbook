# -*- coding: utf-8 -*-

from passbook.features.extensions import db
from passbook.app import create_app
from passbook.webui import WebUI
from passbook.config import BaseConfig as Config
from passbook.models.users import User
from passbook.models.records import PasswordRecord, WalletRecord, FileRecord, NoteRecord

## TODO: http://flask.pocoo.org/snippets/22/ for db init

## TODO: Make compatible with command line http://flask.pocoo.org/snippets/133/

## TODO: Implement Flask Security
BUILD_FAKES = False
app = create_app(config=Config, build_fake_database=BUILD_FAKES)

@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'PasswordRecord': PasswordRecord, 'WalletRecord': WalletRecord, \
			'FileRecord': FileRecord, 'NoteRecord': NoteRecord}

if __name__ == '__main__':
	app.run()
	#ui = WebUI(app, debug=True)
	#ui.run()