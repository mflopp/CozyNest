from flask import Blueprint

# Create a blueprint for users CRUD
country_bp = Blueprint(
    name='location_country',
    import_name=__name__,
    url_prefix="/locations/countries"
)
