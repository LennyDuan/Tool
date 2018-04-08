import csv
from objects import DegreeCourse

def createDegreeCourseTemplate(template, path):
    print('###### Initial Template ######\n')
    template = csv.reader(open(path))
    for arr in template:
        createTemplate(template, arr)
    print('###### End Initializing ######\n')
    return template;

def createTemplate(template, arr):
    print(arr)
