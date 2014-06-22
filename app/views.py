from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
from models import Census
from flask import jsonify

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
    return render_template("index.html")

@app.route('/data', methods = ['GET', 'POST'])
@app.route('/data/<state>', methods = ['GET', 'POST'])
def data(state = None):
    if state:
        state_data = [rec.serialize(state.title())
                      for rec in db.session.\
                                     query(Census).\
                                     filter_by(
                                         state = state.title(),
                                     )]
    else:
        state_data = [rec.serialize()
                      for rec in db.session.query(Census).all()]
    return jsonify(result=state_data)
