from flask import Flask, jsonify
from flask_marshmallow import  Marshmallow
from app import models
from app import api
from flask_cors import CORS
from app.services import user

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/db'
models.init_app(app)
api.init_app(app)
ma = Marshmallow(app)

