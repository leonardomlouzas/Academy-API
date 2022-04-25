from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

db = SQLAlchemy()


def init_app(app: Flask):

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = getenv("SECRET_KEY")

    db.init_app(app)
    app.db = db
