import csv
import os
from passData.objects import PassPass

dir = os.getcwd()
path = dir + '/passData/passpass.csv'


def getExistAccounts():
    print('-----------------------')
    appName = input('App Name: ')
    file = csv.reader(open(path))
    for arr in file:
        checkList(appName, arr)
    print('-----------------------\n')

def checkList(appName, arr):
    data = PassPass(arr[0], arr[1], arr[2], arr[3])
    if str(data.name) == str(appName):
        data.toString()
    elif str(appName) in str(data.name):
        print('|Similar| - '+ data.toString())
