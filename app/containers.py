from app.adapters.event_bus.rabbitmq_event_bus import RabbitMQEventBus
from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import Config

from app.adapters.clients.car_function_client_impl import CarFunctionClient
# User
from app.adapters.repositories.user_repository_impl import UserRepository
from app.application.services.user_service import UserService
from app.routes.user_routes import create_user_blueprint

# Produto
from app.adapters.repositories.produto_repository_impl import ProdutoRepository
from app.application.services.produto_service import ProdutoService
from app.routes.produto_routes import create_produto_blueprint

# API Key flow
from app.adapters.repositories.api_client_repository_impl import ApiClientRepository
from app.application.services.apikey_service import ApiKeyService

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["app.routes"])

    # Database
    engine = providers.Singleton(create_engine, Config.DATABASE_URL)
    session_factory = providers.Singleton(sessionmaker, bind=engine)
    session = providers.Factory(lambda sf: sf(), session_factory)

    car_function_client = providers.Singleton(
        CarFunctionClient,
        api_key=Config.CAR_FUNCTION_API_KEY
    )

    event_bus = providers.Singleton(
        RabbitMQEventBus,
        host=Config.RABBITMQ_HOST,
        username=Config.RABBITMQ_USER,
        password=Config.RABBITMQ_PASSWORD
    )

    # User flow
    user_repository = providers.Factory(UserRepository)
    user_service = providers.Factory(UserService, repository=user_repository)
    user_blueprint = providers.Factory(create_user_blueprint, user_service=user_service)

    # API Key flow
    api_client_repository = providers.Factory(
        ApiClientRepository,
        session_factory=session_factory
    )
    api_key_service = providers.Factory(ApiKeyService,repository=api_client_repository)

    # Produto flow
    produto_repository = providers.Factory(ProdutoRepository, session=session)
    produto_service = providers.Factory(
        ProdutoService,
        repository=produto_repository,
        car_function_client=car_function_client,
        event_bus=event_bus
    )
    produto_blueprint = providers.Factory(
        create_produto_blueprint, 
        produto_service=produto_service, 
        api_key_service=api_key_service
    )

  
