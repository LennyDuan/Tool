import os
from mapper.mapper import createCourseMapper
## Initializing
print('###### Start Initializing ######')
dir = os.getcwd()
path = dir + '/equivalence_course/UM equivalence_course.csv'
print('Find Course Mapper: ' + path)

mapper = {}
mapper = createCourseMapper(mapper, path)

print('###### Start Reading Mapper ######\n ')
for key, val in mapper.items():
    val.toString()
print('###### End Reading Mapper ######')
