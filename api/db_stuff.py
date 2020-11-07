from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import hashlib
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:docker@postgres/hh"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Trade(db.Model):
    __tablename__ = 'trades'

    id = db.Column(db.Integer, primary_key=True)
    country_from = db.Column(db.String())
    country_to = db.Column(db.String())
    weapon_name = db.Column(db.String())
    amount = db.Column(db.Integer())
    trade_start = db.Column(db.Date())
    trade_end = db.Column(db.Date())
    is_verified = db.Column(db.Boolean())
    source = db.Column(db.String())
    api_key = db.Column(db.String())

    def __init__(self, country_from, country_to, weapon_name, amount, trade_start, trade_end, is_verified, source, api_key):
        self.country_from = country_from
        self.country_to = country_to
        self.weapon_name = weapon_name
        self.amount = amount
        self.trade_start = trade_start
        self.trade_end = trade_end
        self.is_verified = is_verified
        self.source = source
        self.api_key = api_key


class Weapon(db.Model):
    __tablename__ = 'weapons'

    weapon_name = db.Column(db.String(), primary_key=True)
    category = db.Column(db.String())

    def __init__(self, weapon_name, category):
        self.weapon_name = weapon_name
        self.category = category


class Api(db.Model):
    __tablename__ = 'api'

    api_key = db.Column(db.String(), primary_key=True)
    email = db.Column(db.String())
    full_name = db.Column(db.String())

    def __init__(self, full_name, email):
        self.email = email
        self.full_name = full_name
        self.api_key = hashlib.md5(
            hex(random.randint(0, 1000000000000000000))).hexdigest()


class Conflict(db.Model):
    __tablename__ = 'conflicts'

    id = db.Column(db.String(), primary_key=True)
    api_key = db.Column(db.String())
    country = db.Column(db.String())
    data = db.Column(db.String())
    picture = db.Column(db.String())
    date_start = db.Column(db.Date())
    is_verified = db.Column(db.Boolean())
    source = db.Column(db.String())

    def __init__(self, api_key, country, data, picture, date_start, is_verified, source):
        self.api_key = api_key
        self.country = country
        self.data = data
        self.picture = picture
        self.date_start = date
        self.is_verified = is_verified
        self.source = source
