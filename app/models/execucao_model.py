from app.configs.database import db
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass

@dataclass
class ExercicioModel(db.Model):
    id: int
    series: int
    repeticoes: int
    carga: str

    __tablename__='execucao'

    id = Column(Integer, primary_key=True)
    series = Column(Integer)
    repeticoes = Column(Integer)
    carga = Column(String)

    exercicio_id = db.Column(
      db.Integer, 
      db.ForeignKey('exercicio.id'), 
      nullable=False,
      unique=True
    )

    exercicio = db.relationship(
      "ExercicioModel",
      backref=db.backref("execucao", uselist=False)
    )