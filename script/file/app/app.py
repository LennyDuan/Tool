import os
from objects import Result, Course, CourseMapper
## Initializing
print('###### Start Initializing ######')
dir = os.getcwd()
path = dir + '/map/mapper.csv'
print('Find Course Mapper: ' + path)

mapper = {}
print('###### Initial Mapper ######')
with open(path) as file:
    for line in file:
        line = line.strip()
        arr = line.split(',')
        result = CourseMapper(arr[0], arr[1], arr[2], arr[3], arr[4])
        mapper[arr[0]] = result

print('###### Start Reading Mapper ######\n ')
for key, val in mapper.items():
    val.toString()
print('###### End Reading Mapper ######')
print('###### End Initializing ######\n\n')

## Start Converting
courses = {}
print('------------------------')
name = input('Please input a full file name: \n')
print('Your input file is: [' + name + ']');
path = dir + '/results/' + name;
print('###### Start Converting Scores from File... ###### \n')
with open(path) as file:
    for line in file:
        line = line.strip()
        eles = line.split(',')
        result = Result(eles[0], eles[1], eles[2])
        ## Looking in the mapper
        resultId = result.id
        if resultId in mapper:
            courseName = mapper[resultId].cName
            coursePoint = mapper[resultId].point
            course = None

            if courseName in courses:
                course = courses[courseName]
            else:
                course = Course(courseName)
                courses[courseName] = course

            course.add(result, coursePoint)
            print('Converting result: [' + result.id + ' ' + result.name
            + '] to Course: [' + course.cName + '] with [' + coursePoint + '] point\n')
        else:
            print('Mapper cannot find the course: ')
            result.toString()
print('###### End Converting ######\n\n')
print('------------------------\n\n')

for key, val in courses.items():
    val.toString()
    print('------\n')
