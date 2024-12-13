from flask import Blueprint

# Create a blueprint for users CRUD
genders_bp = Blueprint(
    'genders', __name__, url_prefix="/users/genders"
)
