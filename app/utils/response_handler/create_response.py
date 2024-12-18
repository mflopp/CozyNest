import json
from collections import OrderedDict
from flask import Response, make_response
from utils.logs_handler import log_info


def create_response(data, code) -> Response:
    log_info('Creating response started!')
    response_data = OrderedDict(data)
    response_json = json.dumps(
        response_data,
        default=str,
        sort_keys=False
    )
    response = make_response(response_json, code)
    response.headers['Content-Type'] = 'application/json'

    log_info(f'Response successfully created: {response}')
    return response
