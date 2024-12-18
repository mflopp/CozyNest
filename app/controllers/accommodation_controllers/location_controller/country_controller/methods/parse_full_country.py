from typing import Type, Any, Dict

from utils.record_handler import Recorder


def parse_full_country(country: Type[Any]) -> Dict:
    parsed_country = Recorder.parse(
        model_instance=country,
        include_fields=['id', 'name']
    )

    return parsed_country
