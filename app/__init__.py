from flask import Flask
from datetime import datetime



def create_app():
    app = Flask(__name__)

    # Importera och registrera blueprint
    from app.main import main_bp
    app.register_blueprint(main_bp)

    @app.context_processor
    def inject_globals():
        return {
            "current_year": datetime.now().year
        }

    return app
