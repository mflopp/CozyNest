from flask import Blueprint

# Create a blueprint for users CRUD
user_info_bp = Blueprint('user_info', __name__, url_prefix="/users/info")
