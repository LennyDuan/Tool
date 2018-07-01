import os
import sys
from security.credentials import checkCredentialsExist, validAccount, createCredential, validPassword

print('\nInitializing...')
print('-----------------------')
loggedIn = False;
while not loggedIn:
    if checkCredentialsExist():
        print('Trying to log in PassPass...')
        account = input('Please enter account:')
        password = input('Please enter password:')
        if not validAccount(account, password):
            print('Invalid account or password')
            loggedIn = False
        else:
            loggedIn = True
    else:
        createCredential()
        loggedIn = False
print('\n-----------------------')
print('Please choose your next steps:')
print('1: List all accounts')
print('2: Get a account')
print('3: Creat/Save a new account')
print('0: Exit')
print('-----------------------\n')
option = int(input('Input a number:'))
while option is not 0:
    if option == 1:
        if validPassword():
            print('Listing all accounts...\n')
    elif option == 2:
        if validPassword():
            print('Get an exist account...\n')
    elif option == 3:
        if validPassword():
            print('Creating a new account...\n')
    elif option == 0:
        sys.exit('Exiting...\n')
    else:
        print('Invalid option...\n')
        
    option = int(input('Input a number:'))
