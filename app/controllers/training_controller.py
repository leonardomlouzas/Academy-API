from http import HTTPStatus
from app.configs.database import db
from app.exception.exercise_error_exc import ExerciseError
from app.exception.id_not_existent_exc import IDNotExistent
from app.exception.type_error_exc import TypeNotAccepted
from app.models.training_model import TreinoModel
from flask import jsonify, request
from sqlalchemy.orm.session import Session
from flask_jwt_extended import jwt_required


@jwt_required()
def create():
    data = request.get_json()
    try:
        TreinoModel.validates_fields(data)

        get_student = data.pop("email_aluno")
        get_exercises = data.pop("exercicios")

        data["personal_id"] = TreinoModel.select_personal().id
        data["aluno_id"] = TreinoModel.select_student(get_student).id

        training = TreinoModel(**data)

        for exercise in get_exercises:
            ex = TreinoModel.select_exercise(exercise)
            training.exercicios.append(ex)

        TreinoModel.add_training(training)

        response = TreinoModel.response(training)

        return jsonify(response), HTTPStatus.CREATED
    except IDNotExistent as e:
        return {"msg": str(e)}, HTTPStatus.NOT_FOUND
    except ExerciseError as e:
        return {"msg": str(e)}, HTTPStatus.BAD_REQUEST
    except TypeNotAccepted as e:
        return {"msg": str(e)}, HTTPStatus.CONFLICT
    except KeyError:
        return {
            "msg": "Chaves nome, email_aluno, dia e exercícios são obrigatórias"
        }, HTTPStatus.NOT_FOUND


@jwt_required()
def update(training_id):
    data = request.get_json()
    try:
        training = TreinoModel.update_training(training_id, data)
        response = TreinoModel.response(training)
        return jsonify(response), HTTPStatus.OK
    except IDNotExistent as e:
        return {"msg": str(e)}, HTTPStatus.NOT_FOUND
    except ExerciseError as e:
        return {"msg": str(e)}, HTTPStatus.BAD_REQUEST
    except TypeNotAccepted as e:
        return {"msg": str(e)}, HTTPStatus.CONFLICT


def access():
    session: Session = db.session()
    workouts = []
    workouts_select = session.query(TreinoModel).all()
    for training in workouts_select:
        workouts.append(TreinoModel.response(training))
    return {"treinos": workouts}, HTTPStatus.OK


def access_by_id(training_id):
    try:
        training = TreinoModel.select_by_id(training_id)
        response = TreinoModel.response(training)
        return jsonify(response), HTTPStatus.OK
    except IDNotExistent:
        return {"msg": "Id não encontrado"}, HTTPStatus.NOT_FOUND


@jwt_required()
def delete(training_id):
    try:
        TreinoModel.delete_training(training_id)
        return "", HTTPStatus.NO_CONTENT
    except IDNotExistent:
        return {"msg": "Id não encontrado"}, HTTPStatus.NOT_FOUND
