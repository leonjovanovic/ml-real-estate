
from geopy.geocoders import GoogleV3
AUTH_KEY = "API_KEY"
geolocator = GoogleV3(api_key=AUTH_KEY)
coords = geolocator.geocode('Aqua 1507 Belgrade Waterfront, Beograd, Srbija')
print(coords.latitude, coords.longitude)
