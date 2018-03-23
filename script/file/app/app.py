import os
from objects import Result
from objects import CourseMapper

dir = os.getcwd()
path = dir + '/map/mapper.csv'
print('Find Course Mapper: ' + path)
print('------------------')

mapper = {}
print('------ Initial Mapper ------')
with open(path) as file:
    for line in file:
        line = line.strip()
        arr = line.split(',')
        result = CourseMapper(arr[0], arr[1], arr[2], arr[3], arr[4])
        mapper[arr[0]] = result

print('------ Start Reading Mapper ------\n ')
for key, val in mapper.items():
    val.toString()
print('------ End Reading Mapper ------')
