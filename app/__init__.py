import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.restless

app = Flask(__name__)
app.config.from_object('config')

#flask-sqlalchemy
db = SQLAlchemy(app)

from app import models, views
from app.models import Fact, Log

#API
manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Fact, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Log, methods=['GET', 'POST', 'PUT', 'DELETE'])

