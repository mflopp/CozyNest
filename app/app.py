from flask import Flask
import logging
from config import init_db, setup_logger, load_config
from routes import register_all_blueprints

# -- start app function
def start_app():
    app = Flask(__name__)
    try:

        init_db()
        setup_logger()

        # register_error_handlers(app)

        app.config.update(load_config())

        register_all_blueprints(app)
        
    except Exception as e:
        logging.critical(f"Failed at initialization: {str(e)}")

    # main
    @app.route('/', methods=["GET"])
    def index():
        return "Hello CozyNest!", 200

    # Catch-all route
    @app.route('/<path:path>', methods=["GET", "POST", "PUT", "DELETE"])
    def catch_all(path):
        return "Route not found", 404

    return app


if __name__ == '__main__':
    app = start_app()
    logging.info("Starting Flask app")
    app.run(debug=app.config["DEBUG"],
            port=app.config["PORT"],
            host=app.config["HOST"])
