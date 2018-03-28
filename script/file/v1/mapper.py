import re
from objects import CourseMapper

def createCourseMapper(mapper, path):
    mapperPattern = re.compile(r'''((?:[^,"']|"[^"]*"|'[^']*')+)''')
    print('###### Initial Mapper ######')
    with open(path) as file:
        for line in file:
            line = line.strip()
            arr = mapperPattern.split(line)[1::2]
            createMapper(mapper, arr);

    print('###### End Initializing ######\n\n')
    return mapper;

def createMapper(mapper, arr):
    print(arr);
