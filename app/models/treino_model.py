from dataclasses import dataclass
import re
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import validates
from app.configs.database import db
from sqlalchemy.orm import validates
from app.exception.exercise_error_exc import ExerciseError
from app.exception.id_not_existent_exc import IDNotExistent
from app.exception.key_not_found import KeyNotFound
from app.exception.type_error_exc import TypeNotAccepted
from sqlalchemy.orm.session import Session
# from sqlalchemy.orm.collections import InstrumentedList
from flask_jwt_extended import get_jwt_identity

import enum
from app.models.aluno_model import AlunoModel

from app.models.exercicio_model import ExercicioModel
from app.models.personal_model import PersonalModel


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
            raise TypeNotAccepted(f"A chave {key} deve ser uma strings")
        return value

    @classmethod
    def validates_keys(cls, payload):
        for key, value in payload.items():
            print(f'{value=}', type(value))
            if type(value) != str and key == "email_aluno":
              raise TypeNotAccepted(f"A chave email_aluno deve ser uma strings")
            elif type(value) != list and key == "exercicios":
              raise TypeNotAccepted(f"A chave exercicios deve ser um  list")
            elif not value in ["A", "B", "C", "D", "E", "F"] and key == "nome":
              raise TypeNotAccepted(f"Valor para nome inválido. Valores válidos: A, B, C, D, E e F")

    @classmethod
    def validates_fields(cls, payload, update=False):
        cls.validates_keys(payload)
        
        expect_keys = {"nome", "email_aluno", "dia", "exercicios"}
        new_payload = {}
        
        for key, value in payload.items():
            if not key in expect_keys and update:
              raise KeyNotFound(f'{key} não encontrada')
            if key in expect_keys:
                new_payload[key] = value
                
        if not update:
            if len(new_payload) != 4:
                raise KeyError
            return new_payload
           
        
    @classmethod
    def add_training(cls, payload):
      session: Session = db.session()
      session.add(payload)
      session.commit()

    @classmethod
    def select_personal(cls):
        current_personal = get_jwt_identity()
        return PersonalModel.query.filter_by(nome=current_personal['nome']).first()

    @classmethod
    def select_student(cls, email_aluno):
      aluno = AlunoModel.query.filter_by(email=email_aluno).first()

      if not aluno:
          raise IDNotExistent("Aluno não cadastrado")
        
      return aluno
    
    @classmethod
    def select_exercise(cls, exercises):
        ex = ExercicioModel.query.filter_by(nome=exercises).first()
        
        if not ex:
          raise ExerciseError(f"Exercísio {exercises} não cadastrado")
        
        return ex
    
    @classmethod
    def select_by_id(cls, training_id):
      session: Session = db.session()
      training = session.query(cls).get(training_id)

      if not training:
        raise IDNotExistent("Id não encontrado")

      return training
    
    @classmethod
    def response(cls, treino):
        session: Session = db.session()     
        personal = session.query(PersonalModel).get(treino.personal_id)
        aluno = session.query(AlunoModel).get(treino.aluno_id)
        response = {
            "id": treino.id,
            "nome": treino.nome,
            "dia": treino.dia,
            "personal": {
                "id": personal.id,
                "nome": personal.nome,
                "email": personal.email,
                "cpf": personal.cpf
                },
            "aluno": aluno,
            "exercicios": treino.exercicios,
        }
        return response

    @classmethod
    def update_training(cls, treino_id, payload):
        training = cls.select_by_id(treino_id)
        cls.validates_fields(payload, update=True)
          
        #Update Exercises
        if 'exercicios' in payload.keys():
            training.exercicios.clear()
            for exercicio in payload['exercicios']:
                ex = cls.select_exercise(exercicio)
                training.exercicios.append(ex)
            payload.pop('exercicios')
        #Update others keys
        if payload: 

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
