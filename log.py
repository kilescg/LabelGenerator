import csv
import os
from datetime import datetime

def WriteCsv(fieldnames, data_list, file_path):
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

def LogMacID(mac_id, file_path):
    # Check if the CSV file exists
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d,%H:%M:%S")
    file_exists = os.path.isfile(file_path)

    # Read existing data to check for duplicates
    existing_data = set()
    if file_exists:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                existing_mac_id = row.get('macID')
                if existing_mac_id:
                    existing_data.add(existing_mac_id)

    # Open the CSV file in append mode (or create a new one)
    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = ['macID','timestamp']  # Specify the header field
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # If the file does not exist, write the header
        if not file_exists:
            writer.writeheader()

        # Check if the macID already exists, and only write if it's not a duplicate
        if mac_id not in existing_data:
            writer.writerow({'macID': mac_id, 'timestamp': dt_string})