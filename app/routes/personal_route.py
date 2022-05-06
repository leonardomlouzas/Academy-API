from flask import Blueprint

from app.controllers import personal_controller

bp = Blueprint("personal", __name__, url_prefix="/personal")

bp.post("/signup")(personal_controller.signup)
bp.post("/signin")(personal_controller.signin)
bp.patch("")(personal_controller.update_personal)
bp.delete("")(personal_controller.delete_personal)
bp.get("")(personal_controller.retrieve_personal)
bp.get("/profile")(personal_controller.retrieve_personal_id)
