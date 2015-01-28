# This file is essentially the database schema. Each class is used to define an
# entry in the table.
from app import db

class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), index=True, unique=False)
    name = db.Column(db.String(50), index=True, unique=True)
    milage = db.Column(db.Integer, index=True, unique=False)

    def __repr__(self):
        return '<Machine %r>' % (self.name)
