from app import app, db

class Census(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    state = db.Column(db.String(30), index = True)
    sex = db.Column(db.String(2), index = True)
    pop2000 = db.Column(db.Integer)
    pop2008 = db.Column(db.Integer)
