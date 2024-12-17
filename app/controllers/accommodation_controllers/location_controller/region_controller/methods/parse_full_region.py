from typing import Type, Any, Dict

from utils.record_handler import Recorder


def parse_full_region(region: Type[Any]) -> Dict:
    parsed_country = Recorder.parse(
        model_instance=region.country,
        include_fields=['id', 'name']
    )

    parsed_region = Recorder.parse(
        model_instance=region,
        include_fields=['id', 'name']
    )

    parsed_region['country'] = parsed_country

    return parsed_region
