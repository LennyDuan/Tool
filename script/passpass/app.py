import os
import sys
from security.credentials import checkCredentialsExist, validAccount, createCredential, validPassword
from common.options import selectOption
from options.listAllAccounts import listAllAccounts

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

option = selectOption()
while option is not 0:
    if option == 1:
        if validPassword():
            print('Listing all accounts...')
            print('-----------------------')
            listAllAccounts()
            print('-----------------------')
    elif option == 2:
        if validPassword():
            print('Get an exist account...')
    elif option == 3:
        if validPassword():
            print('Creating a new account...')
    elif option == 0:
        sys.exit('Exiting...')
    else:
        print('[Error]:Invalid option...')
    option = selectOption()
