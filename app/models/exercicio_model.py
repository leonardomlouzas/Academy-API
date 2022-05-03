from dataclasses import dataclass
from sqlalchemy import Column, ForeignKey, Integer, String
from app.configs.database import db
from sqlalchemy.orm import validates
from app.exception.id_not_existent_exc import IDNotExistent
from app.exception.type_error_exc import TypeNotAccepted
from app.models.equipment_model import EquipmentModel
from app.models.execucao_model import ExecucaoModel
from .treino_exercicio_table import treino_exercicio
from sqlalchemy.orm.session import Session


@dataclass
class ExercicioModel(db.Model):
    id: int
    nome: str
    estimulo: str
    execucao: ExecucaoModel
    aparelho: EquipmentModel

    __tablename__ = 'exercicio'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    estimulo = Column(String)

    aparelho_id = Column(
      Integer, 
      ForeignKey('equipment.id')
    )

    aparelho = db.relationship(
      "EquipmentModel",
      back_populates = "exercicio", uselist=False
    )

    execucao = db.relationship(
      "ExecucaoModel",
      back_populates = "exercicio", uselist=False
    )

    treino = db.relationship(
      "TreinoModel",
      secondary=treino_exercicio,
      backref="exercicios",
      uselist=True
    )

    @validates("nome", "estimulo")
    def validate(self, key, value):
      if type(value) != str:
        raise TypeNotAccepted("As chaves passadas devem ser strings")
      return value

    @classmethod
    def validates_fields(cls, payload):
      for key, value in payload.items():
        if key == 'nome' and type(value) != str:
          raise TypeError

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
      #Update Execucao
      update_execucao = cls.select_by_id(exercise_id).execucao
      for key in payload.keys():
        if key in ['series', 'repeticoes', 'carga']:
          setattr(update_execucao, key, payload[key])
      cls.add_session(update_execucao)

      #Update Aparelho
      if 'aparelho' in payload.keys():
        aparelho_id = EquipmentModel.query.filter_by(nome=payload.pop('aparelho')).first_or_404().id
        payload['aparelho_id'] = aparelho_id

      exercise = cls.select_by_id(exercise_id)

      cls.validates_fields(payload)

      for key,value in payload.items():
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
