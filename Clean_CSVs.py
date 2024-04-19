import os
import pandas as pd

# Step 1: Specify the path where the CSV files are located. Use your own route
ruta_base = '/home/ak/Escritorio/Pyt/log'

# Step 2: Create a list to store the DataFrames of each CSV file
dataframes_list = []

# Step 3: Cycle through each subfolder and CSV file in the base path
for root, _, files in os.walk(ruta_base):
    for file in files:
        if file.endswith('.csv'):
            archivo_csv = os.path.join(root, file)
            # Step 4: Read the CSV file
            data = pd.read_csv(archivo_csv)
            # Step 5: Add the DataFrame to the list
            dataframes_list.append(data)

# Step 6: Concatenate all DataFrames into one
all_data = pd.concat(dataframes_list)

# Step 7: Group data by "SerialNumber"
grouped_data = all_data.groupby('serialNumber')

# Step 8: Create a list to store the DataFrames for each group
grouped_data_list = []

# Step 9: Walk through each group and add it to the list
for serial_number, group in grouped_data:
    grouped_data_list.append(group)

# Step 10: Reconcatenate the DataFrames to have all the data grouped into one
grouped_data_concatenated = pd.concat(grouped_data_list)

# Step 11: Sort rows based on the data in the "location|timeStamp" column
sorted_data = grouped_data_concatenated.sort_values(by='location|timeStamp')

# Step 12: Export the grouped data to a new CSV file. Use your own route
output_file = '/home/ak/Escritorio/Pyt/Exports/archivo_agrupado.csv'
pd.concat(grouped_data_list).to_csv(output_file, index=False)

print("Clustered data successfully exported to:", output_file)

# Step 13: Cycle through each group and save the data in separate CSV files
for serial_number, group in grouped_data:
    # Create a unique file name based on the serialNumber. Use your own route
    output_file = f'/home/ak/Escritorio/Pyt/Exports/{serial_number}.csv'
    # Save the group's data to the CSV file
    group.to_csv(output_file, index=False)

print("CSV files, by serial number, successfully created and saved.")

