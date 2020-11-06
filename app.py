from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@206.81.24.72:1000/"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Trade(db.Model):
    __tablename__ = 'trades'

    id = db.Column(db.Integer, primary_key=True)
    country_from = db.Column(db.String())
    country_to = db.Column(db.String())
    thing = db.Column(db.String())
    amount = db.Column(db.Integer())
    trade_start = db.Column(db.Date())
    trade_end = db.Column(db.Date())

    def __init__(self, country_from, country_to, thing, amount, trade_start, trade_end): 
        self.country_from = country_from
        self.country_to = country_to
        self.thing = thing
        self.amount = amount
        self.trade_start = trade_start
        self.trade_end = trade_end

@app.route('/')
def index(): 
    if request.is_json: 
        data = request.get_json() 

        new_trade = Trade(country_from=data['country_from'], country_to=data['country_to'], thing=data['thing'], amount=data['amount'], trade_start=data['trade_start'], trade_end=data['trade_end'])

        db.session.add(new_trade)
        db.session.commit()

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1234)