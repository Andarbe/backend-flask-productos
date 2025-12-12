from src.repositories.producto_repo import ProductoRepo
from src.models.producto import Producto
from decimal import Decimal

class ProductoService:
    @staticmethod
    def list(page, per_page):
        offset = (page - 1) * per_page
        return ProductoRepo.all(offset=offset, limit=per_page)
    @staticmethod
    def get(id):
        prod = ProductoRepo.get(id)
        if not prod:
            raise ValueError("Producto no encontrado")
        return prod
    @staticmethod
    def create(data):
        if ProductoRepo.get_by_name(data["nombre"]):
            raise ValueError("Nombre ya existe")
        nuevo = Producto(
            nombre=data["nombre"],
            descripcion=data.get("descripcion"),
            precio=Decimal(str(data["precio"]))
        )
        return ProductoRepo.create(nuevo)
    @staticmethod
    def update(id, data):
        prod = ProductoRepo.get(id)
        if not prod:
            raise ValueError("Producto no encontrado")
        prod.nombre = data.get("nombre", prod.nombre)
        prod.descripcion = data.get("descripcion", prod.descripcion)
        if "precio" in data:
            prod.precio = Decimal(str(data["precio"]))
        ProductoRepo.update()
        return prod
    @staticmethod
    def delete(id):
        prod = ProductoRepo.get(id)
        if not prod:
            raise ValueError("Producto no encontrado")
        ProductoRepo.delete(prod)
