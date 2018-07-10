from datetime import datetime
from passbook.features.orm import db

CATEGORY_TYPES = set(['internet', 'money', 'identity', 'notes'])
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

class TimestampMixin(object):
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_accessed = db.Column(db.DateTime)

class RecordMixin(object):
	description = db.Column(db.String(200))
	files = db.Column(db.LargeBinary)
	starred = db.Column(db.Boolean, default=False)
	expiration_date = db.Column(db.Date)
	reprompt = db.Column(db.Boolean, default=False)