from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://dvegrelc:PajpHIoBt0f6V09ZGawWXQJ2beaLa8Ka@surus.db.elephantsql.com/dvegrelc"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



@app.route('/')
def hello():
    return 'My First API !!'