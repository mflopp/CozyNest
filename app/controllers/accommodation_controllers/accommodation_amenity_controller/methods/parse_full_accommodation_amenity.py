from typing import Type, Any, Dict

from utils.record_handler import Recorder
from ...amenity_controller import AmenityController
# from ...accommodation_controller import AccommodationController


def parse_full_accommodation_amenity(accommodation_amenity: Type[Any]) -> Dict:
    parsed_amenity = AmenityController.parse_full(
        accommodation_amenity.amenity
    )
    # parsed_accommodation = accommodationController.parse_full(
    #     accommodation_amenity.accommodation
    # )

    parsed_accommodation_amenity = Recorder.parse(
        model_instance=accommodation_amenity,
        include_fields=['id']
    )

    parsed_accommodation_amenity['amenity_id'] = parsed_amenity
    # parsed_accommodation_amenity['accommodation_id'] = parsed_accommodation

    return parsed_accommodation_amenity
