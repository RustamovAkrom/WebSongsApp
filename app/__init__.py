from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from app.config import config_mapping

from dotenv import load_dotenv
load_dotenv()

import os


app = Flask(__name__)

#Configurations
app.config.from_object(config_mapping[os.getenv("FLASK_ENV")])
db = SQLAlchemy(app)
    
from .routers import main_dp
app.register_blueprint(main_dp)

#Creating database
with app.app_context():
    db.create_all()


