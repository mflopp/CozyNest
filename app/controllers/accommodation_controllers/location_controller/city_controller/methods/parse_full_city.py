from typing import Type, Any, Dict

from utils.record_handler import Recorder
from ...region_controller import RegionController


def parse_full_city(city: Type[Any]) -> Dict:
    parsed_region = RegionController.parse_full(city.region)

    parsed_city = Recorder.parse(
        model_instance=city,
        include_fields=['id', 'name']
    )

    parsed_city['region'] = parsed_region

    return parsed_city
