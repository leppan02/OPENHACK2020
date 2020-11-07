from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

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

    def __init__(self, country_from, country_to, weapon_name, amount, trade_start, trade_end): 
        self.country_from = country_from
        self.country_to = country_to
        self.weapon_name = weapon_name
        self.amount = amount
        self.trade_start = trade_start
        self.trade_end = trade_end

class Weapon(db.Model):
    __tablename__ = 'weapons'

    weapon_name = db.Column(db.String(), primary_key=True)
    category = db.Column(db.String())

    def __init__(self, weapon_name, category):
        self.weapon_name = weapon_name
        self.category = category

def parse_date(data):
    return datetime.strptime(data, "%Y-%m-%d").date()

def get_or_none(data, field):
    if field in data:
        return data[field]

@app.route('/api/add_trade', methods=['POST'])
def add_trade():
    if request.is_json:
        data = request.get_json()

        if "weapon_name" in data:
            print("a")
            included_parts = db.session.query(
                Weapon.weapon_name,
            ).filter(Weapon.weapon_name == data["weapon_name"]).all()

            if len(included_parts) == 0:
                new_weapon = Weapon(
                    weapon_name = data["weapon_name"],
                    category = data["category"],
                )

                db.session.add(new_weapon)

        new_trade = Trade(
            country_from=data['country_from'],
            country_to=data['country_to'],
            weapon_name=get_or_none(data, 'weapon_name'),
            amount=get_or_none(data, 'amount'),
            trade_start=parse_date(data['trade_start']),
            trade_end=parse_date(data['trade_end'])
        )

        db.session.add(new_trade)
        db.session.commit()
        return "Added"

    return "Expected JSON"

@app.route('/api/query_trade', methods=['GET'])
def query_trade():
    # TODO
    return [{
        "id": 75,
        "country_from": "Sweden",
        "country_to": "Vatican State",
        "weapon_name": "kötbullr",
        "weapon_category": "mums",
        "amount": 55,
        "trade_start": "2020-11-07",
        "trade_end": "2020-11-09",
    }]

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1234)
