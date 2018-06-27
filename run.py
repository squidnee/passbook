# -*- coding: utf-8 -*-

from app import create_app
from app.webui import WebUI

if __name__ == '__main__':
	app = create_app()
	ui = WebUI(app, debug=True)
	ui.run()