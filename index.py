import folium
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_geocoder")

def get_coordinates(address):
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None

mapObj = folium.Map(location=[20.0, 84.0], zoom_start=7)  # Updated initial location and zoom level for better visibility

shapesLayer = folium.FeatureGroup(name="circles").add_to(mapObj)

locations = [
    ["Port Blair, Andaman and Nicobar Islands, India"],
    ["Amaravati, Andhra Pradesh, India"],
    ["Itanagar, Arunachal Pradesh, India"],
    ["Dispur, Assam, India"],
    ["Patna, Bihar, India"],
    ["Chandigarh, Chandigarh, India"],
    ["Bhubaneswar, Odisha, India"],  # Updated for Bhubaneswar
    ["Kalpana Square Road, Bhubaneswar, Odisha, India"]  # Added Kalpana Square Road
    # Add more locations as needed
]

image_url_default = "https://example.com/default_image.jpg"  # Replace with a default image URL

for location in locations:
    full_location = location[0]
    coordinates = get_coordinates(full_location)
    
    if coordinates:
        lat, lon = coordinates
        # Use a default image if a specific image URL is not provided
        image_url = image_url_default
        
        popup_content = f"""<h2>{full_location}</h2><br/>
                            <b>Hello Industrialist come up with plastics</b><br/>
                            <img src="{image_url}" alt="Image" style="max-width:100%;max-height:100%">"""

        folium.Marker(
            location=[lat, lon],
            popup=folium.Popup(popup_content, max_width=500),
            icon=folium.Icon(color='green')  # You can set a specific color for the marker
        ).add_to(shapesLayer)

folium.LayerControl().add_to(mapObj)
mapObj.save('output.html')