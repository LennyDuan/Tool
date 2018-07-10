import csv
import os
from passData.objects import PassPass

dir = os.getcwd()
path = dir + '/passData/passpass.csv'

def createAccount():
    print('-----------------------')
    appName = input('New App Name: ')
    account = input('Input account: ')
    passWord = input('Input password: ')
    extra = input('Input extra information: ')
    data = PassPass(appName, account, password, extra)
    writeToCSV(data)
    print('-----------------------')

def writeToCSV(data):
    with open(path, 'w') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')
        line = data.name + ',' + data.account + ','
        + data.password + ',' + data.extra
        csv_file.write(line)
        csv_file.write('\n')
