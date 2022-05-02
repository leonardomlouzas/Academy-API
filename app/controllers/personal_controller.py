from http import HTTPStatus

from flask import jsonify, request
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

from app.configs.database import db
from app.exception.cpf_error_exc import CPFError
from app.exception.id_not_existent_exc import IDNotExistent
from app.exception.password_error_exc import PasswordError
from app.models.personal_model import PersonalModel


def signup():
    data = request.get_json()
    try:       
        new_data = PersonalModel.validate_keys(data)
               
        password_to_hash = new_data.pop("senha")
    
        new_personal = PersonalModel(**new_data)

        new_personal.password = password_to_hash
                
        PersonalModel.add_personal(new_personal)
        return jsonify(new_personal), HTTPStatus.CREATED
    except PasswordError:
        return {'msg': "Senha deve conter ao menos 8 caracterers, uma letra maiúscula, uma minúscula, um número e um caractere especial"}, HTTPStatus.BAD_REQUEST
    except CPFError:
        return {'msg': "Formato do CPF inválido. Formatos válidos: 123.456.789-00 ou 12345678900"}, HTTPStatus.BAD_REQUEST
    except IntegrityError as e:
        if type(e.orig) == UniqueViolation:
            return {'msg': 'email ou CPF já existem'}, HTTPStatus.CONFLICT
    except TypeError:
        return {'msg': 'As chaves devem ser todas string'}, HTTPStatus.BAD_REQUEST
    except KeyError:
        return {'msg': 'As chaves: nome,  email, CPF e senha são obrigatórias'}, HTTPStatus.NOT_FOUND
    

def signin():
    data = request.get_json()
    
    personal: PersonalModel = PersonalModel.query.filter_by(email=data['email']).first()
    
    if not personal or not personal.check_password(data['senha']):
        return {'msg': "email ou senha incorretos"}, HTTPStatus.NOT_FOUND
        
    return {"token": create_access_token(personal)}, HTTPStatus.OK

@jwt_required()
def update_personal():
    data = request.get_json() 
    current_personal = get_jwt_identity()
    
    try:
        return jsonify(PersonalModel.update_personal(current_personal['id'], data)), HTTPStatus.OK
    except IDNotExistent: 
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND
    except KeyError:
        return {'msg': 'A(s) chave(s) não foi encontrada'}, HTTPStatus.NOT_FOUND

@jwt_required()
def delete_personal():
    current_personal = get_jwt_identity()
    try:
        PersonalModel.delete(current_personal['id'])        
        return "", HTTPStatus.NO_CONTENT
    except IDNotExistent: 
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND
    

def retrieve_personal():    
    return {"personal": PersonalModel.read_personal()}, HTTPStatus.OK

@jwt_required()
def retrieve_personal_id():
    current_personal = get_jwt_identity()
    try:
        return jsonify(PersonalModel.select_by_id(current_personal['id'])), HTTPStatus.OK
    except IDNotExistent: 
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND
    
