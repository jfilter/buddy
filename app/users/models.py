from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from datetime import datetime

from app.data import db

import uuid

RANK_USER = 0
RANK_MOD = 1
RANK_ADMIN = 2

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  surname = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(100), unique=True, nullable=False)
  password_hash = db.Column(db.String(100), nullable=False)
  dob = db.Column(db.Date, nullable=False)
  gender = db.Column(db.String(1), nullable=False)
  faculty = db.Column(db.String(50), nullable=False)
  lang1 = db.Column(db.String(50))
  lang2 = db.Column(db.String(50))
  lang3 = db.Column(db.String(50))
  remarks = db.Column(db.Text)
  rank = db.Column(db.Integer, default=RANK_USER)
  status = db.Column(db.String(1), nullable=False)
  registration_date = db.Column(db.DateTime, default=db.func.now())
  last_login = db.Column(db.DateTime)
  num_logins = db.Column(db.Integer, default=0)
  token = db.Column(db.String(100), unique=True)
  matchable = db.Column(db.Boolean, default=True)
  max_buddies = db.Column(db.Integer)
  training = db.Column(db.Integer)
  term = db.Column(db.String(100))

  def __init__(self, **dict):
    self.name = dict['name'].title()
    self.surname = dict['surname'].title()
    self.email = dict['email'].lower()
    self.set_password(dict['password'])
    dob = datetime.strptime(dict['dob'], '%d.%m.%Y')
    self.dob = dob
    self.gender = dict['gender']
    self.faculty = dict['faculty']
    self.lang1 = dict['lang1'] 
    self.lang2 = dict['lang2']
    self.lang3 = dict['lang3']
    self.remarks = dict['remarks']
    self.status = dict['status']
    self.token = str(uuid.uuid4())

    if self.status == 'p':
      self.max_buddies = dict['max_buddies']
      self.training = dict['training']

 
  def set_password(self, password):
    self.password_hash = generate_password_hash(password)
   
  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

  def to_table(self):
    res ="""<td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td>
      <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td>
      """ % (self.id, self.name, self.surname, self.email, self.dob, self.gender, self.faculty,
        self.lang1, self.lang2, self.lang3, self.remarks, self.status)
    return res

  def to_user_table(self):
    res ="""<td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td><td>%s</td> <td>%s</td> 
      <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td>
      """ % (self.id, self.name, self.surname, self.email, self.dob, self.gender, self.faculty,
        self.lang1, self.lang2, self.lang3, self.remarks, self.rank, self.status, self.registration_date,
        self.matchable)
    return res

  def to_short_table(self):
    res ="""<td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td>""" % (self.id, self.name, self.surname, self.email)
    return res 

  def is_admin(self):
    return self.rank == RANK_ADMIN
