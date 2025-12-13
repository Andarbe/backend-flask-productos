# 🧱 API de Productos – Arquitectura de Aplicaciones Web (Flask + SQLAlchemy + Docker + Alembic)

Este proyecto implementa una API REST profesional para la gestión de productos, siguiendo principios modernos de arquitectura por capas, mapeo ORM, documentación OpenAPI y contenedorización con Docker.  
Fue desarrollado como parte de la asignatura **Arquitectura de Aplicaciones Web (Maestría)**.

---

## 🚀 Tecnologías utilizadas

| Componente | Herramienta |
|-----------|-------------|
| Framework | Flask |
| ORM | SQLAlchemy |
| Validación | Marshmallow |
| Migraciones | Alembic / Flask-Migrate |
| BD | PostgreSQL |
| Docs API | Flask-Smorest + OpenAPI 3 |
| Contenedores | Docker & docker-compose |
| Testing | Pytest |
| CI/CD | GitHub Actions |

---

## 📁 Arquitectura por capas

src/

├─ api/ → Rutas / Controladores (Flask Blueprints)

├─ services/ → Reglas de negocio

├─ repositories/ → Acceso a datos (DAO)

├─ models/ → Entidades del dominio (ORM)

├─ schemas/ → Validación / Serialización

├─ core/ → Configuración DB y errores

└─ tests/ → Pruebas unitarias


---

## 🔌 Endpoints principales

| Método | Ruta | Descripción |
|-------|------|-------------|
| GET | /api/productos/ | Lista productos |
| POST | /api/productos/ | Crea producto |
| GET | /api/productos/<id> | Obtiene producto |
| PUT | /api/productos/<id> | Actualiza |
| DELETE | /api/productos/<id> | Elimina |

---

## 📘 Documentación OpenAPI

Swagger UI disponible en:

👉 **http://localhost:5000/api/docs**

Spec JSON:

👉 **http://localhost:5000/api/openapi.json**

---

## 🐳 Ejecutar con Docker (recomendado)

### 1️⃣ Instalar Docker Desktop  
https://www.docker.com/products/docker-desktop/

### 2️⃣ Ejecutar:
```bash
docker-compose up --build


3️⃣ Acceder

API funcionando en:
👉 http://localhost:5000

Swagger:
👉 http://localhost:5000/api/docs

---------------
▶️ Ejecutar en local (sin Docker)

1️⃣ Crear entorno virtual
python -m venv venv
venv\Scripts\activate

2️⃣ Instalar dependencias
pip install -r requirements.txt

3️⃣ Crear base de datos PostgreSQL
CREATE DATABASE productos_db;

4️⃣ Aplicar migraciones
flask db init
flask db migrate -m "Inicial"
flask db upgrade

5️⃣ Ejecutar servidor
flask run

🧪 Ejecutar pruebas
pytest -q

###
🧱 Mapeo ORM → Base de datos

Ejemplo:
class Producto(db.Model):
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False, unique=True)
    descripcion = Column(String(500))
    precio = Column(Numeric(12,2), nullable=False)

Se convierte en:

Campo	Tipo SQL
id	SERIAL PK
nombre	VARCHAR(120) UNIQUE
descripcion	TEXT
precio	NUMERIC(12,2)

También se implementan modelos con herencia (Joined Table) como ejemplo de diseño avanzado.

✨ Autor

Andres Arbelaez – Ingeniero de Software
Maestría en Ingeniería de Software
2025