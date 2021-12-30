from typing import Union, List
from requests.models import Response

from opensea.common import get_opensea_url
from opensea.models.collection_stats import CollectionStats


def get_collection_stats(
    collection: str
) -> Union[CollectionStats, Response]:
    """
    Retrieves NFT Collection Stats from opensea.io.

    :param collection: Collection from which we want to get stats
    :type collection: str
  
    """

    api_parameters = {
        "collection": collection,
    }

    response = get_opensea_url("collection", "stats", **api_parameters)
    if isinstance(response, dict):
        return CollectionStats(response)

    return response
