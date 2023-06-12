animal = input('Enter dog or cat: ')
while not (animal.lower() == 'dog' or animal.lower() == 'cat'):
    animal = input('That is invalid input. Enter dog or cat: ')


# check if input is number
while True:
    try:
        animalAge = float(input('Enter age of animal in number: '))
        break
    except:
        print('That is invalid input. Try again.')
        pass

if animal.lower() == 'dog':
    if animalAge <= 2:
        humanAge = 12 * animalAge
        print('Human age of dog is' + str(humanAge) + '.')
    else:
        humanAge = 24 + 4 * (animalAge - 2)
        print('Human age of dog is ' + str(humanAge) + '.')
else:
    if animalAge <= 1:
        humanAge = 15 * animalAge
        print('Human age of cat is ' + str(humanAge) + '.')
    elif 1 < animalAge <= 2:
        humanAge = 15 + 9 * (animalAge - 1)
        print('Human age of cat is ' + str(humanAge) + '.')
    else:
        humanAge = 24 + 4 * (animalAge - 2)
        print('Human age of cat is ' + str(humanAge) + '.')

