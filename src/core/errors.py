from werkzeug.exceptions import HTTPException
def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http(e):
        return {"error": e.name, "description": e.description}, e.code
    @app.errorhandler(Exception)
    def handle_general(e):
        return {"error": "Server Error", "description": str(e)}, 500
