from flask import Blueprint, jsonify
from app.application.services.user_service import UserService

def create_user_blueprint(user_service: UserService):
    user_bp = Blueprint("users", __name__)

    @user_bp.route("/", methods=["GET"])
    def get_users():
        users = user_service.list_users()  # ✅ usa o objeto direto
        return jsonify([{"id": user.id, "name": user.name} for user in users])

    return user_bp
