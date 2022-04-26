import re
from dataclasses import dataclass

from app.configs.database import db
from app.exception.validad_exc import InvalidCPFError, InvalidPasswordError
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from werkzeug.security import check_password_hash, generate_password_hash


@dataclass
class PersonalModel(db.Model):
    id: int
    nome: str
    email: str
    cpf: str
    
    __tablename__ = 'personal'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    cpf = Column(String, nullable=False, unique=True)
    senha_hash= Column (String, nullable=False)
    
    
    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")
    
    @password.setter
    def password(self, password_to_hash):
        self.senha_hash = generate_password_hash(password_to_hash)
        
    def verify_password(self, password_to_compare):
        return check_password_hash(self.senha_hash, password_to_compare)
    
    @validates("cpf")
    def validate_fields(self, key, value):
        if key == 'cpf':
            pattern = "\d{3}\.\d{3}\.\d{3}\-\d{2}"
            response = re.fullmatch(pattern, value)
            if not response:
                raise InvalidCPFError
            return value
        

        
        