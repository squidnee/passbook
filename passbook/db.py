# -*- coding: utf-8 -*-
"""
This script contains basic database operation commands.
"""

import sqlite3
import click

from flask import current_app, g
from flask.cli import with_appcontext

from passbook.features.extensions import db
from passbook.util.fakes import make_fake_users

def init_app(app):
	app.teardown_appcontext(close_db)
	app.cli.add_command(init_db_command)

def init_db():
	db = get_db()
	with current_app.open_resource('schema.sql') as f:
		db.executescript(f.read().decode('utf8'))

def get_db():
	if 'db' not in g:
		g.db = sqlite3.connect(current_app.config['SQLALCHEMY_DATABASE_URI'])
		g.db.row_factory = sqlite3.Row
	return g.db

def close_db(e=None):
	db = g.pop('db', None)
	if db:
		db.close()

def build_sample_db():
	make_fake_users()

@click.command('init')
@with_appcontext
def init_db_command():
	init_db()
	click.echo("Initialized the database.")

@click.command('fake users')
@with_appcontext
def make_fake_users():
	build_sample_db()
	click.echo("Added fake users to the database.")

click.add_command(init_db_command)
click.add_command(make_fake_users)