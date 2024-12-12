from typing import Dict, List


def fetch_relevant_values(fields: List, data: Dict) -> Dict:

    return {field: data[field] for field in fields if field in data}
