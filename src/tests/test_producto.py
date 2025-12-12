from app import create_app
from src.core.db import db
import pytest

@pytest.fixture
def client():
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TESTING"] = True
    with app.test_client() as c:
        with app.app_context():
            db.create_all()
        yield c

def test_create_producto(client):
    resp = client.post("/api/productos/", json={
        "nombre": "Test",
        "descripcion": "Producto prueba",
        "precio": "10.50"
    })
    assert resp.status_code == 201
