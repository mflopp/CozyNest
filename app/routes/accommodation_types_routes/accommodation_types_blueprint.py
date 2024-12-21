from flask import Blueprint

# Create a blueprint for users CRUD
accommodation_types_bp = Blueprint(
    'accommodation_types', __name__, url_prefix="/accommodation/types"
)
