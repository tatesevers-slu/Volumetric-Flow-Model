import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Load the data
file_path = "filtered_st_louis_coordinates_with_ids.csv"  # File with Well IDs and additional data
data = pd.read_csv(file_path)

# Define the boundary coordinates
boundary_coords = [
    [39.10, -90.0],  # NE
    [39.10, -91.15],  # NW
    [38.40, -91.15],  # SW
    [38.40, -90.0],  # SE
]

# Create a base map centered on the approximate middle of St. Louis
center_lat, center_lon = 38.627003, -90.199404  # Center of St. Louis
map_stl = folium.Map(location=[center_lat, center_lon], zoom_start=12)

# Add a polygon around the boundary with 35% opacity
folium.Polygon(
    locations=boundary_coords,
    color="gray",
    fill=True,
    fill_color="gray",
    fill_opacity=0.30,
    weight=2,
).add_to(map_stl)

# Add a MarkerCluster to the map
marker_cluster = MarkerCluster(options={"maxClusterRadius": 50}).add_to(map_stl)

# Columns to display in the popup
columns_to_display = [
    "WellID", "WELL_STAT", "DATE_COMPL", "SITE_NAME", "SITE_ADD1", "TOTAL_DPTH",
    "DEPTH_GW", "SWL", "WELL_YIELD", "CASING_LEN", "CASING_MAT", "WELL _INST_"
]

# Add points to the cluster with popup table
for _, row in data.iterrows():
    # Create an HTML table for each well
    popup_table = f"""
    <table style="width: 300px; border: 1px solid black; border-collapse: collapse;">
        <tr><th colspan="2" style="border: 1px solid black; background-color: #f2f2f2;">Well Information</th></tr>
        {"".join([f"<tr><td style='border: 1px solid black;'><b>{col}</b></td><td style='border: 1px solid black;'>{row.get(col, 'N/A')}</td></tr>" for col in columns_to_display])}
    </table>
    """
    # Add marker with popup
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=folium.Popup(popup_table, max_width=350)
    ).add_to(marker_cluster)

# Save the map to an HTML file
output_map = "st_louis_wells_clustered_map_with_details.html"
map_stl.save(output_map)

print(f"Map with detailed well information saved as {output_map}. Open this file in a browser to view it.")