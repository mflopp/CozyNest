from typing import Type, Any, Dict

from utils.record_handler import Recorder


def parse_full_amenity_category(pamenity_category: Type[Any]) -> Dict:
    parsed_pamenity_category = Recorder.parse(
        model_instance=pamenity_category,
        include_fields=['id', 'category']
    )

    return parsed_pamenity_category
