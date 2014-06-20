from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
from models import Census
from flask import jsonify

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
    return "index placeholder"

@app.route('/data/<state>', methods = ['GET', 'POST'])
def data(state):
    return state
