from flask import Blueprint

# Create a blueprint for users CRUD
country_bp = Blueprint('location_country', __name__, url_prefix="/locations/countries")
