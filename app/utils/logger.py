import logging


def setup_logger(log_level: int = logging.INFO) -> None:
    """
    Sets up basic logging configuration.
    Args:
        log_level (int): The logging level (default: logging.INFO).
    """
    logger = logging.getLogger('werkzeug')
    logger.setLevel(logging.ERROR)
    logging.basicConfig(
        level=log_level,
        format="%(levelname)s - %(message)s - %(asctime)s",
        datefmt="%H:%M:%S"
    )
