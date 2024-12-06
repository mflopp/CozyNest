from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import logging
from flask import abort, Response
import json

from models.users import Gender
from controllers.controller_utils import fetch_record


def fetch_gender(id: int, session: Session) -> dict:
    try:
        gender = fetch_record(
            session=session,
            Model=Gender,
            criteria={'id': id},
            model_name='Gender'
        )

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
