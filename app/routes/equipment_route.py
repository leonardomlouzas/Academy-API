from flask import Blueprint
from app.controllers import equipment_controller

bp = Blueprint("equipment", __name__, url_prefix="/equipment")


bp.post("")(equipment_controller.create_equipment)
bp.patch("/<equipment_id>")(equipment_controller.update)
bp.delete("/<equipment_id>")(equipment_controller.delete)
bp.get("/<equipment_id>")(equipment_controller.retrieve_by_id)
bp.get("")(equipment_controller.retrieve)
