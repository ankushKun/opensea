from opensea.models.asset import Asset
from opensea.models.account import Account


class Bundle:
    def __init__(self, json_data):
        """
        Put useful information from json_data into their own variables under Bundle class.

        :param json_data: json object returned by the opensea-api
        :type json_data: dict
        """
        # BUNDLE DETAILS
        self.slug = json_data["slug"]

        # ASSETS
        self.assets = [Asset(i) for i in json_data["assets"]]

        # MAKER DETAILS
        self.maker = Account(json_data["maker"])
