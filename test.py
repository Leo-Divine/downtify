import requests

url = "http://home.casper.dpdns.org/Items/7e64e319657a9516ec78490da03edccb/Refresh"
headers = {
    'Authorization': f'MediaBrowser Token="{'0470b2a55c974028b972335086d5b4b5'}"',
    'Content-Type': 'application/json'
}
params = {
    "Recursive": "true",
    "MetadataRefreshMode": "FullRefresh",
    "ImageRefreshMode": "FullRefresh",
    "ReplaceAllMetadata": "false",
    "ReplaceAllImages": "false"
}
try:
    response = requests.post(url, headers=headers, params=params)
    response.raise_for_status()
    print('cool')
except requests.exceptions.RequestException as e:
    raise e