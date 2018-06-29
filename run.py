# -*- coding: utf-8 -*-

from passbook.app import create_app
from passbook.webui import WebUI
from passbook.config import BaseConfig as Config

## TODO: http://flask.pocoo.org/snippets/22/ for db init

## TODO: Make compatible with command line http://flask.pocoo.org/snippets/133/

## TODO: Implement Flask Security

if __name__ == '__main__':
	app = create_app(Config)
	app.run()
	#ui = WebUI(app, debug=True)
	#ui.run()
	#init_gui(app)