# app/__init__.py

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Create Flask app instance
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize Flask extensions
api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Import and register blueprints
from app.user.views import user_bp

app.register_blueprint(user_bp)
