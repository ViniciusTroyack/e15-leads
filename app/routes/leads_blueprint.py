from re import U
from flask import Blueprint
from sqlalchemy.sql.expression import update
from app.controllers.leads_controller import create_lead, get_all, update_leads, delete_leads

bp_leads = Blueprint("bp_lead", __name__, url_prefix="/leads")


bp_leads.post("")(create_lead)
bp_leads.get("")(get_all)
bp_leads.patch("")(update_leads)
bp_leads.delete("")(delete_leads)