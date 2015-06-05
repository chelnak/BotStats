import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask_googlelogin import GoogleLogin
from config import OPENID_TMP

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
googlelogin = GoogleLogin(app)

from app import views, models
