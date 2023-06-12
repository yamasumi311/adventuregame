# pursing csv file without importing 'csv'
import random
score = 0

# open the CSV file
with open('questionList', 'r') as file:
    # read all the lines from the file
    lines = file.readlines()

    # Shuffle the lines randomly
    random.shuffle(lines)

    # Select a specific number of random lines
    num_lines = 3
    random_lines = lines[:num_lines]

    # Iterate over each line
    for line in random_lines:
        # Remove the newline character(\n) at the end of the line
        line = line.strip()

        # Split the line by the comma separator
        values = line.split(', ')

        # Access the values in each column
        question = values[0]
        answer = values[1]

        # Process the data as needed

        user_input = input(f'Question: {question} ').lower()
        if user_input == answer.lower():
            print('You are correct!')
            score = score + 1
        else:
            print(f'You are wrong. The answer is {answer}.')

print(f'Your score is {score}')