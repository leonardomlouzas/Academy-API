from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Float
from app.configs.database import db
from sqlalchemy.orm import validates
from app.exception.type_error_exc import TypeNotAccepted
from sqlalchemy.orm.session import Session
from app.exception.id_not_existent_exc import IDNotExistent


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
    imc = Column(Float)
    
    personal_id = db.Column(
      db.Integer, 
      db.ForeignKey('personal.id')
    )

    treinos = db.relationship("TreinoModel", backref="aluno",uselist=True)

    @validates("nome", "telefone", "email", "peso", "altura")
    def validate(self, key, value):
      
      if type(value) != str and key in ["nome", "telefone", "email"]:
        raise TypeNotAccepted("Nome, telefone e email devem ser strings")
      if type(value) != int and key == 'peso':
        raise TypeNotAccepted("Peso deve ser inteiro")
      if type(value) != float and key in ['altura', 'imc']:
        raise TypeNotAccepted("Altura e imc devem ser float")
      return value
      
    
    @classmethod
    def add_session(cls, payload):
        session: Session = db.session()
        session.add(payload)
        session.commit()
      
    @classmethod
    def select_by_id(cls, aluno_id):
        session: Session = db.session()
        aluno = session.query(cls).get(aluno_id)

        if not aluno:
            raise IDNotExistent

        return aluno
    
    @classmethod
    def update_aluno(cls, aluno_id, payload):
        aluno = cls.select_by_id(aluno_id)       
        
        
        for key, value in payload.items():
            setattr(aluno, key, value)

        cls.add_session(aluno)
        
        return aluno
    
    @classmethod
    def select_by_id(cls, aluno_id):
        session: Session = db.session()
        aluno = session.query(cls).get(aluno_id)

        if not aluno:
            raise IDNotExistent

        return aluno      
    
    @classmethod
    def delete_aluno(cls, aluno_id):
        aluno = cls.select_by_id(aluno_id)
        session: Session = db.session()
        session.delete(aluno)
        session.commit()
    
    