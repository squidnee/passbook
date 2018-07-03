from datetime import datetime
from passbook.features.extensions import db

CATEGORY_TYPES = set(['internet', 'money', 'identity', 'notes'])
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

class TimestampMixin(object):
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
    last_accessed = db.Column(db.DateTime)