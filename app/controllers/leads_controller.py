from flask import request, current_app, jsonify
from sqlalchemy.sql.expression import update
from app.models.leads_model import LeadsModel
from datetime import datetime
import sqlalchemy
import psycopg2
import re


def create_lead():
    data = request.get_json()

    phone_regex = "\(\w{2}\)\w{5}-\w{4}"
    if not re.fullmatch(phone_regex, data['phone']):
        return {"msg": "invalid phone format, use (xx)xxxxx-xxxx"}, 400

    try:
        lead = LeadsModel(**data)
        
        current_app.db.session.add(lead)
        current_app.db.session.commit()

    except sqlalchemy.exc.IntegrityError as e:
        if type(e.orig) == psycopg2.errors.UniqueViolation:
             return {'msg': str(e.orig).split('\n')[1][9:]}, 409


    return jsonify(lead), 201


def get_all():
    leads = LeadsModel.query.order_by(sqlalchemy.desc(LeadsModel.visits)).all()

    if not leads:
        return {"msg": "No registrations found"}, 404
    
    return jsonify(leads), 200


def update_leads():
    data = request.json

    if not 'email' in data.keys() or len(data) != 1 or type(data['email']) != str:
        return {"msg":"Expected only email key with a string"}, 400

    lead_to_updade = LeadsModel.query.filter_by(email=data['email']).first_or_404()
    update = {'visits': lead_to_updade.visits + 1, "last_visit": datetime.utcnow()}

    lead = LeadsModel.query.filter_by(id=lead_to_updade.id).update(update)
    current_app.db.session.commit()

    lead = LeadsModel.query.get(lead_to_updade.id)

    return jsonify(lead), 200


def delete_leads():
    data = request.json

    if not 'email' in data.keys() or len(data) != 1 or type(data['email']) != str:
        return {"msg":"Expected only email key with a string"}, 400

    lead = LeadsModel.query.filter_by(email=data['email']).first_or_404()

    current_app.db.session.delete(lead)
    current_app.db.session.commit()

    return jsonify(lead), 200
