import os
import sys
from security.credentials import checkCredentialsExist, validAccount, createCredential, validPassword
from common.options import selectOption
from options.listAllAccounts import listAllAccounts
from options.createAccount import createAccount

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
valid = False
while option is not 0:
    if option == 1:
        if validPassword(valid) or valid:
            print('\nListing all accounts...')
            listAllAccounts()
    elif option == 2:
        if validPassword(valid) or valid:
            print('\nGet exist accounts...')
    elif option == 3:
        if validPassword(valid) or valid:
            print('\nCreating a new account...')
            createAccount()
    elif option == 0:
        sys.exit('\nExiting...')
    else:
        print('\n[Error]:Invalid option...')
    option = selectOption()
