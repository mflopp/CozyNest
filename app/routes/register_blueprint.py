from .user_routes import users_bp


def register_all_blueprints(app):
    # Register blueprints (routes)
    app.register_blueprint(users_bp)

    # for rule in app.url_map.iter_rules():
    #     print(f"Route: {rule} --> Endpoint: {rule.endpoint}, Methods: {rule.methods}")
