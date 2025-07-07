swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API Produtos",
        "description": "Documentação da API de Produtos",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": ["http", "https"],
    "definitions": {
        "Produto": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "data_criacao": {"type": "string"},
                "nome": {"type": "string"},
                "descricao": {"type": "string"},
                "valor": {"type": "number"},
                "quantidade_estoque": {"type": "integer"},
                "codigo_car": {"type": "string"}
            }
        }
    }
}
