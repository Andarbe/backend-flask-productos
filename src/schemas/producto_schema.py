from marshmallow import Schema, fields

class ProductoSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    descripcion = fields.Str()
    precio = fields.Decimal(required=True, as_string=True)
