import uuid
from flask import jsonify
from app.application.dtos.error_response import ErrorResponse
from app.domain.core.result import BadRequestError, ForbiddenError, NotFoundError, AppError, Result, UnauthorizedError

def manage_response(result: Result, success_status_code=200):
    trace_id = str(uuid.uuid4())

    if result.is_ok():
        value = result.value()
        return jsonify(value), success_status_code 

    error = result.error()

    # Padrão de erro com status e mensagem
    response = ErrorResponse(str(error), trace_id).to_dict()
   
    return jsonify(response), _map_status(error)

def _map_status(error) -> int:
    if isinstance(error, BadRequestError):
        return 400
    if isinstance(error, UnauthorizedError):  # ✅ Adicione esta linha
        return 401
    if isinstance(error, ForbiddenError):
        return 403
    if isinstance(error, NotFoundError):
        return 404
    return 500