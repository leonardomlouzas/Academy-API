from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.configs.database import db
from sqlalchemy.orm import validates
from app.exception.type_error_exc import TypeNotAccepted

@dataclass
class AlunoModel(db.Model):
    id: int
    nome: str
    telefone: str
    email: str
    peso: int
    altura: float
    imc: float

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

    @validates("nome", "telefone", "email", "peso", "altura")
    def valdate(self, key, value):
      
      if type(value) != str and key in ["nome", "telefone", "email"]:
        raise TypeNotAccepted("Nome, telefone e email devem ser strings")
      if type(value) != int and key == 'peso':
        raise TypeNotAccepted("Peso deve ser inteiro")
      if type(value) != float and key in ['altura', 'imc']:
        raise TypeNotAccepted("Altura e imc devem ser float")