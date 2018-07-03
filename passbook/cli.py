import logging
import click

from flask import current_app as app
from flask.cli import FlaskGroup
from flask_login import current_user
from passbook.api.handlers.users import UserHandler

cli = FlaskGroup(app=app)

## Users commands ##
@click.command('whoami')
def whoami():
	click.echo(current_user.username)

@click.command()
def add_user():
	pass