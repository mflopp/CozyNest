from .country_routes import country_bp
from .user_settings_routes import user_settings_bp
from .gender_routes import genders_bp
from .user_roles_routes import user_roles_bp
from .user_info_routes import user_info_bp
from .user_routes import users_bp


def register_all_blueprints(app):
    app.register_blueprint(country_bp)
    app.register_blueprint(user_settings_bp)
    app.register_blueprint(genders_bp)
    app.register_blueprint(user_roles_bp)
    app.register_blueprint(user_info_bp)
    app.register_blueprint(users_bp)
