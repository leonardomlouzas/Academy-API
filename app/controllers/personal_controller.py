from http import HTTPStatus
import re

from flask import jsonify, request
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError
from app.exception.validad_exc import InvalidCPFError, InvalidPasswordError

from app.models.personal_model import PersonalModel
from app.configs.database import db


def create_personal():
    data = request.get_json()
    new_data = {}
    
    expect_keys = {'nome', 'email', 'cpf', 'senha'}
    
    # Verifica se chaves obrigatorias existem
    receveid_keys = data.keys()
    for key in expect_keys:
        if not key in receveid_keys:
            return {'msg': '“As chaves: nome,  email, CPF e senha são obrigatórias'}, HTTPStatus.BAD_REQUEST
    
    # ignora chaves passadas a mais
    for key, value in data.items():
        if key in expect_keys:
            new_data[key] = value    
               
    try:
        # validação para senha
        pattern = '(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$*&@#])[0-9a-zA-Z$*&@#]{8,}'
        response = re.fullmatch(pattern, new_data["senha"])
        if not response:
            raise InvalidPasswordError
        
        password_to_hash = new_data.pop("senha")
    
        new_personal = PersonalModel(**new_data)

        new_personal.password = password_to_hash
        
        session: Session = db.session()
        session.add(new_personal)
        session.commit()
        
    except InvalidCPFError:
        return {'msg': "Formato do CPF inválido. Formatos válidos: 123.456.789-00 ou 12345678900"}, HTTPStatus.BAD_REQUEST
    except InvalidPasswordError:
        return {'msg': "Senha deve conter ao menos 8 caracterers, uma letra maiúscula, uma minúscula, um número e um caractere especial"}, HTTPStatus.BAD_REQUEST
    except IntegrityError as e:
        if f'{type(e.orig)}' == "<class 'psycopg2.errors.UniqueViolation'>":
            return {'msg': 'email ou CPF já existem'}, HTTPStatus.CONFLICT
    except TypeError:
        return {'msg': 'As chaves devem ser todas string'}, HTTPStatus.BAD_REQUEST

    
    
    return jsonify(new_personal), HTTPStatus.CREATED