from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, post_load
import datetime as dt

db = SQLAlchemy()

class Thing(db.Model):
    def __init__(self, description, location, sublocation):
        self.description = description
        self.location = location
        self.created_at = dt.datetime.now()
        self.sublocation = sublocation

    def __repr__(self):
        return f"Thing(id={self.id!r}, name={self.description!r}, location={self.location!r})"

    __tablename__ = 'things_tbl'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    location = db.Column(db.String)
    sublocation = db.Column(db.String)
    created_at = db.Column(db.String)

class ThingSchema(Schema):
    description = fields.Str()
    location = fields.Str()
    created_at = fields.Str()
    sublocation = fields.Str()
    id = fields.Integer()

    @post_load
    def make_thing(self, data, **kwargs):
        return Thing(**data)