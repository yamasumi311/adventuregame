# guess the number game version2
secret_number = 87
n = input('Guess the secret number between 1 and 100: ')
n = int(n) # convert user input into an integer

while not (n == secret_number):
    # not equal to secret_number so check if lower or higher
    if n > secret_number:
        print('Your guess was too high')
    else:
        print('Your guess was too low')
    # ask user for another games
    n = input('Make another guess between 1 and 100: ')
    n = int(n) # convert user input into an integer
print('You got it!')
print('Thanks for playing') # this is done at end in all cases