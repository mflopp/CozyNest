from utils.error_handler import ValidationError
from utils.logs_handler import log_err, log_info


def validate_id(id_value: int) -> None:
    log_info('ID validation started')

    if not (isinstance(id_value, int) and id_value > 0):
        msg = 'ID must be positive integer'
        log_err(msg)
        raise ValidationError(msg)

    log_info('ID validation successfully finidhed')
