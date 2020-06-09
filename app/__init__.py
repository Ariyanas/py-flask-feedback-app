from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initiating app
app = Flask(__name__)

# Database
app.config.from_object('config')

# Initialize DB
db = SQLAlchemy(app)

# Initialize marshmallow
ma = Marshmallow(app)

# Routes, Models & Schema registration
# from . import routes, schemas, models

# HTTP Error Handling
@app.errorhandler(404) 
def not_found(error):
    return render_template('404.html')

@app.errorhandler(500) 
def server_error(error):
    return render_template('500.html')


# Build the DB
# db.create_all()