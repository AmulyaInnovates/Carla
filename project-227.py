import json  # Importing the json library
import csv   # Importing the csv library

# Task 01: Read data from text file data_set.txt and store it in a variable
data_from_txt = []  # Define an empty list to store data from text file

# Open and read the data_set.txt file
with open('data_set.txt', 'r') as f:
    data_from_txt = json.loads(f.read())

# Task 02: Create and Store data in the project_227.csv file from the data_set.txt text file
# Define the field names for the CSV file
field_names = ['throttle', 'steer']

# Create the project_227.csv file
with open('project_227.csv', 'w', newline='') as csvfilestore:
    # Create a DictWriter object to write to the CSV file
    writer = csv.DictWriter(csvfilestore, fieldnames=field_names)
    
    # Write the header to the CSV file
    writer.writeheader()
    
    # Write the data from the text file to the CSV file
    writer.writerows(data_from_txt)

# Task 03: Read the data stored in the project_226.csv file and print on cmd
data_from_csv = []  # Define an empty list to store data from CSV file

# Read the data from the project_226.csv file
with open('project_226.csv', 'r') as file:
    reader = csv.reader(file)
    
    # Loop through the CSV data and append each row to the data_from_csv list
    for row in reader:
        data_from_csv.append(row)

# Print the data from the CSV file
print(data_from_csv)
