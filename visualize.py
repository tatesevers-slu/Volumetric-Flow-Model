import pandas as pd
import folium

# Load the filtered data
file_path = "filtered_st_louis_coordinates.csv"  # Update with your file path if different
data = pd.read_csv(file_path)

# Create a base map centered on the approximate middle of St. Louis
center_lat, center_lon = 38.627003, -90.199404  # Center of St. Louis
map_stl = folium.Map(location=[center_lat, center_lon], zoom_start=12)

# Add points to the map
for _, row in data.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']], popup=f"Well ID: {row.get('WellID', 'N/A')}").add_to(map_stl)

# Save the map to an HTML file
output_map = "st_louis_wells_map.html"
map_stl.save(output_map)

print(f"Map saved as {output_map}. Open this file in a browser to view it.")
