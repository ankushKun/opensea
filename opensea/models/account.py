class Account:
    def __init__(self, json_data):
        """
        Put useful information from json_data into their own variables under Account class.

        :param json_data: json object returned by the opensea-api
        :type json_data: dict
        """
        # ACCOUNT DETAILS
        self.address = json_data["address"]
        self.profile_img_url = json_data["profile_img_url"]
        self.username = json_data["user"]["username"] if json_data["user"] else None
        self.config = json_data["config"]
