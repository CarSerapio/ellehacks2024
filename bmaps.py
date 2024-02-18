import googlemaps
from datetime import datetime
import requests
import os 
from dotenv import load_dotenv
import polyline 

load_dotenv() 

passkey = os.environ.get("GMAPS_KEY")
gmaps = googlemaps.Client(key=passkey)
mapbox_key = os.environ.get("MAPBOX_KEY")


def extract_lat_lon(departure, arrival): 
    now = datetime.now() 

    response = gmaps.directions(departure, # York University 
                                     arrival, # Pioneer Village 
                                     mode="walking",
                                     departure_time=now)

    start_lat = response[0]['legs'][0]['start_location']['lat']
    start_lng = response[0]['legs'][0]['start_location']['lng']
    end_lat = response[0]['legs'][0]['end_location']['lat']
    end_lng = response[0]['legs'][0]['end_location']['lng']
    return start_lng, start_lat, end_lng, end_lat

# Example usage of `extract_lat_lon() -> (start_lat, start_lng, end_lat, end_lng)`
now = datetime.now() 
directions_result = gmaps.directions("4700 Keele St, Toronto, ON", # York University 
                                     "Pioneer Village, Toronto, ON", # Pioneer Village 
                                     mode="walking",
                                     departure_time=now)

print(extract_lat_lon("4700 Keele St, Toronto, ON", "Pioneer Village, Toronto, ON"))
# Output: (43.7740056, -79.50136549999999, 43.7765442, -79.5082935)


def generate_route(departure, arrival): 
    # Get coordinates for departure and arrival with `get_lat_lon()`
    lat_lon_tuple = extract_lat_lon(departure, arrival)

    departure_lat_lon = lat_lon_tuple[0:2]
    arrival_lat_lon = lat_lon_tuple[2:4] 
    
    # Check if both departure and arrival coordinates are obtained succesfully 
    if departure_lat_lon and arrival_lat_lon: 
        # Construct coordinates string
        coordinates = f"{departure_lat_lon[0]},{departure_lat_lon[1]};{arrival_lat_lon[0]},{arrival_lat_lon[1]}"
        print(coordinates) 

        # Construct the payload 
        data = { 
            "coordinates": coordinates, 
            "steps": "true",
            "waypoints": "0;1",
            "waypoint_names": "Departure;Arrival",
            "banner_instructions": "true"
        }

        # Define the URL and parameters for the Mapbox API request
        url = "https://api.mapbox.com/directions/v5/mapbox/walking"
        params = {
            "access_token": mapbox_key 
        }

        # Send a POST request to the Mapbox API
        response = requests.post(url, data=data, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            result = response.json()
            return result
        else:
            print("Request failed.")
            return None
    else:
        print("Failed to obtain coordinates for departure or arrival.")
        return None


departure = "4700 Keele St, Toronto, ON"
arrival = "Pioneer Village, Toronto, ON"

result = generate_route(departure, arrival)
if result:
    print("Route generated successfully!")
    # Process the route data as needed
    print(result)
else:
    print("Failed to generate route.")


"""
encoded_polyline = 'wrdjGprfdNQFl@hEsAd@kA\\D`@Mf@TnBIBz@lGv@xFQDKv@F^]r@k@PBN{FnBCQQF?B_AXe@jAUA'

# Decode the polyline into a list of coordinates
decoded_coordinates = polyline.decode(encoded_polyline)

print(decoded_coordinates) 
"""
