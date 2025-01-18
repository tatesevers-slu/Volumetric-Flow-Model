import pandas as pd

# Load the data
file_path = "filtered_st_louis_coordinates.csv"  # Update this path if different
data = pd.read_csv(file_path)

# Check if 'WellID' column exists, if not, create unique IDs
if 'WellID' not in data.columns:
    data['WellID'] = ["Well_" + str(i + 1) for i in range(len(data))]

# Save the updated dataset with unique IDs
updated_file_path = "filtered_st_louis_coordinates_with_ids.csv"
data.to_csv(updated_file_path, index=False)

print(f"Unique Well IDs assigned and saved to {updated_file_path}.")
