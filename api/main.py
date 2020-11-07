from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
from datetime import datetime
import hashlib
import random

from db_stuff import *


def parse_date(data):
    return datetime.strptime(data, "%Y-%m-%d").date()


def get_or_none(data, field):
    if field in data:
        return data[field]


def verify_api_key(key):
    has_key = db.session.query(
        Api.key,
    ).filter(Api.key == key).all()
    if has_key:
        return True
    else:
        return False


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
                    weapon_name=data["weapon_name"],
                    category=data["category"],
                )

                db.session.add(new_weapon)

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

    return "Expected JSON"


@app.route('/api/query_trade', methods=['GET'])
def query_trade():
    if request.is_json:
        data = request.get_json()

        tradesq = db.session.query(
            Trade.country_from,
            Trade.country_to,
            Trade.weapon_name,
            Trade.amount,
            Trade.trade_start,
            Trade.trade_end,
            Trade.is_verified,
            Trade.source,
        ).filter(Trade.country_from == data["country_from"])

        if "trade_start" in data:
            tradesq = tradesq.filter(
                Trade.trade_start > parse_date(data["trade_start"]))

        if "trade_end" in data:
            tradesq = tradesq.filter(
                Trade.trade_end < parse_date(data["trade_end"]))

        trades = tradesq.all()

        trades_struct = [
            {
                "country_from": trade[0],
                "country_to":   trade[1],
                "weapon_name":  trade[2],
                "amount":       trade[3],
                "trade_start":  datetime.strftime(trade[4], "%Y-%m-%d"),
                "trade_end":    datetime.strftime(trade[5], "%Y-%m-%d"),
                "is_verified":  trade[6],
                "source":       trade[7],
            }
            for trade in trades
        ]

        return json.dumps(trades_struct)

    return "Expected JSON"


@app.route('/api/generate', methods=['POST'])
def generate():
    #{full_name:..., email:...}
    if request.is_json:
        data = request.get_json()
        new_key = Api(data['email'], data['full_name'])
        db.session.add(new_key)
        db.session.commit()
        return new_key.key
    return "Expected JSON"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1234)
