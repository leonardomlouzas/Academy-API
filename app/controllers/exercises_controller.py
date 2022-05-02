from http import HTTPStatus
from app.configs.database import db
from app.exception.id_not_existent_exc import IDNotExistent
from app.exception.type_key_error_exc import TypeKeyError
from app.models.exercicio_model import ExercicioModel
from flask import jsonify, request, session
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session
from flask_jwt_extended import jwt_required

@jwt_required()
def create_exercise():
    data = request.get_json

    try:
        ExercicioModel.validates_fields(data)
        exercise = ExercicioModel(**data)

        ExercicioModel.add_session(exercise)

        return jsonify(exercise), HTTPStatus.CREATED
    except IntegrityError as error:
        if type(error.orig) == UniqueViolation:
            return {'msg': 'exercício já existente'}, HTTPStatus.CONFLICT
    except TypeKeyError:
        return {'msg': 'É esperado que a chave "nome" seja uma string'}, HTTPStatus.CONFLICT
    except TypeError:
        return {'msg': 'Chaves nome, series, repetições, carga, estimulo e aparelho são obrigatórias'}, HTTPStatus.CONFLICT

@jwt_required()
def update(exercise_id):
    data = request.get_json()
    try:
        return jsonify(ExercicioModel.update_exercise(exercise_id, data)), HTTPStatus.OK
    except IDNotExistent:
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND

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
    return exercises, HTTPStatus.OK

def acess_by_id(exercise_id):
    try:
        return jsonify(ExercicioModel.select_by_id(exercise_id)), HTTPStatus.OK
    except IDNotExistent:
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND