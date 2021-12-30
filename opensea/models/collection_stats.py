from opensea.models.account import Account
from requests import request


class CollectionStats:
    def __init__(self, json_data):
        """
        Put useful information from json_data into their own variables under CollectionStats class.

        :param json_data: json object returned by the opensea-api
        :type json_data: dict
        """
    
        self.total_supply = json_data["stats"]["total_supply"]
        self.count = json_data["stats"]["count"]
        self.num_owners = json_data["stats"]["num_owners"]
        self.one_day_volume = json_data["stats"]["one_day_volume"]
        self.seven_day_volume = json_data["stats"]["seven_day_volume"]
        self.total_volume = json_data["stats"]["total_volume"]
        self.total_sales = json_data["stats"]["total_sales"]
        self.average_price = json_data["stats"]["average_price"]
        self.floor_price = json_data["stats"]["floor_price"]

