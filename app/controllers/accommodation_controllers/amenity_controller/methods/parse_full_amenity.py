from typing import Type, Any, Dict

from utils.record_handler import Recorder
from ...amenity_category_controller import AmenityCategoryController


def parse_full_amenity(amenity: Type[Any]) -> Dict:
    parsed_category = AmenityCategoryController.parse_full(
        amenity.amenities_category
    )

    parsed_amenity = Recorder.parse(
        model_instance=amenity,
        include_fields=['id', 'name']
    )

    parsed_amenity['categorie'] = parsed_category

    return parsed_amenity
