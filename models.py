from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  user_type = db.Column(db.String(64))
  relationships = relationship("Relation")

class Gps(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  date = db.Column(sqlalchemy.types.Date)
  time = db.Column(sqlalchemy.types.Time)
  latitude = db.Column(sqlalchemy.types.Float)
  longitude = db.Column(sqlalchemy.types.Float)

  def __repr__(self):
      return '<User %r>' % (self.nickname)

class Relation(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  caregiver_id = Column(Integer, ForeignKey('user.id'))
  carerecepient_id = Column(Integer, ForeignKey('user.id'))


