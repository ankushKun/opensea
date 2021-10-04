# Opensea API

An API wrapper library for opensea api.

## Installation

```bash
pip3 install opensea
```

## Usage

Retrieving assets:

```python
from opensea import get_assets

# This will return a list of assets which you can iterate and get the needed data
asset_list = get_assets(limit=10, verified_only=False)

asset = asset_list[0] # Get the first asset obejct from the list

print(asset.name)
print(asset.description)
print(asset.asset_url)
print(asset.get_floor_price()) # Floor price of the collection
```

Retrieving bundles:

```python
from opensea import get_bundles

# This will return a list of assets which you can iterate and get the needed data
bundles_list = get_bundles(limit=10)

bundle = bundles_list[0] # Get the first asset obejct from the list

print(bundle.slug)
print(bundle.assets[0].name)
```
