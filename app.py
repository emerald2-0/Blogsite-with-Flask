#Main app is here
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

from config import Configuration #Import configuration

SQLALCHEMY_TRACK_MODIFICATIONS = True #I added to suppress the error >Depraciation Warning

app = Flask(__name__)
app.config.from_object(Configuration) #use values from the object
db = SQLAlchemy(app)