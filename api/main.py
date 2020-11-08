from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
from datetime import datetime
import hashlib
import random

from db_stuff import *

NEED_API_KEY = True

def parse_date(data):
    return datetime.strptime(data, "%Y-%m-%d").date()


def get_or_none(data, field):
    if field in data:
        return data[field]


def verify_api_key(key):
    has_key = db.session.query(
        Api.api_key,
    ).filter(Api.api_key == key).all()
    if has_key:
        return True
    else:
        return not NEED_API_KEY

@app.route('/api/add_trade', methods=['POST'])
def add_trade_endpoint():
    if request.is_json:
        return add_trade(request.json)

    return "Expected JSON"

def add_trade(data):
    if not verify_api_key(data['api_key']):
        return 'Exception invalid api_key.'

    if "weapon_name" in data and "category" in data:
        print("a")
        included_parts = db.session.query(
            Weapon.weapon_name,
        ).filter(Weapon.weapon_name == data["weapon_name"]).all()

        if len(included_parts) == 0:
            new_weapon = Weapon(
                weapon_name=data["weapon_name"],
                category=data["category"],
            )

            db.session.add(new_weapon)

    matches = db.session.query(
        Trade.id,
    ).filter(
        Trade.country_from==data['country_from'],
        Trade.country_to==data['country_to'],
        Trade.weapon_name==get_or_none(data, 'weapon_name'),
        Trade.amount==get_or_none(data, 'amount'),
        Trade.trade_start==parse_date(data['trade_start']),
        Trade.source==data['source'],
    ).all()
    if matches != []:
        print("Duplicate")

    new_trade = Trade(
        country_from=data['country_from'],
        api_key=data['api_key'],
        country_to=data['country_to'],
        weapon_name=get_or_none(data, 'weapon_name'),
        amount=get_or_none(data, 'amount'),
        trade_start=parse_date(data['trade_start']),
        trade_end=parse_date(data['trade_end']),
        is_verified=False,
        source=data['source'],
    )

    db.session.add(new_trade)
    db.session.commit()
    return "Added"


@app.route('/api/add_trades', methods=['POST'])
def add_trades():
    if request.is_json:
        last_resp = None
        for k in request.get_json():
            last_resp = add_trade(k)

        return last_resp

    return "Expected JSON"

@app.route('/api/query_trade', methods=['GET'])
def query_trade():
    country_from = request.args.get('country_from') # Optional
    country_to = request.args.get('country_to') # Optional
    start = request.args.get('trade_start') # Optional
    end = request.args.get('trade_end') # Optional

    if country_from is None and country_to is None:
        return "give either country_from or country_to"

    tradesq = db.session.query(
        Trade.country_from,
        Trade.country_to,
        Trade.weapon_name,
        Trade.amount,
        Trade.trade_start,
        Trade.trade_end,
        Trade.is_verified,
        Trade.source,
    )

    if country_from != None:
        tradesq = tradesq.filter(Trade.country_from == country_from)

    if country_to != None:
        tradesq = tradesq.filter(Trade.country_to == country_to)

    if start != None:
        tradesq = tradesq.filter(Trade.trade_start > parse_date(start))

    if end != None:
        tradesq = tradesq.filter(Trade.trade_end < parse_date(end))

    trades = tradesq.all()

    trades_struct = [
        {
            "country_from": trade[0],
            "country_to":   trade[1],
            "weapon_name":  trade[2],
            "amount":       trade[3],
            "trade_start":  datetime.strftime(trade[4], "%Y"),
            "trade_end":    datetime.strftime(trade[5], "%Y"),
            "is_verified":  trade[6],
            "source":       trade[7],
        }
        for trade in trades
    ]

    return json.dumps(trades_struct)


@app.route('/api/generate', methods=['POST'])
def generate():
    #{full_name:..., email:...}
    if request.is_json:
        data = request.get_json()
        new_key = Api(data['email'], data['full_name'])
        db.session.add(new_key)
        db.session.commit()
        return new_key.api_key
    return "Expected JSON"

@app.route('/api/add_conflict', methods=['POST'])
def add_conflict_endpoint():
    if request.is_json:
        return add_conflict(request.json)

    return "Expected JSON"

@app.route('/api/add_conflicts', methods=['POST'])
def add_conflicts():
    if request.is_json:
        last_resp = None
        for k in request.get_json():
            last_resp = add_conflict(k)

        return last_resp

    return "Expected JSON"

def add_conflict(data):
    if not verify_api_key(data['api_key']):
        return 'Exception invalid api_key.'

    new_conflict = Conflict(
        country=data['country'],
        api_key=data['api_key'],
        picture_url=get_or_none(data, 'picture_url'),
        info=get_or_none(data, 'info'),
        date_start=parse_date(data['date_start']),
        verified=False,
        source=data['source'],
    )

    db.session.add(new_conflict)
    db.session.commit()

    return "Added"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1234)
