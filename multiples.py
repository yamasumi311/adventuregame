count = int(input('Enter number you want to count by: '))
n = 0
choice = input('Enter return to continue or q to quit: ').lower()
while not (choice == 'q'):
    print(n)
    n = n + count
    choice = input('Enter return to continue or q to quit: ').lower()



