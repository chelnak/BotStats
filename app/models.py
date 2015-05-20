from app import db
import datetime

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.String(10))
    comment_author = db.Column(db.String(50))
    link_id = db.Column(db.String(10))
    replied = db.Column(db.Integer)
    fact_id = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return '<Comment Id: %r>' % (self.comment_id)

class Fact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fact =  db.Column(db.String(250))

    def __repr__(self):
        return '<Fact Id: %r>' % (self.id)
