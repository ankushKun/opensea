import json
from requests import request


class SingleAsset:
    def __init__(self, json_data):
        """
        Put useful information from json_data into their own variables under SingleAsset class.

        :param json_data: json object returned by the opensea-api
        :type json_data: dict
        """
        # ASSET DETAILS
        self.name = json_data["name"]
        self.description = json_data["description"]
        self.token_id = json_data["token_id"]
        self.asset_url = json_data["permalink"]
        self.contract_address = json_data["asset_contract"]["address"]

        # COLLECTION DETAILS
        self.collection_name = json_data["collection"]["name"]
        self.collection_description = json_data["collection"]["description"]
        self.collection_slug = json_data["collection"]["slug"]
        self.verification_status = json_data["collection"]["safelist_request_status"]
        self.is_verified = json_data["collection"]["safelist_request_status"] == "verified"

        self.__SINGLE_ASSET_API_URL = f"https://api.opensea.io/api/v1/asset/{self.contract_address}/{self.token_id}"

    def get_json(self):
        response = request("GET", self.__SINGLE_ASSET_API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_floor_price(self):
        """
        Returns the floor price of the collection an asset belongs to
        """
        asset_json = self.get_json()
        floor_price = asset_json["collection"]["stats"]["floor_price"]
        return floor_price

    def get_current_price(self):
        asset_json = self.get_json()
        try:
            current_price = asset_json["orders"][0]["current_price"]
        except:
            current_price = None
        return current_price

    def get_average_price(self):
        asset_json = self.get_json()
        average_price = asset_json["collection"]["stats"]["average_price"]
        return average_price


class Assets():
    def __init__(self):
        self.__ASSETS_API_STRING = "https://api.opensea.io/api/v1/assets"

    def get_assets(self, owner: str = "", order_by: str = "pk", order_direction: str = "asc", limit: int = 10, verified_only: bool = False):
        #                                                  ^^
        # I dunno what this 'pk' stands for but I think its the default for fastest ordering
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

        :param verified_only: Filters NFT assets that belong to a verified collection. False by default
        :type verified_only: bool
        """

        if limit > 50:  # set virgin >50 to chad 50
            limit = 50

        api_parameters = {  # parameters needed by the api
            "owner": owner,
            "order_by": order_by,
            "order_direction": order_direction,
            "limit": limit,
        }
        response = request("GET", self.__ASSETS_API_STRING,
                           params=api_parameters)
        if response.status_code == 200:
            assets = []
            response = response.json()["assets"]

            # This function filters the verified assets from unverified ones if needed.
            if verified_only:
                response = list(filter(
                    lambda data: data["collection"]["safelist_request_status"] == "verified", response))

            # append asset data after organising it under SingleAsset class
            for idx in range(len(response)):
                assets.append(SingleAsset(response[idx]))
            return assets
        else:
            return response
