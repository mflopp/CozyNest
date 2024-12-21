from typing import Type, Any, Dict

from utils.record_handler import Recorder


def parse_full_accommodation_type(accommodation_type: Type[Any]) -> Dict:
    parsed_accommodation_type = Recorder.parse(
        model_instance=accommodation_type,
        include_fields=['id', 'accommodation_type']
    )

    return parsed_accommodation_type
