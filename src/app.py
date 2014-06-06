from flask import Flask, render_template

from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient()
db = client.test
coll = db.census

app = Flask(__name__)

client = MongoClient()

@app.route('/')
def list():
    """
    """
    return ""

if __name__ == "__main__":
    app.run()
