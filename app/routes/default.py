from flask import render_template, request, redirect, url_for, flash
from app import app
from ..db import Purchase, Session  


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/")
def post_index():
    name = request.form.get("name")
    number = request.form.get("number")
    amount = request.form.get("amount")
    cost = int(amount) * 10
    with Session.begin() as session:
        register = Purchase(name=name, number=number, amount=amount, cost=cost)
        session.add(register)
        if name:
            return redirect(url_for("result"))
        else:
            flash("Something went wrong")
            return redirect(url_for('index'))
