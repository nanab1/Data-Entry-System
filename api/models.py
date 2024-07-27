from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import datetime


db = SQLAlchemy()

class Security(db.Model):
    __tablename__ = 'Security'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    sec_idNo = db.Column(db.String(36), unique=True)
    username = db.Column(db.String(40), unique=True)

    def __init__(self, name, sec_idNo, username):
        self.name = name
        self.sec_idNo = sec_idNo
        self.username = username

class VehicleInfo(db.Model):
    __tablename__ = 'vehicle_info'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    vehicle_number = db.Column(db.String(100), nullable=False)
    driver_name = db.Column(db.String(100), nullable=False)
    route_to = db.Column(db.String(100), nullable=False)
    post = db.Column(db.String(100), nullable=False)
    date_recorded = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, vehicle_number, driver_name, route_to, post):
        self.vehicle_number = vehicle_number
        self.driver_name = driver_name
        self.route_to = route_to
        self.post = post
    