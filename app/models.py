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

"""
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String(100), index=True, unique=True)
    name = db.Column(db.String(64), index=True)
    family_name = db.Column(db.String(64), index=True)
    given_name = db.Column(db.String(64), index=True)
    picture = db.Column(db.String(100), index=True)
    link  = db.Column(db.String(100), index=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.name)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20), index=True, unique=True)

    def __repr__(self):
        return '<Role %r>' % (self.role)

"""
