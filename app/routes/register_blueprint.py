from .country_routes import country_bp
from .user_settings_routes import user_settings_bp


def register_all_blueprints(app):
    app.register_blueprint(country_bp)
    app.register_blueprint(user_settings_bp)
