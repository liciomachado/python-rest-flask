from flask import Blueprint, request, jsonify
from app.application.services.apikey_service import ApiKeyService
from app.application.services.produto_service import ProdutoService
from app.application.dtos.produto_dto import ProdutoDTO
from app.domain.core.result import Result
from app.routes.decorators.api_key_required import api_key_required
from app.routes.response_manager import manage_response

def create_produto_blueprint(produto_service: ProdutoService, api_key_service: ApiKeyService):
    bp = Blueprint("produtos", __name__)

    @bp.route("/", methods=["POST"])
    @api_key_required(api_key_service)
    def salvar_produto():
        """
        Cria um novo produto
        ---
        tags:
          - Produtos
        parameters:
          - in: body
            name: body
            required: true
            schema:
              type: object
              properties:
                nome:
                  type: string
                descricao:
                  type: string
                valor:
                  type: number
                quantidade_estoque:
                  type: integer
                codigo_car:
                  type: string
        responses:
          201:
            description: Produto criado com sucesso
            schema:
              $ref: '#/definitions/Produto'
          400:
            description: Erro de validação
        security:
          - ApiKeyAuth: []
        """
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
        """
        Lista todos os produtos
        ---
        tags:
          - Produtos
        responses:
          200:
            description: Lista de produtos
            schema:
              type: array
              items:
                $ref: '#/definitions/Produto'
        """
        produtos = produto_service.listar_produtos()
        return jsonify([
            ProdutoDTO.from_entity(produto).to_dict()
            for produto in produtos
        ])

    return bp
