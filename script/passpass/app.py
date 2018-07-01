import os
from security.credentials import checkCredentialsExist, validAccount, createCredential

print('\nInitializing...')
print('-----------------------')
loggedIn = False;
while not loggedIn:
    if checkCredentialsExist():
        print('Trying to log in...')
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
print('-----------------------')
print('Login successfully...\n')
