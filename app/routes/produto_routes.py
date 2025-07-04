from flask import Blueprint, request, jsonify
from app.application.services.produto_service import ProdutoService
from app.application.dtos.produto_dto import ProdutoDTO
from app.domain.core.result import Result
from app.routes.response_manager import manage_response

def create_produto_blueprint(produto_service: ProdutoService):
    bp = Blueprint("produtos", __name__)

    @bp.route("/", methods=["POST"])
    def salvar_produto():
        data = request.get_json()
        result = produto_service.salvar_produto(
            nome=data["nome"],
            descricao=data.get("descricao", ""),
            valor=data["valor"],
            quantidade_estoque=data["quantidade_estoque"],
            codigo_car=data.get("codigo_car")
        )

        if result.is_ok():
            dto = ProdutoDTO.from_entity(result.value())
            return manage_response(Result.Ok(dto.to_dict()), 201)

        return manage_response(result, 201)
        
    @bp.route("/", methods=["GET"])
    def listar_produtos():
        produtos = produto_service.listar_produtos()
        return jsonify([
            ProdutoDTO.from_entity(produto).to_dict()
            for produto in produtos
        ])

    return bp
