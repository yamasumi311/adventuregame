# pursing CSV file using the 'csv' module

import csv
import random


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


score = 0

# open the CSV file
with open('questionList', 'r') as file:
    # Create a CSV reader
    reader = csv.reader(file)

    # Initialize an empty array to store the questions
    questions = []

    # Iterate over each row in the CSV file
    for row in reader:
        # Access the values in each column
        question = row[0]
        answer = row[1]

        # Create a question object and append it to the array
        question_obj = Question(question, answer)
        questions.append(question_obj)

    # Access and print the questions with their answers
    for question_obj in questions:
        user_input = input(f'Question: {question_obj.question} --- ').lower()
        if user_input == question_obj.answer.lower():
            print('You are correct!')
            score = score + 1
        else:
            print(f'You are incorrect. The answer is {question_obj.answer}.')

print(f'Your score is {score}')