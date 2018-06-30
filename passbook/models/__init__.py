from datetime import datetime
from passbook.extensions import db

class TimestampMixin(object):
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
    last_accessed = db.Column(db.DateTime)