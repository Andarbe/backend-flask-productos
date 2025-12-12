from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.models.producto import Producto
from marshmallow import fields

class ProductoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Producto
        load_instance = True
        include_fk = True
    id = fields.Int(dump_only=True)
    precio = fields.Decimal(as_string=True)
