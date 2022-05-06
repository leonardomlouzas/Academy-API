from flask import Flask
from flask_cors import CORS
from app import routes
from app.configs import database, jwt, migration


def create_app():
    app = Flask(__name__)
    app.config["CORS_HEADERS"] = "Content-Type"
    database.init_app(app)
    migration.init_app(app)
    CORS(app)
    jwt.init_app(app)
    routes.init_app(app)

    return app
