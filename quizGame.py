# pursing CSV file using the 'csv' module

import csv
score = 0

# open the CSV file
with open('questionList', 'r') as file:
    # Create a CSV reader
    reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in reader:
        # Access the values in each column
        question = row[0]
        answer = row[1]

        # Process the data as needed
