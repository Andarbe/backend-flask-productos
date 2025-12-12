from flask import Flask
from config import Config
from src.core.db import init_db, db
from flask_migrate import Migrate
from flask_smorest import Api
from src.core.errors import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_db(app)
    Migrate(app, db)
    api = Api(app)
    from src.api.blueprints.producto import bp as producto_bp
    api.register_blueprint(producto_bp)
    register_error_handlers(app)
    @app.route("/health")
    def health():
        return {"status": "ok"}
    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)
