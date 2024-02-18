# Base imports 
from django.shortcuts import render
from django.http import HttpResponse 

# Imports needed for `index` 
import googlemaps
from datetime import datetime
import requests
import os 
from dotenv import load_dotenv
import polyline 
from datetime import datetime


load_dotenv() 

passkey = os.environ.get("GMAPS_KEY")
gmaps = googlemaps.Client(key=passkey)
mapbox_key = os.environ.get("MAPBOX_KEY")

# Create your views here.
def login(request): 
    return render(request, "login.html")

def index(request): 
    return render(request, "index.html")

def volunteer(request): 
    return render(request, "volunteer-page.html")

def senior(request): 
    return render(request, "senior-page.html")

def map(request): 
    # return HttpResponse("Hello, world. This is a test.")
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
        return start_lat, start_lng, end_lat, end_lng

    def generate_route(departure, arrival): 
        # Get coordinates for departure and arrival with `get_lat_lon()`
        lat_lon_tuple = extract_lat_lon(departure, arrival)

        departure_lat_lon = lat_lon_tuple[0:2]
        arrival_lat_lon = lat_lon_tuple[2:4] 

        # Check if both departure and arrival coordinates are obtained succesfully 
        if departure_lat_lon and arrival_lat_lon: 
            # Construct coordinates string
            coordinates = f"{departure_lat_lon[1]},{departure_lat_lon[0]};{arrival_lat_lon[1]},{arrival_lat_lon[0]}"

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
    geometry = result['routes'][0]['geometry'] # Get encoded polyline 

    # Decode encoded polyline into list of list coordinates  
    coordinates_tuples = polyline.decode(geometry)
    coordinates = [[coord[1], coord[0]] for coord in coordinates_tuples] # (long, lat)
    # Find start and end waypoints for marking 
    start = result['waypoints'][0]['location']
    end = result['waypoints'][-1]['location']
    # Find center 
    center_lon = (start[0] + end[0]) / 2 # average longs 
    center_lat = (start[1] + end[1]) / 2 # average lats 
    center_coords = [center_lon, center_lat]

    # Extracting step-by-step instructions 
    instructions = [] 
    for route in result['routes']: 
        for leg in route['legs']: 
            for step in leg['steps']: 
                instruction = step['maneuver']['instruction']
                instructions.append(instruction) 

    # Extracting trip duration
    duration = (result['routes'][0]['duration']) // 60 

    return render(request, "map.html", { 'coordinates' : coordinates, 'start' : start, 'end' : end, 'center_coords' : center_coords, 'instructions': instructions, 'duration': duration})