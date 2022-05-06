from http import HTTPStatus

from app.configs.database import db
from app.exception.id_not_existent_exc import IDNotExistent
from app.exception.type_key_error_exc import TypeKeyError
from app.models.equipment_model import EquipmentModel
from flask import jsonify, request
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session
from flask_jwt_extended import jwt_required


@jwt_required()
def create_equipment():
    data = request.get_json()
    
    try:
        EquipmentModel.validates_fields(data)
        equipment = EquipmentModel(**data)

        EquipmentModel.add_session(equipment)
        
        return jsonify(equipment), HTTPStatus.CREATED
    except IntegrityError as e:
        if type(e.orig) == UniqueViolation:
            return {'msg': 'Nome ou código já existente'}, HTTPStatus.CONFLICT
    except TypeKeyError:
        return {'msg': 'Tipos das chaves incorretos. Espera-se string para nome e inteiro para codigo'}, HTTPStatus.CONFLICT
    except TypeError:
        return {'msg': 'Chaves nome e codigo são obrigatórias'}, HTTPStatus.CONFLICT    
    
@jwt_required()   
def update(equipment_id):
    data = request.get_json()
    try:
        return jsonify(EquipmentModel.update_equipment(equipment_id, data)), HTTPStatus.OK
    except IDNotExistent: 
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND


@jwt_required()
def delete(equipment_id):
    try:
        EquipmentModel.delete_equipment(equipment_id)
        return "", HTTPStatus.NO_CONTENT
    except IDNotExistent: 
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND
    
def retrieve():
    session: Session = db.session()
    equipment = session.query(EquipmentModel).all()
    return {'countador': len(equipment),'equipmentos': equipment}, HTTPStatus.OK

def retrieve_by_id(equipment_id): 
    try: 
        return jsonify(EquipmentModel.select_by_id(equipment_id)), HTTPStatus.OK
    except IDNotExistent: 
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND
