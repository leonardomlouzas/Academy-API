from flask import Blueprint

from app.controllers import treino_controller

bp = Blueprint("training", __name__, url_prefix="/training")

bp.post("")(treino_controller.create)
bp.patch("/<training_id>")(treino_controller.update)
bp.delete("/<training_id>")(treino_controller.delete)
bp.get("/<training_id>")(treino_controller.access_by_id)
bp.get("")(treino_controller.access)
