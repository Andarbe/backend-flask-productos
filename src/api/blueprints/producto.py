from flask_smorest import Blueprint
from src.schemas.producto_schema import ProductoSchema
from src.services.producto_service import ProductoService

bp = Blueprint("productos", __name__, url_prefix="/api/productos", description="Operaciones CRUD de productos")

@bp.route("/")
@bp.response(200, ProductoSchema(many=True))
def list_productos():
    from flask import request
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 20))
    return ProductoService.list(page, per_page)

@bp.route("/", methods=["POST"])
@bp.arguments(ProductoSchema)
@bp.response(201, ProductoSchema)
def create(producto_data):
    return ProductoService.create(producto_data)

@bp.route("/<int:id>")
@bp.response(200, ProductoSchema)
def get(id):
    return ProductoService.get(id)

@bp.route("/<int:id>", methods=["PUT"])
@bp.arguments(ProductoSchema)
@bp.response(200, ProductoSchema)
def update(data, id):
    return ProductoService.update(id, data)

@bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    ProductoService.delete(id)
    return {"message": "El producto ha sido eliminado"}, 200
