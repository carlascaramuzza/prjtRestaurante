from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Response, request
import mysql.connector
import json
from config import DevelopmentConfig as dbConfig

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + dbConfig.MYSQL_USER + ':' + dbConfig.MYSQL_PASSWORD + '@' + dbConfig.MYSQL_HOST + '/' + dbConfig.MYSQL_DB


