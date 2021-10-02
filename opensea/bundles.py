from typing import Union, List
from requests.models import Response

from opensea.common import get_opensea
from opensea.models.bundle import Bundle


def get_bundles(
    owner: str = "",
    limit: int = 10,
    offset: int = 0,
) -> Union[List[Bundle], Response]:
    """
    Retrieves NFT bundles from opensea.io.

    :param owner: The address for the owner of the assets.
    :type owner: str

    :param limit: Number of NFT assets to retrieve, cannot be more than 50 due to api limitations. 10 by default.
    :type limit: int

    :param offset: Number of NFT assets to skip. 0 by default.
    :type offset: int
    """

    api_parameters = {
        "owner": owner,
        "offset": offset,
        "limit": limit,
    }

    response = get_opensea("bundles", **api_parameters)
    if isinstance(response, dict):
        return [Bundle(i) for i in response["bundles"]]

    return response
