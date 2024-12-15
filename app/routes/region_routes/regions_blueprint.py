from flask import Blueprint

# Create a blueprint for users CRUD
region_bp = Blueprint(
    name='location_region',
    import_name=__name__,
    url_prefix="/locations/regions"
)
