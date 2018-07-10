import os
import csv
import hashlib

dir = os.getcwd()
credentialsPath = dir + '/security/credentials.csv'

def checkCredentialsExist():
    if not os.path.exists(credentialsPath):
        return False
    else:
        return True

def validAccount(account, password):
    credentials = csv.reader(open(credentialsPath))
    for arr in credentials:
        if account == arr[0] and hashStr(password) == arr[1]:
            return True
        else:
            return False

def validPassword():
    valid = False
    while not valid:
        password = input('Please enter password:')
        credentials = csv.reader(open(credentialsPath))
        for arr in credentials:
            if hashStr(password) == arr[1]:
                valid = True
                return True
            else:
                print('Inavlid password, unable to excute your command')
                valid = False

def createCredential():
    print('Creating a new account for PassPass...')
    account = input('Please enter account:')
    password = input('Please enter password:')
    with open(credentialsPath, 'w') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')
        csv_file.write(account)
        csv_file.write(',')
        csv_file.write(hashStr(password))

def hashStr(pwd):
    return hashlib.md5(pwd.encode('utf-8')).hexdigest()
