from .user_routes import users_bp
from .user_settings_routes import user_settings_bp


def register_all_blueprints(app):
    # Register blueprints (routes)
    app.register_blueprint(users_bp)
    app.register_blueprint(user_settings_bp)

    # for rule in app.url_map.iter_rules():
    #     print(f"Route: {rule} --> Endpoint: {rule.endpoint}, Methods: {rule.methods}")
