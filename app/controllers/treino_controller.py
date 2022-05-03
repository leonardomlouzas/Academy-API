from http import HTTPStatus
from app.configs.database import db
from app.exception.id_not_existent_exc import IDNotExistent
from app.exception.type_key_error_exc import TypeKeyError
from app.models.treino_model import TreinoModel
from flask import jsonify, request
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session
from flask_jwt_extended import jwt_required


jwt_required()
def create():
    data = request.get_json()

    try:
        TreinoModel.validates_fields(data)
        training = TreinoModel(**data)

        TreinoModel.add_training(training)

        return jsonify(training), HTTPStatus.CREATED
    except IntegrityError as error:
        if type(error.orig) == UniqueViolation:
            return {'msg': 'treino já existente'}, HTTPStatus.CONFLICT
    except TypeKeyError:
        return {'msg': 'É esperado que a chave seja uma string'}, HTTPStatus.CONFLICT
    except TypeError:
        return {'msg': 'Chaves nome, personal, aluno, dia e exercícios são obrigatórias'}


@jwt_required()
def update(training_id):
    data = request.get_json()
    try:
        return jsonify(TreinoModel.update_training(training_id, data)), HTTPStatus.OK
    except IDNotExistent:
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND


def get():
    session: Session = db.treino()
    training = session.query(TreinoModel).all()
    return training, HTTPStatus.OK


def access_by_id(training_id):
    try:
        return jsonify(TreinoModel.select_by_id(training_id)), HTTPStatus.OK
    except IDNotExistent:
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND


@jwt_required()
def delete(training_id):
    try:
        TreinoModel.delete_training(training_id)
        return "", HTTPStatus.NO_CONTENT
    except IDNotExistent:
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND
