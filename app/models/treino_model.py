from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import validates
from app.configs.database import db
from sqlalchemy.orm import validates
from app.exception.id_not_existent_exc import IDNotExistent
from app.exception.type_error_exc import TypeNotAccepted
from sqlalchemy.orm.session import Session
import enum

from app.models.exercicio_model import ExercicioModel


class EnumTreinoName(str, enum.Enum):

    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"



@dataclass
class TreinoModel(db.Model):
    id: int
    nome: str
    dia: str

    __tablename__ = 'treino'

    id = Column(Integer, primary_key=True)
    nome = Column(Enum(EnumTreinoName), nullable=False)
    dia = Column(String, nullable=False)

    personal_id = db.Column(
      db.Integer,
      db.ForeignKey('personal.id')
    )

    aluno_id = db.Column(
      db.Integer,
      db.ForeignKey('aluno.id')
    )

    @validates("nome", "dia")
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
    def add_training(cls, payload):
      session: Session = db.session()
      session.add(payload)
      session.commit()

    @classmethod
    def select_by_id(cls, training_id):
      session: Session = db.session()
      training = session.query(cls).get(training_id)

      if not training:
        raise IDNotExistent

      return training

    @classmethod
    def update_training(cls, treino_id, payload):
      training = cls.select_by_id(treino_id)
      
      #Update Exercises
      if 'exercicios' in payload.keys():
        training.exercicios.clear()
        for exercicio in payload['exercicios']:
          ex = ExercicioModel.query.filter_by(nome=exercicio).first_or_404()
          training.exercicios.append(ex)
        payload.pop('exercicios')
      #Update others keys
      if payload: 
        cls.validates_fields(payload)

        for key, value in payload.items():
          setattr(training, key, value)

        cls.add_training(training)

      return training

    @classmethod
    def delete_training(cls, training_id):
      training = cls.select_by_id(training_id)
      session: Session = db.session()
      session.delete(training)
      session.commit()
