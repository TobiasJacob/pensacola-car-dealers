#%%
import requests
from algoliasearch.search_client import SearchClient
import json
#%%
client = SearchClient.create(
    'V3ZOVI2QFZ',
    'ec7553dd56e6d4c8bb447a0240e7aab3'
)

data = client.list_indices()
#%%

with open("indices.json", "w+") as f:
    json.dump(data, f)

print(len(data["items"]))
# index = client.init_index('petemoorechevy_production_inventory')

# products = requests.get(
#     'https://v3zovi2qfz-dsn.algolia.net/'
# )

# index.save_objects(products.json(), {
#     'autoGenerateObjectIDIfNotExist': True
# })

# %%
def dumpIndex(indexName: str):
    index = client.init_index(indexName)
    it = index.search("", {'hitsPerPage': 1000})
    with open(f"{indexName}.json", "w+") as f:
        json.dump(it, f)

dumpIndex("petemoorechevy_production_inventory")
# %%

dumpIndex("petersenchevybuickinc_development_phone")

# %%

# %%
