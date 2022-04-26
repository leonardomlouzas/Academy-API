from flask import Blueprint
from app.controllers import personal_controller


bp = Blueprint("personal", __name__, url_prefix="/personal")

bp.post("")(personal_controller.create_personal)