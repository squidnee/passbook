import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from passbook.app import create_app, db
from passbook.models.users import User
from passbook.config import BaseConfig as Config

app = create_app(Config)

migrate = Migrate(app, db)
manager = Manager(app)

def make_shell_context():
	return dict(app=app, db=db, User=User)

def make_fake_data():
	pass

def create_dev_env():
	pass

def create_prod_env():
	pass

manager.add_command("shell", Shell(use_ipython=Config.USE_IPYTHON_WITH_MANAGER, make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()