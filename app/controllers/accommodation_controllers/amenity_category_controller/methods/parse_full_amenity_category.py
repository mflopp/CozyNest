from typing import Type, Any, Dict

from utils.record_handler import Recorder


def parse_full_amenity_category(amenity_category: Type[Any]) -> Dict:
    parsed_amenity_category = Recorder.parse(
        model_instance=amenity_category,
        include_fields=['id', 'category']
    )

    return parsed_amenity_category
