from typing import Dict
from models import Region
from utils.record_handler import Recorder
from ...country_controller import CountryController


def parse_full_region(region: Region) -> Dict:
    parsed_country = CountryController.parse_full(region.country)

    parsed_region = Recorder.parse(
        model_instance=region,
        include_fields=['id', 'name']
    )

    parsed_region['country'] = parsed_country

    return parsed_region
