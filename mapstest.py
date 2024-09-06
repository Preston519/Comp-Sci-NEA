import googlemaps
import datetime

gmaps = googlemaps.Client(key="AIzaSyDE2qaxHADLeBQO1zLqfDIasLOalcHWHi0")
print(gmaps.reverse_geocode((40.714224, -73.961452))[0]["formatted_address"])
# print(gmaps.addressvalidation(['1600 Amphitheatre Pk'], 
#                                                     regionCode='US',
#                                                     locality='Mountain View', 
#                                                     enableUspsCass=True))
print(gmaps.directions("Sydney Town Hall",
                                     "aldkd",
                                     mode="transit",
                                     departure_time=datetime.datetime.now()))
