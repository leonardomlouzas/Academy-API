from dataclasses import dataclass

from app.configs.database import db
from app.exception.id_not_existent_exc import IDNotExistent
from app.exception.key_not_found import KeyNotFound
from app.exception.type_error_exc import TypeNotAccepted
from app.models.personal_model import PersonalModel
from flask_jwt_extended import get_jwt_identity
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import validates
from sqlalchemy.orm.session import Session


@dataclass
class AlunoModel(db.Model):
    id: int
    nome: str
    telefone: str
    email: str
    peso: int
    altura: float
    imc: float
    treinos: list

    __tablename__ = "aluno"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    peso = Column(Integer)
    altura = Column(Float)
    imc = Column(Float)

    personal_id = db.Column(db.Integer, db.ForeignKey("personal.id"))

    treinos = db.relationship("TreinoModel", backref="aluno", uselist=True)

    @validates("nome", "telefone", "email", "peso", "altura")
    def validate(self, key, value):
        if type(value) != str and key in ["nome", "telefone", "email"]:
            raise TypeNotAccepted("Nome, telefone e email devem ser strings")
        if type(value) != float and key == "imc":
            raise TypeNotAccepted("Altura e imc devem ser float")
        return value

    @classmethod
    def validate_weight_height(cls, payload):
        if type(payload['peso']) != int:
            raise TypeNotAccepted("Peso deve ser um valor inteiro")
        if type(payload["altura"]) != float:
            raise TypeNotAccepted("Altura deve ser um valor float")

    @classmethod
    def validate_keys(cls, payload: dict, update=False):
        expect_keys = {"nome", "telefone", "email", "peso", "altura"}
        new_payload = {}

        for key, value in payload.items():
            if key not in expect_keys and update:
                raise KeyNotFound
            if key in expect_keys:
                new_payload[key] = value

        if not update:
            if len(new_payload) != 5:
                    raise KeyError("As chaves: nome, telefone, email, peso e altura são obrigatórias")
            cls.validate_weight_height(new_payload)

            return new_payload

    @classmethod
    def add_session(cls, payload):
        session: Session = db.session()
        session.add(payload)
        session.commit()

    @classmethod
    def select_by_id(cls, student_id):
        session: Session = db.session()
        student = session.query(cls).get(student_id)

        if not student:
            raise IDNotExistent

        return student
    
    @classmethod
    def update_student(cls, student_id, payload):
        student = cls.select_by_id(student_id)
        cls.validate_keys(payload, update=True)       
        

        for key, value in payload.items():
            setattr(student, key, value)

        cls.add_session(student)
        
        return student 

    @classmethod
    def select_training(cls, workouts):
        response_training = []
        for training in workouts:
            response = {
                "id": training.id,
                "nome": training.nome,
                "dia": training.dia,
                "exercicios": training.exercicios,
            }
            response_training.append(response)     

        return sorted(response_training, key=lambda response_training: response_training['id']) 
    

    @classmethod
    def delete_student(cls, student_id):
        student = cls.select_by_id(student_id)
        session: Session = db.session()
        session.delete(student)
        session.commit()

    @classmethod
    def response(cls, student):
        session: Session = db.session()     
        personal = session.query(PersonalModel).get(student.personal_id)
        workouts = cls.select_training(student.treinos)
        response = {
            "nome": student.nome,
            "telefone": student.telefone,
            "email":student.email,
            "peso": student.peso,
            "altura":student.altura,
            "imc": student.imc, 
            "personal":{
                "id": personal.id, 
                "nome": personal.nome,
                "cpf": personal.cpf,
            },
            "treinos": workouts                

        }

        return response

    @classmethod
    def caculation_of_imc_and_personal_id(cls, payload):
        new_payload = cls.validate_keys(payload)

        imc_response = new_payload["peso"] / (
            new_payload["altura"] * new_payload["altura"]
        )
        imc_formatted = float("%.2f" % round(imc_response, 2))
        new_payload["imc"] = imc_formatted

        token = get_jwt_identity()
        new_payload["personal_id"] = token["id"]

        return new_payload
