from app.configs.database import db
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass

@dataclass
class ExercicioModel(db.Model):
    id: int
    nome: str
    series: int
    repeticoes: int
    carga: str
    estimulo: str

    __tablename__='exercicios'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    series = Column(Integer)
    repeticoes = Column(Integer)
    carga = Column(String)
    estimulo = Column(String)

    aparelho_id = db.Column(
      db.Integer, 
      db.ForeignKey('aparelho.id')
    )