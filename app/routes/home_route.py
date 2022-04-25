from flask import Blueprint
from app.controllers.home_controller import say_hello

bp = Blueprint("home", __name__, url_prefix="")

bp.get("/")(say_hello)
