from flask import Blueprint

# Create a blueprint for users CRUD
user_settings_bp = Blueprint('user_settings', __name__, url_prefix="/users/settings")
