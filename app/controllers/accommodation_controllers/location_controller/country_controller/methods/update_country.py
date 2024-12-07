from sqlalchemy.orm import Session
import logging
from models.addresses import Country
from controllers.controller_utils.validations import validate_data
from controllers.general_controllers import update_record
from ...utils import throw_error


def update_country(country_id: int, data: dict, session: Session) -> Country:
    """
    Updates an existing country record in the database.

    Args:
        country_id (int): ID of the country to update.
        data (dict): Data for updating the record. Expected key: "name".
        session (Session): SQLAlchemy session for database operations.

    Returns:
        Country: The updated country record.

    Raises:
        werkzeug.exceptions.HTTPException: If validation fails or the country is not found.
    """
    try:
        # Begin a nested transaction to handle potential rollback
        with session.begin_nested():
            # Fetch the existing country record
            country = session.query(Country).filter_by(id=country_id).first()
            if not country:
                throw_error(
                    code=404,
                    description=f"Country with ID {country_id} not found."
                )

            # Define fields for validation
            required_fields = ['name', 'id']
            unique_fields = ['name']

            # Validate the input data to ensure it meets the model requirements
            validate_data(
                session=session,
                Model=Country,
                data=data,
                required_fields=required_fields,
                unique_fields=unique_fields
            )

            # Update the fields of the country record
            for field, value in data.items():
                if hasattr(country, field):
                    setattr(country, field, value)

            # Attempt to update the record
            result, status_code = update_record(
                session=session,
                record=country,
                entity="Country"
            )

            # Log the successful update with the correct object reference
            if status_code == 200:
                logging.info(
                    f"Country with ID {country.id} successfully updated."
                )
                return country

            throw_error(
                code=500,
                description=f"Failed to update country with ID {country.id}."
            )
    except Exception as e:
        logging.error(f"Unexpected error during country update: {e}")
        throw_error(
            code=500,
            description="Unexpected error during country update. Check logs for details."
        )
