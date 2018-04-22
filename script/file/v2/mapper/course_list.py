import csv
from objects import CourseList

def createCourseList(course_list, path):
    file = csv.reader(open(path))
    for arr in file:
        createList(course_list, arr)
    return course_list;

def createList(course_list, arr):
    course_list[arr[0]] = CourseList(arr[0], arr[2], arr[3], arr[7])
