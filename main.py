from opensea import Assets

a = Assets()
asset_list = a.get_assets(limit=1, verified_only=True)

for asset in asset_list:
    details = f"""
CLASS : {type(asset)}
ASSET NAME : {asset.name}
DESCRIPTION : {asset.description}
ASSET URL : {asset.asset_url}
VERIFIED COLLECTION : {asset.is_verified}

CURRENT PRICE : {asset.get_current_price()}
FLOOR PRICE : {asset.get_floor_price()}
AVERAGE PRICE : {asset.get_average_price()}"""
    print(details)
