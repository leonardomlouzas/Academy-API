from flask import Blueprint

from app.controllers import students_controller

bp = Blueprint("students", __name__, url_prefix="/student")

bp.post("")(students_controller.create_aluno)
bp.get("/")(students_controller.retrieve)
bp.get("/<students_id>")(students_controller.retrieve_by_id)
bp.delete("/<students_id>")(students_controller.delete_by_id)
bp.patch("/<students_id>")(students_controller.update_by_id)
