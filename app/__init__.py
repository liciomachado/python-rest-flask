from flask import Flask
from app.config import Config
from app.containers import Container

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    container = Container()
    container.wire(modules=["app.routes.user_routes"])

    user_bp = container.user_blueprint()
    app.register_blueprint(user_bp, url_prefix="/users")

    return app
