from typing import List, Union
from requests.models import Response

from opensea.common import get_opensea
from opensea.models.asset import Asset


def get_assets(
    owner: str = "",
    order_by: str = "pk",
    order_direction: str = "asc",
    limit: int = 10,
    offset: int = 0,
    verified_only: bool = False,
    collection: str = ""
) -> Union[List[Asset], Response]:
    """
    Retrieves NFT assets from opensea.io.

    :param owner: The address for the owner of the assets.
    :type owner: str

    :param order_by: By default, the API returns the fastest ordering (contract address and token id). Available options are 'token_id', 'sale_date', 'sale_count', 'sale_price'.
    :type order_by: str

    :param order_direction: Default is 'asc' for ascending, can be set 'desc' for descending.
    :type order_direction: str

    :param limit: Number of NFT assets to retrieve, cannot be more than 50 due to api limitations. 10 by default.
    :type limit: int

    :param offset: Number of NFT assets to skip. 0 by default.
    :type offset: int

    :param verified_only: Filters NFT assets that belong to a verified collection. False by default
    :type verified_only: bool
    
    :param collection: Filters NFT assets that belong to a specific collection.
    :type collection: str
    """

    api_parameters = {
        "owner": owner,
        "order_by": order_by,
        "order_direction": order_direction,
        "offset": offset,
        "limit": limit,
        "collection": collection
    }

    response = get_opensea("assets", **api_parameters)
    if isinstance(response, dict):
        assets = [Asset(i) for i in response["assets"]]
        if verified_only:
            assets = [i for i in assets if i.is_verified]

        return assets

    return response
