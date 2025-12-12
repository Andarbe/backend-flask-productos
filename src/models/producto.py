from src.core.db import db
from sqlalchemy import Column, Integer, String, Numeric

class Producto(db.Model):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False, unique=True)
    descripcion = Column(String(500))
    precio = Column(Numeric(12,2), nullable=False)
