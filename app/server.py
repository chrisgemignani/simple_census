from flask import Flask, render_template

from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient()
db = client.census
collection = db.collection

app = Flask(__name__)

client = MongoClient()

@app.route('/')
def list():
    coll = []
    for item in collection.find():
        return dumps(item)

if __name__ == "__main__":
    app.run()