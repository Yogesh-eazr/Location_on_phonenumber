import folium
import geocoder

# g = geocoder.ip("me")
g = geocoder.ip("42.106.194.176")
# g = geocoder.ip("2402:3a80:1382:4545:0:26:d632:6701")
myaddress = g.latlng
print(g, type(g))
f = geocoder.ipinfo("42.106.194.176")

# 19.125468527149483, 72.89084337695901
# [19.1624, 72.8694]

print(myaddress)
print(f)
my_map1 = folium.Map(location=myaddress, zoom_start=12)

folium.CircleMarker(location=myaddress,
                    radius=50).add_to(my_map1)

folium.Marker(myaddress,popup="Your location").add_to(my_map1)
# , popup = "Yorkshire"
my_map1.save("my_map1.html")