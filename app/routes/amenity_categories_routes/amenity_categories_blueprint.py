from flask import Blueprint

# Create a blueprint for users CRUD
amenity_categories_bp = Blueprint(
    'amenity_categories', __name__, url_prefix="/amenities/categories"
)
