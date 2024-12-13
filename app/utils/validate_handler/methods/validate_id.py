import logging
from utils.error_handler import ValidationError


def validate_id(id_value: int) -> None:
    logging.info('ID validation started')

    if not (isinstance(id_value, int) and id_value > 0):
        msg = 'ID must be positive integer'
        logging.info(msg)
        raise ValidationError(msg)

    logging.info('ID validation successfully finidhed')
