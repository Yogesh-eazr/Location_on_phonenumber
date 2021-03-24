# import geocoder
import phonenumbers
from phoneNumberList import number
from phonenumbers import geocoder
import folium
yoginumber = phonenumbers.parse(number)
yourlocation = geocoder.description_for_number(yoginumber, 'en')
print(yourlocation)

## service provider of the number

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, 'en'))

Key = '408e3d51d30544068a488083827680b0'

## to get lat and long
from opencage.geocoder import OpenCageGeocode

## copying the API KEY from opencage site
geocoder = OpenCageGeocode(Key)

query = str(yourlocation)
results = geocoder.geocode(query)

# print(results)

lat= results[0]['geometry']['lat']
lng= results[0]['geometry']['lng']

print(lat,lng)

mymap = folium.Map(location = [lat,lng], zoom_start = 9)

folium.Marker([lat,lng],popup=yourlocation).add_to((mymap))

## save in html
mymap.save("mylocviaphone.html")