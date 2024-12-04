import logging

# ANSI-code for colors
COLORS = {
    'DEBUG': "\033[36m",    # Cyan
    'INFO': "\033[32m",     # Green
    'WARNING': "\033[33m",  # Yellow
    'ERROR': "\033[31m",    # Red
    'CRITICAL': "\033[1;31m"    # Bold Red
}


class MultiColorFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        """Formats time in H:M:S"""
        return super().formatTime(record, datefmt=datefmt or "%H:%M:%S")

    def format(self, record):
        RESET = "\033[0m"

        level_color = COLORS.get(record.levelname, RESET)
        levelname = f"{level_color}{record.levelname}{RESET}"

        PURPLE = "\033[35m"
        asctime = f"{PURPLE}{self.formatTime(record)}{RESET}"

        message = record.getMessage()

        return f"{levelname} - {message} - {asctime}"


def setup_logger(log_level: int = logging.INFO) -> None:
    """
    Sets up basic logging configuration with multi-colored output.
    Args:
        log_level (int): The logging level (default: logging.INFO).
    """
    # Create handler
    console_handler = logging.StreamHandler()

    # Apply custom formatter
    formatter = MultiColorFormatter(datefmt="%H:%M:%S")
    console_handler.setFormatter(formatter)

    # Set logger
    logging.basicConfig(handlers=[console_handler], level=log_level)


# Пример использования
if __name__ == "__main__":
    setup_logger()
    logger = logging.getLogger(__name__)
    logger.debug("This is a DEBUG message")
    logger.info("This is an INFO message")
    logger.warning("This is a WARNING message")
    logger.error("This is an ERROR message")
    logger.critical("This is a CRITICAL message")
