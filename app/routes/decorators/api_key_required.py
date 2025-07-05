from functools import wraps
from flask import request
from app.domain.core.result import Result, UnauthorizedError
from app.routes.response_manager import manage_response
from app.application.services.apikey_service import ApiKeyService

def api_key_required(api_key_service: ApiKeyService):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            api_key = request.headers.get("X-API-Key")

            if not api_key:
                return manage_response(Result.Err(UnauthorizedError("API Key ausente")))

            result = api_key_service.validar_chave(api_key)

            if result.is_err():
                return manage_response(result)

            return fn(*args, **kwargs)

        return wrapper
    return decorator