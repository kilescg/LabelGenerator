import csv
import os
import mysql.connector
from datetime import datetime
from utils import *

db_host = "127.0.0.1"
db_user = "root"
db_password = "password"
db_name = "db_sde"


def write_csv(fieldnames, data_list, file_path):
    # Check if the output file already exists and delete it
    if os.path.exists(file_path):
        os.remove(file_path)

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


def log_mac_id(mac_id, note, file_path):
    # Check if the CSV file exists
    dt_string = get_date_time()
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
        fieldnames = ['macID', 'note', 'timestamp']  # Specify the header field
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # If the file does not exist, write the header
        if not file_exists:
            writer.writeheader()

        # Check if the macID already exists, and only write if it's not a duplicate
        if mac_id not in existing_data:
            writer.writerow(
                {'macID': mac_id, 'note': note, 'timestamp': dt_string})


def insert_child_device(device_incoming):
    try:
        conn = mysql.connector.connect(
            host=db_host, user=db_user, password=db_password, database=db_name)
        cursor = conn.cursor()

        # Define the SQL query with placeholders
        sql = '''INSERT INTO child_device (child_id, print_label, datetime, note) VALUES (%s, %s, %s, %s)'''

        # Execute the SQL query with the data
        cursor.execute(sql, device_incoming)

        # Commit the changes to the database
        conn.commit()
        conn.close()
        cursor.close()
        return 1
    except mysql.connector.Error as e:
        print("MySQL error:", e)
        return 0


def update_print_label_by_mac_id(mac_id):
    try:
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        cursor = conn.cursor()
        update_query = "UPDATE child_device SET print_label = '1' WHERE child_id = %s"
        cursor.execute(update_query, (mac_id,))
        conn.commit()
        conn.close()
        return 1
    except mysql.connector.Error as e:
        print("MySQL error:", e)
