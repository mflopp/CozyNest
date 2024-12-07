from flask import Blueprint

# Create a blueprint for users CRUD
user_roles_bp = Blueprint('user_roles', __name__, url_prefix="/users/roles")
