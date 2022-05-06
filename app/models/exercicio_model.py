from dataclasses import dataclass

from app.configs.database import db
from app.exception.id_not_existent_exc import IDNotExistent
from app.exception.key_not_found import KeyNotFound
from app.exception.type_error_exc import TypeNotAccepted
from app.models.equipment_model import EquipmentModel
from app.models.execucao_model import ExecucaoModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import validates, backref
from sqlalchemy.orm.session import Session

from .treino_exercicio_table import treino_exercicio


@dataclass
class ExercicioModel(db.Model):
    id: int
    nome: str
    estimulo: str
    execucao: ExecucaoModel
    aparelho: EquipmentModel

    __tablename__ = "exercicio"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False, unique=True)
    estimulo = Column(String)

    aparelho_id = Column(Integer, ForeignKey("equipment.id"))

    aparelho = db.relationship(
        "EquipmentModel", back_populates="exercicio", uselist=False
    )

    execucao = db.relationship(
        "ExecucaoModel", back_populates="exercicio", uselist=False
    )

    treino = db.relationship(
        "TreinoModel",
        secondary=treino_exercicio,
        backref=backref("exercicios", uselist=True),
        uselist=True,
    )

    @classmethod
    def validate_keys(cls, payload):
        for key, value in payload.items():
            if type(value) != str and key in {"nome", "estimulo", "carga", "aparelho"}:
                raise TypeNotAccepted(f"A chave {key} devem ser uma strings")
            if type(value) != int and key in {"series", "repeticoes"}:
                raise TypeNotAccepted(f"A chave {key} devem ser um inteiro")

    @classmethod
    def validates_fields(cls, payload, update=False):
        cls.validate_keys(payload)

        expect_keys = {"nome", "series", "repeticoes", "carga", "estimulo", "aparelho"}
        new_payload = {}
        for key, value in payload.items():
            if not key in expect_keys and update:
                raise KeyNotFound(f"{key} não encontrado(a)s")
            if key in expect_keys:
                new_payload[key] = value

        if not update:
            if len(new_payload) != 6:
                raise KeyError
            return new_payload

    @classmethod
    def add_session(cls, payload):
        session: Session = db.session()
        session.add(payload)
        session.commit()

    @classmethod
    def select_by_id(cls, exercise_id):
        session: Session = db.session()
        exercise = session.query(cls).get(exercise_id)

        if not exercise:
            raise IDNotExistent

        return exercise

    @classmethod
    def update_exercise(cls, exercise_id, payload):
        cls.validates_fields(payload, update=True)

        update_execucao = cls.select_by_id(exercise_id).execucao
        for key in payload.keys():
            if key in ["series", "repeticoes", "carga"]:
                setattr(update_execucao, key, payload[key])
        cls.add_session(update_execucao)

        if "aparelho" in payload.keys():
            aparelho_id = (
                EquipmentModel.query.filter_by(nome=payload.pop("aparelho"))
                .first_or_404()
                .id
            )
            payload["aparelho_id"] = aparelho_id

        exercise = cls.select_by_id(exercise_id)

        for key, value in payload.items():
            setattr(exercise, key, value)

        cls.add_session(exercise)

        return exercise

    @classmethod
    def delete_exercise(cls, exercise_id):
        session: Session = db.session()
        execucao = cls.select_by_id(exercise_id).execucao
        session.delete(execucao)
        session.commit()

        exercise = cls.select_by_id(exercise_id)
        session.delete(exercise)
        session.commit()
