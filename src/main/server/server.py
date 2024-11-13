from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler

from src.main.routes.pets_routes import pets_routes_bp
from src.main.routes.person_routes import person_routes_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(pets_routes_bp)
app.register_blueprint(person_routes_bp)
