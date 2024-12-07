from .user_routes import users_bp
from .user_settings_routes import user_settings_bp
from .user_roles_routes import user_roles_bp
from .user_info_routes import user_info_bp


def register_all_blueprints(app):
    # Register blueprints (routes)
    app.register_blueprint(users_bp)
    app.register_blueprint(user_settings_bp)
    app.register_blueprint(user_roles_bp)
    app.register_blueprint(user_info_bp)

    # for rule in app.url_map.iter_rules():
    #     print(f"Route: {rule} --> Endpoint: {rule.endpoint}, Methods: {rule.methods}")
