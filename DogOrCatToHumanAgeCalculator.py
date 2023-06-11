import math

animal = input('Enter dog or cat: ')
while not (animal.lower() == 'dog' or animal.lower() == 'cat'):
    print('That is invalid input. Enter dog or cat: ')

animalAge = input('Enter age of animal in number: ')
while not (type(animalAge) == int):
    animaAge = input('That is invalid input. Enter age of animal in number: ')

if animal.lower() == dog:
   if animalAge == 1:
       print('Human age of dog is 12.')
   elif animalAge == 2:
       print('Human age of dog is 24.')
   else:
       humanAge = 24 + 4 * (animalAge - 2)
       print('Human age of dog is' + humanAge +'.')
else:
    if animalAge == 1:
        print('Human age of cat is 15.')
    elif animalAge == 2:
        print('Human age of cat is 24.')
    else:
        humanAge = 24 + 4 * (animalAge - 2)
        print('Human age of dog is' + humanAge + '.')


