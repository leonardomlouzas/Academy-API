from http import HTTPStatus
from app.configs.database import db
from app.exception.exercise_error_exc import ExerciseError
from app.exception.id_not_existent_exc import IDNotExistent
from app.exception.type_error_exc import TypeNotAccepted
from app.exception.type_key_error_exc import TypeKeyError
from app.models.treino_model import TreinoModel
from app.models.personal_model import PersonalModel
from app.models.exercicio_model import ExercicioModel
from app.models.aluno_model import AlunoModel
from flask import jsonify, request, session
from sqlalchemy.orm.session import Session
from flask_jwt_extended import jwt_required


@jwt_required()
def create():
    data = request.get_json()
    try:
        TreinoModel.validates_fields(data)

        get_aluno = data.pop('email_aluno')
        get_exercicios = data.pop('exercicios')        
        
        data['personal_id'] = TreinoModel.select_personal().id
        data['aluno_id'] = TreinoModel.select_student(get_aluno).id

        training = TreinoModel(**data)
        
        for exercicio in get_exercicios:
            ex = TreinoModel.select_exercise(exercicio)
            training.exercicios.append(ex)
        
        TreinoModel.add_training(training)
        
        response = TreinoModel.response(training)

        return jsonify(response), HTTPStatus.CREATED
    except IDNotExistent as e:
        return {'msg': str(e)}, HTTPStatus.NOT_FOUND
    except ExerciseError as e:
        return {'msg': str(e)}, HTTPStatus.BAD_REQUEST
    except TypeNotAccepted as e:
        return {'msg': str(e)}, HTTPStatus.CONFLICT
    except KeyError:
        return {'msg': 'Chaves nome, email_aluno, dia e exercícios são obrigatórias'}, HTTPStatus.NOT_FOUND


@jwt_required()
def update(treino_id):
    data = request.get_json()
    try:
        training = TreinoModel.update_training(treino_id, data)
        response = TreinoModel.response(training)
        return jsonify(response), HTTPStatus.OK
    except IDNotExistent as e:
        return {'msg': str(e)}, HTTPStatus.NOT_FOUND
    except ExerciseError as e:
        return {'msg': str(e)}, HTTPStatus.BAD_REQUEST
    except TypeNotAccepted as e:
        return {'msg': str(e)}, HTTPStatus.CONFLICT


def access():
    session: Session = db.session()
    training = session.query(TreinoModel).all()
    return {"treinos": training}, HTTPStatus.OK


def access_by_id(treino_id):
    try:
        training = TreinoModel.select_by_id(treino_id)
        response = TreinoModel.response(training)
        return jsonify(response), HTTPStatus.OK
    except IDNotExistent:
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND


@jwt_required()
def delete(treino_id):
    try:
        TreinoModel.delete_training(treino_id)
        return "", HTTPStatus.NO_CONTENT
    except IDNotExistent:
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND
