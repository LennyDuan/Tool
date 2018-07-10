import csv
import os
from passData.objects import PassPass

dir = os.getcwd()
path = dir + '/passData/passpass.csv'

def createAccount():
    print('-----------------------')
    appName = input('New App Name: ')
    account = input('Input account: ')
    password = input('Input password: ')
    extra = input('Input extra information: ')
    if extra is None:
        extra = ' None'
    data = PassPass(appName, account, password, extra)
    writeToCSV(data)
    print('New account have been saved: ')
    data.toString()
    print('-----------------------')

def writeToCSV(data):
    with open(path, 'a') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')
        line = str(data.name)
        line += ','
        line += str(data.account)
        line += ','
        line += str(data.password)
        line += ','
        line += str(data.extra)
        csv_file.write(line)
        csv_file.write('\n')
