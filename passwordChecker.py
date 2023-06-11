password = input('Create a password: ')
passwordEntered = input('Enter the password: ')
while not (password == passwordEntered):
    print('Sorry that is incorrect.')
    passwordEntered = input('Enter password again: ')
if password == passwordEntered:
    print('Success: You are correct.')