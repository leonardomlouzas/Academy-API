from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.configs.database import db
from sqlalchemy.orm import validates
from app.exception.type_error_exc import TypeNotAccepted
from .treino_exercicio_table import treino_exercicio


@dataclass
class ExercicioModel(db.Model):
    id: int
    nome: str
    estimulo: str

    __tablename__='exercicio'

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