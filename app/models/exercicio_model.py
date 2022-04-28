from dataclasses import dataclass

from sqlalchemy import Column, Integer, String

from app.configs.database import db

from .treino_exercicio_table import treino_exercicio


@dataclass
class ExercicioModel(db.Model):
    id: int
    nome: str
    series: int
    repeticoes: int
    carga: str
    estimulo: str

    __tablename__='exercicio'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    series = Column(Integer)
    repeticoes = Column(Integer)
    carga = Column(String)
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