from geopy.geocoders import Nominatim
from requests import get

loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode(str(input('Enter a place: \n')).title())

params = {
    'lat': getLoc.latitude,
    'lon': getLoc.longitude,
    'appid': 'a0aaf5b2a66e82ce4c9a4f390dbc4f31',
}

print(get(url='http://api.openweathermap.org/data/2.5/air_pollution', params=params)
      .json()['list'][0]['components']['pm2_5'])
