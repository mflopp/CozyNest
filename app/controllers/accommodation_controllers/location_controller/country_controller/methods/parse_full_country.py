from typing import Dict
from models import Country

from utils.record_handler import Recorder


def parse_full_country(country: Country) -> Dict:
    parsed_country = Recorder.parse(
        model_instance=country,
        include_fields=['id', 'name']
    )

    return parsed_country
