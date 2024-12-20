from flask import Blueprint

# Create a blueprint for users CRUD
accommodation_amenities_bp = Blueprint(
    'accommodation_amenities', __name__, url_prefix="/amenities/accommodation"
)
