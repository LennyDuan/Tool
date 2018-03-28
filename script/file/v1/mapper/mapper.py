import csv
from objects import CourseMapper

def createCourseMapper(mapper, path):
    print('###### Initial Mapper ######')
    mapperLists = csv.reader(open(path))
    for arr in mapperLists:
        createMapper(mapper, arr)
    print('###### End Initializing ######\n\n')
    return mapper;

def createMapper(mapper, arr):
    print(arr);
