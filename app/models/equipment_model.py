from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.session import Session
from app.exception.id_not_existent_exc import IDNotExistent

from app.exception.type_key_error_exc import TypeKeyError


@dataclass
class EquipmentModel(db.Model):
    id: int
    nome: str
    codigo: int

    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False, unique=True)
    codigo = Column(Integer, nullable=False)
    
    
    @classmethod
    def validates_fields(cls, payload):
        for key, value in payload.items():
            if key == 'nome' and type(value) != str or key == 'codigo' and type(value) != int :
                raise TypeKeyError
        
    @classmethod
    def add_session(cls, payload):
        session: Session = db.session()
        session.add(payload)
        session.commit()
        
    @classmethod
    def select_by_id(cls, equipment_id):
        session: Session = db.session()
        equipment = session.query(cls).get(equipment_id)

        if not equipment:
            raise IDNotExistent

        return equipment
    
    @classmethod
    def update_equipment(cls, equipment_id, payload):
        equipment = cls.select_by_id(equipment_id)
        
        cls.validates_fields(payload)
        
        for key, value in payload.items():
            setattr(equipment, key, value)

        cls.add_session(equipment)
        
        return equipment
    
    @classmethod
    def delete_equipment(cls, equipment_id):
        equipment = cls.select_by_id(equipment_id)
        session: Session = db.session()
        session.delete(equipment)
        session.commit()
