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
    def validate_peso_altura(cls, payload):
        if type(payload["peso"]) != int:
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
                raise KeyError(
                    "As chaves: nome, telefone, email, peso e altura são obrigatórias"
                )
            cls.validate_peso_altura(new_payload)
            return new_payload

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
        cls.validate_keys(payload, update=True)

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
    def select_treino(cls, treinos):
        response_treino = []
        for treino in treinos:
            response = {
                "id": treino.id,
                "nome": treino.nome,
                "dia": treino.dia,
                "exercicios": treino.exercicios,
            }
            response_treino.append(response)

        return sorted(
            response_treino, key=lambda response_treino: response_treino["id"]
        )

    @classmethod
    def delete_aluno(cls, aluno_id):
        aluno = cls.select_by_id(aluno_id)
        session: Session = db.session()
        session.delete(aluno)
        session.commit()

    @classmethod
    def response(cls, aluno):
        session: Session = db.session()
        personal = session.query(PersonalModel).get(aluno.personal_id)
        treinos = cls.select_treino(aluno.treinos)
        response = {
            "id": aluno.id,
            "nome": aluno.nome,
            "telefone": aluno.telefone,
            "email": aluno.email,
            "peso": aluno.peso,
            "altura": aluno.altura,
            "imc": aluno.imc,
            "personal": {
                "id": personal.id,
                "nome": personal.nome,
                "cpf": personal.cpf,
            },
            "treinos": treinos,
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
