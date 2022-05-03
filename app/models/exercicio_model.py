from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.configs.database import db
from sqlalchemy.orm import validates
from app.exception.id_not_existent_exc import IDNotExistent
from app.exception.type_error_exc import TypeNotAccepted
from .treino_exercicio_table import treino_exercicio
from sqlalchemy.orm.session import Session


@dataclass
class ExercicioModel(db.Model):
    id: int
    nome: str
    estimulo: str

    __tablename__ = 'exercicio'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    estimulo = Column(String)

    aparelho_id = db.Column(
      db.Integer, 
      db.ForeignKey('equipment.id')
    )

    treino = db.relationship(
      "TreinoModel",
      secondary=treino_exercicio,
      backref="exercicios"
    )

    @validates("nome", "estimulo")
    def validate(self, key, value):
      if type(value) != str:
        raise TypeNotAccepted("As chaves passadas devem ser strings")

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
      exercise = cls.select_by_id(exercise_id)

      cls.validates_fields(payload)

      for key,value in payload.items():
        setattr(exercise, key, value)

      cls.add_session(exercise)

      return exercise

    @classmethod
    def delete_exercise(cls, exercise_id):
      exercise = cls.select_by_id(exercise_id)
      session: Session = db.session()
      session.delete(exercise)
      session.commit()
