from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.sql.expression import false
from app.configs.database import db
from dataclasses import dataclass


@dataclass
class LeadsModel(db.Model):
    name: str
    email: str
    phone: str
    creation_date: str
    last_visit: str
    visits: int

    __tablename__ = "leads"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False, unique=True)
    creation_date = Column(DateTime, default=datetime.utcnow)
    last_visit = Column(DateTime, default=datetime.utcnow)
    visits = Column(Integer, default=1)