from typing import Dict, List


def extract_required_data(fields: List, data: Dict) -> Dict:

    return {field: data[field] for field in fields if field in data}
