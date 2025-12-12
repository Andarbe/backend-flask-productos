from src.core.db import db
from sqlalchemy import Column, Integer, String, ForeignKey

class ProductoBase(db.Model):
    __tablename__ = "productos_base"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120))
    descripcion = Column(String(500))
    tipo = Column(String(50))
    __mapper_args__ = {
        "polymorphic_on": tipo,
        "polymorphic_identity": "base"
    }

class ProductoElectronico(ProductoBase):
    __tablename__ = "productos_electronicos"
    id = Column(Integer, ForeignKey("productos_base.id"), primary_key=True)
    garantia_meses = Column(Integer)
    __mapper_args__ = {
        "polymorphic_identity": "electronico"
    }
