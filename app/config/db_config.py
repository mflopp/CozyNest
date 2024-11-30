import os
from dotenv import load_dotenv
from typing import List, Dict, Any
from utils.env_utils import check_env_variable


def load_config(var_names: List[str],
                defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Load configuration from environment variables with defaults.
    Args:
        var_names (List[str]): List of environment variable names to load.
        defaults (Dict[str, Any]): Default values for
        the environment variables.
    Returns:
        Dict[str, Any]: Loaded configuration.
    """
    load_dotenv()  # Load .env file into environment variables

    config = {}

    for var_name in var_names:
        check_env_variable(var_name)
        value = os.getenv(var_name, defaults.get(var_name))

        # Convert types based on defaults
        default_value = defaults.get(var_name)

        if isinstance(default_value, bool):
            value = value.lower() == "true" if value else default_value
        elif isinstance(default_value, int):
            try:
                value = int(value)  # type: ignore
            except (TypeError, ValueError):
                value = default_value

        config[var_name] = value

    return config


def get_connection_uri(config_data):
    user = config_data['DB_USER']
    password = config_data['DB_PASSWORD']
    db_name = config_data['DB_NAME']
    port = config_data['PORT']
    host = config_data['HOST']

    result_url = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'

    return result_url


default_values = {
    "SECRET_KEY": "default_secret",
    "PORT": 5000,
    "HOST": "0.0.0.0",
    "DB_NAME": "default_db",
    "DB_PASSWORD": "default_password",
    "DB_USER": "default_user",
    "CLIENT_URL": "*"
}

# Load configuration
config_data = load_config(list(default_values.keys()), default_values)

DB_URI = get_connection_uri(config_data)
