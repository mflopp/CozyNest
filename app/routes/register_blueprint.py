from .country_routes import country_bp
from .user_settings_routes import user_settings_bp
from .gender_routes import genders_bp
from .user_roles_routes import user_roles_bp


def register_all_blueprints(app):
    app.register_blueprint(country_bp)
    app.register_blueprint(user_settings_bp)
    app.register_blueprint(genders_bp)
    app.register_blueprint(user_roles_bp)
