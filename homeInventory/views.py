from models import Thing, ThingSchema
from flask import Blueprint, jsonify, request
from models import db

blueprint = Blueprint('views', __name__)

@blueprint.route('/hello')
def hello():
    return 'Hello, World!'

@blueprint.route('/things')
def get_things():
  schema = ThingSchema(many=True)
  things = Thing.query.all()
  things_report = schema.dump(things)
  return jsonify(things_report)


@blueprint.route('/things', methods=['POST'])
def add_thing():
  thing = ThingSchema().load(request.get_json())
  db.session.add(thing)
  db.session.commit()
  thing_report = ThingSchema().dump(thing)
  return jsonify(thing_report)

@blueprint.route('/things/<id>', methods=['DELETE'])
def delete_thing(id):

  schema = ThingSchema()
  thing = Thing.query.filter_by(id=id).first()

  thing_report = schema.dump(thing)

  Thing.query.filter_by(id=id).delete()

  db.session.commit()
  print(f"Deleted {id}")
  return jsonify(thing_report)