import pandas as pd

# Define the bounding coordinates for reference
WEST_BOUND = -96.415043
EAST_BOUND = -88.336608
NORTH_BOUND = 41.098817
SOUTH_BOUND = 34.969039

# Load the CSV file
file_path = "MO_Wells.csv"  # Update with your file path if different
data = pd.read_csv(file_path)

# Define scaling functions
def scale_longitude(value, min_scaled, max_scaled):
    return WEST_BOUND + (value - min_scaled) * (EAST_BOUND - WEST_BOUND) / (max_scaled - min_scaled)

def scale_latitude(value, min_scaled, max_scaled):
    return SOUTH_BOUND + (value - min_scaled) * (NORTH_BOUND - SOUTH_BOUND) / (max_scaled - min_scaled)

# Identify the range of the original scaled coordinates
min_x, max_x = data['X'].min(), data['X'].max()
min_y, max_y = data['Y'].min(), data['Y'].max()

# Apply scaling to the coordinate columns
data['Longitude'] = data['X'].apply(scale_longitude, args=(min_x, max_x))
data['Latitude'] = data['Y'].apply(scale_latitude, args=(min_y, max_y))

# Save the updated data to a new CSV
output_file = "converted_coordinates.csv"
data.to_csv(output_file, index=False)

print(f"Converted coordinates saved to {output_file}")