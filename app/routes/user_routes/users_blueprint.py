from flask import Blueprint

# Create a blueprint for users CRUD
users_bp = Blueprint('users', __name__, url_prefix="/users")
