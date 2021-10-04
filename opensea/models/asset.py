from opensea.models.account import Account
from requests import request


class Asset:
    def __init__(self, json_data):
        """
        Put useful information from json_data into their own variables under Asset class.

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

        # OWNER DETAILS
        self.owner = Account(json_data["owner"])

        self.__ASSET_API_URL = f"https://api.opensea.io/api/v1/asset/{self.contract_address}/{self.token_id}"

    def get_json(self):
        response = request("GET", self.__ASSET_API_URL)
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
