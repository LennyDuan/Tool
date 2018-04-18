import csv
from objects import DegreeCategory

def createDegreeCourseCategory(category, path):
    #print('\n###### Initial Category Template ######\n')
    file = csv.reader(open(path))
    for arr in file:
        createCategory(category, arr)
    #print('\n###### End Category Initializing ######\n')
    return category;

def createCategory(category, arr):
    category[arr[0]] = DegreeCategory(arr[0], arr[1])
