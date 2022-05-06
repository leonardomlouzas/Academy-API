import re
from dataclasses import dataclass

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import backref, relationship, validates
from sqlalchemy.orm.session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from app.configs.database import db
from app.exception.cpf_error_exc import CPFError
from app.exception.id_not_existent_exc import IDNotExistent
from app.exception.password_error_exc import PasswordError


@dataclass
class PersonalModel(db.Model):
    id: int
    nome: str
    email: str
    cpf: str
    alunos: list

    __tablename__ = "personal"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    cpf = Column(String, nullable=False, unique=True)
    senha_hash = Column(String, nullable=False)

    alunos = relationship(
        "AlunoModel", backref=backref("personal", uselist=True), uselist=True
    )

    personal = db.relationship("TreinoModel", backref="personal")

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.senha_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.senha_hash, password_to_compare)

    @validates("cpf")
    def validate_fields(self, key, value):
        if key == "cpf":
            pattern = "\d{3}\.\d{3}\.\d{3}\-\d{2}"
            response = re.fullmatch(pattern, value)
            if not response:
                raise CPFError
            return value

    def verify_password(payload):
        pattern = "(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$*&@#])[0-9a-zA-Z$*&@#]{8,}"
        response = re.fullmatch(pattern, payload["senha"])
        if not response:
            raise PasswordError

    @classmethod
    def add_personal(cls, payload: dict):
        session: Session = db.session()
        session.add(payload)
        session.commit()

    @classmethod
    def read_personal(cls):
        session: Session = db.session()
        return session.query(cls).all()

    @classmethod
    def select_by_id(cls, id):
        session: Session = db.session()
        personal = session.query(cls).get(id)

        if not personal:
            raise IDNotExistent

        return personal

    @classmethod
    def validate_keys(cls, payload: dict, update=False):
        expect_keys = {"nome", "email", "cpf", "senha"}
        new_payload = {}

        for key, value in payload.items():
            if not key in expect_keys and update:
                raise KeyError
            elif key in expect_keys:
                new_payload[key] = value

        if not update:
            if len(new_payload) != 4:
                raise KeyError
            cls.verify_password(payload=new_payload)
            return new_payload

    @classmethod
    def update_personal(cls, personal_id, payload):
        cls.validate_keys(payload, update=True)

        personal = cls.select_by_id(personal_id)

        for key, value in payload.items():
            setattr(personal, key, value)

        cls.add_personal(personal)

        return personal

    @classmethod
    def delete(cls, personal_id: int):
        personal = cls.select_by_id(personal_id)

        session: Session = db.session()
        session.delete(personal)
        session.commit()
