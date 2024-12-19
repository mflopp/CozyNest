from flask import Blueprint

# Create a blueprint for users CRUD
amenities_bp = Blueprint(
    'amenities', __name__, url_prefix="/amenities"
)
