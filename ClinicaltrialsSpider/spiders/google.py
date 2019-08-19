import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'google_msv',
    'query': 'meilleur restaurant',
    'geo_location': 'Paris,Ile-de-France,France',
    'callback_url': 'https://your.callback.url',
    'context': [
        {'key': 'language', 'value': 'french'},
        {'key': 'currency', 'value': 'EUR'},
        {'key': 'ideas', 'value': True}, # Default. Set to False to not get keyword ideas.
    ],
}

# Get response.
response = requests.request(
    'POST',
    'https://data.oxylabs.io/v1/queries',
    auth=('glixingpu', 'vn7yrK4fnk'),
    json=payload,
)

# Print prettfied response to stdout.
pprint(response.json())

url = 'http://data.oxylabs.io/v1/queries/6568041695852628993'

a = requests.get(
    url, auth=('glixingpu', 'vn7yrK4fnk'),
)
print(a)

