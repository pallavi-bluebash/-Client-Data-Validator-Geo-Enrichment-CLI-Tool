import requests
import os

API_KEY = os.getenv("OPENCAGE_API_KEY", "demo")


def get_coordinates(address):
    try:
        response = requests.get("https://api.opencagedata.com/geocode/v1/json", params={
            "q": address,
            "key": API_KEY,
            "limit": 1
        })
        data = response.json()
        if data['results']:
            geometry = data['results'][0]['geometry']
            return geometry['lat'], geometry['lng']
    except Exception:
        return None
