import csv
import os
from passData.objects import PassPass

dir = os.path.dirname(os.path.abspath(__file__))
path = dir + '/../passData/passpass.csv'

def listAllAccounts():
    print('-----------------------')
    file = csv.reader(open(path))
    for arr in file:
        printList(arr)
    print('-----------------------\n')

def printList(arr):
    data = PassPass(arr[0], arr[1], arr[2], arr[3])
    data.toString()
