from typing import Type, Any, Dict

from utils.record_handler import Recorder
from ...country_controller import CountryController


def parse_full_region(region: Type[Any]) -> Dict:
    parsed_country = CountryController.parse_full(region.country)

    parsed_region = Recorder.parse(
        model_instance=region,
        include_fields=['id', 'name']
    )

    parsed_region['country'] = parsed_country

    return parsed_region
