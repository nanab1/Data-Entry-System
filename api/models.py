from api.app import db
import uuid
import datetime

class Security(db.Model):
    id = db.Column(db.String(36), unique=True, primary_key=True)
    name = db.Column(db.String(36))
    sec_idNo = db.Column(db.String(36), unique=True)
    username = db.Colum(db.String(40), unique=True)

    def __init__(self, name, sec_idNo):
        self.id = str(uuid.uuid4)
        self.name = name
        self.sec_idNo = sec_idNo

class VehicleInfo(db.Model):
    id = db.Column(db.String(36), unique=True, primary_key=True)
    vehicleNumber =  db.Column(db.String(36))
    driverName = db.Colum(db.String(100))
    routeTo = db.Column(db.String(100))
    post =  db.Column(db.String(100))
    # date_recorded = db.Column(db.)

    def __init__(self, vehicleNumber, driverName, routeTo, post):
        self.vehicleNumber = vehicleNumber
        self.driverName = driverName
        self.routeTo = routeTo
        self.post = post
    