from passbook.app import create_app, db
from passbook.models.users import User
from passbook.config import BaseConfig as Config

app = create_app(Config)

@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User}