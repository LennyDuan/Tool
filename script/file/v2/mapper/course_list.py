import csv
from objects import CourseList

def createCourseList(course_list, path):
    #print('\n###### Initial Category Template ######\n')
    file = csv.reader(open(path))
    for arr in file:
        createList(course_list, arr)
    #print('\n###### End Category Initializing ######\n')
    return category;

def createList(course_list, arr):
    category[arr[0]] = DegreeCategory(arr[0], arr[1])
