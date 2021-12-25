"""
File responsible for managing simple tasks as requests.
"""
from typing import Union
import requests
from requests.models import Response

import urllib.parse

def get_opensea_url(endpoint: str, endpoint_suffix, **kwargs) -> Union[dict, Response]:
    """Internal function for GETting opensea API endpoints using only url params"""

    url = f"https://api.opensea.io/api/v1/{endpoint}/parameter/{endpoint_suffix}"
    parameter = urllib.parse.quote_plus(list(kwargs.values())[0])
    url = url.replace("parameter", parameter)
    response = requests.get(url)

    # It is better to check the status code like this because you also check for status code 304...
    if response.ok:
        return response.json()

    return response
