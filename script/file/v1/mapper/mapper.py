import csv
from objects import CourseMapper

def createCourseMapper(mapper, path):
    #print('###### Initial Mapper ######\n')
    mapperLists = csv.reader(open(path))
    for arr in mapperLists:
        createMapper(mapper, arr)
    #print('###### End Initializing ######\n\n')
    return mapper;

def createMapper(mapper, arr):
    code = arr[3]
    if '+' in code:
        codePlus = ''.join(code.split('+')[1:])
    else:
        codePlus = ''
    department = arr[2]
    title = arr[4]
    equivalency = arr[7]
    remarks = arr[8]
    category = arr[9]
    credits = arr[10]
    level = arr[12]

    cMapper = CourseMapper(department, code, codePlus, title,
    equivalency, remarks, category, credits, level)
    mapper[code] = cMapper
