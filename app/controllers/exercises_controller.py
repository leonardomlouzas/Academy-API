from http import HTTPStatus

from app.configs.database import db
from app.exception.equipment_error_exc import EquipmentError
from app.exception.id_not_existent_exc import IDNotExistent
from app.exception.key_not_found import KeyNotFound
from app.exception.type_error_exc import TypeNotAccepted
from app.models.equipment_model import EquipmentModel
from app.models.execution_model import ExecucaoModel
from app.models.exercise_model import ExercicioModel
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from sqlalchemy.orm.session import Session


@jwt_required()
def create_exercise():
    data = request.get_json()

    try:
        data = ExercicioModel.validates_fields(data)
        
        new_execution = {
            'series': data.pop('series'), 
            'repeticoes': data.pop('repeticoes'),
            'carga': data.pop('carga')  
        }
        get_equipment = data.pop('aparelho')
        data['aparelho_id'] = EquipmentModel.query.filter_by(nome=get_equipment).first_or_404().id
        exercise = ExercicioModel(**data)
        ExercicioModel.add_session(exercise)
        
        new_execution['exercicio_id'] = exercise.id
        post_execution = ExecucaoModel(**new_execution)
        ExercicioModel.add_session(post_execution)

        return jsonify(exercise), HTTPStatus.CREATED

    except TypeNotAccepted as e:
        return {'msg': str(e)}, HTTPStatus.CONFLICT
    except KeyError:
        return {'msg': 'Chaves nome, series, repetições, carga, estimulo e aparelho são obrigatórias'}, HTTPStatus.CONFLICT

@jwt_required()
def update(exercise_id):
    data = request.get_json()
    try:
        return jsonify(ExercicioModel.update_exercise(exercise_id, data)), HTTPStatus.OK
    except IDNotExistent:
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND
    except KeyNotFound as e:
        return {'msg': str(e)}, HTTPStatus.NOT_FOUND
    except TypeNotAccepted as e:
        return {'msg': str(e)}, HTTPStatus.CONFLICT
    except EquipmentError as e:
        return {'msg': str(e)}, HTTPStatus.BAD_REQUEST


@jwt_required()
def delete(exercise_id):
    try:
        ExercicioModel.delete_exercise(exercise_id)
        return "", HTTPStatus.NO_CONTENT
    except IDNotExistent:
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND

def acess():
    session: Session = db.session()
    exercises = session.query(ExercicioModel).all()
    return jsonify(exercises), HTTPStatus.OK

def acess_by_id(exercise_id):
    try:
        return jsonify(ExercicioModel.select_by_id(exercise_id)), HTTPStatus.OK
    except IDNotExistent:
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND
