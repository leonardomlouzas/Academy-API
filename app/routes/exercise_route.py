from flask import Blueprint
from app.controllers import exercises_controller

bp = Blueprint("exercise", __name__, url_prefix="/exercise")

bp.post("")(exercises_controller.create_exercise)
bp.patch("/<exercise_id>")(exercises_controller.update)
bp.delete("/<exercise_id>")(exercises_controller.delete)
bp.get("/<exercise_id>")(exercises_controller.acess_by_id)
bp.get("")(exercises_controller.acess)