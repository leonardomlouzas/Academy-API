from http import HTTPStatus
from app.configs.database import db
from app.exception.id_not_existent_exc import IDNotExistent
from app.exception.type_key_error_exc import TypeKeyError
from app.models.treino_model import TreinoModel
from app.models.personal_model import PersonalModel
from app.models.exercicio_model import ExercicioModel
from app.models.aluno_model import AlunoModel
from flask import jsonify, request
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session
from flask_jwt_extended import jwt_required


@jwt_required()
def create():
    data = request.get_json()

    try:
        TreinoModel.validates_fields(data)

        get_personal = data.pop('personal')
        get_aluno = data.pop('aluno')
        get_exercicios = data.pop('exercicios')
        data['personal_id'] = PersonalModel.query.filter_by(nome=get_personal).first_or_404().id
        data['aluno_id'] = AlunoModel.query.filter_by(nome=get_aluno).first_or_404().id

        training = TreinoModel(**data)

        for exercicio in get_exercicios:
            ex = ExercicioModel.query.filter_by(nome=exercicio).first_or_404()
            training.exercicios.append(ex)
        response = {
            "id": training.id,
            "nome": training.nome,
            "dia": training.dia,
            "personal": {
                "id": training.personal.id,
                "nome": training.personal.nome,
                "email": training.personal.email,
                "cpf": training.personal.cpf
                },
            "aluno": training.aluno,
            "exercicios": training.exercicios,
        }
        TreinoModel.add_training(training)

        return jsonify(response), HTTPStatus.CREATED
    except IntegrityError as error:
        if type(error.orig) == UniqueViolation:
            return {'msg': 'treino já existente'}, HTTPStatus.CONFLICT
    except TypeKeyError:
        return {'msg': 'É esperado que a chave seja uma string'}, HTTPStatus.CONFLICT
    except TypeError:
        return {'msg': 'Chaves nome, personal, aluno, dia e exercícios são obrigatórias'}




#@jwt_required()
def update(treino_id):
    data = request.get_json()
    try:
        training = TreinoModel.update_training(treino_id, data)
        response = {
            "id": training.id,
            "nome": training.nome,
            "dia": training.dia,
            "personal": {
                "id": training.personal.id,
                "nome": training.personal.nome,
                "email": training.personal.email,
                "cpf": training.personal.cpf
                },
            "aluno": training.aluno,
            "exercicios": training.exercicios,
        }
        return jsonify(response), HTTPStatus.OK
    except IDNotExistent:
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND


def access():
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
