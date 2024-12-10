import json
import logging
from flask import abort, Response
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Dict

from models import Gender
from controllers.controller_utils import Finder


def fetch_gender(id: int, session: Session) -> Dict:
    try:
        gender = Finder.fetch_record(session, Gender, 'id', id)

        # Use json.dumps to ensure order and return a Response
        response = Response(
            response=json.dumps(user_data, default=str),
            status=200,
            mimetype='application/json'
        )

        return response
    except SQLAlchemyError as e:
        logging.error(f"Database error: {e}")
        abort(500, description="Database error")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        abort(500, description="An unexpected error occurred")
