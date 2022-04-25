from flask import Flask


def init_app(app: Flask):

    from .home_route import bp as bp_home

    app.register_blueprint(bp_home)
