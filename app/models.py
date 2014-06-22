from app import app, db

class Census(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    state = db.Column(db.String(30))
    sex = db.Column(db.String(2))
    age = db.Column(db.Integer)
    pop2000 = db.Column(db.Integer)
    pop2008 = db.Column(db.Integer)

    def serialize(self, state = None):
        """Return object data in easily serializeable format"""
        if state:
           return {
               "sex"       : self.sex,
               "age"       : self.age,
               "pop2000"   : self.pop2000,
               "pop2008"   : self.pop2008
            }
        else:
            return {
                "state"     : self.state,
                "sex"       : self.sex,
                "age"       : self.age,
                "pop2000"   : self.pop2000,
                "pop2008"   : self.pop2008
            }
