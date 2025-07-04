from dependency_injector import containers, providers

from app.adapters.repositories.user_repository_impl import UserRepository
from app.application.services.user_service import UserService
from app.routes.user_routes import create_user_blueprint

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["app.routes"])

    # Repositórios (adapters)
    user_repository = providers.Factory(UserRepository)

    # Serviços (casos de uso)
    user_service = providers.Factory(
        UserService,
        repository=user_repository
    )

    # Rotas
    user_blueprint = providers.Factory(
        create_user_blueprint,
        user_service=user_service
    )
