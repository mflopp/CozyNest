from .country_routes import country_bp


def register_all_blueprints(app):
    app.register_blueprint(country_bp)
