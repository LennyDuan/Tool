import csv
from objects import DegreeCourse

def createDegreeCourseTemplate(template, path):
    print('###### Initial Template ######\n')
    template = csv.reader(open(path))
    category = None
    for arr in template:
        createTemplate(template, arr, category)
    print('###### End Initializing ######\n')
    return template;

def createTemplate(template, arr, category):
    if (len(arr) == 1):
        category = arr[0]
        print('Current Category is: ' + category)
    else:
        print(arr)
