from src.core.db import db
from src.models.producto import Producto

class ProductoRepo:
    @staticmethod
    def all(offset=0, limit=20):
        return Producto.query.offset(offset).limit(limit).all()
    @staticmethod
    def get(id):
        return Producto.query.get(id)
    @staticmethod
    def get_by_name(name):
        return Producto.query.filter_by(nombre=name).first()
    @staticmethod
    def create(entity):
        db.session.add(entity)
        db.session.commit()
        return entity
    @staticmethod
    def update():
        db.session.commit()
    @staticmethod
    def delete(entity):
        db.session.delete(entity)
        db.session.commit()
