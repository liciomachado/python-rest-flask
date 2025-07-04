from flask import Blueprint, request, jsonify
from app.application.services.produto_service import ProdutoService
from app.application.dtos.produto_dto import ProdutoDTO

def create_produto_blueprint(produto_service: ProdutoService):
    bp = Blueprint("produtos", __name__)

    @bp.route("/", methods=["POST"])
    def salvar_produto():
        data = request.get_json()
        produto = produto_service.salvar_produto(
            nome=data["nome"],
            descricao=data.get("descricao", ""),
            valor=data["valor"],
            quantidade_estoque=data["quantidade_estoque"],
        )
        return jsonify(ProdutoDTO.from_entity(produto).to_dict()), 201

    @bp.route("/", methods=["GET"])
    def listar_produtos():
        produtos = produto_service.listar_produtos()
        return jsonify([
            ProdutoDTO.from_entity(produto).to_dict()
            for produto in produtos
        ])

    return bp
