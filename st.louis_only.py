import pandas as pd

# Define the St. Louis boundary coordinates
#BOUNDARY_NE = (38.84137118479565, -90.15259889796783)  # Northeast
#BOUNDARY_NW = (38.86871475815717, -90.82286930245763)  # Northwest
#BOUNDARY_SW = (38.53615231466545, -90.80573496620926)  # Southwest
#BOUNDARY_SE = (38.520794599896945, -90.18907418355701)  # Southeast

BOUNDARY_NE = (39.10, -90.0)  # Northeast
BOUNDARY_NW = (39.10, -91.15)  # Northwest
BOUNDARY_SW = (38.40, -91.15)  # Southwest
BOUNDARY_SE = (38.40, -90.0)  # Southeast

# Load the converted coordinates CSV
file_path = "converted_coordinates.csv"  # Update with your file path if different
data = pd.read_csv(file_path)

# Define a function to check if a point is within the bounding box
def is_within_boundary(lat, lon):
    # Latitude range: between the north and south bounds
    within_lat = BOUNDARY_SW[0] <= lat <= BOUNDARY_NW[0]
    # Longitude range: between the west and east bounds
    within_lon = BOUNDARY_NW[1] <= lon <= BOUNDARY_NE[1]
    return within_lat and within_lon

# Apply the filter to the data
filtered_data = data[data.apply(lambda row: is_within_boundary(row['Latitude'], row['Longitude']), axis=1)]

# Save the filtered data to a new CSV file
output_file = "filtered_st_louis_coordinates.csv"
filtered_data.to_csv(output_file, index=False)

print(f"Filtered data saved to {output_file}")