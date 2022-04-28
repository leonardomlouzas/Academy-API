from flask import Blueprint, Flask

from .home_route import bp as bp_home
from .personal_route import bp as bp_personal


def init_app(app: Flask):
    app.register_blueprint(bp_home)
    app.register_blueprint(bp_personal)

