from flask import Blueprint, jsonify
from app.adapters.repositories.user_repository_impl import UserRepository
from app.application.services.user_service import UserService

user_bp = Blueprint("users", __name__)

repo = UserRepository()
service = UserService(repo)

@user_bp.route("/", methods=["GET"])
def get_users():
    users = service.list_users()
    return jsonify([{"id": user.id, "name": user.name} for user in users])
