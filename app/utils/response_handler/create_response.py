import json
from collections import OrderedDict
from flask import Response, make_response


def create_response(data, code) -> Response:
    response_data = OrderedDict(data)
    response_json = json.dumps(
        response_data,
        default=str,
        sort_keys=False
    )
    response = make_response(response_json, code)
    response.headers['Content-Type'] = 'application/json'

    return response
