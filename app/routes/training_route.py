from flask import Blueprint

from app.controllers import training_controller

bp = Blueprint("training", __name__, url_prefix="/training")

bp.post("")(training_controller.create)
bp.patch("/<training_id>")(training_controller.update)
bp.delete("/<training_id>")(training_controller.delete)
bp.get("/<training_id>")(training_controller.access_by_id)
bp.get("")(training_controller.access)
