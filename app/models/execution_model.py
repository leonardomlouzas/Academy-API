from app.configs.database import db
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass
from sqlalchemy.orm import validates
from app.exception.type_error_exc import TypeNotAccepted

@dataclass
class ExecucaoModel(db.Model):
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
      back_populates = "execucao", uselist=False
    )

    @validates("series", "repeticoes", "carga")
    def validate(self, key, value):
      if type(value) != str and key in ["carga"]:
        raise TypeNotAccepted("Carga deve ser string")
      if type(value) != int and key in ["series", "repeticoes"]:
        raise TypeNotAccepted("Series e repeticoes devem ser inteiros")
      return value