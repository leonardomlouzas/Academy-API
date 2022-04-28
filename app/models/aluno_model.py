from dataclasses import dataclass

from sqlalchemy import Column, Integer, String

from app.configs.database import db


@dataclass
class AlunoModel(db.Model):
    id: int
    nome: str
    telefone: str
    email: str
    peso: int
    altura: int
    imc: int

    __tablename__ = 'aluno'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    peso = Column(Integer)
    altura = Column(Integer)
    imc = Column(Integer)
    
    personal_id = db.Column(
      db.Integer, 
      db.ForeignKey('personal.id')
    )

    treinos = db.relationship("TreinoModel", backref="aluno",uselist=True)
