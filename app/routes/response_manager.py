import uuid
from flask import jsonify
from app.application.dtos.error_response import ErrorResponse
from app.domain.core.result import BadRequestError, NotFoundError, AppError, Result

def manage_response(result: Result, success_status_code=200):
    trace_id = str(uuid.uuid4())

    if result.is_ok():
        value = result.value()
        return jsonify(value), success_status_code 

    error = result.error()

    # Padrão de erro com status e mensagem
    response = ErrorResponse(str(error), trace_id).to_dict()
   
    if isinstance(error, BadRequestError):
        return jsonify(response), 400
    elif isinstance(error, NotFoundError):
        return jsonify(response), 404
    else:
        return jsonify(response), 500
