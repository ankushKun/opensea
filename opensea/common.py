"""
File responsible for managing simple tasks as requests.
"""
from typing import Union
import requests
from requests.models import Response


def get_opensea(endpoint: str, **kwargs) -> Union[dict, Response]:
    """Internal function for GETting opensea API endpoints."""

    # Limiting "limit" parametar to 50
    if kwargs.get("limit"):
        kwargs["limit"] = 50 if kwargs["limit"] > 50 else kwargs["limit"]

    url = f"https://api.opensea.io/api/v1/{endpoint}"
    response = requests.get(url, params=kwargs)

    # It is better to check the status code like this because you also check for status code 304...
    if response.ok:
        return response.json()

    return response
