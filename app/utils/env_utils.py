import os
import logging
from .logger import setup_logger

setup_logger()


def warning_msg(var_name: str) -> str:
    """
    Returns a warning message for missing environment variables.
    Args:
        var_name (str): The name of the missing environment variable.
    Returns:
        str: Warning message.
    """
    return f"{var_name} isn't found in the environment, using the default."


def check_env_variable(var_name: str, raise_exception: bool = False) -> None:
    """
    Checks for the presence of an environment variable and logs a warning
    if not found.
    Args:
        var_name (str): The name of the environment variable to check.
        raise_exception (bool): If True, raises an exception for missing
        variables.
    Raises:
        ValueError: If raise_exception is True and the variable is missing.
    """
    if not os.getenv(var_name):
        logging.warning(warning_msg(var_name))
        if raise_exception:
            raise ValueError(f"Environment variable {var_name} is missing!")
