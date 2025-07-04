from flask import Flask
from app.routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    app.register_blueprint(user_bp, url_prefix="/users")

    return app