from .user_routes import *
from .register_blueprint import register_all_blueprints

__all__ = [
    *user_routes.__all__,
    'register_all_blueprints',
]
