from flask import render_template, request 
from sqlalchemy import select

from app import app
from ..db import Purchase, Session


@app.get("/result")
def result():
    with Session.begin() as session:
        purchases = session.execute(select(Purchase.name, Purchase.number, Purchase.amount, Purchase.cost)).all()
    
    results = [{'name': p[0], 'number': p[1], 'amount': p[2], 'cost': p[3]} for p in purchases]
    return render_template('result.html', purchases=results)