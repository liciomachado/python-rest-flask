from flask import Blueprint, request, jsonify
from app.application.services.produto_service import ProdutoService

def create_produto_blueprint(produto_service: ProdutoService):
    bp = Blueprint("produtos", __name__)

    @bp.route("/", methods=["POST"])
    def salvar_produto():
        data = request.get_json()
        produto = produto_service.salvar_produto(
            nome=data["nome"],
            descricao=data.get("descricao", ""),
            valor=data["valor"],
            quantidade_estoque=data["quantidade_estoque"]
        )
        return jsonify({
            "id": str(produto.id),
            "data_criacao": produto.data_criacao.isoformat(),
            "nome": produto.nome,
            "descricao": produto.descricao,
            "valor": produto.valor,
            "quantidade_estoque": produto.quantidade_estoque
        }), 201

    return bp
