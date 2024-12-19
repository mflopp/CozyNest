from utils.error_handler import (
    NoRecordsFound,
    ValidationError,
    HasChildError
)
from sqlalchemy.exc import SQLAlchemyError

from utils.logs_handler import log_err
from utils import create_response


def crud_exceptions_handler(ERR_MSG):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                log_err(f"Value {ERR_MSG}: {str(e)}")
                return create_response(data=[("error", str(e))], code=400)
            except NoRecordsFound as e:
                log_err(f"{ERR_MSG}: {str(e)}")
                return create_response(data=[("error", str(e))], code=404)
            except HasChildError as e:
                log_err(f"{ERR_MSG}: {str(e)}")
                return create_response(data=[("error", str(e))], code=409)
            except ValidationError as e:
                log_err(f'Validation {ERR_MSG}: {str(e)}')
                return create_response(data=[("error", str(e))], code=409)
            except SQLAlchemyError as e:
                log_err(f"Data Base {ERR_MSG}: {str(e)}")
                return create_response(data=[("error", str(e))], code=500)
            except Exception as e:
                log_err(f"Unexpected {ERR_MSG}: {str(e)}")
                return create_response(
                    data=[("error", "Fetching error")], code=500
                )
        return wrapper
    return decorator
