import enum

from passbook.features.orm import db
from sqlalchemy_utils import ChoiceType
from .base import BaseTable

class NoteType(enum.Enum):
	passwords = 1
	wallet = 2
	notes = 3

NoteType.passwords.label = _(u'Passwords')
NoteType.wallet.label = _(u'Wallet')
NoteType.notes.label = _(u'Notes')

class EncryptedNote(BaseTable):

	__tablename__ = 'note'

	name = db.Column(db.String(36))
	type = db.Column(ChoiceType(NoteType, impl=db.Integer()))