import os
import sys
from security.credentials import checkCredentialsExist, validAccount, createCredential, validPassword
from common.options import selectOption
from options.listAllAccounts import listAllAccounts
from options.createAccount import createAccount
from options.getExistAccounts import getExistAccounts

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
# setup validation:
valid = True
while option is not 0:
    if option == 1:
        if valid or validPassword():
            valid = True
            print('\nListing all accounts...')
            listAllAccounts()
    elif option == 2:
        if valid or validPassword():
            valid = True
            print('\nGet exist accounts...')
            getExistAccounts()
    elif option == 3:
        if valid or alidPassword():
            valid = True
            print('\nCreating a new account...')
            createAccount()
    elif option == 0:
        sys.exit('\nExiting...')
    else:
        print('\n[Error]:Invalid option...')
    option = selectOption()
