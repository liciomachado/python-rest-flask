from flask import Flask
from app.config import Config
from app.containers import Container
from app.adapters.repositories.sqlalchemy_models import Base

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa o container
    container = Container()
    container.init_resources()
    container.wire(modules=[
        "app.routes.user_routes",
        "app.routes.produto_routes",
        "app.routes.decorators",
    ])

    # Criação de tabelas no banco de dados
    engine = container.engine()
    Base.metadata.create_all(engine)

    # Registra todos os blueprints
    user_bp = container.user_blueprint()
    produto_bp = container.produto_blueprint()

    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(produto_bp, url_prefix="/produtos")

    return app
