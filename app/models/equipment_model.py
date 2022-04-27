from app.configs.database import db
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass

@dataclass
class EquipmentModel(db.Model):
    id: int
    nome: str
    codigo: int

    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    codigo = Column(Integer, nullable=False)
    