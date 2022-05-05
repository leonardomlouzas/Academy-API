from flask import Blueprint

from app.controllers import alunos_controller

bp = Blueprint("alunos", __name__, url_prefix="/alunos")

bp.post("")(alunos_controller.create_aluno)
bp.get("/")(alunos_controller.retrieve)
bp.get("/<aluno_id>")(alunos_controller.retrieve_by_id)
bp.delete("/<aluno_id>")(alunos_controller.delete_by_id)
bp.patch("/<aluno_id>")(alunos_controller.update_by_id)