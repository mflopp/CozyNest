from typing import Dict
from models import City
from utils.record_handler import Recorder
from ...region_controller import RegionController


def parse_full_city(city: City) -> Dict:
    parsed_region = RegionController.parse_full(city.region)

    parsed_city = Recorder.parse(
        model_instance=city,
        include_fields=['id', 'name']
    )

    parsed_city['region'] = parsed_region

    return parsed_city
