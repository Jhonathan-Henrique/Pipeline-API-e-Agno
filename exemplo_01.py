import requests

url = "https://api.coinbase.com/v2/prices/spot"

responde = requests.get(url)

print(responde.json())