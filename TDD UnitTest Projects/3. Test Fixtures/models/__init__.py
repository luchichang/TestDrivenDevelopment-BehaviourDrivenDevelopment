"""
  Data Model
"""

# file import
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# creating the Flask Application 
app = Flask(__name__)

# disabling the tracking option
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# setting the db URI to SQLite
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'

# creating the SQLAlchemy instance associated with Flask Application
# NOTE: this instance db is used to create database model and interact with databse throughout the application
db = SQLAlchemy(app)

