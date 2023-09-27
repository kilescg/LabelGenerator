import csv
import os

file_path = "database/devices.csv"
fieldnames = ['macID']

def WriteCsv(data_list):
    # Check if the output file already exists and delete it
    if os.path.exists(file_path):
        print("deleting csv")
        os.remove(file_path)
    print("writing new csv")


    # Open the CSV file for writing
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write data rows
        for inner_list in data_list:
            if len(inner_list) == len(fieldnames):
                # Create a dictionary by zipping fieldnames and inner_list
                data_dict = dict(zip(fieldnames, inner_list))
                writer.writerow(data_dict)
            else:
                print(f"Skipping invalid data: {inner_list}")