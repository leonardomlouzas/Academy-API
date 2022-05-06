from http import HTTPStatus
from app.exception.type_error_exc import TypeNotAccepted
from app.models.aluno_model import AlunoModel
from flask_jwt_extended import jwt_required
from flask import jsonify, request
from app.configs.database import db
from app.exception.id_not_existent_exc import IDNotExistent
from app.exception.key_not_found import KeyNotFound
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from sqlalchemy.orm.session import Session
from app.models.aluno_model import AlunoModel

@jwt_required()
def create_aluno():
        try:    
            data = request.get_json()
            data = AlunoModel.caculation_of_imc_and_personal_id(data)

            aluno = AlunoModel(**data)

            AlunoModel.add_session(aluno) 
            
            response = AlunoModel.response(aluno)
            
            return jsonify(response), HTTPStatus.CREATED
        except IntegrityError as e:
            if type(e.orig) == UniqueViolation:
                return {'msg': 'Email já existe'}, HTTPStatus.CONFLICT 
        except TypeNotAccepted as e:
            return {'msg': str(e)}, HTTPStatus.BAD_REQUEST
        except KeyError as e:
            return {'msg': str(e)}, HTTPStatus.BAD_REQUEST         

@jwt_required()
def update_by_id(aluno_id):
    data = request.get_json()
    try:
        return jsonify(AlunoModel.update_aluno(aluno_id, data)), HTTPStatus.OK
    except KeyNotFound:
        return {'msg': 'Chave não encontrada'}, HTTPStatus.NOT_FOUND 
    except IDNotExistent: 
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND

@jwt_required()
def retrieve():
      session: Session = db.session()
      alunos = session.query(AlunoModel).all()
      return {'count': len(alunos),'alunos': alunos}, HTTPStatus.OK

@jwt_required()
def retrieve_by_id(aluno_id): 
    try:
        aluno = AlunoModel.select_by_id(aluno_id)
        response = AlunoModel.response(aluno)
        return jsonify(response), HTTPStatus.OK
    except IDNotExistent: 
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND
      
@jwt_required()
def delete_by_id(aluno_id):
    try:
        AlunoModel.delete_aluno(aluno_id)
        return '',HTTPStatus.NO_CONTENT
    except IDNotExistent: 
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND
    
    