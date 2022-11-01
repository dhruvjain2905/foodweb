from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.geocode("Paris, France")

print((location.latitude, location.longitude))