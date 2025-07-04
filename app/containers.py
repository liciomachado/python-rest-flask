from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import Config

# User
from app.adapters.repositories.user_repository_impl import UserRepository
from app.application.services.user_service import UserService
from app.routes.user_routes import create_user_blueprint

# Produto
from app.adapters.repositories.produto_repository_impl import ProdutoRepository
from app.application.services.produto_service import ProdutoService
from app.routes.produto_routes import create_produto_blueprint

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["app.routes"])

    # Database
    engine = providers.Singleton(create_engine, Config.DATABASE_URL)
    session_factory = providers.Singleton(sessionmaker, bind=engine)
    session = providers.Factory(lambda sf: sf(), session_factory)

    # User flow
    user_repository = providers.Factory(UserRepository)
    user_service = providers.Factory(UserService, repository=user_repository)
    user_blueprint = providers.Factory(create_user_blueprint, user_service=user_service)

    # Produto flow
    produto_repository = providers.Factory(ProdutoRepository, session=session)
    produto_service = providers.Factory(ProdutoService, repository=produto_repository)
    produto_blueprint = providers.Factory(create_produto_blueprint, produto_service=produto_service)
